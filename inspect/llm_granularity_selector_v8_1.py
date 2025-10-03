#!/usr/bin/env python3
"""
V8.1: Context-Aware LLM-Guided Granularity Selection

Improvements over V8:
- Provides full scene graph context (objects + relationships + bboxes)
- Two-stage selection: mid first, then coarse
- Goal-oriented prompting: emphasizes traceable abstraction levels
- Spatial and relational context for each object
"""
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
import re
from collections import defaultdict
from nltk.corpus import wordnet as wn


class Qwen3GranularitySelectorV8_1:
    """
    V8.1: Context-aware LLM-based granularity selector.

    Key features:
    - Scene graph context: all objects, relationships, spatial layout
    - Two-stage selection: mid-level first, then coarse-level
    - Goal-oriented: creates traceable coarse → mid → fine hierarchy
    """

    def __init__(self, model_name="Qwen/Qwen3-0.6B", device="cuda:2", verbose=False):
        """
        Initialize Qwen3 model for context-aware granularity selection.

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

    def format_scene_context(self, all_objects, relationships, current_object_name):
        """
        Format scene graph context for the prompt.

        Args:
            all_objects: List of all objects in the scene
            relationships: Scene graph relationships
            current_object_name: The object we're selecting granularity for

        Returns:
            dict with:
                - objects_summary: Brief summary of all objects
                - current_bbox: Spatial info for current object
                - relationships_summary: Relevant relationships
        """
        # Create objects summary
        objects_list = []
        current_bbox = None
        current_obj_id = None

        for obj in all_objects:
            if not obj.get('names'):
                continue

            obj_name = obj['names'][0]
            x = obj.get('x', 0)
            y = obj.get('y', 0)
            w = obj.get('w', 0)
            h = obj.get('h', 0)

            objects_list.append(f"{obj_name}@({x},{y},{w}x{h})")

            if obj_name == current_object_name:
                current_bbox = f"position ({x},{y}), size {w}x{h}"
                current_obj_id = obj.get('object_id')

        # Limit to first 15 objects to avoid overly long prompts
        if len(objects_list) > 15:
            objects_summary = ", ".join(objects_list[:15]) + f", ... (+{len(objects_list)-15} more)"
        else:
            objects_summary = ", ".join(objects_list)

        # Find relationships involving current object
        related_to = []
        if relationships and relationships.get('relationships') and current_obj_id:
            for rel in relationships['relationships']:
                subj_id = rel.get('subject_id')
                obj_id = rel.get('object_id')
                predicate = rel.get('predicate', 'related_to')

                # Find object names
                if subj_id == current_obj_id:
                    # Current object is subject
                    for obj in all_objects:
                        if obj.get('object_id') == obj_id and obj.get('names'):
                            obj_name = obj['names'][0]
                            related_to.append(f"{predicate}-{obj_name}")
                            break
                elif obj_id == current_obj_id:
                    # Current object is object
                    for obj in all_objects:
                        if obj.get('object_id') == subj_id and obj.get('names'):
                            subj_name = obj['names'][0]
                            related_to.append(f"{subj_name}-{predicate}")
                            break

        # Limit relationships
        if len(related_to) > 5:
            relationships_summary = ", ".join(related_to[:5]) + f" (+{len(related_to)-5} more)"
        else:
            relationships_summary = ", ".join(related_to) if related_to else "none"

        return {
            'objects_summary': objects_summary,
            'current_bbox': current_bbox or "unknown",
            'relationships_summary': relationships_summary
        }

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

    def create_two_stage_prompt(self, object_name, wordnet_path, scene_context):
        """
        Create context-aware two-stage selection prompt.

        Stage 1: Select mid-level concept (depth 4-6)
        Stage 2: Select coarse-level concept (depth 1-3) based on mid selection

        Args:
            object_name: Original object name
            wordnet_path: List of (concept, depth) tuples
            scene_context: Dict with objects, bbox, relationships

        Returns:
            str: Formatted prompt
        """
        # Extract candidates for each level
        mid_candidates = [(c, d) for c, d in wordnet_path if 4 <= d <= 6]
        coarse_candidates = [(c, d) for c, d in wordnet_path if 1 <= d <= 3]

        # Format candidates
        mid_options = [f'"{c}" (depth {d})' for c, d in mid_candidates]
        coarse_options = [f'"{c}" (depth {d})' for c, d in coarse_candidates]

        # Build context section
        context_str = f"""**Scene Context**:
