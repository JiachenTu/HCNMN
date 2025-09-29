#!/usr/bin/env python3

import os
import json
import h5py
import pickle
from pathlib import Path

def check_file_exists(filepath, description=""):
    """Check if a file exists and return status"""
    if os.path.exists(filepath):
        if os.path.islink(filepath):
            target = os.readlink(filepath)
            if os.path.exists(target):
                print(f"✓ {filepath} -> {target} {description}")
                return True
            else:
                print(f"✗ {filepath} -> {target} (BROKEN SYMLINK) {description}")
                return False
        else:
            size = os.path.getsize(filepath)
            size_str = f"({size / (1024**2):.1f} MB)" if size > 1024*1024 else f"({size} bytes)"
            print(f"✓ {filepath} {size_str} {description}")
            return True
    else:
        print(f"✗ {filepath} - MISSING {description}")
        return False

def check_directory_exists(dirpath, description=""):
    """Check if a directory exists and has content"""
    if os.path.exists(dirpath) and os.path.isdir(dirpath):
        files = os.listdir(dirpath)
        if files:
            print(f"✓ {dirpath} ({len(files)} files) {description}")
            return True
        else:
            print(f"⚠ {dirpath} (EMPTY) {description}")
            return False
    else:
        print(f"✗ {dirpath} - MISSING {description}")
        return False

def verify_json_file(filepath, expected_keys=None):
    """Verify JSON file can be loaded and has expected structure"""
    if not check_file_exists(filepath):
        return False

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if expected_keys:
            missing_keys = [key for key in expected_keys if key not in data]
            if missing_keys:
                print(f"  ⚠ Missing keys in {filepath}: {missing_keys}")
                return False

        print(f"  ✓ JSON structure valid")
        return True
    except Exception as e:
        print(f"  ✗ JSON validation failed: {e}")
        return False

def verify_h5_file(filepath):
    """Verify H5 file can be opened"""
    if not check_file_exists(filepath):
        return False

    try:
        with h5py.File(filepath, 'r') as f:
            keys = list(f.keys())
            print(f"  ✓ H5 file valid, keys: {keys[:5]}{'...' if len(keys) > 5 else ''}")
        return True
    except Exception as e:
        print(f"  ✗ H5 validation failed: {e}")
        return False

def verify_pickle_file(filepath):
    """Verify pickle file can be loaded"""
    if not check_file_exists(filepath):
        return False

    try:
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        print(f"  ✓ Pickle file valid, type: {type(data)}")
        return True
    except Exception as e:
        print(f"  ✗ Pickle validation failed: {e}")
        return False

def main():
    print("=== HCNMN Data Verification ===\n")

    # Change to HCNMN directory
    os.chdir('/home/jiachen/scratch/graph_reasoning/HCNMN')

    all_good = True

    print("1. Basic Directory Structure:")
    required_dirs = [
        ('data', 'Main data directory'),
        ('data/vg', 'Visual Genome data (symlink)'),
        ('data/vqa', 'VQA v2 data'),
        ('data/knowledge', 'Knowledge sources'),
        ('data/glove', 'GloVe embeddings'),
        ('data/features', 'Processed features'),
        ('data/concepts', 'Concept graphs'),
        ('scripts', 'Download/processing scripts')
    ]

    for dirname, desc in required_dirs:
        if not check_directory_exists(dirname, desc):
            all_good = False

    print("\n2. Raw Data Files:")
    raw_files = [
        ('data/vqa/v2_OpenEnded_mscoco_train2014_questions.json', 'VQA training questions'),
        ('data/vqa/v2_mscoco_train2014_annotations.json', 'VQA training annotations'),
        ('data/vqa/v2_OpenEnded_mscoco_val2014_questions.json', 'VQA validation questions'),
        ('data/vqa/v2_mscoco_val2014_annotations.json', 'VQA validation annotations'),
        ('data/knowledge/conceptnet.db', 'ConceptNet database'),
        ('data/glove/glove.840B.300d.txt', 'GloVe embeddings text'),
    ]

    for filepath, desc in raw_files:
        if not check_file_exists(filepath, desc):
            all_good = False

    print("\n3. Processed Files:")
    processed_files = [
        ('data/glove/glove.pt', 'GloVe embeddings pickle'),
        ('data/features/train_questions.pt', 'Processed training questions'),
        ('data/features/vocab.json', 'Vocabulary'),
        ('data/features/hierarchy.json', 'Concept hierarchy'),
        ('data/features/topology.json', 'Knowledge topology'),
        ('data/features/relation.json', 'Relations vocabulary'),
        ('data/features/property.json', 'Properties vocabulary'),
        ('data/features/concept_property.json', 'Concept properties'),
        ('data/features/trainval_feature.h5', 'Visual features'),
    ]

    for filepath, desc in processed_files:
        if os.path.exists(filepath):
            if filepath.endswith('.json'):
                verify_json_file(filepath)
            elif filepath.endswith('.h5'):
                verify_h5_file(filepath)
            elif filepath.endswith('.pt'):
                verify_pickle_file(filepath)
            else:
                check_file_exists(filepath, desc)
        else:
            print(f"⚠ {filepath} - NOT YET PROCESSED {desc}")

    print("\n4. Feature Directory:")
    if os.path.exists('data/features/trainval_36'):
        check_directory_exists('data/features/trainval_36', 'LXMERT features')
    else:
        print("⚠ data/features/trainval_36 - NOT YET DOWNLOADED")

    print("\n5. Scripts:")
    scripts = [
        'scripts/download_vqa.sh',
        'scripts/download_knowledge.sh',
        'scripts/download_glove.sh',
        'scripts/download_lxmert_features.sh',
        'scripts/process_glove.py',
        'scripts/setup_nltk.py'
    ]

    for script in scripts:
        if not check_file_exists(script):
            all_good = False

    print(f"\n=== Summary ===")
    if all_good:
        print("✓ All required directories and scripts are present!")
    else:
        print("⚠ Some files are missing. Run the download scripts to fetch required data.")

    print("\nNext steps:")
    print("1. Run download scripts: bash scripts/download_*.sh")
    print("2. Setup NLTK: python scripts/setup_nltk.py")
    print("3. Process GloVe: python scripts/process_glove.py --input data/glove/glove.840B.300d.txt --output data/glove/glove.pt")
    print("4. Run preprocessing pipeline from README")

if __name__ == "__main__":
    main()