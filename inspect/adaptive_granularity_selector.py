#!/usr/bin/env python3
"""
Adaptive Granularity Selector using Intelligent Rules

Since LLM-based selection encounters challenges with Qwen3's thinking mode,
this implements a sophisticated rule-based approach that adaptively selects
the best concepts from depth ranges based on semantic criteria.

Improvements over fixed-depth v6.1:
- Coarse: Adaptive selection from depth 1-3 (not fixed at 4)
- Mid: Adaptive selection from depth 4-6 (not fixed semantic categories)
- Fine: Original object (unchanged)
"""

from collections import defaultdict
from nltk.corpus import wordnet as wn


class AdaptiveGranularitySelector:
    """
    Adaptive granularity selector using intelligent heuristics.

    Strategy:
    - Coarse (depth 1-3): Select most abstract, domain-level concept
      Priority: depth 2 > depth 1 > depth 3
      Reason: depth 1 is too abstract (entity, abstraction), depth 3 can be too specific

    - Mid (depth 4-6): Select most categorical concept
      Priority: depth 5 > depth 4 > depth 6
      Reason: depth 5 typically contains clear categories (vehicle, organism, structure)

    - Fine: Original object name
    """

    # Preferred concepts at each level (higher score = better)
    COARSE_PREFERRED = {
        # Depth 2 preferred concepts (good domain level)
        'object': 10,
        'matter': 10,
        'process': 10,
        'thing': 9,
        'substance': 9,
        'state': 9,
        # Depth 1 (fallback, very abstract)
        'entity': 5,
        'abstraction': 5,
        'physical_entity': 7,
        # Depth 3 (sometimes too specific)
        'whole': 6,
        'living_thing': 8,
        'artifact': 8,
    }

    MID_PREFERRED = {
        # Depth 5 preferred concepts (good categories)
        'instrumentality': 10,
        'organism': 10,
        'structure': 10,
        'covering': 9,
        'equipment': 9,
        'container': 9,
        'conveyance': 9,
        'external_body_part': 9,
        # Depth 4 (broader categories)
        'artifact': 7,
        'living_thing': 7,
        'natural_object': 7,
        # Depth 6 (more specific)
        'device': 8,
        'facility': 8,
        'clothing': 8,
    }

    def __init__(self, verbose=False):
        self.verbose = verbose

    def format_wordnet_path(self, synset):
        """Extract WordNet path with depth annotations."""
        paths = synset.hypernym_paths()
        if not paths:
            return []

        longest_path = max(paths, key=len)
        formatted_path = []
        for idx, s in enumerate(longest_path):
            concept_name = s.name().split('.')[0].replace('_', ' ')
            formatted_path.append((concept_name, idx))

        return formatted_path

    def score_concept(self, concept, depth, level='coarse'):
        """
        Score a concept based on depth and semantic quality.

        Args:
            concept: Concept name
            depth: Depth in WordNet hierarchy
            level: 'coarse' or 'mid'

        Returns:
            float: Score (higher is better)
        """
        preferred = self.COARSE_PREFERRED if level == 'coarse' else self.MID_PREFERRED

        # Base score from depth preference
        if level == 'coarse':
            depth_score = {1: 5, 2: 10, 3: 6}.get(depth, 0)
        else:  # mid
            depth_score = {4: 7, 5: 10, 6: 8}.get(depth, 0)

        # Bonus from preferred concepts
        concept_key = concept.lower().replace(' ', '_')
        semantic_score = preferred.get(concept_key, 0)

        return depth_score + semantic_score

    def select_best_from_range(self, candidates, level='coarse'):
        """
        Select best concept from candidates based on scoring.

        Args:
            candidates: List of (concept, depth) tuples
            level: 'coarse' or 'mid'

        Returns:
            (concept, depth): Best selection
        """
        if not candidates:
            return None

        # Score all candidates
        scored = [(c, d, self.score_concept(c, d, level)) for c, d in candidates]

        # Sort by score (descending)
        scored.sort(key=lambda x: x[2], reverse=True)

        if self.verbose:
            print(f"\n{level.upper()} candidates scored:")
            for c, d, s in scored:
                print(f"  {c} (d{d}): score={s}")
            print(f"  → Selected: {scored[0][0]} (d{scored[0][1]})")

        return (scored[0][0], scored[0][1])

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
                'method': 'adaptive_rules'
            }
        """
        # Get WordNet path
        wordnet_path = self.format_wordnet_path(synset)

        if len(wordnet_path) < 2:
            # Very short path, use defaults
            return {
                'fine': object_name,
                'mid': object_name,
                'mid_depth': 0,
                'coarse': wordnet_path[0][0] if wordnet_path else object_name,
                'coarse_depth': 0,
                'method': 'adaptive_rules_fallback'
            }

        # Extract candidates
        coarse_candidates = [(c, d) for c, d in wordnet_path if 1 <= d <= 3]
        mid_candidates = [(c, d) for c, d in wordnet_path if 4 <= d <= 6]

        # Select coarse
        if coarse_candidates:
            coarse_concept, coarse_depth = self.select_best_from_range(coarse_candidates, 'coarse')
        else:
            # Fallback to earliest available
            coarse_concept, coarse_depth = wordnet_path[min(2, len(wordnet_path)-1)]

        # Select mid
        if mid_candidates:
            mid_concept, mid_depth = self.select_best_from_range(mid_candidates, 'mid')
        else:
            # Fallback
            if len(wordnet_path) > 5:
                mid_concept, mid_depth = wordnet_path[5]
            elif len(wordnet_path) > 3:
                mid_concept, mid_depth = wordnet_path[-1]
            else:
                mid_concept, mid_depth = wordnet_path[-1]

        return {
            'fine': object_name,
            'mid': mid_concept,
            'mid_depth': mid_depth,
            'coarse': coarse_concept,
            'coarse_depth': coarse_depth,
            'method': 'adaptive_rules'
        }

    def batch_select(self, objects_with_synsets):
        """Process multiple objects."""
        results = {}
        for obj_name, synset in objects_with_synsets:
            results[obj_name] = self.select_granularity_concepts(obj_name, synset)
        return results


if __name__ == "__main__":
    # Quick test
    print("Testing Adaptive Granularity Selector\n")

    selector = AdaptiveGranularitySelector(verbose=True)

    test_objects = [
        ("clock", wn.synsets("clock")[0]),
        ("car", wn.synsets("car")[0]),
        ("flower", wn.synsets("flower")[0]),
    ]

    for obj_name, synset in test_objects:
        result = selector.select_granularity_concepts(obj_name, synset)
        print(f"\n{'='*60}")
        print(f"{obj_name.upper()}:")
        print(f"  Fine: {result['fine']}")
        print(f"  Mid: {result['mid']} (depth {result['mid_depth']})")
        print(f"  Coarse: {result['coarse']} (depth {result['coarse_depth']})")
        print(f"  Method: {result['method']}")
