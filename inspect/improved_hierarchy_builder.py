#!/usr/bin/env python3
"""
Improved Hierarchy Builder with Better Merging
Uses adaptive WordNet traversal for meaningful multi-granularity concept grouping.
"""
import sys
from nltk.corpus import wordnet as wn
from collections import defaultdict

# Semantic category mapping for top-level coarse categories
COARSE_SEMANTIC_CATEGORIES = {
    # Physical objects
    'physical_object': {
        'keywords': ['object', 'whole', 'artifact', 'instrumentality', 'structure', 'construction'],
        'members': []
    },
    # Living things
    'living_thing': {
        'keywords': ['organism', 'life', 'being', 'animate'],
        'members': []
    },
    # Natural entities
    'natural_object': {
        'keywords': ['natural_object', 'natural_entity', 'substance'],
        'members': []
    },
    # Abstract concepts
    'abstraction': {
        'keywords': ['abstraction', 'abstract_entity', 'attribute', 'psychological_feature'],
        'members': []
    },
    # Locations
    'location': {
        'keywords': ['location', 'place', 'region', 'area'],
        'members': []
    },
    # Events/Actions
    'event': {
        'keywords': ['event', 'act', 'action', 'activity'],
        'members': []
    },
}


def get_hypernym_paths_to_root(synset):
    """Get all hypernym paths from synset to root."""
    paths = synset.hypernym_paths()
    if not paths:
        return [[synset]]
    return paths


def get_hypernym_at_depth_from_root(synset, target_depth):
    """
    Get hypernym at specific depth from root.

    Args:
        synset: WordNet synset
        target_depth: Distance from root (0 = root 'entity', higher = more specific)

    Returns:
        Synset at that depth, or None if path too short
    """
    paths = get_hypernym_paths_to_root(synset)
    if not paths:
        return None

    # Use longest path (most specific)
    longest_path = max(paths, key=len)

    # Check if path is long enough
    if len(longest_path) <= target_depth:
        return None

    # Return synset at target depth from root
    return longest_path[target_depth]


def find_semantic_category(synset):
    """Map synset to a top-level semantic category."""
    paths = get_hypernym_paths_to_root(synset)
    if not paths:
        return 'unknown'

    # Check all hypernyms in the path
    longest_path = max(paths, key=len)
    hypernym_names = set([s.name().split('.')[0] for s in longest_path])

    # Match against semantic categories
    for category, info in COARSE_SEMANTIC_CATEGORIES.items():
        keywords = set(info['keywords'])
        if hypernym_names & keywords:  # If any overlap
            return category

    return 'entity'  # Default top-level


