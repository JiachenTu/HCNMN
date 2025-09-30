#!/usr/bin/env python3
"""
Visualize multi-granularity hierarchical ontology with merged bounding boxes.
At each granularity level, objects with the same concept are merged into a single node
with a combined bounding box.
"""
import os
import sys
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from nltk.corpus import wordnet as wn

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_vg_data(vg_dir, image_id):
    """Load Visual Genome scene graph data for a specific image."""
    print(f"\nLoading VG data for image {image_id}...")

    scene_graphs_path = os.path.join(vg_dir, 'annotations', 'v1.2', 'scene_graphs.json')

    with open(scene_graphs_path) as f:
        all_scene_graphs = json.load(f)

    # Find the scene graph for this image
    scene_graph = None
    for sg in all_scene_graphs:
        if sg['image_id'] == image_id:
            scene_graph = sg
            break

    if scene_graph is None:
        raise ValueError(f"Image ID {image_id} not found in scene graphs")

    objects = scene_graph.get('objects', [])
    relationships = scene_graph.get('relationships', [])

    # Try to load image from VG_100K only (not VG_100K_2)
    image_path = os.path.join(vg_dir, 'images', 'VG_100K', 'VG_100K', f'{image_id}.jpg')
    if not os.path.exists(image_path):
        print(f"Warning: Image not found at {image_path}")
        image_path = None

    print(f"Found {len(objects)} objects and {len(relationships)} relationships")

    return image_path, objects, relationships

def build_clean_hierarchy(objects, max_depth=3):
    """
    Build 3-level hierarchy from VG objects using WordNet.
    """
    hierarchy = {'fine': [], 'mid': [], 'coarse': []}
    concept_paths = {}
    object_to_levels = {}

    for obj in objects:
        if not obj.get('names'):
            continue

        obj_name = obj['names'][0]
        obj_clean = obj_name.replace('_', ' ')

        # L0: Fine-grained (original object)
        hierarchy['fine'].append(obj_name)
        path = [obj_name]
        obj_to_levels = {'fine': obj_name}

        # L1: Mid-level (immediate hypernym)
        synsets = wn.synsets(obj_clean)
        if synsets and len(synsets) > 0:
            synset = synsets[0]
            if synset.hypernyms():
                parent = synset.hypernyms()[0]
                parent_name = parent.name().split('.')[0].replace('_', ' ')
                hierarchy['mid'].append(parent_name)
                path.append(parent_name)
                obj_to_levels['mid'] = parent_name

                # L2: Coarse-grained (second-level hypernym)
                if parent.hypernyms():
                    grandparent = parent.hypernyms()[0]
                    grandparent_name = grandparent.name().split('.')[0].replace('_', ' ')
                    hierarchy['coarse'].append(grandparent_name)
                    path.append(grandparent_name)
                    obj_to_levels['coarse'] = grandparent_name

        concept_paths[obj_name] = path
        object_to_levels[obj_name] = obj_to_levels

    # Remove duplicates
    hierarchy['fine'] = list(set(hierarchy['fine']))
    hierarchy['mid'] = list(set(hierarchy['mid']))
    hierarchy['coarse'] = list(set(hierarchy['coarse']))

    return hierarchy, concept_paths, object_to_levels

def merge_bounding_boxes(bboxes):
    """
    Merge multiple bounding boxes into a single enclosing box.

    Args:
        bboxes: List of dicts with keys 'x', 'y', 'w', 'h'

    Returns:
        Dict with merged bbox: {'x', 'y', 'w', 'h'}
    """
    if not bboxes:
        return {'x': 0, 'y': 0, 'w': 0, 'h': 0}

    # Find minimum enclosing rectangle
    x_min = min(bbox['x'] for bbox in bboxes)
    y_min = min(bbox['y'] for bbox in bboxes)
    x_max = max(bbox['x'] + bbox['w'] for bbox in bboxes)
    y_max = max(bbox['y'] + bbox['h'] for bbox in bboxes)

    return {
        'x': x_min,
        'y': y_min,
        'w': x_max - x_min,
        'h': y_max - y_min
    }

