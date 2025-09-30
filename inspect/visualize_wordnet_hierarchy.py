#!/usr/bin/env python3
"""
Visualize WordNet Hierarchy for Visual Genome Concepts
Focus on ontology formulation and multi-granularity hierarchy structure.
"""
import os
import sys
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from collections import defaultdict
from PIL import Image

# Add parent directory for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import NLTK WordNet
from nltk.corpus import wordnet as wn

def load_vg_sample(objects_file, image_id):
    """Load specific VG image by ID."""
    print(f"Loading VG image {image_id} from {objects_file}")

    with open(objects_file, 'r') as f:
        data = json.load(f)

    for item in data:
        if item['image_id'] == image_id:
            return item

    return None

def extract_wordnet_hierarchy(concept_name):
    """
    Extract complete WordNet hierarchy for a concept.
    Returns list of hypernym paths from specific to abstract.
    """
    synsets = wn.synsets(concept_name)

    if not synsets:
        return [], []

    all_paths = []
    all_depths = []

    for synset in synsets:
        # Get all hypernym paths for this synset
        paths = synset.hypernym_paths()

        for path in paths:
            # Convert synset path to concept names
            concept_path = [s.name().split('.')[0].replace('_', ' ') for s in path]
            all_paths.append(concept_path)
            all_depths.append(len(concept_path))

    return all_paths, all_depths

def build_hierarchy_tree(objects):
    """
    Build hierarchical tree structure from VG objects using WordNet.
    Returns hierarchy organized by depth levels.
    """
    print("\nBuilding WordNet hierarchy tree...")

    # Extract unique object names
    object_names = []
    for obj in objects:
        if obj.get('names'):
            object_names.extend(obj['names'])

    unique_names = list(set(object_names))
    print(f"Processing {len(unique_names)} unique object types")

    # Build hierarchy
    hierarchy_by_depth = defaultdict(set)  # depth -> set of concepts
    concept_to_paths = {}  # concept -> list of hypernym paths
    concept_depths = {}  # concept -> max depth

    for name in unique_names:
        name_clean = name.lower().replace(' ', '_')
        paths, depths = extract_wordnet_hierarchy(name_clean)

        if paths:
            concept_to_paths[name] = paths
            max_depth = max(depths) if depths else 0
            concept_depths[name] = max_depth

            # Add all concepts in paths to hierarchy
            for path in paths:
                for depth, concept in enumerate(path):
                    hierarchy_by_depth[depth].add(concept)

    # Calculate statistics
    max_depth = max(hierarchy_by_depth.keys()) if hierarchy_by_depth else 0
    total_concepts = sum(len(concepts) for concepts in hierarchy_by_depth.values())

    print(f"\nHierarchy Statistics:")
    print(f"  Base concepts: {len(unique_names)}")
    print(f"  Expanded concepts: {total_concepts}")
    print(f"  Expansion ratio: {total_concepts/len(unique_names):.2f}x")
    print(f"  Max hierarchy depth: {max_depth}")
    print(f"  Concepts per level:")
    for depth in sorted(hierarchy_by_depth.keys()):
        print(f"    Level {depth}: {len(hierarchy_by_depth[depth])} concepts")

    return hierarchy_by_depth, concept_to_paths, concept_depths

