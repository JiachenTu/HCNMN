#!/usr/bin/env python3
"""
Create annotated Visual Genome image with object bounding boxes and labels.
Verifies that VG annotations are correctly loaded and visualized.
"""
import os
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np

def create_annotated_image(input_dir, output_dir):
    """Create annotated VG image with bounding boxes and labels."""

    # Load VG objects data
    vg_objects_file = os.path.join(input_dir, 'vg_objects.json')
    with open(vg_objects_file, 'r') as f:
        vg_data = json.load(f)

    image_id = vg_data['image_id']
    objects = vg_data['objects']

    # Load the image
    image_file = os.path.join(input_dir, f'{image_id}.jpg')
    if not os.path.exists(image_file):
        print(f"Image file not found: {image_file}")
        return

    img = Image.open(image_file)
    img_array = np.array(img)

    # Create figure with high resolution
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.imshow(img_array)

    # Define colors for different object types
    colors = plt.cm.tab20(np.linspace(0, 1, 20))

    print(f"Annotating {len(objects)} objects on VG Image {image_id}")

    # Add bounding boxes and labels
    for i, obj in enumerate(objects):
        # Extract bounding box
        x, y, w, h = obj['x'], obj['y'], obj['w'], obj['h']

        # Choose color
        color = colors[i % len(colors)]

        # Create bounding box
        bbox = patches.Rectangle((x, y), w, h,
                               linewidth=2,
                               edgecolor=color,
                               facecolor='none',
                               alpha=0.8)
        ax.add_patch(bbox)

        # Get object name (first name in the list)
        obj_name = obj['names'][0] if obj['names'] else f"obj_{obj['object_id']}"

        # Get synset info if available
        synset_info = ""
        if obj.get('synsets'):
            synset_info = f" ({obj['synsets'][0]})"

        # Create label with background
        label_text = f"{i+1}: {obj_name}{synset_info}"

        # Position label above the bounding box
        label_y = max(0, y - 5)

        # Add text with background
        ax.text(x, label_y, label_text,
                color='white',
                fontsize=8,
                fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.3",
                         facecolor=color,
                         alpha=0.8,
                         edgecolor='white'))

        # Add object ID number inside the box
        center_x = x + w/2
        center_y = y + h/2
        ax.text(center_x, center_y, str(i+1),
                color='white',
                fontsize=12,
                fontweight='bold',
                ha='center', va='center',
                bbox=dict(boxstyle="circle,pad=0.3",
                         facecolor='red',
                         alpha=0.8))

    ax.set_title(f'Visual Genome Image {image_id} - Annotated Objects ({len(objects)} total)',
                fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')

    # Save annotated image
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'vg_image_{image_id}_annotated.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"Saved annotated image: {output_file}")

    # Create object legend
    create_object_legend(objects, output_dir, image_id)

    return output_file

def create_object_legend(objects, output_dir, image_id):
    """Create a separate legend showing all objects with their details."""

    fig, ax = plt.subplots(figsize=(12, max(8, len(objects) * 0.4)))
    ax.axis('off')

    # Create legend table
    legend_text = f"Visual Genome Image {image_id} - Object Annotations\n"
    legend_text += "=" * 60 + "\n\n"

    for i, obj in enumerate(objects):
        obj_name = obj['names'][0] if obj['names'] else f"obj_{obj['object_id']}"
        bbox_info = f"({obj['x']}, {obj['y']}, {obj['w']}×{obj['h']})"
        synset_info = obj['synsets'][0] if obj.get('synsets') else "No synset"

        legend_text += f"{i+1:2d}. {obj_name:<20} {bbox_info:<15} {synset_info}\n"

        # List all names if multiple
        if len(obj['names']) > 1:
            other_names = ", ".join(obj['names'][1:])
            legend_text += f"     Aliases: {other_names}\n"

    # Add summary statistics
    legend_text += "\n" + "=" * 60 + "\n"
    legend_text += f"Total Objects: {len(objects)}\n"
    legend_text += f"Objects with Synsets: {sum(1 for obj in objects if obj.get('synsets'))}\n"
    legend_text += f"Unique Object Types: {len(set(obj['names'][0] for obj in objects if obj['names']))}\n"

    # Calculate bounding box statistics
    areas = [obj['w'] * obj['h'] for obj in objects]
    legend_text += f"Average Object Size: {np.mean(areas):.0f} pixels²\n"
    legend_text += f"Size Range: {min(areas):.0f} - {max(areas):.0f} pixels²\n"

    ax.text(0.05, 0.95, legend_text,
            transform=ax.transAxes,
            fontsize=10,
            fontfamily='monospace',
            verticalalignment='top',
            bbox=dict(boxstyle="round,pad=0.5", facecolor='lightgray', alpha=0.8))

    # Save legend
    legend_file = os.path.join(output_dir, f'vg_image_{image_id}_legend.png')
    plt.savefig(legend_file, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

    print(f"Saved object legend: {legend_file}")

    return legend_file

if __name__ == "__main__":
    input_dir = "/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/sample_1/input"
    output_dir = "/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/sample_1/outputs"

    create_annotated_image(input_dir, output_dir)