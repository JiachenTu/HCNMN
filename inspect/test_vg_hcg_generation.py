#!/usr/bin/env python3
"""
Visual Genome Hierarchical Concept Graph (HCG) Generation Demo
Demonstrates end-to-end HCG creation from Visual Genome object annotations.
"""
import os
import sys
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import networkx as nx
from collections import defaultdict
import shutil
import urllib.request
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_vg_objects(objects_file, sample_image_id=None):
    """Load Visual Genome objects and select a good sample."""
    print(f"Loading Visual Genome objects from {objects_file}")

    # For very large files, we'll process in chunks to find a good sample
    sample_data = None
    samples_checked = 0
    target_object_range = (15, 30)  # Good range for rich concept graphs

    try:
        with open(objects_file, 'r') as f:
            # Try to load incrementally to find a good sample
            content = f.read()
            if content.startswith('['):
                # Parse as JSON array
                data = json.loads(content)

                if sample_image_id:
                    # Find specific image
                    for item in data:
                        if item['image_id'] == sample_image_id:
                            sample_data = item
                            break
                else:
                    # Find image with good object count
                    for item in data[:100]:  # Check first 100 images
                        object_count = len(item.get('objects', []))
                        if target_object_range[0] <= object_count <= target_object_range[1]:
                            sample_data = item
                            break
                        samples_checked += 1

                    # Fallback to first available if no ideal found
                    if not sample_data and data:
                        sample_data = data[0]

    except Exception as e:
        print(f"Error loading VG objects: {e}")
        # Create a sample mock data for demonstration
        sample_data = create_mock_vg_sample()

    if sample_data:
        print(f"Selected VG sample:")
        print(f"  Image ID: {sample_data['image_id']}")
        print(f"  Objects: {len(sample_data.get('objects', []))}")
        print(f"  URL: {sample_data.get('image_url', 'N/A')}")

    return sample_data

def create_mock_vg_sample():
    """Create a mock VG sample for demonstration when real data is unavailable."""
    return {
        'image_id': 1,
        'image_url': 'https://cs.stanford.edu/people/rak248/VG_100K_2/1.jpg',
        'objects': [
            {'synsets': ['tree.n.01'], 'h': 557, 'object_id': 1058549, 'names': ['trees'], 'w': 799, 'y': 0, 'x': 0},
            {'synsets': ['sidewalk.n.01'], 'h': 290, 'object_id': 1058534, 'names': ['sidewalk'], 'w': 722, 'y': 308, 'x': 78},
            {'synsets': ['building.n.01'], 'h': 538, 'object_id': 1058508, 'names': ['building'], 'w': 222, 'y': 0, 'x': 1},
            {'synsets': ['street.n.01'], 'h': 258, 'object_id': 1058539, 'names': ['street'], 'w': 359, 'y': 283, 'x': 439},
            {'synsets': ['wall.n.01'], 'h': 535, 'object_id': 1058543, 'names': ['wall'], 'w': 135, 'y': 1, 'x': 0},
            {'synsets': ['tree.n.01'], 'h': 360, 'object_id': 1058545, 'names': ['tree'], 'w': 476, 'y': 0, 'x': 178},
            {'synsets': ['van.n.05'], 'h': 176, 'object_id': 1058542, 'names': ['van'], 'w': 241, 'y': 278, 'x': 533},
            {'synsets': ['clock.n.01'], 'h': 363, 'object_id': 1058498, 'names': ['clock'], 'w': 77, 'y': 63, 'x': 422},
            {'synsets': ['window.n.01'], 'h': 147, 'object_id': 3798579, 'names': ['windows'], 'w': 198, 'y': 1, 'x': 602},
            {'synsets': ['man.n.01'], 'h': 248, 'object_id': 3798576, 'names': ['man'], 'w': 82, 'y': 264, 'x': 367},
            {'synsets': ['man.n.01'], 'h': 259, 'object_id': 3798577, 'names': ['man'], 'w': 57, 'y': 254, 'x': 238},
            {'synsets': ['sign.n.02'], 'h': 179, 'object_id': 1058507, 'names': ['sign'], 'w': 78, 'y': 13, 'x': 123},
            {'synsets': ['car.n.01'], 'h': 164, 'object_id': 1058515, 'names': ['car'], 'w': 80, 'y': 342, 'x': 719},
            {'synsets': ['jacket.n.01'], 'h': 98, 'object_id': 1058530, 'names': ['jacket'], 'w': 82, 'y': 296, 'x': 367},
            {'synsets': ['car.n.01'], 'h': 95, 'object_id': 5049, 'names': ['car'], 'w': 78, 'y': 319, 'x': 478},
            {'synsets': ['trouser.n.01'], 'h': 128, 'object_id': 1058531, 'names': ['pants'], 'w': 48, 'y': 369, 'x': 388},
            {'synsets': ['shirt.n.01'], 'h': 103, 'object_id': 1058511, 'names': ['shirt'], 'w': 54, 'y': 287, 'x': 241},
            {'synsets': ['parking_meter.n.01'], 'h': 143, 'object_id': 1058519, 'names': ['parking meter'], 'w': 26, 'y': 325, 'x': 577},
            {'synsets': ['shoe.n.01'], 'h': 28, 'object_id': 1058525, 'names': ['shoes'], 'w': 48, 'y': 485, 'x': 388},
            {'synsets': ['bicycle.n.01'], 'h': 36, 'object_id': 1058535, 'names': ['bike'], 'w': 27, 'y': 319, 'x': 337}
        ]
    }