def visualize_hierarchy_tree(hierarchy_by_depth, concept_to_paths, sample_concepts, output_path):
    """
    Create comprehensive hierarchy visualization showing WordNet tree structure.
    """
    print("\nCreating hierarchy visualization...")

    fig = plt.figure(figsize=(24, 16))

    # Panel 1: Multi-level Hierarchy Tree (Top-down view)
    ax1 = plt.subplot(2, 3, 1)
    visualize_tree_structure(ax1, hierarchy_by_depth, "WordNet Hierarchy Levels")

    # Panel 2: Sample Concept Paths (Detailed view)
    ax2 = plt.subplot(2, 3, 2)
    visualize_concept_paths(ax2, concept_to_paths, sample_concepts, "Sample Hypernym Paths")

    # Panel 3: Depth Distribution
    ax3 = plt.subplot(2, 3, 3)
    visualize_depth_distribution(ax3, hierarchy_by_depth, "Concepts per Hierarchy Level")

    # Panel 4: Granularity Pyramid
    ax4 = plt.subplot(2, 3, 4)
    visualize_granularity_pyramid(ax4, hierarchy_by_depth, "Multi-Granularity Pyramid")

    # Panel 5: Concept Example Table
    ax5 = plt.subplot(2, 3, 5)
    visualize_concept_examples(ax5, concept_to_paths, sample_concepts, "Concept → Abstract Hierarchy")

    # Panel 6: Statistics Summary
    ax6 = plt.subplot(2, 3, 6)
    visualize_hierarchy_stats(ax6, hierarchy_by_depth, concept_to_paths, "Hierarchy Statistics")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved hierarchy visualization: {output_path}")

def visualize_tree_structure(ax, hierarchy_by_depth, title):
    """Visualize hierarchy as a tree with levels."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title(title, fontsize=14, weight='bold', pad=20)

    max_depth = max(hierarchy_by_depth.keys())
    level_height = 8 / (max_depth + 1)

    # Color map for depths
    colors = plt.cm.viridis(np.linspace(0, 1, max_depth + 1))

    for depth in sorted(hierarchy_by_depth.keys()):
        y_pos = 9 - (depth * level_height)
        concepts = list(hierarchy_by_depth[depth])[:5]  # Show first 5

        # Draw level box
        box_width = 8
        box_height = level_height * 0.8

        rect = FancyBboxPatch(
            (1, y_pos - box_height/2), box_width, box_height,
            boxstyle="round,pad=0.1",
            facecolor=colors[depth],
            edgecolor='black',
            alpha=0.7,
            linewidth=2
        )
        ax.add_patch(rect)

        # Add level label
        ax.text(0.5, y_pos, f"L{depth}", fontsize=10, weight='bold',
                ha='right', va='center')

        # Add sample concepts
        concept_text = ", ".join(concepts[:3])
        if len(concepts) > 3:
            concept_text += f" ... (+{len(hierarchy_by_depth[depth])-3})"

        ax.text(5, y_pos, concept_text, fontsize=8,
                ha='center', va='center', color='white', weight='bold')

    # Add granularity labels
    ax.text(9.5, 9 - (0 * level_height), "Fine-grained", fontsize=9,
            ha='left', va='center', style='italic', color='darkgreen')
    ax.text(9.5, 9 - (max_depth * level_height), "Coarse-grained", fontsize=9,
            ha='left', va='center', style='italic', color='darkred')

def visualize_concept_paths(ax, concept_to_paths, sample_concepts, title):
    """Visualize detailed hypernym paths for sample concepts."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title(title, fontsize=14, weight='bold', pad=20)

    y_pos = 9.5

    for i, concept in enumerate(sample_concepts[:5]):
        if concept not in concept_to_paths:
            continue

        paths = concept_to_paths[concept]
        if not paths:
            continue

        # Use the longest path (most detailed hierarchy)
        path = max(paths, key=len)

        # Draw concept name
        ax.text(0.5, y_pos, concept, fontsize=10, weight='bold',
                ha='left', va='center', color='darkblue')

        # Draw arrow path
        arrow_y = y_pos - 0.3
        arrow_start_x = 0.5

        for j, parent in enumerate(path[:4]):  # Show first 4 levels
            if j == 0:
                continue  # Skip the concept itself

            arrow_end_x = arrow_start_x + 1.8

            # Draw arrow
            ax.annotate('', xy=(arrow_end_x, arrow_y), xytext=(arrow_start_x, arrow_y),
                       arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))

            # Draw parent concept
            ax.text(arrow_end_x + 0.1, arrow_y, parent[:10], fontsize=8,
                   ha='left', va='center', style='italic')

            arrow_start_x = arrow_end_x + 1.2

        y_pos -= 1.8

    if y_pos > 1:
        ax.text(5, y_pos - 0.5, "(Paths show: concept → parent → grandparent → ...)",
               fontsize=8, ha='center', va='center', style='italic', color='gray')

