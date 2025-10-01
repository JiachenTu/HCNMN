#!/usr/bin/env python3
"""
Visualize VG Scene Graph + Clean Hierarchical Ontology
Focus on original VG annotations with 3-level hierarchy (fine/mid/coarse).
NO massive concept expansion - keep it clean and interpretable.
"""
import os
import sys
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from collections import defaultdict
from PIL import Image
import networkx as nx

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nltk.corpus import wordnet as wn

def load_vg_sample_with_relationships(objects_file, relationships_file, image_id):
    """Load VG sample with both objects and relationships."""
    print(f"Loading VG image {image_id}")

    # Load objects
    with open(objects_file, 'r') as f:
        objects_data = json.load(f)

    sample_objects = None
    for item in objects_data:
        if item['image_id'] == image_id:
            sample_objects = item
            break

    if not sample_objects:
        return None, None

    # Load relationships
    with open(relationships_file, 'r') as f:
        relationships_data = json.load(f)

    sample_relationships = None
    for item in relationships_data:
        if item['image_id'] == image_id:
            sample_relationships = item
            break

    return sample_objects, sample_relationships

def get_hypernym_at_depth_from_root(synset, target_depth):
    """Get hypernym at specific depth from root."""
    paths = synset.hypernym_paths()
    if not paths:
        return None

    # Use longest path (most specific)
    longest_path = max(paths, key=len)

    # Check if path is long enough
    if len(longest_path) <= target_depth:
        return None

    # Return synset at target depth from root
    return longest_path[target_depth]


def build_clean_hierarchy(objects, max_depth=3):
    """
    Build CLEAN 3-level hierarchy from VG objects.
    Uses improved merging strategy for better abstraction at coarse level.

    Strategy:
    - Fine: Original VG objects
    - Mid: 1 hop up in WordNet (moderate abstraction)
    - Coarse: depth 3-5 from root (high abstraction for better merging)
    """
    print("\nBuilding clean 3-level hierarchy...")

    hierarchy = {
        'fine': [],      # L0: Original objects
        'mid': [],       # L1: Immediate categories
        'coarse': []     # L2: High-level groups
    }

    concept_paths = {}  # For visualization
    object_to_levels = {}  # Track which levels each object appears in

    # Extract unique objects
    object_names = []
    for obj in objects:
        if obj.get('names'):
            object_names.extend(obj['names'])

    unique_objects = list(set(object_names))
    print(f"Processing {len(unique_objects)} unique objects")

    for obj_name in unique_objects:
        obj_clean = obj_name.lower().replace(' ', '_')

        # Add to fine-grained
        hierarchy['fine'].append(obj_name)
        object_to_levels[obj_name] = {'fine': obj_name}

        # Get WordNet synset
        synsets = wn.synsets(obj_clean)
        if not synsets:
            # No WordNet mapping - use object name for all levels
            if obj_name not in hierarchy['mid']:
                hierarchy['mid'].append(obj_name)
            if obj_name not in hierarchy['coarse']:
                hierarchy['coarse'].append(obj_name)
            object_to_levels[obj_name]['mid'] = obj_name
            object_to_levels[obj_name]['coarse'] = obj_name
            concept_paths[obj_name] = [obj_name]
            continue

        # Use first synset (most common meaning)
        synset = synsets[0]
        path = [obj_name]

        # Mid-level: 1 hop up (same as before)
        if synset.hypernyms():
            parent = synset.hypernyms()[0]
            parent_name = parent.name().split('.')[0].replace('_', ' ')
            path.append(parent_name)

            if parent_name not in hierarchy['mid']:
                hierarchy['mid'].append(parent_name)
            object_to_levels[obj_name]['mid'] = parent_name
        else:
            # No parent - use object for mid level
            if obj_name not in hierarchy['mid']:
                hierarchy['mid'].append(obj_name)
            object_to_levels[obj_name]['mid'] = obj_name

        # Coarse-level: depth 3-5 from root for better merging
        coarse_synset = None
        for depth in [4, 3, 5, 6]:  # Try in order of preference
            coarse_synset = get_hypernym_at_depth_from_root(synset, depth)
            if coarse_synset:
                break

        if coarse_synset:
            coarse_name = coarse_synset.name().split('.')[0].replace('_', ' ')
            path.append(coarse_name)

            if coarse_name not in hierarchy['coarse']:
                hierarchy['coarse'].append(coarse_name)
            object_to_levels[obj_name]['coarse'] = coarse_name
        else:
            # Fallback to mid-level if path too short
            mid_name = object_to_levels[obj_name].get('mid', obj_name)
            if mid_name not in hierarchy['coarse']:
                hierarchy['coarse'].append(mid_name)
            object_to_levels[obj_name]['coarse'] = mid_name

        concept_paths[obj_name] = path

    # Remove duplicates and sort
    for level in ['fine', 'mid', 'coarse']:
        hierarchy[level] = sorted(list(set(hierarchy[level])))

    print(f"\nHierarchy Statistics:")
    print(f"  Fine-grained:   {len(hierarchy['fine'])} concepts")
    print(f"  Mid-level:      {len(hierarchy['mid'])} concepts ({len(hierarchy['fine'])/max(1,len(hierarchy['mid'])):.2f}x compression)")
    print(f"  Coarse-grained: {len(hierarchy['coarse'])} concepts ({len(hierarchy['fine'])/max(1,len(hierarchy['coarse'])):.2f}x compression)")
    print(f"  Total:          {len(hierarchy['fine']) + len(hierarchy['mid']) + len(hierarchy['coarse'])} concepts")

    return hierarchy, concept_paths, object_to_levels