def extract_concepts_from_objects(vg_sample, vocab_data, hierarchy_data):
    """Extract hierarchical concepts from VG object annotations."""
    print("\nExtracting concepts from VG objects...")

    objects = vg_sample.get('objects', [])
    all_object_names = []

    # Extract all object names
    for obj in objects:
        names = obj.get('names', [])
        all_object_names.extend(names)

    # Remove duplicates while preserving order
    unique_names = []
    seen = set()
    for name in all_object_names:
        if name not in seen:
            unique_names.append(name)
            seen.add(name)

    print(f"  Unique object names: {unique_names[:10]}{'...' if len(unique_names) > 10 else ''}")

    # Expand concepts using hierarchies (similar to VQA approach)
    concepts = []
    concept_hierarchies = []
    token_to_idx = vocab_data.get('question_token_to_idx', {})

    for name in unique_names:
        name_clean = name.lower().replace(' ', '_')

        if name_clean in hierarchy_data:
            # Use hierarchy expansion
            expanded = hierarchy_data[name_clean][:5]  # Limit to top 5
            concepts.extend(expanded)
            concept_hierarchies.extend([len(expanded)] * len(expanded))
        elif name_clean in token_to_idx:
            # Use vocabulary
            concepts.append(name_clean)
            concept_hierarchies.append(0)
        else:
            # Keep original
            concepts.append(name)
            concept_hierarchies.append(0)

    # Remove duplicates
    unique_concepts = []
    unique_hierarchies = []
    seen = set()

    for concept, hierarchy in zip(concepts, concept_hierarchies):
        if concept not in seen:
            unique_concepts.append(concept)
            unique_hierarchies.append(hierarchy)
            seen.add(concept)

    print(f"  Original objects: {len(unique_names)}")
    print(f"  Expanded concepts: {len(unique_concepts)}")
    print(f"  Concept sample: {unique_concepts[:8]}...")

    return unique_concepts, unique_hierarchies, objects

def calculate_spatial_overlap(box1, box2):
    """Calculate overlap ratio between two bounding boxes."""
    x1, y1, w1, h1 = box1['x'], box1['y'], box1['w'], box1['h']
    x2, y2, w2, h2 = box2['x'], box2['y'], box2['w'], box2['h']

    # Calculate intersection
    x_left = max(x1, x2)
    y_top = max(y1, y2)
    x_right = min(x1 + w1, x2 + w2)
    y_bottom = min(y1 + h1, y2 + h2)

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    intersection = (x_right - x_left) * (y_bottom - y_top)
    area1 = w1 * h1
    area2 = w2 * h2
    union = area1 + area2 - intersection

    return intersection / union if union > 0 else 0.0