- Objects in scene: {scene_context['objects_summary']}
- Current object "{object_name}": {scene_context['current_bbox']}
- Relationships: {scene_context['relationships_summary']}"""

        # Build full path for reference
        path_str = " → ".join([f"{c}(d={d})" for c, d in wordnet_path])

        prompt = f"""**Task**: Create a 3-level hierarchical abstraction of scene graphs using WordNet ontology.

**Goal**: Select concepts that create meaningful, traceable abstraction levels. The hierarchy should:
1. Preserve high-level semantic information at the coarse level
2. Allow progressive refinement: coarse → mid → fine for more detail
3. Group similar objects meaningfully at each level

{context_str}

**WordNet Path**: {path_str}

**Two-Stage Selection**:

**STAGE 1 - Select MID-level concept (depth 4-6)**:
Options: {', '.join(mid_options)}

Question: Which concept best represents "{object_name}" as a mid-level category in this scene context?
Consider: What functional/semantic category does this object belong to?

**STAGE 2 - Select COARSE-level concept (depth 1-3)**:
Options: {', '.join(coarse_options)}

Question: Which concept provides appropriate high-level abstraction?
Consider: What is the most general meaningful domain for grouping similar objects?

**Output JSON format**:
{{"mid": "concept_name", "mid_depth": depth_number, "coarse": "concept_name", "coarse_depth": depth_number, "reasoning": "brief explanation"}}

**Example for "clock"**:
{{"mid": "instrumentality", "mid_depth": 5, "coarse": "object", "coarse_depth": 2, "reasoning": "Clock is an instrument/tool (mid) and a physical object (coarse)"}}