def visualize_depth_distribution(ax, hierarchy_by_depth, title):
    """Bar chart of concept count per hierarchy level."""
    ax.set_title(title, fontsize=14, weight='bold', pad=20)

    depths = sorted(hierarchy_by_depth.keys())
    counts = [len(hierarchy_by_depth[d]) for d in depths]

    colors = plt.cm.viridis(np.linspace(0, 1, len(depths)))
    bars = ax.bar(depths, counts, color=colors, edgecolor='black', linewidth=1.5)

    ax.set_xlabel("Hierarchy Depth Level", fontsize=11, weight='bold')
    ax.set_ylabel("Number of Concepts", fontsize=11, weight='bold')
    ax.set_xticks(depths)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Add value labels on bars
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height,
               f'{int(count)}', ha='center', va='bottom', fontsize=9, weight='bold')

def visualize_granularity_pyramid(ax, hierarchy_by_depth, title):
    """Pyramid showing multi-granularity structure."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title(title, fontsize=14, weight='bold', pad=20)

    max_depth = max(hierarchy_by_depth.keys())

    # Draw inverted pyramid (fine-grained at bottom, coarse at top)
    for depth in sorted(hierarchy_by_depth.keys(), reverse=True):
        y_top = 1 + (depth * 1.2)
        width = 8 - (depth * 0.8)
        x_left = 5 - width/2

        # Draw trapezoid
        if depth > 0:
            prev_width = 8 - ((depth-1) * 0.8)
            vertices = [
                [5 - prev_width/2, y_top + 1.2],  # top left
                [5 + prev_width/2, y_top + 1.2],  # top right
                [5 + width/2, y_top],             # bottom right
                [5 - width/2, y_top]              # bottom left
            ]
        else:
            vertices = [
                [5 - width/2, y_top + 1.2],
                [5 + width/2, y_top + 1.2],
                [5 + width/2, y_top],
                [5 - width/2, y_top]
            ]

        color = plt.cm.RdYlGn_r(depth / max_depth)
        polygon = plt.Polygon(vertices, facecolor=color, edgecolor='black',
                            linewidth=2, alpha=0.7)
        ax.add_patch(polygon)

        # Add label
        count = len(hierarchy_by_depth[depth])
        ax.text(5, y_top + 0.6, f"L{depth}\n({count})", fontsize=9,
               ha='center', va='center', weight='bold')

    # Add granularity labels
    ax.text(0.5, 9, "Most Abstract", fontsize=10, weight='bold',
           color='darkred', style='italic')
    ax.text(0.5, 1.5, "Most Specific", fontsize=10, weight='bold',
           color='darkgreen', style='italic')

def visualize_concept_examples(ax, concept_to_paths, sample_concepts, title):
    """Table showing concept hierarchy examples."""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title(title, fontsize=14, weight='bold', pad=20)

    y_pos = 9

    ax.text(1, y_pos, "Concept", fontsize=10, weight='bold', ha='left', va='center')
    ax.text(6, y_pos, "Hierarchy Path", fontsize=10, weight='bold', ha='left', va='center')

    # Draw header line
    ax.plot([0.5, 9.5], [y_pos - 0.3, y_pos - 0.3], 'k-', linewidth=2)

    y_pos -= 0.8

    for concept in sample_concepts[:8]:
        if concept not in concept_to_paths:
            continue

        paths = concept_to_paths[concept]
        if not paths:
            continue

        # Use longest path
        path = max(paths, key=len)

        # Draw concept
        ax.text(1, y_pos, concept[:15], fontsize=9, ha='left', va='center',
               color='darkblue', weight='bold')

        # Draw hierarchy
        hierarchy_str = " → ".join(path[:5])
        if len(path) > 5:
            hierarchy_str += " → ..."

        ax.text(6, y_pos, hierarchy_str[:50], fontsize=8, ha='left', va='center',
               style='italic', family='monospace')

        y_pos -= 0.9

        if y_pos < 1:
            break

def visualize_hierarchy_stats(ax, hierarchy_by_depth, concept_to_paths, title):
    """Display hierarchy statistics."""
    ax.axis('off')
    ax.set_title(title, fontsize=14, weight='bold', pad=20)

    total_base = len(concept_to_paths)
    total_expanded = sum(len(concepts) for concepts in hierarchy_by_depth.values())
    max_depth = max(hierarchy_by_depth.keys())
    avg_depth = np.mean([len(max(paths, key=len)) for paths in concept_to_paths.values() if paths])

    stats_text = f"""
