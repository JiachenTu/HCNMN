#!/usr/bin/env python3
"""
Select diverse test images from Visual Genome for comprehensive method comparison.
Selects 10 images with varying complexity and scene types.
"""

import json
import random
from collections import defaultdict

# Load Visual Genome scene graphs
print("Loading Visual Genome scene graphs...")
scene_graphs_path = "/nas/jiachen/graph_reasoning/Graph-CoT/data/visual_genome/annotations/v1.2/scene_graphs.json"

with open(scene_graphs_path, 'r') as f:
    scene_graphs = json.load(f)

print(f"Total scene graphs: {len(scene_graphs)}")

# Analyze complexity
image_stats = []

for sg in scene_graphs:
    image_id = sg['image_id']
    num_objects = len(sg.get('objects', []))
    num_relationships = len(sg.get('relationships', []))

    # Filter: 10-40 objects, at least 5 relationships
    if 10 <= num_objects <= 40 and num_relationships >= 5:
        image_stats.append({
            'image_id': image_id,
            'num_objects': num_objects,
            'num_relationships': num_relationships,
            'complexity_score': num_objects + num_relationships * 0.5
        })

print(f"Filtered candidates: {len(image_stats)} images")

# Sort by complexity
image_stats.sort(key=lambda x: x['complexity_score'])

# Select 10 diverse images across complexity spectrum
# Take images from different quartiles to ensure diversity
total = len(image_stats)
indices = [
    int(0.05 * total),   # Very simple (5th percentile)
    int(0.15 * total),   # Simple
    int(0.25 * total),   # Lower-medium
    int(0.35 * total),   # Medium-low
    int(0.45 * total),   # Medium
    int(0.55 * total),   # Medium-high
    int(0.65 * total),   # Upper-medium
    int(0.75 * total),   # Complex
    int(0.85 * total),   # Very complex
    int(0.95 * total),   # Extremely complex (95th percentile)
]

selected_images = [image_stats[i] for i in indices]

# Add image 498335 (reference image) if not already selected
reference_id = 498335
if reference_id not in [img['image_id'] for img in selected_images]:
    # Find it in the stats
    reference_img = next((img for img in image_stats if img['image_id'] == reference_id), None)
    if reference_img:
        # Replace the median complexity image with reference
        selected_images[4] = reference_img
        print(f"✓ Added reference image {reference_id}")

# Sort by image_id for easier tracking
selected_images.sort(key=lambda x: x['image_id'])

# Display selection
print("\n=== Selected 10 Test Images ===\n")
print(f"{'Image ID':<10} {'Objects':<10} {'Relationships':<15} {'Complexity':<12}")
print("-" * 55)

for img in selected_images:
    print(f"{img['image_id']:<10} {img['num_objects']:<10} {img['num_relationships']:<15} {img['complexity_score']:<12.1f}")

# Save to file
output_file = "/nas/jiachen/graph_reasoning/HCNMN/inspect/test_images.txt"
with open(output_file, 'w') as f:
    for img in selected_images:
        f.write(f"{img['image_id']}\n")

print(f"\n✓ Saved to: {output_file}")

# Save detailed stats
stats_file = "/nas/jiachen/graph_reasoning/HCNMN/inspect/test_images_stats.json"
with open(stats_file, 'w') as f:
    json.dump(selected_images, f, indent=2)

print(f"✓ Saved stats to: {stats_file}")

print("\n=== Summary ===")
print(f"Total images selected: {len(selected_images)}")
print(f"Objects range: {min(img['num_objects'] for img in selected_images)}-{max(img['num_objects'] for img in selected_images)}")
print(f"Relationships range: {min(img['num_relationships'] for img in selected_images)}-{max(img['num_relationships'] for img in selected_images)}")
print(f"Complexity range: {min(img['complexity_score'] for img in selected_images):.1f}-{max(img['complexity_score'] for img in selected_images):.1f}")
