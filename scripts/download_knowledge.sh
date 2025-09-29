#!/bin/bash

# Download knowledge sources for HCNMN
# This script downloads ConceptNet and WikiText-2

set -e

echo "=== Downloading Knowledge Sources ==="

# Create knowledge directory if it doesn't exist
mkdir -p data/knowledge
cd data/knowledge

echo "Downloading ConceptNet database..."
wget -c https://conceptnet-lite.fra1.cdn.digitaloceanspaces.com/conceptnet.db.zip

echo "Extracting ConceptNet..."
unzip -o conceptnet.db.zip

echo "Downloading WikiText-2..."
wget -c https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-2-v1.zip

echo "Extracting WikiText-2..."
unzip -o wikitext-2-v1.zip

echo "Cleaning up zip files..."
rm -f *.zip

echo "Knowledge sources download completed!"
echo "Available files:"
ls -la

cd ../..