def visualize_scene_graph(vg_sample, objects, relationships, image_path, output_path):
    """
    Visualize original VG scene graph: image + bboxes + relationships.
    """
    print("\nCreating scene graph visualization...")

    fig, ax = plt.subplots(figsize=(16, 12))

    # Load and display image if available
    if image_path and os.path.exists(image_path):
        img = Image.open(image_path)
        ax.imshow(img)

        # Create object ID map
        object_map = {obj['object_id']: obj for obj in objects}

        # Draw bounding boxes
        colors = plt.cm.tab20(np.linspace(0, 1, min(20, len(objects))))
        for i, obj in enumerate(objects[:20]):  # Limit to 20 for clarity
            color = colors[i % len(colors)]

            # Draw bbox
            rect = patches.Rectangle((obj['x'], obj['y']), obj['w'], obj['h'],
                                    linewidth=2, edgecolor=color, facecolor='none', alpha=0.8)
            ax.add_patch(rect)

            # Add label
            name = obj['names'][0] if obj['names'] else f"obj_{i}"
            ax.text(obj['x'], max(0, obj['y'] - 5), name,
                   color='white', fontsize=9, weight='bold',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor=color, alpha=0.9))

        # Draw relationship edges
        if relationships and 'relationships' in relationships:
            for rel in relationships['relationships'][:30]:  # Limit to 30 edges
                try:
                    subj_id = rel['subject']['object_id']
                    obj_id = rel['object']['object_id']
                    predicate = rel['predicate']

                    if subj_id in object_map and obj_id in object_map:
                        subj = object_map[subj_id]
                        obj_target = object_map[obj_id]

                        # Draw arrow from subject center to object center
                        subj_center = (subj['x'] + subj['w']/2, subj['y'] + subj['h']/2)
                        obj_center = (obj_target['x'] + obj_target['w']/2, obj_target['y'] + obj_target['h']/2)

                        arrow = FancyArrowPatch(subj_center, obj_center,
                                              arrowstyle='->', mutation_scale=20,
                                              color='yellow', linewidth=2, alpha=0.6)
                        ax.add_patch(arrow)

                        # Add predicate label
                        mid_x = (subj_center[0] + obj_center[0]) / 2
                        mid_y = (subj_center[1] + obj_center[1]) / 2
                        ax.text(mid_x, mid_y, predicate, fontsize=7, color='yellow',
                               weight='bold', bbox=dict(boxstyle="round,pad=0.2",
                               facecolor='black', alpha=0.7))
                except:
                    continue
    else:
        ax.text(0.5, 0.5, f"VG Image {vg_sample['image_id']}\n({len(objects)} objects)",
               ha='center', va='center', transform=ax.transAxes, fontsize=16)

    ax.set_title(f"VG Scene Graph - Image {vg_sample['image_id']}", fontsize=16, weight='bold')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved scene graph: {output_path}")

