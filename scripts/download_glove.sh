#!/bin/bash

# Download GloVe embeddings
# This script downloads GloVe 840B 300d embeddings

set -e

echo "=== Downloading GloVe Embeddings ==="

# Create glove directory if it doesn't exist
mkdir -p data/glove
cd data/glove

echo "Downloading GloVe 840B 300d embeddings..."
echo "Warning: This is a large file (~2.0GB compressed, ~5.4GB uncompressed)"
wget -c http://nlp.stanford.edu/data/glove.840B.300d.zip

echo "Extracting GloVe embeddings..."
unzip -o glove.840B.300d.zip

echo "Cleaning up zip file..."
rm -f glove.840B.300d.zip

echo "GloVe embeddings download completed!"
echo "File size:"
ls -lh glove.840B.300d.txt

cd ../..