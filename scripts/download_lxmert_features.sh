#!/bin/bash

# Download LXMERT grounded features
# This script downloads pre-extracted visual features from LXMERT

set -e

echo "=== Downloading LXMERT Features ==="

# Create features directory if it doesn't exist
mkdir -p data/features
cd data/features

echo "Downloading LXMERT trainval features..."
echo "Warning: This is a large file (~8.4GB)"
echo "Downloading from LXMERT repository..."

# Download trainval features
wget -c https://nlp.cs.unc.edu/data/lxmert_data/mscoco_imgfeat/trainval_obj36.zip

echo "Extracting LXMERT features..."
unzip -o trainval_obj36.zip

echo "Organizing extracted files..."
# The extracted files might be in a nested structure, let's check and organize
if [ -d "trainval_obj36" ]; then
    mv trainval_obj36 trainval_36
fi

echo "Cleaning up zip file..."
rm -f trainval_obj36.zip

echo "LXMERT features download completed!"
echo "Features directory contents:"
ls -la trainval_36/ | head -10

cd ../..