def create_merged_scene_graph(objects, object_to_levels, granularity):
    """
    Create merged scene graph at a specific granularity level.
    Objects with the same concept are merged into a single node with combined bbox.

    Args:
        objects: List of VG object annotations
        object_to_levels: Dict mapping object names to concepts at each level
        granularity: 'fine', 'mid', or 'coarse'

    Returns:
        Dict mapping concept names to merged nodes with:
        - 'concept': concept name
        - 'bbox': merged bounding box
        - 'object_count': number of objects merged
        - 'original_objects': list of original object names
    """
    concept_groups = {}

    for obj in objects:
        if not obj.get('names'):
            continue

        obj_name = obj['names'][0]
        if obj_name not in object_to_levels:
            continue

        # Get concept at this granularity level
        concept = object_to_levels[obj_name].get(granularity, obj_name)

        if concept not in concept_groups:
            concept_groups[concept] = {
                'concept': concept,
                'bboxes': [],
                'original_objects': []
            }

        concept_groups[concept]['bboxes'].append({
            'x': obj['x'],
            'y': obj['y'],
            'w': obj['w'],
            'h': obj['h']
        })
        concept_groups[concept]['original_objects'].append(obj_name)

    # Merge bounding boxes for each concept
    merged_nodes = {}
    for concept, group in concept_groups.items():
        merged_bbox = merge_bounding_boxes(group['bboxes'])
        merged_nodes[concept] = {
            'concept': concept,
            'bbox': merged_bbox,
            'object_count': len(group['bboxes']),
            'original_objects': group['original_objects']
        }

    return merged_nodes

def visualize_merged_granularity(image_path, merged_nodes, granularity, output_path):
    """
    Visualize merged scene graph at a specific granularity level.
    """
    print(f"\nVisualizing merged {granularity}-grained scene graph...")

    fig, ax = plt.subplots(figsize=(18, 12))

    # Color map for granularity
    colors = {
        'fine': '#2ecc71',      # Green
        'mid': '#3498db',       # Blue
        'coarse': '#e74c3c'     # Red
    }
    base_color = colors[granularity]

    # Load image
    if image_path and os.path.exists(image_path):
        img = Image.open(image_path)
        ax.imshow(img)

        # Assign unique color to each concept
        unique_concepts = list(merged_nodes.keys())
        cmap = plt.cm.tab20
        concept_colors = {concept: cmap(i % 20)
                         for i, concept in enumerate(unique_concepts)}

        # Draw merged bounding boxes
        for concept, node in merged_nodes.items():
            bbox = node['bbox']
            color = concept_colors[concept]

            # Draw merged bbox with thicker border
            rect = patches.Rectangle((bbox['x'], bbox['y']), bbox['w'], bbox['h'],
                                   linewidth=5, edgecolor=color,
                                   facecolor='none', alpha=0.9)
            ax.add_patch(rect)

            # Add label with object count
            label = f"{concept}\n({node['object_count']} obj)"
            ax.text(bbox['x'], max(0, bbox['y'] - 10), label,
                   color='white', fontsize=12, weight='bold',
                   bbox=dict(boxstyle="round,pad=0.5",
                           facecolor=color, alpha=0.95, edgecolor='white', linewidth=2))

        # Create legend
        legend_elements = []
        for concept in sorted(unique_concepts)[:15]:
            legend_elements.append(
                patches.Patch(facecolor=concept_colors[concept],
                            edgecolor='black', label=concept, linewidth=1.5)
            )

        if legend_elements:
            legend = ax.legend(handles=legend_elements, loc='upper right',
                              fontsize=10, framealpha=0.9)
            legend.get_frame().set_edgecolor('black')
            legend.get_frame().set_linewidth(2)

    else:
        ax.text(0.5, 0.5, f"Image not available\n{granularity.capitalize()}-grained merged view",
               ha='center', va='center', transform=ax.transAxes, fontsize=16)

    # Add title
    title_text = f"Merged {granularity.capitalize()}-Grained Scene Graph"
    subtitle = f"({len(merged_nodes)} merged concept nodes)"
    ax.set_title(f"{title_text}\n{subtitle}",
                fontsize=16, weight='bold', color=base_color, pad=20)
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved merged {granularity}-grained visualization: {output_path}")

