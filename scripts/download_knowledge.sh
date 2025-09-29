#!/bin/bash

# Download knowledge sources for HCNMN
# This script downloads ConceptNet and WikiText-2

set -e

echo "=== Downloading Knowledge Sources ==="

# Create knowledge directory if it doesn't exist
mkdir -p data/knowledge
cd data/knowledge

echo "Downloading ConceptNet assertions (CSV format)..."
# Primary: ConceptNet 5.7 assertions in CSV format (~1.1GB compressed)
if wget -c https://s3.amazonaws.com/conceptnet/downloads/2019/edges/conceptnet-assertions-5.7.0.csv.gz; then
    echo "Extracting ConceptNet assertions..."
    gunzip -f conceptnet-assertions-5.7.0.csv.gz
    echo "✅ ConceptNet CSV download successful"
else
    echo "❌ Primary ConceptNet URL failed, trying alternative method..."

    # Alternative: Use conceptnet-lite package
    echo "Installing conceptnet-lite via pip..."
    pip install conceptnet-lite

    echo "Creating ConceptNet database via Python..."
    python3 -c "
import conceptnet_lite
import os
db_path = 'conceptnet.db'
try:
    # This will download and create the database
    db = conceptnet_lite.connect(db_path)
    print('✅ ConceptNet database created successfully')
except Exception as e:
    print(f'❌ ConceptNet-lite method failed: {e}')
    print('Manual download may be required from: https://github.com/commonsense/conceptnet5/wiki/Downloads')
"
fi

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