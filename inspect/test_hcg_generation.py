#!/usr/bin/env python3
"""
Test script for Hierarchical Concept Graph (HCG) generation.
Demonstrates end-to-end HCG creation from sample VQA question and image.
"""
import os
import sys
import json
import pickle
import argparse
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_sample_question(questions_file, annotations_file, sample_id=0):
    """Load a sample question and annotation from VQA dataset."""
    print(f"Loading sample question {sample_id}...")

    with open(questions_file, 'r') as f:
        questions_data = json.load(f)

    with open(annotations_file, 'r') as f:
        annotations_data = json.load(f)

    # Get sample question
    question_data = questions_data['questions'][sample_id]
    question_id = question_data['question_id']
    question_text = question_data['question']
    image_id = question_data['image_id']

    # Find corresponding annotation
    annotation = None
    for ann in annotations_data['annotations']:
        if ann['question_id'] == question_id:
            annotation = ann
            break

    sample = {
        'question_id': question_id,
        'image_id': image_id,
        'question': question_text,
        'answer': annotation['multiple_choice_answer'] if annotation else 'unknown',
        'answer_type': annotation['answer_type'] if annotation else 'unknown'
    }

    print(f"Sample {sample_id}:")
    print(f"  Question: {question_text}")
    print(f"  Answer: {sample['answer']}")
    print(f"  Image ID: {image_id}")

    return sample

def extract_question_concepts(question_text, vocab_data, hierarchy_data):
    """Extract concepts from question using vocabulary and hierarchy."""
    print("\\nExtracting concepts from question...")

    # Tokenize question (simple word splitting)
    question_tokens = question_text.lower().replace('?', '').replace(',', '').split()

    # Find tokens that exist in vocabulary
    token_to_idx = vocab_data.get('question_token_to_idx', {})
    valid_tokens = [token for token in question_tokens if token in token_to_idx]

    # Get hierarchical expansion for each token
    concepts = []
    concept_hierarchies = []

    if 'terms' in vocab_data and 'term_per_question' in vocab_data:
        # Use pre-computed term expansions
        for i, term in enumerate(vocab_data['terms']):
            if term in valid_tokens:
                expanded_terms = vocab_data['term_per_question'][i]
                hierarchies = vocab_data.get('hierarchy_per_question', [[]] * len(vocab_data['terms']))[i]

                concepts.extend(expanded_terms[:5])  # Limit to top 5 expansions
                concept_hierarchies.extend(hierarchies[:5])
    else:
        # Fallback: use vocabulary hierarchy data
        for token in valid_tokens:
            if token in hierarchy_data:
                expanded_terms = hierarchy_data[token][:5]  # Limit expansions
                concepts.extend(expanded_terms)
                concept_hierarchies.extend([len(expanded_terms)] * len(expanded_terms))
            else:
                concepts.append(token)
                concept_hierarchies.append(0)

    # Remove duplicates while preserving order
    unique_concepts = []
    unique_hierarchies = []
    seen = set()

    for concept, hierarchy in zip(concepts, concept_hierarchies):
        if concept not in seen:
            unique_concepts.append(concept)
            unique_hierarchies.append(hierarchy)
            seen.add(concept)

    print(f"  Original tokens: {question_tokens}")
    print(f"  Valid vocabulary tokens: {valid_tokens}")
    print(f"  Expanded concepts: {unique_concepts[:10]}...")  # Show first 10
    print(f"  Hierarchy depths: {unique_hierarchies[:10]}...")

    return unique_concepts, unique_hierarchies

def build_concept_topology(concepts, relation_data, property_data):
    """Build topology matrix showing concept relationships."""
    print("\\nBuilding concept topology...")

    n_concepts = len(concepts)
    topology_matrix = np.zeros((n_concepts, n_concepts))

    # Load relation mappings
    relations = relation_data.get('relations', [])
    concept_relations = defaultdict(list)

    # Simple relation mapping (can be enhanced with real ConceptNet data)
    for i, concept1 in enumerate(concepts):
        for j, concept2 in enumerate(concepts):
            if i != j:
                # Example relations based on word similarity or hierarchy
                if concept1 in concept2 or concept2 in concept1:
                    topology_matrix[i, j] = 1.0  # Hierarchical relation
                elif len(set(concept1.split()) & set(concept2.split())) > 0:
                    topology_matrix[i, j] = 0.5  # Semantic similarity

    print(f"  Topology matrix shape: {topology_matrix.shape}")
    print(f"  Number of connections: {np.sum(topology_matrix > 0)}")

    return topology_matrix

