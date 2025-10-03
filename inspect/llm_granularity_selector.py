#!/usr/bin/env python3
"""
LLM-Guided Granularity Selection using Qwen3
Intelligently selects optimal WordNet concepts for each granularity level.
"""
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
import re
from collections import defaultdict
from nltk.corpus import wordnet as wn


class Qwen3GranularitySelector:
    """
    LLM-based granularity selector using Qwen3 model.

    Selects best concepts from WordNet paths:
    - Coarse: depth 1-3 (general domains)
    - Mid: depth 4-6 (categories)
    - Fine: original object (unchanged)
    """

    def __init__(self, model_name="Qwen/Qwen3-0.6B", device="cuda:2", verbose=False):
        """
        Initialize Qwen3 model for granularity selection.

        Args:
            model_name: Hugging Face model name
            device: CUDA device (e.g., "cuda:2")
            verbose: Print detailed logs
        """
        self.device_id = device.split(":")[-1] if ":" in device else "0"
        os.environ['CUDA_VISIBLE_DEVICES'] = self.device_id

        self.verbose = verbose
        self.model_name = model_name

        if self.verbose:
            print(f"Loading {model_name} on device {device}...")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            trust_remote_code=True
        )

        if self.verbose:
            print(f"✓ Model loaded on: {self.model.device}")

    def format_wordnet_path(self, synset):
        """
        Extract and format WordNet path with depth annotations.

        Returns:
            list of tuples: [(concept_name, depth), ...]
        """
        paths = synset.hypernym_paths()
        if not paths:
            return []

        # Use longest path (most specific)
        longest_path = max(paths, key=len)

        formatted_path = []
        for idx, s in enumerate(longest_path):
            concept_name = s.name().split('.')[0].replace('_', ' ')
            formatted_path.append((concept_name, idx))

        return formatted_path

    def create_selection_prompt(self, object_name, wordnet_path):
        """
        Create prompt for LLM to select granularity concepts.

        Args:
            object_name: Original object name
            wordnet_path: List of (concept, depth) tuples

        Returns:
            str: Formatted prompt
        """
        # Format path for display
        path_str = "\n".join([f"- {concept} (depth {depth})" for concept, depth in wordnet_path])

        # Find concepts in each depth range
        coarse_candidates = [(c, d) for c, d in wordnet_path if 1 <= d <= 3]
        mid_candidates = [(c, d) for c, d in wordnet_path if 4 <= d <= 6]

        # Build candidate lists with depths
        coarse_options = [f'"{c}" (depth {d})' for c, d in coarse_candidates]
        mid_options = [f'"{c}" (depth {d})' for c, d in mid_candidates]

        prompt = f"""Task: Select the best concept from each list for object "{object_name}".

COARSE level (choose ONE from depths 1-3):
{', '.join(coarse_options)}

MID level (choose ONE from depths 4-6):
{', '.join(mid_options)}

Instructions:
1. For COARSE: Pick the most general, abstract concept
2. For MID: Pick a clear categorical concept

Output JSON format (fill in actual concept names and depths):
{{"coarse": "concept_name_here", "coarse_depth": depth_number, "mid": "concept_name_here", "mid_depth": depth_number}}"""

        return prompt

    def extract_json_from_response(self, response):
        """
        Extract JSON from LLM response (may contain extra text/reasoning).

        Args:
            response: Raw LLM response string

        Returns:
            dict or None: Parsed JSON or None if parsing fails
        """
        # Try direct JSON parse first
        try:
            return json.loads(response.strip())
        except:
            pass

        # Try to find JSON object in response
        json_pattern = r'\{[^}]*"coarse"[^}]*"mid"[^}]*\}'
        matches = re.findall(json_pattern, response, re.DOTALL)

        if matches:
            try:
                return json.loads(matches[0])
            except:
                pass

        # Try to extract key-value pairs
        try:
            coarse_match = re.search(r'"coarse"\s*:\s*"([^"]+)"', response)
            coarse_depth_match = re.search(r'"coarse_depth"\s*:\s*(\d+)', response)
            mid_match = re.search(r'"mid"\s*:\s*"([^"]+)"', response)
            mid_depth_match = re.search(r'"mid_depth"\s*:\s*(\d+)', response)

            if all([coarse_match, coarse_depth_match, mid_match, mid_depth_match]):
                return {
                    "coarse": coarse_match.group(1),
                    "coarse_depth": int(coarse_depth_match.group(1)),
                    "mid": mid_match.group(1),
                    "mid_depth": int(mid_depth_match.group(1))
                }
        except:
            pass

        return None

    def validate_selection(self, selection, wordnet_path):
        """
        Validate LLM selection against actual WordNet path.

        Returns:
            bool: True if selection is valid
        """
        if not selection or not isinstance(selection, dict):
            return False

        required_keys = ['coarse', 'coarse_depth', 'mid', 'mid_depth']
        if not all(k in selection for k in required_keys):
            return False

        # Check depth ranges
        if not (1 <= selection['coarse_depth'] <= 3):
            return False
        if not (4 <= selection['mid_depth'] <= 6):
            return False

        # Check if concepts exist in path
        path_concepts = {c.lower(): d for c, d in wordnet_path}

        coarse_lower = selection['coarse'].lower()
        mid_lower = selection['mid'].lower()

        if coarse_lower not in path_concepts and coarse_lower.replace(' ', '_') not in path_concepts:
            return False
        if mid_lower not in path_concepts and mid_lower.replace(' ', '_') not in path_concepts:
            return False

        return True

    def fallback_selection(self, wordnet_path):
        """
        Rule-based fallback if LLM fails.

        Returns:
            dict: Fallback selection
        """
        # Conservative: middle of each range
        coarse_candidates = [(c, d) for c, d in wordnet_path if 1 <= d <= 3]
        mid_candidates = [(c, d) for c, d in wordnet_path if 4 <= d <= 6]

        # Prefer depth 2 for coarse, depth 5 for mid
        coarse = None
        for c, d in coarse_candidates:
            if d == 2:
                coarse = (c, d)
                break
        if not coarse and coarse_candidates:
            coarse = coarse_candidates[0]

        mid = None
        for c, d in mid_candidates:
            if d == 5:
                mid = (c, d)
                break
        if not mid and mid_candidates:
            mid = mid_candidates[0]

        # Handle edge cases
        if not coarse:
            coarse = wordnet_path[min(2, len(wordnet_path)-1)]
        if not mid:
            mid = wordnet_path[min(5, len(wordnet_path)-1)]

        return {
            'coarse': coarse[0],
            'coarse_depth': coarse[1],
            'mid': mid[0],
            'mid_depth': mid[1],
            'method': 'fallback'
        }

    def select_granularity_concepts(self, object_name, synset):
        """
        Select optimal concepts for each granularity level.

        Args:
            object_name: Object name (e.g., "clock")
            synset: WordNet synset

        Returns:
            dict: {
                'fine': object_name,
                'mid': mid_concept,
                'mid_depth': depth,
                'coarse': coarse_concept,
                'coarse_depth': depth,
                'method': 'llm' or 'fallback'
            }
        """
        # Get WordNet path
        wordnet_path = self.format_wordnet_path(synset)

        if len(wordnet_path) < 4:
            # Path too short, use fallback
            result = self.fallback_selection(wordnet_path)
            result['fine'] = object_name
            return result

        # Create prompt
        prompt = self.create_selection_prompt(object_name, wordnet_path)

        # Generate LLM response
        try:
            messages = [{"role": "user", "content": prompt}]
            text = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=False  # KEY FIX: Disable thinking mode!
            )
            inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=80,
                    temperature=0.7,  # Non-thinking mode settings
                    top_p=0.8,
                    top_k=20,
                    do_sample=True,  # Enable sampling for non-thinking mode
                    pad_token_id=self.tokenizer.eos_token_id
                )

            response = self.tokenizer.decode(
                outputs[0][len(inputs.input_ids[0]):],
                skip_special_tokens=True
            )

            if self.verbose:
                print(f"\nLLM Response for '{object_name}':\n{response}\n")

            # Parse response
            selection = self.extract_json_from_response(response)

            # Validate
            if self.validate_selection(selection, wordnet_path):
                selection['fine'] = object_name
                selection['method'] = 'llm'
                return selection
            else:
                if self.verbose:
                    print(f"⚠ Invalid LLM selection for '{object_name}', using fallback")

        except Exception as e:
            if self.verbose:
                print(f"⚠ LLM error for '{object_name}': {e}")

        # Fallback
        result = self.fallback_selection(wordnet_path)
        result['fine'] = object_name
        return result

    def batch_select(self, objects_with_synsets):
        """
        Process multiple objects efficiently.

        Args:
            objects_with_synsets: List of (object_name, synset) tuples

        Returns:
            dict: {object_name: selection_result}
        """
        results = {}

        for obj_name, synset in objects_with_synsets:
            results[obj_name] = self.select_granularity_concepts(obj_name, synset)

        return results


if __name__ == "__main__":
    # Quick test
    print("Testing Qwen3 Granularity Selector\n")

    selector = Qwen3GranularitySelector(device="cuda:2", verbose=True)

    # Test objects
    test_objects = [
        ("clock", wn.synsets("clock")[0]),
        ("flower", wn.synsets("flower")[0]),
        ("car", wn.synsets("car")[0])
    ]

    for obj_name, synset in test_objects:
        result = selector.select_granularity_concepts(obj_name, synset)
        print(f"\n{obj_name.upper()}:")
        print(f"  Fine: {result['fine']}")
        print(f"  Mid: {result['mid']} (depth {result['mid_depth']})")
        print(f"  Coarse: {result['coarse']} (depth {result['coarse_depth']})")
        print(f"  Method: {result['method']}")
