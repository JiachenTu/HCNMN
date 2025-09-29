# HCNMN Data Preparation Guide

This guide provides step-by-step instructions for preparing all data required to train and evaluate the HCNMN model.

## Quick Start

```bash
# 1. Create and activate conda environment
conda env create -f environment.yml
conda activate hcnmn

# 2. Run complete setup (downloads ~11GB of data)
bash scripts/setup_all.sh

# 3. Verify data integrity
python scripts/verify_data.py
```

## Manual Setup

If you prefer to download data step by step:

### 1. Environment Setup

```bash
conda env create -f environment.yml
conda activate hcnmn
```

### 2. Data Downloads

```bash
# VQA v2 Questions and Annotations (~100MB)
bash scripts/download_vqa.sh

# Knowledge Sources: ConceptNet + WikiText-2 (~500MB)
bash scripts/download_knowledge.sh

# GloVe Word Embeddings (~2GB)
bash scripts/download_glove.sh

# LXMERT Visual Features (~8GB)
bash scripts/download_lxmert_features.sh
```

### 3. NLTK Setup

```bash
python scripts/setup_nltk.py
```

### 4. Data Processing

```bash
# Process GloVe embeddings to pickle format
python scripts/process_glove.py \
    --input data/glove/glove.840B.300d.txt \
    --output data/glove/glove.pt
```

## Data Preprocessing Pipeline

After downloading raw data, follow these steps to create the hierarchical concept graph:

### Step 1: Process Questions
```bash
python preprocess/preprocess_questions.py \
    --glove_pt data/glove/glove.pt \
    --input_questions_json data/vqa/v2_OpenEnded_mscoco_train2014_questions.json \
    --input_annotations_json data/vqa/v2_mscoco_train2014_annotations.json \
    --output_pt data/features/train_questions.pt \
    --vocab_json data/features/vocab.json \
    --mode train
```

### Step 2: Augment Vocabulary with WordNet
```bash
python preprocess/vocab_augmentation.py \
    --input_vocab data/features/vocab.json \
    --glove_pt data/glove/glove.pt \
    --vocab_json data/features/vocab_augmented.json \
    --hierarchy data/features/hierarchy.json \
    --wordnet_base
```

### Step 3: Incorporate Knowledge Sources
```bash
# Generate topology
python preprocess/incorporate_knowledge.py \
    --input_vocab data/features/vocab_augmented.json \
    --knowledge_dir data/knowledge/ \
    --glove_pt data/glove/glove.pt \
    --input_hierarchy data/features/hierarchy.json \
    --topology_json data/features/topology.json \
    --relation_vocab data/features/relation.json \
    --hierarchy

# Extract concept properties
python preprocess/incorporate_knowledge.py \
    --input_vocab data/features/vocab_augmented.json \
    --knowledge_dir data/knowledge/ \
    --glove_pt data/glove/glove.pt \
    --property_vocab data/features/property.json \
    --concept_property data/features/concept_property.json \
    --property
```

### Step 4: Process Visual Features
```bash
python preprocess/preprocess_features.py \
    --input_tsv_folder data/features/trainval_36/ \
    --output_h5 data/features/trainval_feature.h5
```

### Step 5: Generate Concept Graph
```bash
python preprocess/preprocess_concepts.py \
    --input_knowledge_folder data/knowledge/ \
    --output_folder data/concepts/ \
    --glove_pt data/glove/glove.pt
```

## Directory Structure

After setup completion:

```
HCNMN/
├── data/
│   ├── vg/                           # Visual Genome (symlink)
│   ├── vqa/                          # VQA v2 data
│   │   ├── v2_OpenEnded_mscoco_train2014_questions.json
│   │   ├── v2_mscoco_train2014_annotations.json
│   │   └── v2_*val2014*.json
│   ├── knowledge/                    # Knowledge sources
│   │   ├── conceptnet.db
│   │   └── wikitext-2/
│   ├── glove/                        # Word embeddings
│   │   ├── glove.840B.300d.txt
│   │   └── glove.pt
│   ├── features/                     # Processed features
│   │   ├── trainval_36/              # LXMERT features
│   │   ├── train_questions.pt
│   │   ├── vocab.json
│   │   ├── hierarchy.json
│   │   ├── topology.json
│   │   ├── relation.json
│   │   ├── property.json
│   │   ├── concept_property.json
│   │   └── trainval_feature.h5
│   ├── concepts/                     # Concept graphs
│   └── checkpoints/                  # Model checkpoints
└── scripts/                          # Setup scripts
    ├── download_*.sh
    ├── process_glove.py
    ├── setup_nltk.py
    ├── verify_data.py
    └── setup_all.sh
```

## Training

Once data preparation is complete:

```bash
python train.py \
    --input_dir data/features/ \
    --concept data/concepts/ \
    --concept_property data/features/concept_property.json \
    --topology data/features/topology.json \
    --relation_list data/features/relation.json \
    --property_list data/features/property.json \
    --save_dir data/checkpoints/ \
    --model HCNMN \
    --T_ctrl 3 \
    --stack_len 4 \
    --cuda 0 \
    --val
```

## Troubleshooting

### Disk Space Requirements
- Total space needed: ~12GB
- GloVe embeddings: ~5.4GB (uncompressed)
- LXMERT features: ~8GB
- Other data: ~1GB

### Common Issues

1. **Download timeouts**: Re-run the download scripts - they use `wget -c` for resumable downloads

2. **NLTK data issues**:
   ```bash
   python -c "import nltk; nltk.download('wordnet'); nltk.download('omw-1.4')"
   ```

3. **Memory issues during GloVe processing**: Use a machine with >16GB RAM

4. **Missing dependencies**:
   ```bash
   pip install conceptnet-lite wikitextparser
   ```

## Verification

Run the verification script at any time to check data integrity:

```bash
python scripts/verify_data.py
```

This will check all files and provide guidance on missing components.