#!/usr/bin/env python3
"""
V8.1: Context-Aware LLM-Guided Granularity Scene Graph Hierarchy

Improvements over V8:
- Provides full scene graph context (objects + relationships + bboxes)
- Two-stage selection: mid-level first, then coarse-level
- Goal-oriented prompting: emphasizes traceable abstraction (coarse → mid → fine)
- Spatial and relational context for each object decision
- Uses Qwen3 LLM with enhanced contextual prompting
- Falls back to V7 adaptive rules if LLM fails
"""
import os
import sys
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from nltk.corpus import wordnet as wn

# Import V8.1 context-aware LLM selector
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from llm_granularity_selector_v8_1 import Qwen3GranularitySelectorV8_1

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


def build_llm_hierarchy_v8_1(objects, relationships, device="cuda:2"):
    """
    Build 3-level hierarchy using context-aware LLM-guided granularity selection.

    Strategy (v8.1):
    - Fine: Original VG objects
    - Mid: LLM selects best from depth 4-6 with scene context
    - Coarse: LLM selects best from depth 1-3 with scene context
    - Two-stage selection: mid first, then coarse
    - Context: Full scene graph (objects, relationships, bboxes)
    - Fallback: V7 adaptive rules if LLM fails

    Returns:
        hierarchy: dict with fine/mid/coarse lists
        concept_paths: dict mapping objects to their hierarchical paths
        object_to_levels: dict mapping objects to their fine/mid/coarse assignments
        llm_stats: dict with LLM success rate statistics
    """
    print("\nBuilding V8.1 context-aware LLM-guided 3-level hierarchy...")

    # Initialize V8.1 context-aware LLM selector
    selector = Qwen3GranularitySelectorV8_1(device=device, verbose=False)

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

        # Use V8.1 context-aware LLM selector
        synset = synsets[0]
        result = selector.select_granularity_with_context(
            obj_name,
            synset,
            objects,
            relationships
        )

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

        # Store mappings with method and reasoning
        object_to_levels[obj_name] = {
            'fine': obj_name,
            'mid': result['mid'],
            'coarse': result['coarse'],
            'method': result.get('method', 'unknown'),
            'reasoning': result.get('reasoning', '')
        }

        concept_paths[obj_name] = [
            obj_name,
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


def run_v8_1_pipeline(vg_dir, image_id, output_dir, device="cuda:2"):
    """
    V8.1 pipeline with context-aware LLM-guided granularity selection.

    Generates 24+ output files:
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
    - Reports (ontology, WordNet, merged, concepts, V8.1 method with reasoning)
    """
    print(f"\n{'='*70}")
    print(f"V8.1 Context-Aware LLM-Guided Pipeline - Image {image_id}")
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

    # 2. Build V8.1 context-aware LLM-guided hierarchy
    print("\nStep 2: Building V8.1 context-aware 3-level hierarchy...")
    hierarchy, concept_paths, object_to_levels, llm_stats = build_llm_hierarchy_v8_1(objects, relationships, device)

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

    # LLM reasoning log
    with open(os.path.join(sample_dir, 'LLM_REASONING_LOG.txt'), 'w') as f:
        f.write("V8.1 LLM Reasoning Log\n")
        f.write("="*70 + "\n\n")
        for obj_name, levels in object_to_levels.items():
            f.write(f"Object: {obj_name}\n")
            f.write(f"  Fine: {levels['fine']}\n")
            f.write(f"  Mid: {levels['mid']}\n")
            f.write(f"  Coarse: {levels['coarse']}\n")
            f.write(f"  Method: {levels.get('method', 'unknown')}\n")
            if levels.get('reasoning'):
                f.write(f"  Reasoning: {levels['reasoning']}\n")
            f.write("\n")

    # V8.1 method documentation
    with open(os.path.join(sample_dir, 'V8_1_CONTEXT_METHOD.md'), 'w') as f:
        f.write(f"""# V8.1: Context-Aware LLM-Guided Granularity Selection

**Image ID**: {image_id}
**Date**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}

## Method Overview

V8.1 uses **context-aware Qwen3 LLM** with full scene graph information:
- **LLM Model**: Qwen3-0.6B (Apache 2.0 license)
- **Context**: Full scene graph (objects, relationships, spatial bboxes)
- **Selection**: Two-stage (mid first, then coarse)
- **Goal**: Traceable abstraction levels (coarse → mid → fine)
- **Key Fix**: `enable_thinking=False` in tokenizer
- **Fallback**: V7 adaptive rules if LLM fails
- **Success Rate**: {llm_stats['llm_success']}/{llm_stats['total']} ({llm_stats['llm_success']/llm_stats['total']*100:.1f}%)

### Why Context-Aware?

1. **Scene Understanding**: LLM sees all objects and relationships
2. **Spatial Awareness**: Bbox positions inform semantic decisions
3. **Relational Context**: Relationships guide abstraction choices
4. **Goal-Oriented**: Emphasizes traceable hierarchy not just compression
5. **Two-Stage Selection**: Mid-level first, then coarse for consistency
6. **Reasoning**: LLM provides explanation for each decision

## Granularity Definitions

### Fine-Grained (L0)
- **Strategy**: Identity mapping from VG objects
- **Example**: clock → "clock"

### Mid-Level (L1) - Stage 1
- **Strategy**: LLM selects best from **depth 4-6** with scene context
- **Prompt**: "Which concept best represents this object as a mid-level category in this scene?"
- **Context Provided**:
  - All objects in scene with bboxes
  - Current object's position and size
  - Relationships involving this object
- **LLM considers**: Functional/semantic category, scene role
- **Fallback**: V7 adaptive scoring if LLM fails

### Coarse-Grained (L2) - Stage 2
- **Strategy**: LLM selects best from **depth 1-3** based on mid selection
- **Prompt**: "Which concept provides appropriate high-level abstraction?"
- **Context Provided**: Same as mid-level plus mid selection
- **LLM considers**: General domain, meaningful grouping
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
    print(f"  18. V8_1_CONTEXT_METHOD.md")
    print(f"  19. graph_structure_comparison.png")
    print(f"  20. graph_structure_fine.png")
    print(f"  21. graph_structure_mid.png")
    print(f"  22. graph_structure_coarse.png")
    print(f"  23. GRAPH_STRUCTURE_REPORT.md")
    print(f"  24. LLM_REASONING_LOG.txt (detailed LLM selections with reasoning)")

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='V8.1: Context-Aware LLM-Guided Granularity Scene Graph Hierarchy')
    parser.add_argument('--vg_dir', type=str,
                        default='/nas/jiachen/graph_reasoning/Graph-CoT/data/visual_genome',
                        help='Path to Visual Genome dataset directory')
    parser.add_argument('--image_id', type=int, required=True,
                        help='Visual Genome image ID to process')
    parser.add_argument('--output_dir', type=str, default='vg/v8_1',
                        help='Output directory for results')
    parser.add_argument('--device', type=str, default='cuda:2',
                        help='CUDA device for LLM (e.g., cuda:2)')

    args = parser.parse_args()

    success = run_v8_1_pipeline(args.vg_dir, args.image_id, args.output_dir, args.device)

    if success:
        print("\n✅ V8.1 visualization complete!")
    else:
        print("\n❌ V8.1 visualization failed!")
        sys.exit(1)
