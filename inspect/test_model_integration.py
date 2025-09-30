#!/usr/bin/env python3
"""
Test script for HCNMN model integration with generated HCG data.
Tests loading and inference with hierarchical concept graphs.
"""
import os
import sys
import json
import torch
import numpy as np
import argparse
from collections import defaultdict

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from DataLoader import QADataLoader
    from model.net import HCNMN
    from utils.misc import todevice
except ImportError as e:
    print(f"Warning: Could not import HCNMN modules: {e}")
    print("Running in test mode without actual model loading")

def verify_hcg_files(data_dir):
    """Verify all required HCG files exist and have valid structure."""
    print("Verifying HCG files...")

    required_files = {
        'vocab_augmented.json': 'Augmented vocabulary with hierarchies',
        'hierarchy.json': 'WordNet concept hierarchies',
        'topology.json': 'Concept topology matrices',
        'relation.json': 'Relation vocabulary and embeddings',
        'concept_property.json': 'Concept property vectors',
        'property.json': 'Property vocabulary and embeddings'
    }

    file_status = {}
    for filename, description in required_files.items():
        filepath = os.path.join(data_dir, 'features', filename)

        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    size = os.path.getsize(filepath)
                    file_status[filename] = {
                        'exists': True,
                        'size': size,
                        'description': description,
                        'keys': list(data.keys()) if isinstance(data, dict) else 'non-dict',
                        'empty': len(data) == 0 if isinstance(data, (dict, list)) else False
                    }
            except Exception as e:
                file_status[filename] = {
                    'exists': True,
                    'error': str(e),
                    'description': description
                }
        else:
            file_status[filename] = {
                'exists': False,
                'description': description
            }

    # Print verification results
    print("\\nFile Verification Results:")
    print("-" * 80)

    all_exist = True
    all_valid = True

    for filename, status in file_status.items():
        if status['exists']:
            if 'error' in status:
                print(f"❌ {filename:<25} ERROR: {status['error']}")
                all_valid = False
            elif status.get('empty', False):
                print(f"⚠️  {filename:<25} EMPTY ({status['size']} bytes)")
                all_valid = False
            else:
                size_str = f"{status['size']:,} bytes" if status['size'] < 1024*1024 else f"{status['size']/(1024*1024):.1f} MB"
                print(f"✅ {filename:<25} {size_str:<12} Keys: {status.get('keys', 'N/A')}")
        else:
            print(f"❌ {filename:<25} FILE NOT FOUND")
            all_exist = False

    print("-" * 80)

    if not all_exist:
        print("⚠️  Some required files are missing. Run the complete pipeline first.")
    elif not all_valid:
        print("⚠️  Some files exist but may be empty or invalid.")
    else:
        print("✅ All HCG files verified successfully!")

    return all_exist and all_valid, file_status

def load_hcg_data(data_dir):
    """Load all HCG data structures."""
    print("\\nLoading HCG data...")

    features_dir = os.path.join(data_dir, 'features')

    # Load vocabulary and hierarchies
    with open(os.path.join(features_dir, 'vocab_augmented.json'), 'r') as f:
        vocab_data = json.load(f)

    with open(os.path.join(features_dir, 'hierarchy.json'), 'r') as f:
        hierarchy_data = json.load(f)

    # Load knowledge structures
    with open(os.path.join(features_dir, 'topology.json'), 'r') as f:
        topology_data = json.load(f)

    with open(os.path.join(features_dir, 'relation.json'), 'r') as f:
        relation_data = json.load(f)

    with open(os.path.join(features_dir, 'concept_property.json'), 'r') as f:
        property_data = json.load(f)

    with open(os.path.join(features_dir, 'property.json'), 'r') as f:
        property_vocab_data = json.load(f)

    hcg_data = {
        'vocab': vocab_data,
        'hierarchy': hierarchy_data,
        'topology': topology_data,
        'relations': relation_data,
        'concept_properties': property_data,
        'property_vocab': property_vocab_data
    }

    # Print data statistics
    print("HCG Data Statistics:")
    print(f"  Vocabulary terms: {len(vocab_data.get('terms', []))}")
    print(f"  Question tokens: {len(vocab_data.get('question_token_to_idx', {}))}")
    print(f"  Hierarchical concepts: {len(hierarchy_data)}")
    print(f"  Topology questions: {len(topology_data.get('topology_per_question', []))}")
    print(f"  Relations: {len(relation_data.get('relations', []))}")
    print(f"  Properties: {len(property_vocab_data.get('properties', []))}")

    return hcg_data