def create_merged_comparison(image_path, objects, object_to_levels, output_path):
    """
    Create 3-panel comparison showing merged scene graphs at all granularity levels.
    """
    print("\nCreating merged multi-granularity comparison...")

    fig = plt.figure(figsize=(24, 8))

    granularities = ['fine', 'mid', 'coarse']
    colors = {'fine': '#2ecc71', 'mid': '#3498db', 'coarse': '#e74c3c'}

    for idx, granularity in enumerate(granularities):
        ax = plt.subplot(1, 3, idx + 1)

        # Create merged scene graph for this level
        merged_nodes = create_merged_scene_graph(objects, object_to_levels, granularity)

        if image_path and os.path.exists(image_path):
            img = Image.open(image_path)
            ax.imshow(img)

            # Assign colors
            unique_concepts = sorted(merged_nodes.keys())
            cmap = plt.cm.tab20
            concept_colors = {concept: cmap(i % 20)
                             for i, concept in enumerate(unique_concepts)}

            # Draw merged bboxes
            for concept, node in merged_nodes.items():
                bbox = node['bbox']
                color = concept_colors[concept]

                rect = patches.Rectangle((bbox['x'], bbox['y']), bbox['w'], bbox['h'],
                                       linewidth=4, edgecolor=color,
                                       facecolor='none', alpha=0.85)
                ax.add_patch(rect)

                # Add label
                label = f"{concept}\n({node['object_count']})"
                ax.text(bbox['x'], max(0, bbox['y'] - 8), label,
                       color='white', fontsize=9, weight='bold',
                       bbox=dict(boxstyle="round,pad=0.3",
                               facecolor=color, alpha=0.9))

            # Add concept count
            ax.text(0.02, 0.98, f"{len(merged_nodes)} merged nodes",
                   transform=ax.transAxes, fontsize=12, weight='bold',
                   color='white', va='top', ha='left',
                   bbox=dict(boxstyle="round,pad=0.5",
                           facecolor=colors[granularity], alpha=0.9))

        ax.set_title(f"Merged {granularity.capitalize()}-Grained",
                    fontsize=14, weight='bold', color=colors[granularity], pad=10)
        ax.axis('off')

    plt.suptitle("Merged Multi-Granularity Scene Graph Comparison",
                fontsize=18, weight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved merged comparison: {output_path}")

def generate_merged_report(output_dir, image_id, merged_nodes_by_level, statistics):
    """Generate markdown report documenting merged scene graphs."""
    report_path = os.path.join(output_dir, 'MERGED_SCENE_GRAPH_REPORT.md')

    with open(report_path, 'w') as f:
        f.write(f"# Merged Multi-Granularity Scene Graph Report\n\n")
        f.write(f"## Image ID: {image_id}\n\n")
        f.write(f"**Total Objects**: {statistics['num_objects']}\n")
        f.write(f"**Hierarchy Levels**: 3 (Fine → Mid → Coarse)\n\n")
        f.write("---\n\n")

        f.write("## Merged Scene Graph Statistics\n\n")
        f.write("At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.\n\n")

        f.write("| Granularity | Original Objects | Merged Nodes | Compression Ratio |\n")
        f.write("|-------------|------------------|--------------|-------------------|\n")

        for gran in ['fine', 'mid', 'coarse']:
            merged_count = len(merged_nodes_by_level[gran])
            compression = statistics['num_objects'] / max(1, merged_count)
            f.write(f"| {gran.capitalize()} | {statistics['num_objects']} | {merged_count} | {compression:.2f}x |\n")

        f.write("\n---\n\n")

        # Document each granularity level
        for gran in ['fine', 'mid', 'coarse']:
            f.write(f"## {gran.capitalize()}-Grained Merged Nodes\n\n")
            f.write(f"**Node Count**: {len(merged_nodes_by_level[gran])}\n\n")

            # List merged nodes
            merged_nodes = merged_nodes_by_level[gran]
            for concept in sorted(merged_nodes.keys()):
                node = merged_nodes[concept]
                f.write(f"### {concept}\n")
                f.write(f"- **Merged Objects**: {node['object_count']}\n")
                f.write(f"- **Original Objects**: {', '.join(node['original_objects'][:10])}")
                if len(node['original_objects']) > 10:
                    f.write(f" (+{len(node['original_objects']) - 10} more)")
                f.write("\n")
                bbox = node['bbox']
                f.write(f"- **Merged BBox**: x={bbox['x']}, y={bbox['y']}, w={bbox['w']}, h={bbox['h']}\n\n")

            f.write("---\n\n")

        f.write("## Visualization Files\n\n")
        f.write("- `merged_fine.png`: Merged fine-grained scene graph\n")
        f.write("- `merged_mid.png`: Merged mid-level scene graph\n")
        f.write("- `merged_coarse.png`: Merged coarse-grained scene graph\n")
        f.write("- `merged_comparison.png`: Side-by-side comparison of all 3 levels\n\n")

        f.write("---\n\n")
        f.write(f"**Generated**: {output_dir}\n")

    print(f"Generated merged scene graph report: {report_path}")

def main():
    parser = argparse.ArgumentParser(description='Visualize merged multi-granularity scene graphs')
    parser.add_argument('--vg_dir', type=str,
                       default='/home/jiachen/scratch/graph_reasoning/HCNMN/data/vg',
                       help='Visual Genome data directory')
    parser.add_argument('--output_dir', type=str,
                       default='/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg',
                       help='Output directory')
    parser.add_argument('--image_id', type=int, required=True,
                       help='VG image ID to process')

    args = parser.parse_args()

    # Create output directory
    sample_dir = os.path.join(args.output_dir, f'sample_{args.image_id}')
    os.makedirs(sample_dir, exist_ok=True)

    # Load VG data
    image_path, objects, relationships = load_vg_data(args.vg_dir, args.image_id)

    # Build hierarchy
    hierarchy, concept_paths, object_to_levels = build_clean_hierarchy(objects)

    # Statistics
    statistics = {
        'num_objects': len(objects),
        'num_relationships': len(relationships),
        'fine_concepts': len(hierarchy['fine']),
        'mid_concepts': len(hierarchy['mid']),
        'coarse_concepts': len(hierarchy['coarse']),
        'total_concepts': len(hierarchy['fine']) + len(hierarchy['mid']) + len(hierarchy['coarse'])
    }

    print(f"\nStatistics:")
    print(f"  Objects: {statistics['num_objects']}")
    print(f"  Relationships: {statistics['num_relationships']}")
    print(f"  Fine concepts: {statistics['fine_concepts']}")
    print(f"  Mid concepts: {statistics['mid_concepts']}")
    print(f"  Coarse concepts: {statistics['coarse_concepts']}")

    # Create merged scene graphs for each granularity
    merged_nodes_by_level = {}
    for granularity in ['fine', 'mid', 'coarse']:
        merged_nodes = create_merged_scene_graph(objects, object_to_levels, granularity)
        merged_nodes_by_level[granularity] = merged_nodes

        # Visualize
        output_path = os.path.join(sample_dir, f'merged_{granularity}.png')
        visualize_merged_granularity(image_path, merged_nodes, granularity, output_path)

    # Create comparison visualization
    comparison_path = os.path.join(sample_dir, 'merged_comparison.png')
    create_merged_comparison(image_path, objects, object_to_levels, comparison_path)

    # Generate report
    generate_merged_report(sample_dir, args.image_id, merged_nodes_by_level, statistics)

    # Save merged scene graph data
    merged_data = {
        'image_id': args.image_id,
        'statistics': statistics,
        'merged_nodes': {gran: {k: {
            'concept': v['concept'],
            'bbox': v['bbox'],
            'object_count': v['object_count'],
            'original_objects': v['original_objects']
        } for k, v in nodes.items()} for gran, nodes in merged_nodes_by_level.items()}
    }

    merged_data_path = os.path.join(sample_dir, 'merged_scene_graph_data.json')
    with open(merged_data_path, 'w') as f:
        json.dump(merged_data, f, indent=2)

    print(f"\n✓ Merged scene graph generation complete!")
    print(f"  Output directory: {sample_dir}")

if __name__ == '__main__':
    main()