def build_spatial_topology(objects, concepts):
    """Build topology matrix based on spatial relationships between objects."""
    print("\nBuilding spatial topology from object relationships...")

    n_concepts = len(concepts)
    n_objects = len(objects)

    # Create object-to-concept mapping (simplified: 1-to-1 for now)
    object_concept_map = {}
    for i, obj in enumerate(objects[:n_concepts]):
        object_concept_map[i] = i

    # Calculate spatial topology
    topology_matrix = np.zeros((n_concepts, n_concepts))

    overlap_threshold = 0.1  # Minimum overlap for connection
    spatial_connections = 0

    for i in range(min(n_objects, n_concepts)):
        for j in range(i + 1, min(n_objects, n_concepts)):
            if i in object_concept_map and j in object_concept_map:
                overlap = calculate_spatial_overlap(objects[i], objects[j])

                if overlap > overlap_threshold:
                    ci, cj = object_concept_map[i], object_concept_map[j]
                    topology_matrix[ci, cj] = overlap
                    topology_matrix[cj, ci] = overlap  # Symmetric
                    spatial_connections += 1

                # Also add proximity-based connections
                dist = np.sqrt((objects[i]['x'] - objects[j]['x'])**2 +
                              (objects[i]['y'] - objects[j]['y'])**2)
                if dist < 200:  # Close proximity threshold
                    ci, cj = object_concept_map[i], object_concept_map[j]
                    proximity_weight = max(0.1, 1.0 - dist/200)
                    topology_matrix[ci, cj] = max(topology_matrix[ci, cj], proximity_weight * 0.5)
                    topology_matrix[cj, ci] = topology_matrix[ci, cj]

    print(f"  Topology matrix shape: {topology_matrix.shape}")
    print(f"  Spatial connections: {spatial_connections}")
    print(f"  Total connections: {np.sum(topology_matrix > 0)}")

    return topology_matrix

def generate_object_properties(objects, concepts, property_data):
    """Generate property vectors based on object characteristics."""
    print("\nGenerating object-based properties...")

    properties = property_data.get('properties', [])
    if not properties:
        # Create comprehensive visual properties
        properties = [
            'red', 'blue', 'green', 'yellow', 'black', 'white', 'brown', 'gray',
            'large', 'small', 'medium', 'tiny', 'huge',
            'round', 'square', 'rectangular', 'circular', 'linear',
            'metal', 'wood', 'glass', 'plastic', 'fabric', 'stone',
            'indoor', 'outdoor', 'natural', 'artificial', 'movable', 'fixed'
        ]

    n_concepts = len(concepts)
    n_properties = len(properties)
    property_vectors = np.zeros((n_concepts, n_properties))

    # Property assignment based on object names and types
    property_assignments = 0

    for i, concept in enumerate(concepts):
        concept_lower = concept.lower()

        # Color properties
        color_map = {
            'red': 0, 'blue': 1, 'green': 2, 'yellow': 3,
            'black': 4, 'white': 5, 'brown': 6, 'gray': 7
        }
        for color, idx in color_map.items():
            if idx < n_properties and color in concept_lower:
                property_vectors[i, idx] = 1.0
                property_assignments += 1

        # Size properties
        if any(word in concept_lower for word in ['big', 'large', 'huge', 'giant']) and 8 < n_properties:
            property_vectors[i, 8] = 1.0  # large
            property_assignments += 1
        if any(word in concept_lower for word in ['small', 'tiny', 'little', 'mini']) and 9 < n_properties:
            property_vectors[i, 9] = 1.0  # small
            property_assignments += 1

        # Shape properties
        if any(word in concept_lower for word in ['round', 'circle', 'ball', 'wheel']) and 13 < n_properties:
            property_vectors[i, 13] = 1.0  # round
            property_assignments += 1
        if any(word in concept_lower for word in ['square', 'box', 'rectangle']) and 14 < n_properties:
            property_vectors[i, 14] = 1.0  # square
            property_assignments += 1

        # Material properties
        material_map = {
            'metal': ['metal', 'steel', 'iron', 'car', 'bike'],
            'wood': ['wood', 'tree', 'wooden'],
            'glass': ['glass', 'window'],
            'fabric': ['shirt', 'pants', 'jacket', 'clothing']
        }

        for prop_idx, (material, keywords) in enumerate(material_map.items()):
            prop_pos = 19 + prop_idx  # Starting from position 19
            if prop_pos < n_properties and any(kw in concept_lower for kw in keywords):
                property_vectors[i, prop_pos] = 1.0
                property_assignments += 1

    print(f"  Property matrix shape: {property_vectors.shape}")
    print(f"  Available properties: {len(properties)}")
    print(f"  Property assignments: {property_assignments}")

    return property_vectors, properties