def test_dataloader_integration(data_dir, hcg_data):
    """Test DataLoader integration with HCG data."""
    print("\\nTesting DataLoader integration...")

    try:
        # Create minimal DataLoader configuration
        loader_kwargs = {
            'question_pt': os.path.join(data_dir, 'features/train_questions.pt'),
            'vocab_json': os.path.join(data_dir, 'features/vocab_augmented.json'),
            'feature_h5': os.path.join(data_dir, 'features/trainval_feature.h5'),
            'batch_size': 1,
            'spatial': True,
            'concept_h5': None,  # Not used in current setup
            'kg': None,
            'num_workers': 1,
            'shuffle': False,
            'topology': os.path.join(data_dir, 'features/topology.json'),
            'relation': os.path.join(data_dir, 'features/relation.json'),
            'concept_property': os.path.join(data_dir, 'features/concept_property.json'),
            'property': os.path.join(data_dir, 'features/property.json'),
        }

        # Check if required files exist
        missing_files = []
        for key, filepath in loader_kwargs.items():
            if filepath and not os.path.exists(filepath):
                missing_files.append(f"{key}: {filepath}")

        if missing_files:
            print("❌ Missing files for DataLoader:")
            for missing in missing_files:
                print(f"    {missing}")
            return False

        # Try to create DataLoader (may fail if files are empty)
        try:
            dataloader = QADataLoader(**loader_kwargs)
            print("✅ DataLoader created successfully")

            # Try to get one batch
            batch = next(iter(dataloader))
            print(f"✅ Successfully loaded batch with {len(batch)} items")

            # Analyze batch structure
            print("Batch structure:")
            for key, value in batch.items():
                if isinstance(value, torch.Tensor):
                    print(f"  {key}: {value.shape} ({value.dtype})")
                else:
                    print(f"  {key}: {type(value)}")

            return True

        except Exception as e:
            print(f"❌ DataLoader failed: {e}")
            print("   This may be due to empty knowledge files or format issues")
            return False

    except Exception as e:
        print(f"❌ Could not test DataLoader: {e}")
        return False

def test_model_creation(vocab_data, device='cpu'):
    """Test HCNMN model creation with HCG data."""
    print(f"\\nTesting HCNMN model creation (device: {device})...")

    try:
        # Extract vocabulary info
        vocab = {
            'question_token_to_idx': vocab_data.get('question_token_to_idx', {}),
            'answer_token_to_idx': vocab_data.get('answer_token_to_idx', {}),
            'question_answer_token_to_idx': vocab_data.get('question_answer_token_to_idx', {}),
            'program_token_to_idx': vocab_data.get('program_token_to_idx', {})
        }

        # Model configuration
        model_kwargs = {
            'vocab': vocab,
            'dim_v': 2048,  # LXMERT feature dimension
            'dim_word': 300,  # GloVe embedding dimension
            'dim_hidden': 256,
            'dim_vision': 2048,
            'dim_edge': 256,
            'glimpses': 2,
            'cls_fc_dim': 512,
            'dropout_prob': 0.1,
            'T_ctrl': 3,
            'stack_len': 4,
            'device': device,
            'use_gumbel': True
        }

        # Create model
        model = HCNMN(**model_kwargs)
        model.to(device)

        print("✅ HCNMN model created successfully")
        print(f"   Parameters: {sum(p.numel() for p in model.parameters()):,}")
        print(f"   Trainable parameters: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}")

        # Test model forward pass with dummy data
        batch_size = 2
        max_seq_len = 10
        num_objects = 36

        dummy_input = {
            'question_tokens': torch.randint(0, len(vocab['question_token_to_idx']),
                                           (batch_size, max_seq_len)).to(device),
            'question_lengths': torch.tensor([max_seq_len, max_seq_len-2]).to(device),
            'image_features': torch.randn(batch_size, num_objects, 2048).to(device),
            'spatial_features': torch.randn(batch_size, num_objects, 4).to(device)
        }

        print("\\nTesting model forward pass...")
        model.eval()
        with torch.no_grad():
            try:
                output = model(dummy_input)
                print(f"✅ Forward pass successful")
                print(f"   Output shape: {output.shape if hasattr(output, 'shape') else type(output)}")
                return True
            except Exception as e:
                print(f"❌ Forward pass failed: {e}")
                return False

    except Exception as e:
        print(f"❌ Model creation failed: {e}")
        return False