Ontology Formulation Statistics:

Base Concepts (VG Objects):    {total_base}
Expanded Concepts (WordNet):   {total_expanded}
Expansion Ratio:               {total_expanded/total_base:.2f}x

Hierarchy Structure:
  Maximum Depth:               {max_depth} levels
  Average Depth:               {avg_depth:.1f} levels
  Unique Concepts:             {len(set.union(*[hierarchy_by_depth[d] for d in hierarchy_by_depth]))}

Multi-Granularity Levels:
  Fine-grained (L0-L2):        {sum(len(hierarchy_by_depth.get(i, set())) for i in range(3))}
  Mid-level (L3-L5):           {sum(len(hierarchy_by_depth.get(i, set())) for i in range(3, 6))}
  Coarse-grained (L6+):        {sum(len(hierarchy_by_depth.get(i, set())) for i in range(6, max_depth+1))}

Ontology Coverage:
  Synsets with paths:          {sum(1 for paths in concept_to_paths.values() if paths)}
  Concepts without hierarchy:  {sum(1 for paths in concept_to_paths.values() if not paths)}
  Coverage rate:               {100 * sum(1 for paths in concept_to_paths.values() if paths) / max(1, total_base):.1f}%
"""

    ax.text(0.1, 0.9, stats_text, transform=ax.transAxes,
           fontsize=10, verticalalignment='top', fontfamily='monospace',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.8))

def visualize_image_with_hierarchy(vg_sample, objects, hierarchy_by_depth,
                                  concept_to_paths, output_path, image_path=None):
    """
    Create combined visualization: VG image + hierarchy overlay.
    """
    print("\nCreating combined image + hierarchy visualization...")

    fig = plt.figure(figsize=(20, 12))

    # Left panel: Original image with objects
    ax_img = plt.subplot(1, 2, 1)

    if image_path and os.path.exists(image_path):
        img = Image.open(image_path)
        ax_img.imshow(img)

        # Add bounding boxes colored by hierarchy depth
        for i, obj in enumerate(objects[:15]):
            name = obj['names'][0] if obj['names'] else f"obj_{i}"

            # Get hierarchy depth
            depth = 0
            if name in concept_to_paths and concept_to_paths[name]:
                depth = len(max(concept_to_paths[name], key=len))

            # Color by depth
            color = plt.cm.viridis(min(depth / 10, 1.0))

            # Draw bbox
            from matplotlib.patches import Rectangle
            rect = Rectangle((obj['x'], obj['y']), obj['w'], obj['h'],
                           linewidth=3, edgecolor=color, facecolor='none', alpha=0.8)
            ax_img.add_patch(rect)

            # Add label with depth
            ax_img.text(obj['x'], obj['y'] - 5, f"{name[:10]} (L{depth})",
                       color=color, fontsize=8, weight='bold',
                       bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    else:
        ax_img.text(0.5, 0.5, f"VG Image {vg_sample['image_id']}\n({len(objects)} objects)",
                   ha='center', va='center', transform=ax_img.transAxes, fontsize=16)

    ax_img.set_title(f"VG Image {vg_sample['image_id']} - Objects Colored by Hierarchy Depth",
                    fontsize=14, weight='bold')
    ax_img.axis('off')

    # Right panel: Hierarchy tree for this image
    ax_hier = plt.subplot(1, 2, 2)
    sample_concepts = [obj['names'][0] for obj in objects[:10] if obj.get('names')]
    visualize_concept_paths(ax_hier, concept_to_paths, sample_concepts,
                           f"WordNet Hierarchy for Image {vg_sample['image_id']} Objects")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved combined visualization: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Visualize WordNet hierarchy for VG concepts')
    parser.add_argument('--vg_dir', default='../data/vg', help='Visual Genome data directory')
    parser.add_argument('--output_dir', default='hierarchy_viz', help='Output directory')
    parser.add_argument('--image_id', type=int, required=True, help='VG image ID to process')

    args = parser.parse_args()

    print("=" * 60)
    print("WordNet Hierarchy Visualization for Visual Genome")
    print("=" * 60)

    # Load VG sample
    vg_objects_file = os.path.join(args.vg_dir, 'annotations/v1.4/objects.json')
    vg_sample = load_vg_sample(vg_objects_file, args.image_id)

    if not vg_sample:
        print(f"❌ Could not find VG image {args.image_id}")
        return

    objects = vg_sample['objects']
    print(f"\n✅ Loaded VG Image {args.image_id} with {len(objects)} objects")

    # Create output directory
    output_dir = os.path.join(args.output_dir, f"image_{args.image_id}")
    os.makedirs(output_dir, exist_ok=True)

    # Build WordNet hierarchy
    hierarchy_by_depth, concept_to_paths, concept_depths = build_hierarchy_tree(objects)

    # Get sample concepts for detailed visualization
    sample_concepts = [obj['names'][0] for obj in objects[:10] if obj.get('names')]

    # Create hierarchy visualization
    hierarchy_viz_path = os.path.join(output_dir, 'wordnet_hierarchy_detailed.png')
    visualize_hierarchy_tree(hierarchy_by_depth, concept_to_paths,
                            sample_concepts, hierarchy_viz_path)

    # Try to find image file
    image_path = None
    for part in ['VG_100K/VG_100K', 'VG_100K_2']:
        test_path = os.path.join(args.vg_dir, f'images/{part}/{args.image_id}.jpg')
        if os.path.exists(test_path):
            image_path = test_path
            break

    # Create combined visualization
    combined_viz_path = os.path.join(output_dir, 'image_with_hierarchy.png')
    visualize_image_with_hierarchy(vg_sample, objects, hierarchy_by_depth,
                                   concept_to_paths, combined_viz_path, image_path)

    # Save hierarchy data
    hierarchy_data = {
        'image_id': args.image_id,
        'hierarchy_by_depth': {str(k): list(v) for k, v in hierarchy_by_depth.items()},
        'concept_paths': {k: v for k, v in concept_to_paths.items()},
        'concept_depths': concept_depths,
        'statistics': {
            'base_concepts': len(concept_to_paths),
            'expanded_concepts': sum(len(concepts) for concepts in hierarchy_by_depth.values()),
            'max_depth': max(hierarchy_by_depth.keys()),
            'expansion_ratio': sum(len(concepts) for concepts in hierarchy_by_depth.values()) / max(1, len(concept_to_paths))
        }
    }

    with open(os.path.join(output_dir, 'hierarchy_data.json'), 'w') as f:
        json.dump(hierarchy_data, f, indent=2)

    print("\n" + "=" * 60)
    print("✅ Hierarchy Visualization Complete!")
    print("=" * 60)
    print(f"Output directory: {output_dir}")
    print(f"  - wordnet_hierarchy_detailed.png (6-panel hierarchy visualization)")
    print(f"  - image_with_hierarchy.png (image + hierarchy overlay)")
    print(f"  - hierarchy_data.json (complete hierarchy data)")

if __name__ == '__main__':
    main()