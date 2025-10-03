#!/usr/bin/env python3
"""
V20: Vision-Grounded VLM-Guided Granularity Selection

Key improvements over V8.1:
- Uses Vision-Language Model (Qwen2.5-VL-3B) instead of text-only LLM
- Provides actual image to VLM for visual grounding
- VLM can see objects in context and make vision-aware semantic decisions
- Enhanced prompting that asks VLM to consider visual features
- Two-stage selection with visual context
"""
import os
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor
from PIL import Image
import json
import re
from nltk.corpus import wordnet as wn


class Qwen25VLGranularitySelectorV20:
    """
    V20: Vision-grounded VLM-based granularity selector.

    Key features:
    - Visual grounding: VLM sees actual image
    - Scene graph context: objects, relationships, spatial layout
    - Two-stage selection: mid-level first, then coarse-level
    - Vision-aware reasoning: considers visual features for semantic decisions
    """

    def __init__(self, model_name="Qwen/Qwen2.5-VL-3B-Instruct", device="cuda:2", verbose=False):
        """
        Initialize Qwen2.5-VL model for vision-grounded granularity selection.

        Args:
            model_name: Hugging Face VLM model name
            device: CUDA device (e.g., "cuda:2")
            verbose: Print detailed logs
        """
        self.device_id = device.split(":")[-1] if ":" in device else "0"
        os.environ['CUDA_VISIBLE_DEVICES'] = self.device_id
        os.environ['HF_HOME'] = '/nas/jiachen/huggingface_cache'

        self.verbose = verbose
        self.model_name = model_name

        if self.verbose:
            print(f"Loading {model_name} on device {device}...")

        self.processor = AutoProcessor.from_pretrained(model_name)
        self.model = AutoModelForImageTextToText.from_pretrained(
            model_name,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            trust_remote_code=True,
            attn_implementation="flash_attention_2",
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
                - current_obj: Full object dict
        """
        objects_list = []
        current_bbox = None
        current_obj_id = None
        current_obj = None

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
                current_obj = obj

        # Limit to first 12 objects (VLM prompts are longer)
        if len(objects_list) > 12:
            objects_summary = ", ".join(objects_list[:12]) + f", ... (+{len(objects_list)-12} more)"
        else:
            objects_summary = ", ".join(objects_list)

        # Find relationships involving current object
        related_to = []
        if relationships and relationships.get('relationships') and current_obj_id:
            for rel in relationships['relationships']:
                subj_id = rel.get('subject_id')
                obj_id = rel.get('object_id')
                predicate = rel.get('predicate', 'related_to')

                if subj_id == current_obj_id:
                    for obj in all_objects:
                        if obj.get('object_id') == obj_id and obj.get('names'):
                            obj_name = obj['names'][0]
                            related_to.append(f"{predicate}-{obj_name}")
                            break
                elif obj_id == current_obj_id:
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
            'relationships_summary': relationships_summary,
            'current_obj': current_obj
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

    def create_vision_grounded_prompt(self, object_name, wordnet_path, scene_context):
        """
        Create vision-grounded two-stage selection prompt.

        This prompt asks the VLM to:
        1. Look at the actual image
        2. Consider visual features of the object
        3. Use scene context for semantic decisions
        4. Select mid and coarse concepts based on visual understanding

        Args:
            object_name: Original object name
            wordnet_path: List of (concept, depth) tuples
            scene_context: Dict with objects, bbox, relationships

        Returns:
            str: Formatted prompt for VLM
        """
        # Extract candidates for each level
        mid_candidates = [(c, d) for c, d in wordnet_path if 4 <= d <= 6]
        coarse_candidates = [(c, d) for c, d in wordnet_path if 1 <= d <= 3]

        # Format candidates
        mid_options = [f'"{c}" (depth {d})' for c, d in mid_candidates]
        coarse_options = [f'"{c}" (depth {d})' for c, d in coarse_candidates]

        # Build context section with visual grounding emphasis
        context_str = f"""**Scene Context**:
- Look at the image to see "{object_name}" and its surroundings
- Objects in scene: {scene_context['objects_summary']}
- Target object "{object_name}": {scene_context['current_bbox']}
- Relationships: {scene_context['relationships_summary']}"""

        # Build full path for reference (abbreviated)
        if len(wordnet_path) > 8:
            path_str = " → ".join([f"{c}(d={d})" for c, d in wordnet_path[:4]]) + " → ... → " + \
                       " → ".join([f"{c}(d={d})" for c, d in wordnet_path[-3:]])
        else:
            path_str = " → ".join([f"{c}(d={d})" for c, d in wordnet_path])

        prompt = f"""**CRITICAL INSTRUCTION**: YOU MUST RESPOND WITH ONLY VALID JSON. NO explanations. NO conversational text. NO markdown. ONLY the raw JSON object below.

**Task**: Select WordNet concepts for hierarchical abstraction using visual analysis.

{context_str}

**WordNet Path**: {path_str}

**Selection Task**:
MID-level (depth 4-6): {', '.join(mid_options)}
COARSE-level (depth 1-3): {', '.join(coarse_options)}

Look at the image. Consider visual appearance of "{object_name}". Select ONE concept from each level.

**REQUIRED JSON OUTPUT FORMAT** (THIS IS YOUR ENTIRE RESPONSE):
{{"mid": "concept", "mid_depth": N, "coarse": "concept", "coarse_depth": N, "reasoning": "brief visual description"}}

**CORRECT Examples**:

Example 1 (clock):
{{"mid": "instrumentality", "mid_depth": 5, "coarse": "object", "coarse_depth": 2, "reasoning": "Visible timekeeper instrument mounted on pole"}}

Example 2 (flower):
{{"mid": "plant", "mid_depth": 6, "coarse": "object", "coarse_depth": 2, "reasoning": "Living plant with visible petals in pot"}}

Example 3 (sign):
{{"mid": "clue", "mid_depth": 5, "coarse": "communication", "coarse_depth": 2, "reasoning": "Text signboard displaying store name"}}

**INCORRECT Example** (DO NOT DO THIS):
"Based on the image, I can see the clock. Here is the JSON: {{"mid": "instrumentality", ...}}"  ← WRONG! No extra text!

**NOW OUTPUT ONLY THE JSON FOR "{object_name}"** (no other text):"""

        return prompt

    def extract_json_from_response(self, response):
        """
        Extract JSON from VLM response with enhanced strategies.

        Expected format:
        {"mid": "...", "mid_depth": N, "coarse": "...", "coarse_depth": N, "reasoning": "..."}

        Args:
            response: Raw VLM response string

        Returns:
            dict or None: Parsed JSON or None if parsing fails
        """
        original_response = response

        # Strategy 1: Strip common conversational prefixes
        conversational_prefixes = [
            "here is the json", "here's the json", "here is your json",
            "the json is", "json:", "here you go", "based on",
            "looking at", "i can see", "the output is"
        ]

        response_lower = response.lower()
        for prefix in conversational_prefixes:
            if prefix in response_lower:
                idx = response_lower.index(prefix)
                response = response[idx + len(prefix):]
                break

        # Strategy 2: Strip markdown code blocks
        if "```json" in response:
            response = response.split("```json")[1].split("```")[0]
        elif "```" in response:
            response = response.split("```")[1].split("```")[0]

        # Strategy 3: Try direct JSON parse after cleaning
        try:
            data = json.loads(response.strip())
            if all(k in data for k in ['mid', 'mid_depth', 'coarse', 'coarse_depth']):
                return data
        except:
            pass

        # Strategy 4: Extract content between first { and last }
        try:
            first_brace = response.find('{')
            last_brace = response.rfind('}')
            if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
                json_str = response[first_brace:last_brace+1]
                data = json.loads(json_str)
                if all(k in data for k in ['mid', 'mid_depth', 'coarse', 'coarse_depth']):
                    return data
        except:
            pass

        # Strategy 5: Find JSON object with required keys (more flexible regex)
        json_pattern = r'\{[^{}]*"mid"[^{}]*"mid_depth"[^{}]*"coarse"[^{}]*"coarse_depth"[^{}]*\}'
        matches = re.findall(json_pattern, response, re.DOTALL)

        if matches:
            for match in matches:
                try:
                    data = json.loads(match)
                    if all(k in data for k in ['mid', 'mid_depth', 'coarse', 'coarse_depth']):
                        return data
                except:
                    continue

        # Strategy 6: Extract key-value pairs manually (last resort)
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
        Validate VLM selection against actual WordNet path.

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
        Adaptive rule-based fallback (from V7) if VLM fails.

        Returns:
            dict: Fallback selection with method='fallback'
        """
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

    def select_granularity_with_vision(self, object_name, synset, all_objects, relationships, image):
        """
        Select granularity concepts for an object with vision grounding.

        This is the main method that combines:
        - Visual understanding (VLM sees the image)
        - Scene graph context (objects, relationships)
        - WordNet semantic hierarchy

        Args:
            object_name: Original object name
            synset: WordNet synset for the object
            all_objects: List of all objects in the scene
            relationships: Scene graph relationships
            image: PIL Image object

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

        # Create vision-grounded prompt
        prompt = self.create_vision_grounded_prompt(object_name, wordnet_path, scene_context)

        if self.verbose:
            print(f"\n{'='*60}")
            print(f"Object: {object_name}")
            print(f"Prompt:\n{prompt[:400]}...")

        # Generate VLM response with image
        try:
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "image": image},
                        {"type": "text", "text": prompt}
                    ]
                }
            ]

            inputs = self.processor.apply_chat_template(
                messages,
                tokenize=True,
                add_generation_prompt=True,
                return_dict=True,
                return_tensors="pt"
            )
            inputs = inputs.to(self.model.device)

            with torch.no_grad():
                generated_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=150,  # Longer for vision reasoning
                    temperature=0.7,
                    top_p=0.8,
                    do_sample=True
                )

            generated_ids_trimmed = [
                out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
            ]
            response = self.processor.batch_decode(
                generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
            )[0]

            if self.verbose:
                print(f"Response: {response}")

            # Parse and validate
            selection = self.extract_json_from_response(response)

            if selection and self.validate_selection(selection, wordnet_path):
                selection['method'] = 'vlm'
                if self.verbose:
                    print(f"✓ VLM selection: {selection}")
                return selection
            else:
                if self.verbose:
                    print(f"⚠ VLM failed, using fallback")
                return self.fallback_selection(wordnet_path)

        except Exception as e:
            if self.verbose:
                print(f"❌ Error: {e}")
            return self.fallback_selection(wordnet_path)