def download_image(image_url, output_path):
    """Download VG image from URL."""
    try:
        print(f"Downloading image from: {image_url}")
        urllib.request.urlretrieve(image_url, output_path)
        return True
    except Exception as e:
        print(f"Failed to download image: {e}")
        return False

def create_vg_visualization(vg_sample, objects, concepts, topology_matrix,
                           property_vectors, properties, output_dir):
    """Create comprehensive 5-panel VG HCG visualization."""
    print("\nCreating VG HCG visualizations...")

    image_id = vg_sample['image_id']

    # Try to get the actual image
    image_path = os.path.join(output_dir, f"input/{image_id}.jpg")
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    has_image = False
    if vg_sample.get('image_url'):
        has_image = download_image(vg_sample['image_url'], image_path)

    # Create the 5-panel visualization
    fig = plt.figure(figsize=(20, 12))

    # Panel 1: Original Image with Bounding Boxes (if available)
    ax1 = plt.subplot(2, 3, 1)
    if has_image and os.path.exists(image_path):
        try:
            img = plt.imread(image_path)
            ax1.imshow(img)

            # Add bounding boxes
            for i, obj in enumerate(objects[:10]):  # Limit to first 10 for clarity
                bbox = patches.Rectangle((obj['x'], obj['y']), obj['w'], obj['h'],
                                       linewidth=2, edgecolor=plt.cm.tab10(i % 10),
                                       facecolor='none', alpha=0.8)
                ax1.add_patch(bbox)

                # Add object label
                ax1.text(obj['x'], obj['y'] - 5, obj['names'][0] if obj['names'] else f"obj_{i}",
                        color=plt.cm.tab10(i % 10), fontsize=8, weight='bold',
                        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.7))

        except Exception as e:
            ax1.text(0.5, 0.5, f"Image unavailable\nID: {image_id}",
                    ha='center', va='center', transform=ax1.transAxes)
    else:
        ax1.text(0.5, 0.5, f"VG Image {image_id}\n({len(objects)} objects)",
                ha='center', va='center', transform=ax1.transAxes, fontsize=14)

    ax1.set_title(f"VG Image {image_id} with Objects", fontsize=14)
    ax1.axis('off')

    # Panel 2: Concept Graph Network
    ax2 = plt.subplot(2, 3, 2)
    G = nx.Graph()

    # Add nodes
    for i, concept in enumerate(concepts):
        G.add_node(i, label=concept[:8])

    # Add edges based on topology
    for i in range(len(concepts)):
        for j in range(i+1, len(concepts)):
            if topology_matrix[i, j] > 0.1:  # Threshold for visualization
                G.add_edge(i, j, weight=topology_matrix[i, j])

    pos = nx.spring_layout(G, k=3, iterations=50)

    # Draw network
    nx.draw_networkx_nodes(G, pos, node_color='lightblue',
                          node_size=1000, alpha=0.7, ax=ax2)
    nx.draw_networkx_edges(G, pos, alpha=0.5, ax=ax2)

    # Labels
    labels = {i: concept[:8] + '...' if len(concept) > 8 else concept
              for i, concept in enumerate(concepts)}
    nx.draw_networkx_labels(G, pos, labels, font_size=8, ax=ax2)

    ax2.set_title("Concept Graph Network")
    ax2.axis('off')

    # Panel 3: Spatial Topology Matrix
    ax3 = plt.subplot(2, 3, 3)
    im3 = ax3.imshow(topology_matrix, cmap='Blues', aspect='auto')
    plt.colorbar(im3, ax=ax3)
    ax3.set_title("Spatial Topology Matrix")
    ax3.set_xlabel("Concept Index")
    ax3.set_ylabel("Concept Index")

    # Panel 4: Object Properties
    ax4 = plt.subplot(2, 3, 4)
    im4 = ax4.imshow(property_vectors.T, cmap='Reds', aspect='auto')
    plt.colorbar(im4, ax=ax4)
    ax4.set_title("Object Properties")
    ax4.set_xlabel("Concept Index")
    ax4.set_ylabel("Property Index")

    # Add property labels if not too many
    if len(properties) <= 15:
        ax4.set_yticks(range(len(properties)))
        ax4.set_yticklabels(properties, fontsize=8)

    # Panel 5: Property Distribution
    ax5 = plt.subplot(2, 3, 5)
    property_counts = np.sum(property_vectors, axis=1)
    concept_indices = range(min(len(concepts), 15))  # Show first 15
    concept_names = [concept[:8] for concept in concepts[:15]]

    bars = ax5.bar(concept_indices, property_counts[:15])
    ax5.set_title("Properties per Concept")
    ax5.set_xlabel("Concept")
    ax5.set_ylabel("Number of Properties")
    ax5.set_xticks(concept_indices)
    ax5.set_xticklabels(concept_names, rotation=45, ha='right', fontsize=8)

    # Panel 6: Statistics Summary
    ax6 = plt.subplot(2, 3, 6)
    ax6.axis('off')

    stats_text = f"""VG HCG Statistics:

Image ID: {image_id}
Objects: {len(objects)}
Concepts: {len(concepts)}
Spatial Connections: {np.sum(topology_matrix > 0)}
Properties: {len(properties)}
Property Assignments: {np.sum(property_vectors > 0)}

Topology Density: {np.sum(topology_matrix > 0) / (len(concepts)**2):.3f}
Avg Properties/Concept: {np.mean(np.sum(property_vectors, axis=1)):.2f}
Coverage: {len(concepts)/len(objects):.2f}x expansion
    """

    ax6.text(0.1, 0.9, stats_text, transform=ax6.transAxes, fontsize=10,
             verticalalignment='top', fontfamily='monospace')

    plt.tight_layout()

    # Save visualization
    viz_path = os.path.join(output_dir, 'outputs/vg_hcg_visualization.png')
    os.makedirs(os.path.dirname(viz_path), exist_ok=True)
    plt.savefig(viz_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"  Saved VG HCG visualization: {viz_path}")

    return viz_path

