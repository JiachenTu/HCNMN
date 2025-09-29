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

# Try multiple alternative URLs
echo "Trying primary LXMERT repository..."
if wget -c https://nlp.cs.unc.edu/data/lxmert_data/mscoco_imgfeat/train2014_obj36.zip && \
   wget -c https://nlp.cs.unc.edu/data/lxmert_data/mscoco_imgfeat/val2014_obj36.zip; then
    echo "✅ Downloaded separate train and val files"
    DOWNLOAD_SUCCESS=true
elif wget -c https://nlp1.cs.unc.edu/data/lxmert_data/mscoco_imgfeat/trainval_obj36.zip; then
    echo "✅ Downloaded from alternative UNC server"
    DOWNLOAD_SUCCESS=true
elif wget -c https://nlp1.cs.unc.edu/data/lxmert_data/mscoco_imgfeat/train2014_obj36.zip && \
     wget -c https://nlp1.cs.unc.edu/data/lxmert_data/mscoco_imgfeat/val2014_obj36.zip; then
    echo "✅ Downloaded separate files from alternative server"
    DOWNLOAD_SUCCESS=true
else
    echo "❌ All automatic download URLs failed!"
    echo ""
    echo "🔧 Manual Download Required:"
    echo "Please download LXMERT features manually from:"
    echo "1. Google Drive: https://drive.google.com/drive/folders/1Gq1uLUk6NdD0CcJOptXjxE6ssY5XAuat"
    echo "2. Look for 'train2014_obj36.zip' and 'val2014_obj36.zip'"
    echo "3. Place them in the 'data/features/' directory"
    echo "4. Run this script again to extract them"
    echo ""

    # Check if files were manually downloaded
    if [ -f "train2014_obj36.zip" ] || [ -f "val2014_obj36.zip" ] || [ -f "trainval_obj36.zip" ]; then
        echo "✅ Found manually downloaded files!"
        DOWNLOAD_SUCCESS=true
    else
        echo "❌ No LXMERT feature files found. Exiting."
        cd ../..
        exit 1
    fi
fi

echo "Extracting LXMERT features..."

# Extract available zip files
for zipfile in *.zip; do
    if [ -f "$zipfile" ]; then
        echo "Extracting $zipfile..."
        unzip -o "$zipfile"
    fi
done

echo "Organizing extracted files..."
# Create trainval_36 directory and organize files
mkdir -p trainval_36

# Move extracted files to the correct location
if [ -d "trainval_obj36" ]; then
    mv trainval_obj36/* trainval_36/ 2>/dev/null || true
    rmdir trainval_obj36 2>/dev/null || true
fi

# Move any .tsv files to trainval_36
mv *.tsv trainval_36/ 2>/dev/null || true

echo "Cleaning up zip files..."
rm -f *.zip

echo "LXMERT features download completed!"
echo "Features directory contents:"
ls -la trainval_36/ | head -10

cd ../..