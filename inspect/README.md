# HCNMN Testing and Inspection Tools

This directory contains testing and demonstration tools for the HCNMN (Hierarchical Cross-Modality Neural Module Network) pipeline.

## Overview

These tools help verify, test, and demonstrate the hierarchical concept graph (HCG) generation pipeline and model integration.

## Available Tools

### 1. `test_hcg_generation.py` - HCG Generation Demo

**Purpose**: Demonstrates end-to-end hierarchical concept graph generation from a sample VQA question.

**Features**:
- Loads sample questions from VQA v2 dataset
- Extracts concepts using WordNet vocabulary augmentation
- Builds concept topology matrices showing relationships
- Generates concept property vectors
- Creates visualizations of the hierarchical concept graph
- Outputs model-compatible data files

**Usage**:
```bash
# Basic usage with default sample
python test_hcg_generation.py

# Test with specific sample and custom output
python test_hcg_generation.py --sample_id 5 --output_dir my_outputs

# Use custom data directory
python test_hcg_generation.py --data_dir /path/to/data --sample_id 10
```

**Parameters**:
- `--data_dir`: Path to HCNMN data directory (default: `../data`)
- `--output_dir`: Output directory for results (default: `outputs`)
- `--sample_id`: Which VQA sample to test (default: 0)

**Outputs**:
- `hcg_visualization.png`: Multi-panel visualization of concept graph
- `hcg_data.json`: Complete HCG data structure with statistics
- `topology_sample.json`: Model-compatible topology matrices
- `concept_property_sample.json`: Model-compatible property vectors
- `relation_sample.json`: Model-compatible relation data
- `property_sample.json`: Model-compatible property vocabularies

### 2. `test_model_integration.py` - Model Integration Test

**Purpose**: Tests HCNMN model integration with generated HCG data structures.

**Features**:
- Verifies all required HCG files exist and are valid
- Tests DataLoader integration with knowledge files
- Tests HCNMN model creation and configuration
- Simulates hierarchical reasoning inference
- Generates comprehensive integration report

**Usage**:
```bash
# Basic integration test
python test_model_integration.py

# Test with custom configuration
python test_model_integration.py --device cuda --sample_question "What is the color of the sky?"

# Custom data and output directories
python test_model_integration.py --data_dir /path/to/data --output_dir results
```

**Parameters**:
- `--data_dir`: Path to HCNMN data directory (default: `../data`)
- `--output_dir`: Output directory for test results (default: `outputs`)
- `--device`: Computing device - cpu or cuda (default: `cpu`)
- `--sample_question`: Question for inference simulation (default: "What color is the car?")

**Outputs**:
- `integration_test_report.json`: Comprehensive test results and diagnostics
- Console output with detailed test progress and results

## Expected Data Structure

Both tools expect the following data structure:

```
data/
├── vqa/
│   ├── v2_OpenEnded_mscoco_train2014_questions.json
│   └── v2_mscoco_train2014_annotations.json
├── features/
│   ├── vocab_augmented.json      # WordNet-augmented vocabulary
│   ├── hierarchy.json            # Concept hierarchies
│   ├── topology.json             # Concept topology matrices
│   ├── relation.json             # Relation vocabulary with embeddings
│   ├── concept_property.json     # Property vectors per question
│   ├── property.json             # Property vocabulary with embeddings
│   ├── train_questions.pt        # Processed questions
│   └── trainval_feature.h5       # Visual features
└── knowledge/
    ├── conceptnet.json            # Processed ConceptNet relations
    └── wikitext.json              # Processed WikiText descriptions
```

## Test Examples

### Example 1: Quick HCG Demo

```bash
cd inspect
python test_hcg_generation.py --sample_id 0
```

Expected output:
```
=== HCNMN Hierarchical Concept Graph Generation Test ===

Loading sample question 0...
Sample 0:
  Question: What is this photo taken looking through?
  Answer: window
  Image ID: 458755

Loading vocabulary and knowledge data...

Extracting concepts from question...
  Original tokens: ['what', 'is', 'this', 'photo', 'taken', 'looking', 'through']
  Valid vocabulary tokens: ['what', 'is', 'this', 'photo', 'taken', 'looking', 'through']
  Expanded concepts: ['what', 'entity', 'be', 'exist', 'this', 'photograph', 'picture', 'image', 'take', 'accept']...

Building concept topology...
  Topology matrix shape: (15, 15)
  Number of connections: 8

Generating concept properties...
  Property matrix shape: (15, 8)
  Properties: ['red', 'blue', 'large', 'small', 'round', 'square', 'metal', 'wood']
  Non-zero property assignments: 3

Creating HCG visualizations...
  Saved visualization: outputs/hcg_visualization.png
  Saved HCG data: outputs/hcg_data.json

=== HCG Generation Summary ===
Question: What is this photo taken looking through?
Answer: window
Concepts extracted: 15
Concept connections: 8
Properties assigned: 8
Graph density: 0.036
Avg properties per concept: 0.20
```

### Example 2: Model Integration Test

```bash
cd inspect
python test_model_integration.py
```

