# HCNMN Hierarchical Concept Graph (HCG) Generation Pipeline

Complete pipeline for generating hierarchical concept graphs for the HCNMN (Hierarchical Cross-Modality Neural Module Network) model.

## Overview

This pipeline transforms raw VQA questions, visual features, and knowledge sources into hierarchical concept graphs that enable multi-granularity visual reasoning. The process involves:

1. **Vocabulary Processing** - Extract and augment question vocabulary with WordNet hierarchies
2. **Knowledge Integration** - Process ConceptNet and WikiText to extract concept relations and properties
3. **HCG Generation** - Build hierarchical concept graphs with topology matrices and embeddings
4. **Model Integration** - Prepare data structures for HCNMN training and inference

## Prerequisites

- **Environment**: Conda environment with Python 3.7+ (see `environment.yml`)
- **Data Requirements**: ~25GB disk space for complete pipeline
- **Memory**: 16GB+ RAM recommended for knowledge processing
- **Processing Time**: 2-4 hours for complete pipeline

## Data Sources

| Component | Source | Size | Description |
|-----------|--------|------|-------------|
| VQA v2 Questions | MS COCO | ~100MB | Training/validation questions and annotations |
| GloVe Embeddings | Stanford NLP | ~5.4GB | Pre-trained word embeddings (840B.300d) |
| ConceptNet | ConceptNet 5.7 | ~10GB | Semantic knowledge base (CSV format) |
| WikiText-2 | PyTorch | ~13MB | Wikipedia text corpus |
| LXMERT Features | UNC NLP | ~25GB | Pre-extracted visual features |

## Pipeline Stages

### Stage 1: Environment Setup

```bash
# Create conda environment
conda env create -f environment.yml
conda activate hcnmn

# Install additional dependencies
pip install conceptnet-lite wikitextparser
```

### Stage 2: Data Download and Extraction

```bash
# Download all required data (runs in parallel)
bash scripts/setup_all.sh

# Verify data integrity
python scripts/verify_data.py
```

Expected directory structure after downloads:
```
data/
├── vqa/                    # VQA v2 questions and annotations
├── glove/                  # GloVe embeddings (raw and processed)
├── knowledge/              # ConceptNet CSV + WikiText files
├── features/               # LXMERT visual features + processed outputs
└── vg/ -> /path/to/vg/     # Visual Genome symlink
```

### Stage 3: Core Preprocessing

#### 3.1 GloVe Processing
```bash
# Convert GloVe text to pickle format (background process)
python scripts/process_glove.py \\
    --input data/glove/glove.840B.300d.txt \\
    --output data/glove/glove_fixed.pt
```
**Output**: `glove_fixed.pt` (665MB) - Processed embeddings compatible with current NumPy

#### 3.2 Question Preprocessing
```bash
# Process VQA questions with GloVe embeddings
python preprocess/preprocess_questions.py \\
    --glove_pt data/glove/glove_fixed.pt \\
    --input_questions_json data/vqa/v2_OpenEnded_mscoco_train2014_questions.json \\
    --input_annotations_json data/vqa/v2_mscoco_train2014_annotations.json \\
    --output_pt data/features/train_questions.pt \\
    --vocab_json data/features/vocab.json \\
    --mode train
```
**Outputs**:
- `vocab.json` (421KB) - Base vocabulary from questions/answers
- `train_questions.pt` (73MB) - Processed questions with embeddings

#### 3.3 Visual Feature Processing
```bash
# Process LXMERT features to HDF5 format
python preprocess/preprocess_features.py \\
    --input_tsv_folder data/features/trainval_36/ \\
    --output_h5 data/features/trainval_feature.h5
```
**Output**: `trainval_feature.h5` (36GB) - Visual features in HDF5 format

### Stage 4: Hierarchical Concept Graph Generation

#### 4.1 Vocabulary Augmentation with WordNet
```bash
# Augment vocabulary with WordNet hypernym hierarchies
python preprocess/vocab_augmentation.py \\
    --input_vocab data/features/vocab.json \\
    --glove_pt data/glove/glove_fixed.pt \\
    --vocab_json data/features/vocab_augmented.json \\
    --hierarchy data/features/hierarchy.json
```
**Outputs**:
- `vocab_augmented.json` (3.9MB) - Vocabulary with augmented terms and hierarchies
- `hierarchy.json` (2.9MB) - WordNet concept hierarchies per question

