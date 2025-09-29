#!/bin/bash

# Download VQA v2 data
# This script downloads VQA v2 training and validation questions and annotations

set -e

echo "=== Downloading VQA v2 Data ==="

# Create VQA directory if it doesn't exist
mkdir -p data/vqa
cd data/vqa

echo "Downloading VQA v2 training questions..."
wget -c https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Train_mscoco.zip

echo "Downloading VQA v2 training annotations..."
wget -c https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Train_mscoco.zip

echo "Downloading VQA v2 validation questions..."
wget -c https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Questions_Val_mscoco.zip

echo "Downloading VQA v2 validation annotations..."
wget -c https://s3.amazonaws.com/cvmlp/vqa/mscoco/vqa/v2_Annotations_Val_mscoco.zip

echo "Extracting files..."
unzip -o v2_Questions_Train_mscoco.zip
unzip -o v2_Annotations_Train_mscoco.zip
unzip -o v2_Questions_Val_mscoco.zip
unzip -o v2_Annotations_Val_mscoco.zip

echo "Cleaning up zip files..."
rm -f *.zip

echo "VQA v2 data download completed!"
echo "Files available:"
ls -la *.json

cd ../..