def visualize_hierarchy_tree(hierarchy, concept_paths, output_path):
    """
    Visualize clean 3-level hierarchy as a tree.
    """
    print("\nCreating hierarchy tree visualization...")

    fig = plt.figure(figsize=(20, 14))

    # Create 3-column layout
    ax_tree = plt.subplot(1, 1, 1)

    # Set up coordinate system
    ax_tree.set_xlim(0, 20)
    ax_tree.set_ylim(0, 30)
    ax_tree.axis('off')

    # Define column positions and colors
    level_info = {
        'fine': {'x': 2, 'y_start': 28, 'color': '#2ecc71', 'label': 'Fine-grained (Specific)'},
        'mid': {'x': 10, 'y_start': 28, 'color': '#3498db', 'label': 'Mid-level (Categories)'},
        'coarse': {'x': 18, 'y_start': 28, 'color': '#e74c3c', 'label': 'Coarse-grained (High-level)'}
    }

    # Draw level headers
    for level, info in level_info.items():
        ax_tree.text(info['x'], 29, info['label'], fontsize=13, weight='bold',
                    ha='center', va='center', color=info['color'])

        # Draw column background
        rect = FancyBboxPatch((info['x']-1.8, 0.5), 3.6, 27.5,
                             boxstyle="round,pad=0.1", facecolor=info['color'],
                             edgecolor='black', alpha=0.1, linewidth=2)
        ax_tree.add_patch(rect)

    # Position concepts in each column
    level_positions = {}
    for level in ['fine', 'mid', 'coarse']:
        concepts = hierarchy[level][:15]  # Limit to 15 per column
        y_spacing = 25 / max(len(concepts), 1)

        level_positions[level] = {}
        for i, concept in enumerate(concepts):
            y_pos = level_info[level]['y_start'] - 1.5 - (i * y_spacing)
            x_pos = level_info[level]['x']
            level_positions[level][concept] = (x_pos, y_pos)

            # Draw concept box
            box = FancyBboxPatch((x_pos - 1.5, y_pos - 0.3), 3, 0.6,
                                boxstyle="round,pad=0.05", facecolor=level_info[level]['color'],
                                edgecolor='black', alpha=0.8, linewidth=1.5)
            ax_tree.add_patch(box)

            # Add text
            display_text = concept[:18] if len(concept) > 18 else concept
            ax_tree.text(x_pos, y_pos, display_text, fontsize=9, ha='center', va='center',
                        weight='bold', color='white')

    # Draw connections between levels
    for obj_name, path in list(concept_paths.items())[:15]:  # Limit connections
        if len(path) >= 2:
            # Fine → Mid
            if obj_name in level_positions['fine'] and path[1] in level_positions['mid']:
                start_pos = level_positions['fine'][obj_name]
                end_pos = level_positions['mid'][path[1]]

                arrow = FancyArrowPatch(start_pos, end_pos,
                                      arrowstyle='->', mutation_scale=15,
                                      color='gray', linewidth=1.5, alpha=0.4,
                                      connectionstyle="arc3,rad=0.1")
                ax_tree.add_patch(arrow)

            # Mid → Coarse
            if len(path) >= 3 and path[1] in level_positions['mid'] and path[2] in level_positions['coarse']:
                start_pos = level_positions['mid'][path[1]]
                end_pos = level_positions['coarse'][path[2]]

                arrow = FancyArrowPatch(start_pos, end_pos,
                                      arrowstyle='->', mutation_scale=15,
                                      color='gray', linewidth=1.5, alpha=0.4,
                                      connectionstyle="arc3,rad=0.1")
                ax_tree.add_patch(arrow)

    ax_tree.set_title("Hierarchical Ontology Tree (3-Level Clean Structure)",
                     fontsize=16, weight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved hierarchy tree: {output_path}")

def create_combined_visualization(vg_sample, objects, relationships, hierarchy, concept_paths,
                                 image_path, output_path):
    """
    Create combined 2-column visualization: scene graph + hierarchy.
    """
    print("\nCreating combined visualization...")

    fig = plt.figure(figsize=(24, 12))

    # Left panel: Scene graph
    ax_scene = plt.subplot(1, 2, 1)

    if image_path and os.path.exists(image_path):
        img = Image.open(image_path)
        ax_scene.imshow(img)

        object_map = {obj['object_id']: obj for obj in objects}
        colors = plt.cm.tab20(np.linspace(0, 1, min(20, len(objects))))

        # Draw bboxes
        for i, obj in enumerate(objects[:15]):
            color = colors[i % len(colors)]
            rect = patches.Rectangle((obj['x'], obj['y']), obj['w'], obj['h'],
                                    linewidth=3, edgecolor=color, facecolor='none', alpha=0.9)
            ax_scene.add_patch(rect)

            name = obj['names'][0] if obj['names'] else f"obj_{i}"
            ax_scene.text(obj['x'], max(0, obj['y'] - 5), name,
                         color='white', fontsize=10, weight='bold',
                         bbox=dict(boxstyle="round,pad=0.3", facecolor=color, alpha=0.9))

        # Draw relationships
        if relationships and 'relationships' in relationships:
            for rel in relationships['relationships'][:20]:
                try:
                    subj_id = rel['subject']['object_id']
                    obj_id = rel['object']['object_id']
                    predicate = rel['predicate']

                    if subj_id in object_map and obj_id in object_map:
                        subj = object_map[subj_id]
                        obj_target = object_map[obj_id]

                        subj_center = (subj['x'] + subj['w']/2, subj['y'] + subj['h']/2)
                        obj_center = (obj_target['x'] + obj_target['w']/2, obj_target['y'] + obj_target['h']/2)

                        arrow = FancyArrowPatch(subj_center, obj_center,
                                              arrowstyle='->', mutation_scale=25,
                                              color='yellow', linewidth=3, alpha=0.7)
                        ax_scene.add_patch(arrow)

                        mid_x = (subj_center[0] + obj_center[0]) / 2
                        mid_y = (subj_center[1] + obj_center[1]) / 2
                        ax_scene.text(mid_x, mid_y, predicate, fontsize=9, color='yellow',
                                     weight='bold', bbox=dict(boxstyle="round,pad=0.3",
                                     facecolor='black', alpha=0.8))
                except:
                    continue

    ax_scene.set_title("Original VG Scene Graph", fontsize=14, weight='bold')
    ax_scene.axis('off')

    # Right panel: Hierarchy tree (simplified)
    ax_hier = plt.subplot(1, 2, 2)
    ax_hier.set_xlim(0, 10)
    ax_hier.set_ylim(0, 10)
    ax_hier.axis('off')
    ax_hier.set_title("Hierarchical Ontology", fontsize=14, weight='bold')

    # Draw 3 levels vertically
    levels = ['coarse', 'mid', 'fine']
    colors_hier = ['#e74c3c', '#3498db', '#2ecc71']
    y_positions = [8, 5, 2]

    for i, level in enumerate(levels):
        y = y_positions[i]
        concepts = hierarchy[level][:8]

        # Draw level box
        rect = FancyBboxPatch((0.5, y - 0.5), 9, 1.5,
                             boxstyle="round,pad=0.1", facecolor=colors_hier[i],
                             edgecolor='black', alpha=0.3, linewidth=2)
        ax_hier.add_patch(rect)

        # Add label
        level_name = level.capitalize()
        ax_hier.text(0.2, y + 0.25, level_name, fontsize=11, weight='bold',
                    ha='left', va='center', color=colors_hier[i])

        # Add concepts
        concept_text = ", ".join(concepts[:5])
        if len(concepts) > 5:
            concept_text += f" ... (+{len(hierarchy[level])-5})"
        ax_hier.text(5, y + 0.25, concept_text, fontsize=9,
                    ha='center', va='center', style='italic')

        # Draw arrows between levels
        if i < len(levels) - 1:
            for j in range(3):
                ax_hier.arrow(2 + j*3, y - 0.6, 0, -1.3, head_width=0.2, head_length=0.2,
                            fc='gray', ec='gray', alpha=0.5, linewidth=1.5)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Saved combined visualization: {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Visualize VG scene graph + clean hierarchy')
    parser.add_argument('--vg_dir', default='../data/vg', help='VG data directory')
    parser.add_argument('--output_dir', default='vg', help='Output directory')
    parser.add_argument('--image_id', type=int, required=True, help='VG image ID')

    args = parser.parse_args()

    print("=" * 70)
    print("VG Scene Graph + Hierarchical Ontology Visualization")
    print("=" * 70)

    # Load VG data
    objects_file = os.path.join(args.vg_dir, 'annotations/v1.4/objects.json')
    relationships_file = os.path.join(args.vg_dir, 'annotations/v1.4/relationships.json')

    vg_sample, vg_relationships = load_vg_sample_with_relationships(
        objects_file, relationships_file, args.image_id)

    if not vg_sample:
        print(f"❌ Could not find VG image {args.image_id}")
        return

    objects = vg_sample['objects']
    print(f"✅ Loaded image {args.image_id} with {len(objects)} objects")

    if vg_relationships and 'relationships' in vg_relationships:
        print(f"✅ Loaded {len(vg_relationships['relationships'])} relationships")

    # Create output directory
    output_dir = os.path.join(args.output_dir, f"sample_{args.image_id}")
    os.makedirs(output_dir, exist_ok=True)

    # Find image file
    image_path = None
    for part in ['VG_100K/VG_100K', 'VG_100K_2']:
        test_path = os.path.join(args.vg_dir, f'images/{part}/{args.image_id}.jpg')
        if os.path.exists(test_path):
            image_path = test_path
            print(f"✅ Found image: {image_path}")
            break

    # Build hierarchy
    hierarchy, concept_paths, object_to_levels = build_clean_hierarchy(objects)

    # Create visualizations
    scene_graph_path = os.path.join(output_dir, 'original_scene_graph.png')
    visualize_scene_graph(vg_sample, objects, vg_relationships, image_path, scene_graph_path)

    hierarchy_path = os.path.join(output_dir, 'hierarchical_ontology_tree.png')
    visualize_hierarchy_tree(hierarchy, concept_paths, hierarchy_path)

    combined_path = os.path.join(output_dir, 'combined_visualization.png')
    create_combined_visualization(vg_sample, objects, vg_relationships, hierarchy,
                                 concept_paths, image_path, combined_path)

    # Save data
    output_data = {
        'image_id': args.image_id,
        'hierarchy': hierarchy,
        'concept_paths': concept_paths,
        'object_to_levels': object_to_levels,
        'statistics': {
            'num_objects': len(objects),
            'num_relationships': len(vg_relationships['relationships']) if vg_relationships else 0,
            'fine_concepts': len(hierarchy['fine']),
            'mid_concepts': len(hierarchy['mid']),
            'coarse_concepts': len(hierarchy['coarse']),
            'total_concepts': sum(len(hierarchy[k]) for k in hierarchy.keys())
        }
    }

    with open(os.path.join(output_dir, 'ontology_data.json'), 'w') as f:
        json.dump(output_data, f, indent=2)

    print("\n" + "=" * 70)
    print("✅ Visualization Complete!")
    print("=" * 70)
    print(f"Output: {output_dir}/")
    print(f"  - original_scene_graph.png")
    print(f"  - hierarchical_ontology_tree.png")
    print(f"  - combined_visualization.png")
    print(f"  - ontology_data.json")

if __name__ == '__main__':
    main()