def save_vg_hcg_data(vg_sample, objects, concepts, topology_matrix,
                     property_vectors, properties, output_dir):
    """Save comprehensive VG HCG data and analysis."""
    print("\nSaving VG HCG data...")

    image_id = vg_sample['image_id']

    # Create output directories
    input_dir = os.path.join(output_dir, 'input')
    hcg_dir = os.path.join(output_dir, 'hcg_data')
    outputs_dir = os.path.join(output_dir, 'outputs')
    model_dir = os.path.join(outputs_dir, 'model_integration')

    for dir_path in [input_dir, hcg_dir, outputs_dir, model_dir]:
        os.makedirs(dir_path, exist_ok=True)

    # Save input VG data
    with open(os.path.join(input_dir, 'vg_objects.json'), 'w') as f:
        json.dump({
            'image_id': image_id,
            'image_url': vg_sample.get('image_url'),
            'objects': objects
        }, f, indent=2)

    # Save HCG data
    hcg_data = {
        'image_id': image_id,
        'concepts': concepts,
        'objects': objects,
        'topology_matrix': topology_matrix.tolist(),
        'property_vectors': property_vectors.tolist(),
        'properties': properties,
        'statistics': {
            'num_objects': len(objects),
            'num_concepts': len(concepts),
            'num_properties': len(properties),
            'spatial_connections': int(np.sum(topology_matrix > 0)),
            'property_assignments': int(np.sum(property_vectors > 0)),
            'topology_density': float(np.sum(topology_matrix > 0) / (len(concepts)**2)) if len(concepts) > 0 else 0,
            'avg_properties_per_concept': float(np.mean(np.sum(property_vectors, axis=1))) if len(concepts) > 0 else 0,
            'concept_coverage': len(concepts) / len(objects) if len(objects) > 0 else 0
        }
    }

    with open(os.path.join(hcg_dir, 'concepts.json'), 'w') as f:
        json.dump({'concepts': concepts, 'hierarchies': []}, f, indent=2)

    with open(os.path.join(hcg_dir, 'topology.json'), 'w') as f:
        json.dump({'topology_matrix': topology_matrix.tolist()}, f, indent=2)

    with open(os.path.join(hcg_dir, 'properties.json'), 'w') as f:
        json.dump({
            'property_vectors': property_vectors.tolist(),
            'properties': properties
        }, f, indent=2)

    # Save complete analysis
    with open(os.path.join(outputs_dir, 'vg_hcg_analysis.json'), 'w') as f:
        json.dump(hcg_data, f, indent=2)

    # Save model-compatible files
    with open(os.path.join(model_dir, 'topology_vg.json'), 'w') as f:
        json.dump({'topology_per_question': [topology_matrix.tolist()]}, f)

    with open(os.path.join(model_dir, 'concept_property_vg.json'), 'w') as f:
        json.dump({'property_vector_per_question': [property_vectors.tolist()]}, f)

    with open(os.path.join(model_dir, 'relation_vg.json'), 'w') as f:
        json.dump({
            'relations': ['spatial_overlap', 'spatial_proximity', 'visual_similarity'],
            'relation_embeddings': []
        }, f)

    with open(os.path.join(model_dir, 'property_vg.json'), 'w') as f:
        json.dump({'properties': properties, 'property_embeddings': []}, f)

    print(f"  Saved VG data: {input_dir}/")
    print(f"  Saved HCG data: {hcg_dir}/")
    print(f"  Saved analysis: {outputs_dir}/vg_hcg_analysis.json")
    print(f"  Saved model files: {model_dir}/")

    return hcg_data