**Now select for "{object_name}"**:"""

        return prompt

    def extract_json_from_response(self, response):
        """
        Extract JSON from LLM response with V8.1 format.

        Expected format:
        {"mid": "...", "mid_depth": N, "coarse": "...", "coarse_depth": N, "reasoning": "..."}

        Args:
            response: Raw LLM response string

        Returns:
            dict or None: Parsed JSON or None if parsing fails
        """
        # Try direct JSON parse first
        try:
            data = json.loads(response.strip())
            # Validate structure
            if all(k in data for k in ['mid', 'mid_depth', 'coarse', 'coarse_depth']):
                return data
        except:
            pass

        # Try to find JSON object in response
        json_pattern = r'\{[^}]*"mid"[^}]*"coarse"[^}]*\}'
        matches = re.findall(json_pattern, response, re.DOTALL)

        if matches:
            for match in matches:
                try:
                    data = json.loads(match)
                    if all(k in data for k in ['mid', 'mid_depth', 'coarse', 'coarse_depth']):
                        return data
                except:
                    continue

        # Try to extract key-value pairs
        try:
            mid_match = re.search(r'"mid"\s*:\s*"([^"]+)"', response)
            mid_depth_match = re.search(r'"mid_depth"\s*:\s*(\d+)', response)
            coarse_match = re.search(r'"coarse"\s*:\s*"([^"]+)"', response)
            coarse_depth_match = re.search(r'"coarse_depth"\s*:\s*(\d+)', response)
            reasoning_match = re.search(r'"reasoning"\s*:\s*"([^"]+)"', response)

            if all([mid_match, mid_depth_match, coarse_match, coarse_depth_match]):
                return {
                    "mid": mid_match.group(1),
                    "mid_depth": int(mid_depth_match.group(1)),
                    "coarse": coarse_match.group(1),
                    "coarse_depth": int(coarse_depth_match.group(1)),
                    "reasoning": reasoning_match.group(1) if reasoning_match else ""
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

        required_keys = ['mid', 'mid_depth', 'coarse', 'coarse_depth']
        if not all(k in selection for k in required_keys):
            return False

        # Check depth ranges
        if not (4 <= selection['mid_depth'] <= 6):
            return False
        if not (1 <= selection['coarse_depth'] <= 3):
            return False

        # Check if concepts exist in path
        path_concepts = {c.lower(): d for c, d in wordnet_path}

        mid_lower = selection['mid'].lower()
        coarse_lower = selection['coarse'].lower()

        if mid_lower not in path_concepts and mid_lower.replace(' ', '_') not in path_concepts:
            return False
        if coarse_lower not in path_concepts and coarse_lower.replace(' ', '_') not in path_concepts:
            return False

        return True

    def fallback_selection(self, wordnet_path):
        """
        Adaptive rule-based fallback (from V7) if LLM fails.

        Returns:
            dict: Fallback selection with method='fallback'
        """
        # Score each depth level
        def score_concept(concept, depth, target_depth, semantic_bonuses):
            score = 0

            # Depth preference
            if depth == target_depth:
                score += 10
            elif abs(depth - target_depth) == 1:
                score += 7 - abs(depth - target_depth)

            # Semantic bonuses
            concept_lower = concept.lower()
            for keyword, bonus in semantic_bonuses.items():
                if keyword in concept_lower:
                    score += bonus

            return score

        # Mid-level: prefer depth 5
        mid_semantic = {
            'instrumentality': 10, 'organism': 10, 'structure': 10,
            'artifact': 8, 'living_thing': 8, 'facility': 8
        }

        mid_candidates = [(c, d) for c, d in wordnet_path if 4 <= d <= 6]
        if mid_candidates:
            mid_scored = [(c, d, score_concept(c, d, 5, mid_semantic)) for c, d in mid_candidates]
            mid_best = max(mid_scored, key=lambda x: x[2])
            mid_concept, mid_depth = mid_best[0], mid_best[1]
        else:
            mid_concept, mid_depth = wordnet_path[-1][0], wordnet_path[-1][1]

        # Coarse-level: prefer depth 2
        coarse_semantic = {
            'object': 10, 'matter': 10, 'abstraction': 8,
            'living_thing': 8, 'entity': 5
        }

        coarse_candidates = [(c, d) for c, d in wordnet_path if 1 <= d <= 3]
        if coarse_candidates:
            coarse_scored = [(c, d, score_concept(c, d, 2, coarse_semantic)) for c, d in coarse_candidates]
            coarse_best = max(coarse_scored, key=lambda x: x[2])
            coarse_concept, coarse_depth = coarse_best[0], coarse_best[1]
        else:
            coarse_concept, coarse_depth = wordnet_path[min(2, len(wordnet_path)-1)]

        return {
            'mid': mid_concept,
            'mid_depth': mid_depth,
            'coarse': coarse_concept,
            'coarse_depth': coarse_depth,
            'method': 'fallback',
            'reasoning': 'Adaptive rule-based fallback (V7)'
        }

    def select_granularity_with_context(self, object_name, synset, all_objects, relationships):
        """
        Select granularity concepts for an object with full scene context.

        Args:
            object_name: Original object name
            synset: WordNet synset for the object
            all_objects: List of all objects in the scene
            relationships: Scene graph relationships

        Returns:
            dict with mid, mid_depth, coarse, coarse_depth, method, reasoning
        """
        # Format WordNet path
        wordnet_path = self.format_wordnet_path(synset)
        if not wordnet_path:
            return {
                'mid': object_name,
                'mid_depth': 0,
                'coarse': object_name,
                'coarse_depth': 0,
                'method': 'no_wordnet',
                'reasoning': 'No WordNet path found'
            }

        # Format scene context
        scene_context = self.format_scene_context(all_objects, relationships, object_name)

        # Create prompt
        prompt = self.create_two_stage_prompt(object_name, wordnet_path, scene_context)

        if self.verbose:
            print(f"\n{'='*60}")
            print(f"Object: {object_name}")
            print(f"Prompt:\n{prompt[:500]}...")

        # Generate LLM response
        try:
            messages = [
                {"role": "system", "content": "You are a helpful assistant for semantic hierarchy construction."},
                {"role": "user", "content": prompt}
            ]

            text = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=False  # Critical: disable thinking mode
            )

            inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

            outputs = self.model.generate(
                **inputs,
                max_new_tokens=100,
                temperature=0.7,
                top_p=0.8,
                top_k=20,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )

            response = self.tokenizer.decode(outputs[0][len(inputs['input_ids'][0]):], skip_special_tokens=True)

            if self.verbose:
                print(f"Response: {response}")

            # Parse and validate
            selection = self.extract_json_from_response(response)

            if selection and self.validate_selection(selection, wordnet_path):
                selection['method'] = 'llm'
                if self.verbose:
                    print(f"✓ LLM selection: {selection}")
                return selection
            else:
                if self.verbose:
                    print(f"⚠ LLM failed, using fallback")
                return self.fallback_selection(wordnet_path)

        except Exception as e:
            if self.verbose:
                print(f"❌ Error: {e}")
            return self.fallback_selection(wordnet_path)