#### 4.2 Knowledge Source Processing
```bash
# Process ConceptNet and WikiText into structured JSON
python preprocess/process_knowledge.py \\
    --vocab_json data/features/vocab_augmented.json \\
    --conceptnet_csv data/knowledge/conceptnet-assertions-5.7.0.csv \\
    --wikitext_dir data/knowledge/ \\
    --glove_pt data/glove/glove_fixed.pt \\
    --output_dir data/knowledge/ \\
    --max_relations 500000
```
**Outputs**:
- `conceptnet.json` (~50MB) - Structured ConceptNet relations and properties
- `wikitext.json` (~10MB) - Concept descriptions from WikiText

#### 4.3 Knowledge Integration and Topology Generation
```bash
# Generate concept topology matrices
python preprocess/incorporate_knowledge.py \\
    --input_vocab data/features/vocab_augmented.json \\
    --input_knowledge_folder data/knowledge/ \\
    --glove_pt data/glove/glove_fixed.pt \\
    --input_hierarchy data/features/hierarchy.json \\
    --vocab_json data/features/vocab_augmented.json \\
    --topology_json data/features/topology.json \\
    --relation_vocab data/features/relation.json \\
    --concept_property data/features/concept_property.json \\
    --property_vocab data/features/property.json \\
    --hierarchy

# Generate concept properties
python preprocess/incorporate_knowledge.py \\
    --input_vocab data/features/vocab_augmented.json \\
    --input_knowledge_folder data/knowledge/ \\
    --glove_pt data/glove/glove_fixed.pt \\
    --concept_property data/features/concept_property.json \\
    --property_vocab data/features/property.json \\
    --property
```
**Outputs**:
- `topology.json` - Hierarchical concept adjacency matrices per question
- `relation.json` - ConceptNet relations with embeddings
- `concept_property.json` - Property vectors per question concept
- `property.json` - Property vocabulary with embeddings

## Generated HCG Data Structure

### Hierarchical Concept Graph Components

#### 1. Topology Matrices (`topology.json`)
```json
{
  "topology_per_question": [
    [  // Question 1: NxN adjacency matrix where N = number of concepts in question
      [0, 1, 0],  // concept[0] connected to concept[1]
      [1, 0, 1],  // concept[1] connected to concept[0] and concept[2]
      [0, 1, 0]   // concept[2] connected to concept[1]
    ],
    // ... more questions
  ]
}
```

#### 2. Relation Embeddings (`relation.json`)
```json
{
  "relations": ["IsA", "PartOf", "HasProperty", "AtLocation", ...],
  "relation_embeddings": [
    [0.1, 0.2, ...],  // 300-dim GloVe embedding for "IsA"
    [0.3, 0.1, ...],  // 300-dim GloVe embedding for "PartOf"
    // ... embeddings for each relation
  ]
}
```

#### 3. Concept Properties (`concept_property.json`)
```json
{
  "property_vector_per_question": [
    [  // Question 1: Property vectors for each concept
      [1, 0, 1, 0],  // concept[0]: has properties 0 and 2
      [0, 1, 0, 1],  // concept[1]: has properties 1 and 3
      [1, 1, 0, 0]   // concept[2]: has properties 0 and 1
    ],
    // ... more questions
  ]
}
```

#### 4. Property Embeddings (`property.json`)
```json
{
  "properties": ["red", "large", "round", "metal", ...],
  "property_embeddings": [
    [0.2, 0.1, ...],  // 300-dim GloVe embedding for "red"
    [0.1, 0.3, ...],  // 300-dim GloVe embedding for "large"
    // ... embeddings for each property
  ]
}
```

## Model Training Integration

### Training Command
```bash
python train.py \\
    --input_dir data/features/ \\
    --concept data/concepts/ \\
    --concept_property data/features/concept_property.json \\
    --topology data/features/topology.json \\
    --relation_list data/features/relation.json \\
    --property_list data/features/property.json \\
    --save_dir data/checkpoints/ \\
    --model HCNMN \\
    --T_ctrl 3 \\
    --stack_len 4 \\
    --cuda 0 \\
    --val
```