def generate_concept_properties(concepts, property_data):
    """Generate property vectors for concepts."""
    print("\\nGenerating concept properties...")

    properties = property_data.get('properties', [])
    if not properties:
        # Create sample properties
        properties = ['red', 'blue', 'large', 'small', 'round', 'square', 'metal', 'wood']

    n_concepts = len(concepts)
    n_properties = len(properties)
    property_vectors = np.zeros((n_concepts, n_properties))

    # Assign properties based on concept characteristics (simplified)
    for i, concept in enumerate(concepts):
        concept_lower = concept.lower()

        # Color properties
        if 'red' in concept_lower or 'fire' in concept_lower:
            property_vectors[i, 0] = 1.0  # red
        if 'blue' in concept_lower or 'sky' in concept_lower or 'water' in concept_lower:
            property_vectors[i, 1] = 1.0  # blue

        # Size properties
        if any(word in concept_lower for word in ['big', 'large', 'huge', 'giant']):
            property_vectors[i, 2] = 1.0  # large
        if any(word in concept_lower for word in ['small', 'tiny', 'little']):
            property_vectors[i, 3] = 1.0  # small

        # Shape properties
        if any(word in concept_lower for word in ['round', 'circle', 'ball']):
            property_vectors[i, 4] = 1.0  # round
        if any(word in concept_lower for word in ['square', 'box', 'rectangle']):
            property_vectors[i, 5] = 1.0  # square

        # Material properties
        if any(word in concept_lower for word in ['metal', 'steel', 'iron']):
            property_vectors[i, 6] = 1.0  # metal
        if any(word in concept_lower for word in ['wood', 'tree', 'wooden']):
            property_vectors[i, 7] = 1.0  # wood

    print(f"  Property matrix shape: {property_vectors.shape}")
    print(f"  Properties: {properties}")
    print(f"  Non-zero property assignments: {np.sum(property_vectors > 0)}")

    return property_vectors, properties

def visualize_hcg(concepts, topology_matrix, property_vectors, properties, output_dir):
    """Create visualizations of the hierarchical concept graph."""
    print("\\nCreating HCG visualizations...")

    os.makedirs(output_dir, exist_ok=True)

    # 1. Concept Graph Network
    plt.figure(figsize=(12, 8))

    # Create networkx graph
    G = nx.Graph()

    # Add nodes
    for i, concept in enumerate(concepts):
        G.add_node(i, label=concept)

    # Add edges based on topology matrix
    for i in range(len(concepts)):
        for j in range(i+1, len(concepts)):
            if topology_matrix[i, j] > 0:
                G.add_edge(i, j, weight=topology_matrix[i, j])

    # Create layout
    pos = nx.spring_layout(G, k=2, iterations=50)

    # Draw network
    plt.subplot(2, 2, 1)
    nx.draw_networkx_nodes(G, pos, node_color='lightblue',
                          node_size=1000, alpha=0.7)
    nx.draw_networkx_edges(G, pos, alpha=0.5)

    # Add labels
    labels = {i: concept[:8] + '...' if len(concept) > 8 else concept
              for i, concept in enumerate(concepts)}
    nx.draw_networkx_labels(G, pos, labels, font_size=8)

    plt.title("Concept Graph Network")
    plt.axis('off')

    # 2. Topology Matrix Heatmap
    plt.subplot(2, 2, 2)
    plt.imshow(topology_matrix, cmap='Blues', aspect='auto')
    plt.colorbar()
    plt.title("Concept Topology Matrix")
    plt.xlabel("Concept Index")
    plt.ylabel("Concept Index")

    # 3. Property Matrix Heatmap
    plt.subplot(2, 2, 3)
    plt.imshow(property_vectors.T, cmap='Reds', aspect='auto')
    plt.colorbar()
    plt.title("Concept Properties")
    plt.xlabel("Concept Index")
    plt.ylabel("Property Index")

    # Add property labels
    if len(properties) <= 10:  # Only if not too many properties
        plt.yticks(range(len(properties)), properties, fontsize=8)

    # 4. Concept Hierarchy Bar Chart
    plt.subplot(2, 2, 4)
    concept_indices = range(min(len(concepts), 10))  # Show first 10 concepts
    concept_names = [concept[:10] for concept in concepts[:10]]

    plt.bar(concept_indices, [np.sum(property_vectors[i]) for i in concept_indices])
    plt.title("Property Count per Concept")
    plt.xlabel("Concept")
    plt.ylabel("Number of Properties")
    plt.xticks(concept_indices, concept_names, rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'hcg_visualization.png'), dpi=300, bbox_inches='tight')
    plt.close()

    # Save detailed concept information
    concept_info = {
        'concepts': concepts,
        'topology_matrix': topology_matrix.tolist(),
        'property_vectors': property_vectors.tolist(),
        'properties': properties,
        'statistics': {
            'num_concepts': len(concepts),
            'num_properties': len(properties),
            'num_connections': int(np.sum(topology_matrix > 0)),
            'avg_properties_per_concept': float(np.mean(np.sum(property_vectors, axis=1))),
            'graph_density': float(np.sum(topology_matrix > 0) / (len(concepts) * (len(concepts) - 1)))
        }
    }

    with open(os.path.join(output_dir, 'hcg_data.json'), 'w') as f:
        json.dump(concept_info, f, indent=2)

    print(f"  Saved visualization: {output_dir}/hcg_visualization.png")
    print(f"  Saved HCG data: {output_dir}/hcg_data.json")

    return concept_info