def simulate_hcg_inference(hcg_data, sample_question="What color is the car?"):
    """Simulate hierarchical reasoning with HCG data."""
    print(f"\\nSimulating HCG inference for: '{sample_question}'")

    # Extract concepts from question
    question_tokens = sample_question.lower().replace('?', '').split()
    vocab = hcg_data['vocab']
    token_to_idx = vocab.get('question_token_to_idx', {})

    valid_tokens = [token for token in question_tokens if token in token_to_idx]
    print(f"Valid tokens: {valid_tokens}")

    if not valid_tokens:
        print("❌ No valid tokens found in vocabulary")
        return

    # Simulate hierarchical concept expansion
    hierarchy = hcg_data['hierarchy']
    expanded_concepts = []

    for token in valid_tokens:
        if token in hierarchy:
            concepts = hierarchy[token][:5]  # Top 5 related concepts
            expanded_concepts.extend(concepts)
        else:
            expanded_concepts.append(token)

    print(f"Expanded concepts: {expanded_concepts[:10]}...")

    # Simulate topology-based reasoning
    topology = hcg_data['topology'].get('topology_per_question', [])
    if topology:
        print(f"Using topology data: {len(topology)} questions available")
        sample_topology = np.array(topology[0]) if topology else np.eye(len(expanded_concepts))
    else:
        print("Creating sample topology matrix")
        n = min(len(expanded_concepts), 10)
        sample_topology = np.random.rand(n, n) > 0.7  # Random sparse connections

    print(f"Topology matrix shape: {sample_topology.shape}")
    print(f"Number of concept connections: {np.sum(sample_topology)}")

    # Simulate property-based reasoning
    properties = hcg_data['property_vocab'].get('properties', [])
    if properties:
        print(f"Available properties: {properties[:10]}...")
    else:
        print("No properties available, using placeholders")
        properties = ['red', 'blue', 'large', 'small']

    # Generate reasoning path
    reasoning_path = {
        'question': sample_question,
        'tokens': question_tokens,
        'valid_tokens': valid_tokens,
        'expanded_concepts': expanded_concepts[:10],
        'topology_shape': sample_topology.shape,
        'connections': int(np.sum(sample_topology)),
        'properties': properties[:5],
        'hierarchical_depth': len(expanded_concepts) / len(valid_tokens) if valid_tokens else 0
    }

    print("\\nReasoning Path Summary:")
    print(f"  Question complexity: {len(question_tokens)} tokens")
    print(f"  Vocabulary coverage: {len(valid_tokens)}/{len(question_tokens)} tokens")
    print(f"  Concept expansion: {len(expanded_concepts)} concepts")
    print(f"  Topology density: {reasoning_path['connections']/(sample_topology.shape[0]**2 if sample_topology.shape[0] > 0 else 1):.3f}")
    print(f"  Hierarchical depth: {reasoning_path['hierarchical_depth']:.2f}")

    return reasoning_path

def save_integration_report(results, output_dir):
    """Save integration test results to file."""
    os.makedirs(output_dir, exist_ok=True)

    import datetime
    report = {
        'timestamp': str(datetime.datetime.now()),
        'test_results': results,
        'summary': {
            'hcg_files_valid': results.get('hcg_files_valid', False),
            'dataloader_success': results.get('dataloader_success', False),
            'model_creation_success': results.get('model_creation_success', False),
            'inference_simulation_success': results.get('inference_simulation_success', False)
        }
    }

    report_path = os.path.join(output_dir, 'integration_test_report.json')
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2, default=str)

    print(f"\\nIntegration test report saved: {report_path}")

def main():
    parser = argparse.ArgumentParser(description='Test HCNMN model integration')
    parser.add_argument('--data_dir', default='../data', help='Data directory')
    parser.add_argument('--output_dir', default='outputs', help='Output directory')
    parser.add_argument('--device', default='cpu', help='Device (cpu/cuda)')
    parser.add_argument('--sample_question', default='What color is the car?',
                       help='Sample question for inference test')

    args = parser.parse_args()

    print("=== HCNMN Model Integration Test ===\\n")

    results = {}

    # 1. Verify HCG files
    hcg_files_valid, file_status = verify_hcg_files(args.data_dir)
    results['hcg_files_valid'] = hcg_files_valid
    results['file_status'] = file_status

    if not hcg_files_valid:
        print("\\n❌ Cannot proceed with model testing due to missing or invalid HCG files")
        save_integration_report(results, args.output_dir)
        return

    # 2. Load HCG data
    try:
        hcg_data = load_hcg_data(args.data_dir)
        results['hcg_data_loaded'] = True
    except Exception as e:
        print(f"❌ Failed to load HCG data: {e}")
        results['hcg_data_loaded'] = False
        save_integration_report(results, args.output_dir)
        return

    # 3. Test DataLoader integration
    dataloader_success = test_dataloader_integration(args.data_dir, hcg_data)
    results['dataloader_success'] = dataloader_success

    # 4. Test model creation
    model_success = test_model_creation(hcg_data['vocab'], args.device)
    results['model_creation_success'] = model_success

    # 5. Simulate HCG inference
    try:
        reasoning_path = simulate_hcg_inference(hcg_data, args.sample_question)
        results['inference_simulation_success'] = True
        results['reasoning_path'] = reasoning_path
    except Exception as e:
        print(f"❌ Inference simulation failed: {e}")
        results['inference_simulation_success'] = False

    # 6. Save results
    save_integration_report(results, args.output_dir)

    # Print final summary
    print("\\n=== Integration Test Summary ===")
    success_count = sum([
        results.get('hcg_files_valid', False),
        results.get('dataloader_success', False),
        results.get('model_creation_success', False),
        results.get('inference_simulation_success', False)
    ])

    print(f"Tests passed: {success_count}/4")

    if success_count == 4:
        print("🎉 All integration tests passed! HCNMN is ready for training.")
    elif success_count >= 2:
        print("⚠️  Partial success. Some components working, others need attention.")
    else:
        print("❌ Major issues found. Please fix HCG generation pipeline.")

    return results

if __name__ == '__main__':
    main()