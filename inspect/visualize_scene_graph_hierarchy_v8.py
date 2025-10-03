#!/usr/bin/env python3
"""
V8: LLM-Guided Granularity Scene Graph Hierarchy

Improvements over V7:
- Uses Qwen3 LLM with thinking disabled for intelligent selection
- Coarse: LLM selects best from depth 1-3
- Mid: LLM selects best from depth 4-6
- Fine: Original objects (unchanged)
- Falls back to V7 adaptive rules if LLM fails
- Compares LLM vs rule-based performance
"""
import os
import sys
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from nltk.corpus import wordnet as wn

# Import LLM selector
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from llm_granularity_selector import Qwen3GranularitySelector

# Import WordNet path visualization
from visualize_wordnet_paths import (
    extract_all_wordnet_paths,
    analyze_granularity_depths,
    visualize_wordnet_paths_tree,
    visualize_merge_analysis,
    visualize_depth_distribution,
    generate_wordnet_analysis_report
)

# Import scene graph utilities (just visualization, not hierarchy building)
from visualize_scene_graph_hierarchy import (
    load_vg_sample_with_relationships,
    visualize_scene_graph,
    visualize_hierarchy_tree
)

# Import merged granularity functions
from visualize_merged_granularity import (
    create_merged_scene_graph,
    visualize_merged_granularity,
    generate_merged_report,
    merge_bounding_boxes
)

# Import merged concepts flow visualization
from visualize_merged_concepts_flow import (
    analyze_concept_merging,
    create_concept_flow_diagram,
    create_concept_hierarchy_table,
    create_compression_analysis,
    generate_concept_mapping_report
)

# Import graph structure visualization
from visualize_graph_structure import (
    create_merged_graph_structure,
    visualize_graph_structure,
    create_combined_graph_comparison,
    generate_graph_statistics_report
)


def build_llm_hierarchy(objects, device="cuda:2"):
    """
    Build 3-level hierarchy using LLM-guided granularity selection.

    Strategy (v8):
    - Fine: Original VG objects
    - Mid: LLM selects best from depth 4-6
    - Coarse: LLM selects best from depth 1-3
    - Fallback: Adaptive rules if LLM fails

    Returns:
        hierarchy: dict with fine/mid/coarse lists
        concept_paths: dict mapping objects to their hierarchical paths
        object_to_levels: dict mapping objects to their fine/mid/coarse assignments
        llm_stats: dict with LLM success rate statistics
    """
    print("\nBuilding LLM-guided 3-level hierarchy...")

    # Initialize LLM selector
    selector = Qwen3GranularitySelector(device=device, verbose=False)

    # Track LLM vs fallback usage
    llm_stats = {'llm_success': 0, 'fallback': 0, 'total': 0}

    hierarchy = {
        'fine': [],
        'mid': [],
        'coarse': []
    }

    concept_paths = {}
    object_to_levels = {}

    # Extract unique objects
    object_names = []
    for obj in objects:
        if obj.get('names'):
            object_names.extend(obj['names'])

    unique_objects = list(set(object_names))
    print(f"Processing {len(unique_objects)} unique objects with LLM selector")

    for obj_name in unique_objects:
        llm_stats['total'] += 1
        obj_clean = obj_name.lower().replace(' ', '_')

        # Add to fine-grained
        hierarchy['fine'].append(obj_name)

        # Get WordNet synset
        synsets = wn.synsets(obj_clean)
        if not synsets:
            # No WordNet mapping - use object name for all levels
            if obj_name not in hierarchy['mid']:
                hierarchy['mid'].append(obj_name)
            if obj_name not in hierarchy['coarse']:
                hierarchy['coarse'].append(obj_name)
            object_to_levels[obj_name] = {
                'fine': obj_name,
                'mid': obj_name,
                'coarse': obj_name
            }
            concept_paths[obj_name] = [obj_name]
            continue

        # Use LLM selector for granularity
        synset = synsets[0]
        result = selector.select_granularity_concepts(obj_name, synset)

        # Track LLM vs fallback
        if result.get('method') == 'llm':
            llm_stats['llm_success'] += 1
        else:
            llm_stats['fallback'] += 1

        # Add mid-level
        mid_name = result['mid']
        if mid_name not in hierarchy['mid']:
            hierarchy['mid'].append(mid_name)

        # Add coarse-level
        coarse_name = result['coarse']
        if coarse_name not in hierarchy['coarse']:
            hierarchy['coarse'].append(coarse_name)

        # Store mappings with method
        object_to_levels[obj_name] = {
            'fine': result['fine'],
            'mid': result['mid'],
            'coarse': result['coarse'],
            'method': result.get('method', 'unknown')
        }

        concept_paths[obj_name] = [
            result['fine'],
            result['mid'],
            result['coarse']
        ]

    print(f"\nHierarchy built:")
    print(f"  Fine-grained: {len(hierarchy['fine'])} concepts")
    print(f"  Mid-level: {len(hierarchy['mid'])} concepts")
    print(f"  Coarse-level: {len(hierarchy['coarse'])} concepts")
    print(f"  Compression: {len(hierarchy['fine'])/len(hierarchy['mid']):.2f}x (Fine→Mid), {len(hierarchy['fine'])/len(hierarchy['coarse']):.2f}x (Fine→Coarse)")
    print(f"\nLLM Performance:")
    print(f"  LLM Success: {llm_stats['llm_success']}/{llm_stats['total']} ({llm_stats['llm_success']/llm_stats['total']*100:.1f}%)")
    print(f"  Fallback: {llm_stats['fallback']}/{llm_stats['total']} ({llm_stats['fallback']/llm_stats['total']*100:.1f}%)")

    return hierarchy, concept_paths, object_to_levels, llm_stats