def test_model_integration(hcg_data, output_dir):
    """Test integration with HCNMN model format."""
    print("\\nTesting model integration format...")

    # Create model-compatible data structures
    model_data = {
        'topology_per_question': [hcg_data['topology_matrix']],
        'property_vector_per_question': [hcg_data['property_vectors']],
        'relations': ['IsA', 'PartOf', 'HasProperty', 'SimilarTo'],
        'properties': hcg_data['properties']
    }

    # Save in expected format
    with open(os.path.join(output_dir, 'topology_sample.json'), 'w') as f:
        json.dump({'topology_per_question': model_data['topology_per_question']}, f)

    with open(os.path.join(output_dir, 'concept_property_sample.json'), 'w') as f:
        json.dump({'property_vector_per_question': model_data['property_vector_per_question']}, f)

    with open(os.path.join(output_dir, 'relation_sample.json'), 'w') as f:
        json.dump({'relations': model_data['relations'], 'relation_embeddings': []}, f)

    with open(os.path.join(output_dir, 'property_sample.json'), 'w') as f:
        json.dump({'properties': model_data['properties'], 'property_embeddings': []}, f)

    print("  Generated model-compatible files:")
    print("    - topology_sample.json")
    print("    - concept_property_sample.json")
    print("    - relation_sample.json")
    print("    - property_sample.json")

def main():
    parser = argparse.ArgumentParser(description='Test HCG generation')
    parser.add_argument('--data_dir', default='../data', help='Data directory')
    parser.add_argument('--output_dir', default='outputs', help='Output directory')
    parser.add_argument('--sample_id', type=int, default=0, help='Sample question ID')

    args = parser.parse_args()

    # Setup paths
    questions_file = os.path.join(args.data_dir, 'vqa/v2_OpenEnded_mscoco_train2014_questions.json')
    annotations_file = os.path.join(args.data_dir, 'vqa/v2_mscoco_train2014_annotations.json')
    vocab_file = os.path.join(args.data_dir, 'features/vocab_augmented.json')
    hierarchy_file = os.path.join(args.data_dir, 'features/hierarchy.json')
    relation_file = os.path.join(args.data_dir, 'features/relation.json')
    property_file = os.path.join(args.data_dir, 'features/property.json')

    print("=== HCNMN Hierarchical Concept Graph Generation Test ===\\n")

    # Load sample question
    sample = load_sample_question(questions_file, annotations_file, args.sample_id)

    # Load vocabulary and hierarchy data
    print("\\nLoading vocabulary and knowledge data...")

    with open(vocab_file, 'r') as f:
        vocab_data = json.load(f)

    with open(hierarchy_file, 'r') as f:
        hierarchy_data = json.load(f)

    # Load relation and property data (may be empty initially)
    try:
        with open(relation_file, 'r') as f:
            relation_data = json.load(f)
    except FileNotFoundError:
        relation_data = {'relations': [], 'relation_embeddings': []}

    try:
        with open(property_file, 'r') as f:
            property_data = json.load(f)
    except FileNotFoundError:
        property_data = {'properties': [], 'property_embeddings': []}

    # Extract concepts from question
    concepts, hierarchies = extract_question_concepts(
        sample['question'], vocab_data, hierarchy_data)

    # Build concept topology
    topology_matrix = build_concept_topology(concepts, relation_data, property_data)

    # Generate concept properties
    property_vectors, properties = generate_concept_properties(concepts, property_data)

    # Create visualizations
    hcg_data = visualize_hcg(concepts, topology_matrix, property_vectors,
                            properties, args.output_dir)

    # Test model integration
    test_model_integration(hcg_data, args.output_dir)

    # Print summary
    print("\\n=== HCG Generation Summary ===")
    print(f"Question: {sample['question']}")
    print(f"Answer: {sample['answer']}")
    print(f"Concepts extracted: {len(concepts)}")
    print(f"Concept connections: {hcg_data['statistics']['num_connections']}")
    print(f"Properties assigned: {len(properties)}")
    print(f"Graph density: {hcg_data['statistics']['graph_density']:.3f}")
    print(f"Avg properties per concept: {hcg_data['statistics']['avg_properties_per_concept']:.2f}")
    print(f"\\nOutputs saved to: {args.output_dir}/")

    return hcg_data

if __name__ == '__main__':
    main()