### Data Loading Process
The model loads HCG data through the `QADataLoader` which:
1. **Question Processing**: Loads tokenized questions with GloVe embeddings
2. **Visual Features**: Loads LXMERT features for image regions
3. **Concept Graphs**: Loads topology matrices and relation/property embeddings
4. **Hierarchical Reasoning**: Enables multi-granularity attention over concept hierarchies

## Testing and Validation

### Pipeline Verification
```bash
# Verify all generated files
python scripts/verify_data.py

# Test HCG generation on sample
python inspect/test_hcg_generation.py

# Test model integration
python inspect/test_model_integration.py
```

### Expected File Sizes
```
data/features/
├── vocab.json              421KB   ✓ Base vocabulary
├── vocab_augmented.json     3.9MB   ✓ WordNet-augmented vocabulary
├── hierarchy.json           2.9MB   ✓ Concept hierarchies
├── topology.json           ~50MB   ✓ Concept topology matrices
├── relation.json           ~10MB   ✓ Relation embeddings
├── concept_property.json   ~20MB   ✓ Property vectors
├── property.json           ~5MB    ✓ Property embeddings
├── train_questions.pt       73MB   ✓ Processed questions
└── trainval_feature.h5      36GB   ✓ Visual features
```

## Troubleshooting

### Common Issues

#### 1. Memory Issues During ConceptNet Processing
```bash
# Reduce max_relations parameter
python preprocess/process_knowledge.py --max_relations 100000 [other args...]
```

#### 2. Empty Knowledge Files
- **Cause**: ConceptNet CSV parsing failed or vocabulary mismatch
- **Solution**: Check ConceptNet file format and vocabulary structure
- **Debug**: Run with `--max_relations 1000` for quick testing

#### 3. GloVe Loading Errors
- **Cause**: NumPy version incompatibility or corrupted pickle
- **Solution**: Regenerate GloVe pickle with current environment
```bash
python scripts/process_glove.py --input data/glove/glove.840B.300d.txt --output data/glove/glove_fixed.pt
```

#### 4. LXMERT Feature Format Issues
- **Cause**: TSV file structure mismatch (expected 6 fields, actual 10)
- **Solution**: Preprocessing script handles this automatically
- **Verification**: Check `trainval_feature.h5` size should be ~36GB

### Performance Optimization

#### Processing Time Estimates
- **GloVe Processing**: 30-60 minutes
- **Question Preprocessing**: 5-10 minutes
- **ConceptNet Processing**: 30-90 minutes (depending on max_relations)
- **Knowledge Integration**: 5-15 minutes
- **Visual Feature Processing**: 60-120 minutes

#### Memory Usage
- **ConceptNet Processing**: 8-16GB RAM
- **Knowledge Integration**: 4-8GB RAM
- **Visual Feature Processing**: 4-8GB RAM

#### Disk Space
- **Intermediate Files**: ~15GB
- **Final Output**: ~36GB total
- **Temporary Space**: ~10GB during processing

## Advanced Configuration

### Custom Vocabulary
To use custom vocabulary instead of VQA questions:
```python
# Modify vocab_augmentation.py
custom_terms = ["apple", "tree", "red", ...]  # Your custom vocabulary
vocab['terms'] = custom_terms
```

### Knowledge Source Customization
To add custom ConceptNet relations:
```python
# Modify process_knowledge.py
relevant_relations = {
    'IsA', 'PartOf', 'HasA',  # Standard relations
    'CustomRelation1',        # Your custom relations
    'CustomRelation2'
}
```

### Evaluation Metrics
The HCG quality can be evaluated through:
- **Coverage**: Percentage of vocabulary terms with knowledge
- **Connectivity**: Average concept connections per question
- **Hierarchy Depth**: Distribution of WordNet hierarchy levels
- **Model Performance**: Downstream VQA accuracy improvement

## Citation

If you use this pipeline, please cite the original HCNMN paper:
```bibtex
@inproceedings{zhang2023hcnmn,
  title={Toward Multi-Granularity Decision-Making: Explicit Visual Reasoning with Hierarchical Knowledge},
  author={Zhang, Your Name and others},
  booktitle={ICCV},
  year={2023}
}
```

## Support

- **Issues**: Report bugs and feature requests in GitHub issues
- **Documentation**: Full API documentation in `/docs/`
- **Examples**: Sample scripts and notebooks in `/inspect/`