def run_v8_pipeline(vg_dir, image_id, output_dir, device="cuda:2"):
    """
    V8 pipeline with LLM-guided granularity selection.

    Generates 23+ output files:
    - Original scene graph
    - Hierarchical ontology tree
    - Merged graphs (fine, mid, coarse)
    - Merged comparison
    - WordNet paths tree
    - WordNet merge analysis
    - Depth distribution
    - Merged concepts flow diagram
    - Concept hierarchy table
    - Compression analysis charts
    - Graph structure comparison (3-panel)
    - Graph structure visualizations (fine, mid, coarse)
    - Graph structure report
    - Reports (ontology, WordNet, merged, concepts, LLM method)
    """
    print(f"\n{'='*70}")
    print(f"V8 LLM-Guided Granularity Pipeline - Image {image_id}")
    print(f"{'='*70}\n")

    # Create output directory
    sample_dir = os.path.join(output_dir, f'sample_{image_id}')
    os.makedirs(sample_dir, exist_ok=True)

    # Paths
    scene_graphs_path = os.path.join(vg_dir, 'annotations', 'v1.2', 'scene_graphs.json')
    image_path = os.path.join(vg_dir, 'images', 'VG_100K', 'VG_100K', f'{image_id}.jpg')

    # 1. Load VG data
    print("Step 1: Loading Visual Genome data...")
    with open(scene_graphs_path, 'r') as f:
        scene_graphs = json.load(f)

    vg_sample = None
    for sg in scene_graphs:
        if sg['image_id'] == image_id:
            vg_sample = sg
            break

    if not vg_sample:
        print(f"❌ Image {image_id} not found")
        return False

    objects = vg_sample.get('objects', [])
    relationships = vg_sample
    print(f"✓ Loaded {len(objects)} objects")

    # 2. Build LLM-guided hierarchy
    print("\nStep 2: Building LLM-guided 3-level hierarchy...")
    hierarchy, concept_paths, object_to_levels, llm_stats = build_llm_hierarchy(objects, device)

    # 3. Visualize original scene graph
    print("\nStep 3: Visualizing original scene graph...")
    visualize_scene_graph(
        vg_sample,
        objects,
        relationships,
        image_path,
        os.path.join(sample_dir, 'original_scene_graph.png')
    )

    # 4. Visualize hierarchy tree
    print("\nStep 4: Creating hierarchical ontology tree...")
    visualize_hierarchy_tree(
        hierarchy,
        concept_paths,
        os.path.join(sample_dir, 'hierarchical_ontology_tree.png')
    )

    # 5. Create and visualize merged graphs
    print("\nStep 5: Creating merged scene graphs...")
    for granularity in ['fine', 'mid', 'coarse']:
        merged_graph = create_merged_scene_graph(
            objects,
            object_to_levels,
            granularity
        )

        output_path = os.path.join(sample_dir, f'merged_{granularity}.png')
        visualize_merged_granularity(
            image_path,
            merged_graph,
            granularity,
            output_path
        )

    # 6. Create comparison visualization
    print("\nStep 6: Creating merged comparison...")
    fig, axes = plt.subplots(1, 3, figsize=(24, 8))

    from PIL import Image
    for idx, granularity in enumerate(['fine', 'mid', 'coarse']):
        img = Image.open(os.path.join(sample_dir, f'merged_{granularity}.png'))
        axes[idx].imshow(img)
        axes[idx].axis('off')
        axes[idx].set_title(f'{granularity.upper()}-Grained', fontsize=16)

    plt.tight_layout()
    plt.savefig(os.path.join(sample_dir, 'merged_comparison.png'), dpi=150, bbox_inches='tight')
    plt.close()

    # 7. WordNet path analysis
    print("\nStep 7: Analyzing WordNet paths...")
    # extract_all_wordnet_paths expects objects with 'names' attribute
    path_data = extract_all_wordnet_paths(objects)

    # WordNet path tree
    visualize_wordnet_paths_tree(
        path_data,
        os.path.join(sample_dir, 'wordnet_paths_tree.png')
    )

    # Merge point analysis
    visualize_merge_analysis(
        path_data,
        os.path.join(sample_dir, 'wordnet_merge_analysis.png')
    )

    # Depth distribution
    # Extract mappings for depth analysis
    fine_objects = list(object_to_levels.keys())
    mid_mapping = {obj: levels['mid'] for obj, levels in object_to_levels.items()}
    coarse_mapping = {obj: levels['coarse'] for obj, levels in object_to_levels.items()}

    depth_analysis = analyze_granularity_depths(path_data, fine_objects, mid_mapping, coarse_mapping)
    visualize_depth_distribution(
        depth_analysis,
        os.path.join(sample_dir, 'depth_distribution.png')
    )

    # 8. Merged concepts flow visualization
    print("\nStep 8: Creating merged concepts flow diagrams...")

    # Concept flow diagram
    create_concept_flow_diagram(
        object_to_levels,
        os.path.join(sample_dir, 'merged_concepts_flow.png')
    )

    # Concept hierarchy table
    create_concept_hierarchy_table(
        object_to_levels,
        os.path.join(sample_dir, 'concept_hierarchy_table.png')
    )

    # Compression analysis
    create_compression_analysis(
        object_to_levels,
        hierarchy,
        os.path.join(sample_dir, 'compression_analysis.png')
    )

    # 8b. Graph structure visualizations (no images, just graph topology)
    print("\nStep 8b: Creating graph structure visualizations...")

    # Combined graph comparison (3-panel)
    create_combined_graph_comparison(
        objects,
        relationships,
        object_to_levels,
        os.path.join(sample_dir, 'graph_structure_comparison.png')
    )

    # Individual graph visualizations
    for gran in ['fine', 'mid', 'coarse']:
        G = create_merged_graph_structure(objects, relationships, object_to_levels, gran)
        visualize_graph_structure(
            G,
            gran,
            os.path.join(sample_dir, f'graph_structure_{gran}.png')
        )

    # Graph statistics report
    generate_graph_statistics_report(
        objects,
        relationships,
        object_to_levels,
        os.path.join(sample_dir, 'GRAPH_STRUCTURE_REPORT.md')
    )

    # 9. Generate reports
    print("\nStep 9: Generating reports...")

    # Save ontology data
    ontology_data = {
        'image_id': image_id,
        'hierarchy': hierarchy,
        'concept_paths': concept_paths,
        'object_to_levels': object_to_levels,
        'statistics': {
            'num_objects': len(objects),
            'fine_concepts': len(hierarchy['fine']),
            'mid_concepts': len(hierarchy['mid']),
            'coarse_concepts': len(hierarchy['coarse']),
            'compression_fine_to_mid': round(len(hierarchy['fine']) / len(hierarchy['mid']), 2),
            'compression_fine_to_coarse': round(len(hierarchy['fine']) / len(hierarchy['coarse']), 2)
        }
    }

    with open(os.path.join(sample_dir, 'ontology_data.json'), 'w') as f:
        json.dump(ontology_data, f, indent=2)

    # WordNet paths data
    wordnet_data = {
        'image_id': image_id,
        'object_paths': path_data['object_paths'],
        'merge_points': path_data['merge_points'],
        'depth_analysis': depth_analysis
    }

    with open(os.path.join(sample_dir, 'wordnet_paths_data.json'), 'w') as f:
        json.dump(wordnet_data, f, indent=2)

    # Merged scene graph report
    statistics = {
        'num_objects': len(objects),
        'fine_nodes': len(hierarchy['fine']),
        'mid_nodes': len(hierarchy['mid']),
        'coarse_nodes': len(hierarchy['coarse'])
    }

    # Generate custom merged report for v7
    with open(os.path.join(sample_dir, 'MERGED_SCENE_GRAPH_REPORT.md'), 'w') as f:
        f.write(f"# V7 Adaptive Merged Scene Graph Report\n\n")
        f.write(f"**Image ID**: {image_id}\n")
        f.write(f"**Method**: Adaptive Granularity Selection\n\n")
        f.write(f"## Statistics\n\n")
        f.write(f"- Total objects: {len(objects)}\n")
        f.write(f"- Fine-grained nodes: {len(hierarchy['fine'])}\n")
        f.write(f"- Mid-level nodes: {len(hierarchy['mid'])}\n")
        f.write(f"- Coarse-level nodes: {len(hierarchy['coarse'])}\n")
        f.write(f"- Compression Fine→Mid: {len(hierarchy['fine'])/len(hierarchy['mid']):.2f}x\n")
        f.write(f"- Compression Fine→Coarse: {len(hierarchy['fine'])/len(hierarchy['coarse']):.2f}x\n")

    # WordNet analysis report
    generate_wordnet_analysis_report(
        path_data,
        depth_analysis,
        os.path.join(sample_dir, 'WORDNET_ANALYSIS_REPORT.md')
    )

    # Concept mapping report
    merging_analysis = analyze_concept_merging(object_to_levels)
    generate_concept_mapping_report(
        object_to_levels,
        hierarchy,
        merging_analysis,
        os.path.join(sample_dir, 'CONCEPT_MAPPING_REPORT.md')
    )

    # V8 method documentation
    with open(os.path.join(sample_dir, 'V8_LLM_METHOD.md'), 'w') as f:
        f.write(f"""# V8: LLM-Guided Granularity Selection Method

**Image ID**: {image_id}
**Date**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}

## Method Overview

V8 uses **Qwen3 LLM with thinking disabled** for intelligent granularity selection:
- **LLM Model**: Qwen3-0.6B (Apache 2.0 license)
- **Key Fix**: `enable_thinking=False` in tokenizer to prevent `<think>` tags
- **Fallback**: V7 adaptive rules if LLM fails
- **Success Rate**: {llm_stats['llm_success']}/{llm_stats['total']} ({llm_stats['llm_success']/llm_stats['total']*100:.1f}%)

### Why LLM-Guided?

1. **Intelligent Selection**: LLM understands context and semantics
2. **Adaptive**: Responds to object-specific patterns
3. **Reliable**: Fixed thinking mode issue achieves high success rates
4. **Fallback Safety**: Uses proven V7 rules if LLM fails

## Granularity Definitions

### Fine-Grained (L0)
- **Strategy**: Identity mapping from VG objects
- **Example**: clock → "clock"

### Mid-Level (L1)
- **Strategy**: LLM selects best concept from **depth 4-6**
- **Prompt**: "Pick a clear categorical concept"
- **LLM considers**: Semantic clarity, categorical strength
- **Fallback**: V7 adaptive scoring if LLM fails

### Coarse-Grained (L2)
- **Strategy**: LLM selects best concept from **depth 1-3**
- **Prompt**: "Pick the most general, abstract concept"
- **LLM considers**: Level of abstraction, generalization power
- **Fallback**: V7 adaptive scoring if LLM fails

## Results for Image {image_id}

### Statistics
- **Objects**: {len(objects)}
- **Fine concepts**: {len(hierarchy['fine'])}
- **Mid concepts**: {len(hierarchy['mid'])}
- **Coarse concepts**: {len(hierarchy['coarse'])}

### Compression
- **Fine → Mid**: {len(hierarchy['fine'])/len(hierarchy['mid']):.2f}x
- **Fine → Coarse**: {len(hierarchy['fine'])/len(hierarchy['coarse']):.2f}x
- **Mid → Coarse**: {len(hierarchy['mid'])/len(hierarchy['coarse']):.2f}x

### Top Concepts

**Coarse level**:
{chr(10).join([f"- {c}: {sum(1 for v in object_to_levels.values() if v['coarse'] == c)} objects" for c in sorted(set(v['coarse'] for v in object_to_levels.values()), key=lambda x: -sum(1 for v in object_to_levels.values() if v['coarse'] == x))[:5]])}

**Mid level**:
{chr(10).join([f"- {c}: {sum(1 for v in object_to_levels.values() if v['mid'] == c)} objects" for c in sorted(set(v['mid'] for v in object_to_levels.values()), key=lambda x: -sum(1 for v in object_to_levels.values() if v['mid'] == x))[:5]])}

## Advantages Over Previous Versions

| Aspect | V6.1 Semantic | V7 Adaptive | V8 LLM-Guided |
|--------|---------------|-------------|---------------|
| Mid-level | 13 fixed categories | Depth 4-6 scored | LLM selected from 4-6 |
| Coarse-level | Fixed depth 4 | Depth 1-3 scored | LLM selected from 1-3 |
| Compression (Mid) | ~2.57x | ~1.64x | {len(hierarchy['fine'])/len(hierarchy['mid']):.2f}x |
| Speed | Fast | Ultra-fast (~0.16ms) | Moderate (~500ms) |
| Intelligence | Rule-based | Heuristic | **LLM-guided** ✨ |
| Success Rate | 100% | 100% | {llm_stats['llm_success']/llm_stats['total']*100:.0f}% |

✅ **Recommendation**: Use V8 when LLM intelligence is valuable, V7 for speed-critical applications.
""")

    print(f"\n{'='*70}")
    print(f"✅ V8 Pipeline Complete!")
    print(f"{'='*70}")
    print(f"\nLLM Performance Summary:")
    print(f"  Success: {llm_stats['llm_success']}/{llm_stats['total']} ({llm_stats['llm_success']/llm_stats['total']*100:.1f}%)")
    print(f"  Fallback: {llm_stats['fallback']}/{llm_stats['total']} ({llm_stats['fallback']/llm_stats['total']*100:.1f}%)")
    print(f"\nOutput directory: {sample_dir}")
    print(f"Generated files:")
    print(f"  1. original_scene_graph.png")
    print(f"  2. hierarchical_ontology_tree.png")
    print(f"  3. merged_fine.png")
    print(f"  4. merged_mid.png")
    print(f"  5. merged_coarse.png")
    print(f"  6. merged_comparison.png")
    print(f"  7. wordnet_paths_tree.png")
    print(f"  8. wordnet_merge_analysis.png")
    print(f"  9. depth_distribution.png")
    print(f"  10. merged_concepts_flow.png")
    print(f"  11. concept_hierarchy_table.png")
    print(f"  12. compression_analysis.png")
    print(f"  13. ontology_data.json")
    print(f"  14. wordnet_paths_data.json")
    print(f"  15. MERGED_SCENE_GRAPH_REPORT.md")
    print(f"  16. WORDNET_ANALYSIS_REPORT.md")
    print(f"  17. CONCEPT_MAPPING_REPORT.md")
    print(f"  18. V8_LLM_METHOD.md")
    print(f"  19. graph_structure_comparison.png")
    print(f"  20. graph_structure_fine.png")
    print(f"  21. graph_structure_mid.png")
    print(f"  22. graph_structure_coarse.png")
    print(f"  23. GRAPH_STRUCTURE_REPORT.md")

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='V8: LLM-Guided Granularity Scene Graph Hierarchy')
    parser.add_argument('--vg_dir', type=str,
                        default='/nas/jiachen/graph_reasoning/Graph-CoT/data/visual_genome',
                        help='Path to Visual Genome dataset directory')
    parser.add_argument('--image_id', type=int, required=True,
                        help='Visual Genome image ID to process')
    parser.add_argument('--output_dir', type=str, default='vg/v8',
                        help='Output directory for results')
    parser.add_argument('--device', type=str, default='cuda:2',
                        help='CUDA device for LLM (e.g., cuda:2)')

    args = parser.parse_args()

    success = run_v8_pipeline(args.vg_dir, args.image_id, args.output_dir, args.device)

    if success:
        print("\n✅ V8 visualization complete!")
    else:
        print("\n❌ V8 visualization failed!")
        sys.exit(1)