def main():
    parser = argparse.ArgumentParser(description='Generate HCG from Visual Genome annotations')
    parser.add_argument('--vg_dir', default='../data/vg', help='Visual Genome data directory')
    parser.add_argument('--data_dir', default='../data', help='HCNMN data directory')
    parser.add_argument('--output_dir', default='vg', help='Output directory (relative to inspect/)')
    parser.add_argument('--sample_id', type=int, default=None, help='Specific VG image ID to process')

    args = parser.parse_args()

    # Setup paths
    vg_objects_file = os.path.join(args.vg_dir, 'annotations/v1.4/objects.json')
    vocab_file = os.path.join(args.data_dir, 'features/vocab_augmented.json')
    hierarchy_file = os.path.join(args.data_dir, 'features/hierarchy.json')
    property_file = os.path.join(args.data_dir, 'features/property.json')

    print("=== Visual Genome HCG Generation Demo ===\n")

    # Load VG sample
    vg_sample = load_vg_objects(vg_objects_file, args.sample_id)
    if not vg_sample:
        print("❌ Could not load VG sample")
        return

    # Create sample-specific output directory
    sample_output_dir = os.path.join(args.output_dir, f"sample_{vg_sample['image_id']}")
    os.makedirs(sample_output_dir, exist_ok=True)

    # Load vocabulary and hierarchy data
    print("\nLoading vocabulary and knowledge data...")
    try:
        with open(vocab_file, 'r') as f:
            vocab_data = json.load(f)
        with open(hierarchy_file, 'r') as f:
            hierarchy_data = json.load(f)
    except FileNotFoundError as e:
        print(f"❌ Missing required file: {e}")
        return

    # Load property data (optional)
    try:
        with open(property_file, 'r') as f:
            property_data = json.load(f)
    except FileNotFoundError:
        property_data = {'properties': [], 'property_embeddings': []}

    # Extract concepts from VG objects
    concepts, hierarchies, objects = extract_concepts_from_objects(
        vg_sample, vocab_data, hierarchy_data)

    # Build spatial topology
    topology_matrix = build_spatial_topology(objects, concepts)

    # Generate object properties
    property_vectors, properties = generate_object_properties(objects, concepts, property_data)

    # Create visualizations
    viz_path = create_vg_visualization(
        vg_sample, objects, concepts, topology_matrix,
        property_vectors, properties, sample_output_dir)

    # Save comprehensive data
    hcg_data = save_vg_hcg_data(
        vg_sample, objects, concepts, topology_matrix,
        property_vectors, properties, sample_output_dir)

    # Print summary
    print("\n=== VG HCG Generation Summary ===")
    print(f"Image ID: {vg_sample['image_id']}")
    print(f"Objects detected: {len(objects)}")
    print(f"Concepts extracted: {len(concepts)}")
    print(f"Spatial connections: {hcg_data['statistics']['spatial_connections']}")
    print(f"Properties assigned: {len(properties)}")
    print(f"Topology density: {hcg_data['statistics']['topology_density']:.3f}")
    print(f"Concept coverage: {hcg_data['statistics']['concept_coverage']:.2f}x")
    print(f"\nOutputs saved to: {sample_output_dir}/")

    return hcg_data

if __name__ == '__main__':
    main()