Expected output:
```
=== HCNMN Model Integration Test ===

Verifying HCG files...
File Verification Results:
--------------------------------------------------------------------------------
✅ vocab_augmented.json   3.9 MB       Keys: ['question_token_to_idx', 'terms', 'term_per_question', ...]
✅ hierarchy.json         2.9 MB       Keys: dict with 1327 entries
✅ topology.json          50.2 MB      Keys: ['topology_per_question']
✅ relation.json          10.1 MB      Keys: ['relations', 'relation_embeddings']
✅ concept_property.json  20.3 MB      Keys: ['property_vector_per_question']
✅ property.json          5.2 MB       Keys: ['properties', 'property_embeddings']
--------------------------------------------------------------------------------
✅ All HCG files verified successfully!

Loading HCG data...
HCG Data Statistics:
  Vocabulary terms: 13758
  Question tokens: 5747
  Hierarchical concepts: 1327
  Topology questions: 248349
  Relations: 14
  Properties: 127

Testing DataLoader integration...
✅ DataLoader created successfully
✅ Successfully loaded batch with 8 items

Testing HCNMN model creation (device: cpu)...
✅ HCNMN model created successfully
   Parameters: 15,847,329
   Trainable parameters: 15,847,329

Testing model forward pass...
✅ Forward pass successful
   Output shape: torch.Size([2, 3129])

Simulating HCG inference for: 'What color is the car?'
Valid tokens: ['what', 'color', 'is', 'the', 'car']
Expanded concepts: ['what', 'entity', 'color', 'colour', 'coloring', 'be', 'exist', 'the', 'car', 'automobile']...

Reasoning Path Summary:
  Question complexity: 5 tokens
  Vocabulary coverage: 5/5 tokens
  Concept expansion: 24 concepts
  Topology density: 0.083
  Hierarchical depth: 4.80

=== Integration Test Summary ===
Tests passed: 4/4
🎉 All integration tests passed! HCNMN is ready for training.
```

## Troubleshooting

### Common Issues

1. **Missing Data Files**
   - **Error**: "FILE NOT FOUND" for vocabulary or knowledge files
   - **Solution**: Run the complete pipeline first:
     ```bash
     # From main directory
     python preprocess/vocab_augmentation.py --input_vocab data/features/vocab.json ...
     python preprocess/incorporate_knowledge.py --hierarchy ...
     ```

2. **Empty Knowledge Files**
   - **Error**: "EMPTY" warning for topology.json or relation.json
   - **Solution**: Run ConceptNet processing to generate real knowledge:
     ```bash
     python preprocess/process_knowledge.py --vocab_json data/features/vocab_augmented.json ...
     ```

3. **DataLoader Failures**
   - **Error**: "DataLoader failed" during integration test
   - **Solution**: Check that all required files exist and have valid formats:
     ```bash
     ls -la data/features/*.{json,pt,h5}
     ```

4. **Model Creation Issues**
   - **Error**: "Model creation failed"
   - **Solution**: Ensure vocabulary has required keys:
     ```python
     # Check vocab structure
     import json
     with open('data/features/vocab_augmented.json', 'r') as f:
         vocab = json.load(f)
     print(vocab.keys())
     ```

5. **CUDA Errors**
   - **Error**: CUDA out of memory or not available
   - **Solution**: Use CPU device:
     ```bash
     python test_model_integration.py --device cpu
     ```

### Performance Notes

- **HCG Generation**: ~10-30 seconds for single sample
- **Model Integration**: ~1-2 minutes for complete test
- **Memory Usage**: ~2-4GB RAM for testing
- **Visualization**: Requires matplotlib, saves ~1MB PNG files

### Dependencies

Required packages for testing:
```bash
pip install torch torchvision numpy matplotlib networkx tqdm
```

Optional packages:
```bash
pip install seaborn pandas  # Enhanced visualizations
```

## Advanced Usage

### Custom Concept Analysis

```python
# Run HCG generation with custom concept extraction
python test_hcg_generation.py --sample_id 42

# Analyze the generated concept graph
import json
with open('outputs/hcg_data.json', 'r') as f:
    hcg = json.load(f)

print(f"Concept hierarchy depth: {hcg['statistics']['hierarchical_depth']}")
print(f"Most connected concepts: {hcg['concepts'][:5]}")
```

### Batch Testing

```bash
# Test multiple samples
for i in {0..9}; do
    python test_hcg_generation.py --sample_id $i --output_dir "outputs/sample_$i"
done
```

### Integration with Training

```python
# Use generated HCG data for model training
from DataLoader import QADataLoader

loader = QADataLoader(
    question_pt='data/features/train_questions.pt',
    vocab_json='data/features/vocab_augmented.json',
    topology='data/features/topology.json',
    relation='data/features/relation.json',
    concept_property='data/features/concept_property.json',
    property='data/features/property.json',
    # ... other parameters
)
```

## Output Examples

### HCG Visualization Components

1. **Concept Graph Network**: NetworkX visualization showing concept connections
2. **Topology Matrix**: Heatmap of concept-to-concept relationships
3. **Property Matrix**: Heatmap showing which concepts have which properties
4. **Property Distribution**: Bar chart of property counts per concept

### Integration Report Structure

```json
{
  "timestamp": "2023-09-30T22:30:00",
  "test_results": {
    "hcg_files_valid": true,
    "dataloader_success": true,
    "model_creation_success": true,
    "inference_simulation_success": true
  },
  "reasoning_path": {
    "question": "What color is the car?",
    "concepts": ["what", "color", "car", "automobile", ...],
    "topology_shape": [15, 15],
    "hierarchical_depth": 4.2
  }
}
```

For more details, see the main [PIPELINE_README.md](../PIPELINE_README.md).