def build_improved_hierarchy(objects, strategy='adaptive'):
    """
    Build improved 3-level hierarchy with better merging.

    Strategies:
    - 'adaptive': Use depth-from-root (4-5 for mid, 7-9 for coarse)
    - 'semantic': Use predefined semantic categories
    - 'balanced': Hybrid approach

    Returns:
        hierarchy: dict with 'fine', 'mid', 'coarse' keys
        concept_paths: dict mapping object to [fine, mid, coarse] path
        object_to_levels: dict mapping object to level assignments
        stats: merging statistics
    """
    hierarchy = {'fine': [], 'mid': [], 'coarse': []}
    concept_paths = {}
    object_to_levels = {}

    # Extract unique object names
    object_names = []
    for obj in objects:
        if obj.get('names'):
            object_names.extend(obj['names'])

    unique_objects = list(set(object_names))

    # Statistics
    stats = {
        'total_objects': len(object_names),
        'unique_objects': len(unique_objects),
        'wordnet_found': 0,
        'wordnet_missing': 0,
        'mid_depth_used': [],
        'coarse_depth_used': []
    }

    for obj_name in unique_objects:
        obj_clean = obj_name.lower().replace(' ', '_')

        # Fine: Always original object
        hierarchy['fine'].append(obj_name)
        path = [obj_name]
        obj_to_levels = {'fine': obj_name}

        # Get WordNet synsets
        synsets = wn.synsets(obj_clean)

        if not synsets:
            # No WordNet entry - use object name for all levels
            hierarchy['mid'].append(obj_name)
            hierarchy['coarse'].append(obj_name)
            obj_to_levels['mid'] = obj_name
            obj_to_levels['coarse'] = obj_name
            path = [obj_name, obj_name, obj_name]
            stats['wordnet_missing'] += 1
        else:
            stats['wordnet_found'] += 1
            synset = synsets[0]  # Most common meaning

            if strategy == 'adaptive':
                # Mid-level: 1-2 hops up (same as before, moderate abstraction)
                mid_synset = None
                if synset.hypernyms():
                    mid_synset = synset.hypernyms()[0]  # 1 hop up
                    stats['mid_depth_used'].append(1)

                if mid_synset:
                    mid_name = mid_synset.name().split('.')[0].replace('_', ' ')
                    hierarchy['mid'].append(mid_name)
                    obj_to_levels['mid'] = mid_name
                    path.append(mid_name)
                else:
                    mid_name = obj_name
                    hierarchy['mid'].append(mid_name)
                    obj_to_levels['mid'] = mid_name
                    path.append(mid_name)

                # Coarse-level: depth 3-5 from root (higher abstraction)
                coarse_synset = None
                for depth in [4, 3, 5, 6]:  # Try in order of preference
                    coarse_synset = get_hypernym_at_depth_from_root(synset, depth)
                    if coarse_synset:
                        stats['coarse_depth_used'].append(depth)
                        break

                if coarse_synset:
                    coarse_name = coarse_synset.name().split('.')[0].replace('_', ' ')
                    hierarchy['coarse'].append(coarse_name)
                    obj_to_levels['coarse'] = coarse_name
                    path.append(coarse_name)
                else:
                    # Fallback to semantic category
                    coarse_name = find_semantic_category(synset)
                    hierarchy['coarse'].append(coarse_name)
                    obj_to_levels['coarse'] = coarse_name
                    path.append(coarse_name)

            elif strategy == 'semantic':
                # Mid-level: Use depth 3-4
                mid_synset = get_hypernym_at_depth_from_root(synset, 3)
                if not mid_synset:
                    mid_synset = get_hypernym_at_depth_from_root(synset, 4)

                if mid_synset:
                    mid_name = mid_synset.name().split('.')[0].replace('_', ' ')
                else:
                    mid_name = obj_name
                hierarchy['mid'].append(mid_name)
                obj_to_levels['mid'] = mid_name
                path.append(mid_name)

                # Coarse-level: Use semantic categories
                coarse_name = find_semantic_category(synset)
                hierarchy['coarse'].append(coarse_name)
                obj_to_levels['coarse'] = coarse_name
                path.append(coarse_name)

            elif strategy == 'balanced':
                # Mid-level: Adaptive depth 4-5
                mid_synset = get_hypernym_at_depth_from_root(synset, 4)
                if not mid_synset:
                    mid_synset = get_hypernym_at_depth_from_root(synset, 3)

                if mid_synset:
                    mid_name = mid_synset.name().split('.')[0].replace('_', ' ')
                else:
                    mid_name = obj_name
                hierarchy['mid'].append(mid_name)
                obj_to_levels['mid'] = mid_name
                path.append(mid_name)

                # Coarse-level: Mix of depth and semantic
                coarse_synset = get_hypernym_at_depth_from_root(synset, 7)
                if coarse_synset:
                    coarse_name = coarse_synset.name().split('.')[0].replace('_', ' ')
                else:
                    coarse_name = find_semantic_category(synset)
                hierarchy['coarse'].append(coarse_name)
                obj_to_levels['coarse'] = coarse_name
                path.append(coarse_name)

        concept_paths[obj_name] = path
        object_to_levels[obj_name] = obj_to_levels

    # Remove duplicates
    for level in ['fine', 'mid', 'coarse']:
        hierarchy[level] = sorted(list(set(hierarchy[level])))

    # Calculate statistics
    stats['fine_concepts'] = len(hierarchy['fine'])
    stats['mid_concepts'] = len(hierarchy['mid'])
    stats['coarse_concepts'] = len(hierarchy['coarse'])
    stats['mid_compression'] = stats['unique_objects'] / max(1, stats['mid_concepts'])
    stats['coarse_compression'] = stats['unique_objects'] / max(1, stats['coarse_concepts'])

    return hierarchy, concept_paths, object_to_levels, stats


def compare_strategies(objects):
    """Compare different strategies on same objects."""
    print("="*70)
    print("STRATEGY COMPARISON")
    print("="*70)

    strategies = ['adaptive', 'semantic', 'balanced']

    for strategy in strategies:
        hierarchy, paths, obj_levels, stats = build_improved_hierarchy(objects, strategy=strategy)

        print(f"\n{strategy.upper()} Strategy:")
        print(f"  Fine:   {stats['fine_concepts']} concepts")
        print(f"  Mid:    {stats['mid_concepts']} concepts ({stats['mid_compression']:.2f}x compression)")
        print(f"  Coarse: {stats['coarse_concepts']} concepts ({stats['coarse_compression']:.2f}x compression)")

        # Show sample mappings
        print(f"  Sample mappings:")
        for i, (obj, path) in enumerate(list(paths.items())[:5]):
            print(f"    {obj:15} → {' → '.join(path)}")


def test_improved_hierarchy():
    """Test with example objects."""
    # Mock VG objects for testing
    test_objects = [
        {'names': ['tree']}, {'names': ['tree']}, {'names': ['tree']},
        {'names': ['bush']}, {'names': ['bush']},
        {'names': ['flower']}, {'names': ['flower']},
        {'names': ['grass']},
        {'names': ['car']}, {'names': ['car']},
        {'names': ['truck']}, {'names': ['truck']},
        {'names': ['bus']},
        {'names': ['bike']},
        {'names': ['person']}, {'names': ['person']}, {'names': ['person']},
        {'names': ['man']}, {'names': ['man']},
        {'names': ['woman']},
        {'names': ['child']}, {'names': ['child']},
        {'names': ['building']},
        {'names': ['house']},
        {'names': ['road']},
        {'names': ['sky']},
        {'names': ['water']},
    ]

    print("Testing with sample objects:")
    print(f"Total objects: {len(test_objects)}")
    print(f"Unique objects: {len(set([obj['names'][0] for obj in test_objects]))}")

    compare_strategies(test_objects)


if __name__ == '__main__':
    test_improved_hierarchy()
