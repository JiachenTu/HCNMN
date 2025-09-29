#!/bin/bash

# Complete setup script for HCNMN data preparation
# This script runs all download and setup steps in sequence

set -e

echo "=== HCNMN Data Preparation Setup ==="
echo "This script will download and prepare all required data for HCNMN"
echo "Warning: This will download several GB of data"
echo ""

# Function to check if user wants to continue
ask_continue() {
    read -p "Continue with $1? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Skipping $1"
        return 1
    fi
    return 0
}

# Ensure we're in the right directory
cd /home/jiachen/scratch/graph_reasoning/HCNMN

echo "Current directory: $(pwd)"
echo ""

# Step 1: Download VQA data
if ask_continue "VQA v2 data download (~100MB)"; then
    echo "Step 1/6: Downloading VQA v2 data..."
    bash scripts/download_vqa.sh
    echo ""
fi

# Step 2: Download knowledge sources
if ask_continue "Knowledge sources download (ConceptNet + WikiText-2, ~500MB)"; then
    echo "Step 2/6: Downloading knowledge sources..."
    bash scripts/download_knowledge.sh
    echo ""
fi

# Step 3: Download GloVe embeddings
if ask_continue "GloVe embeddings download (~2GB)"; then
    echo "Step 3/6: Downloading GloVe embeddings..."
    bash scripts/download_glove.sh
    echo ""
fi

# Step 4: Download LXMERT features
if ask_continue "LXMERT features download (~8GB)"; then
    echo "Step 4/6: Downloading LXMERT features..."
    bash scripts/download_lxmert_features.sh
    echo ""
fi

# Step 5: Setup NLTK
if ask_continue "NLTK setup"; then
    echo "Step 5/6: Setting up NLTK..."
    python scripts/setup_nltk.py
    echo ""
fi

# Step 6: Process GloVe embeddings
if ask_continue "GloVe processing (may take 10-20 minutes)"; then
    echo "Step 6/6: Processing GloVe embeddings..."
    python scripts/process_glove.py \
        --input data/glove/glove.840B.300d.txt \
        --output data/glove/glove.pt
    echo ""
fi

echo "=== Setup Complete! ==="
echo "Running verification..."
python scripts/verify_data.py

echo ""
echo "Next steps:"
echo "1. Activate conda environment: conda activate hcnmn"
echo "2. Run preprocessing pipeline following the README instructions"
echo "3. Start training with: python train.py [args]"