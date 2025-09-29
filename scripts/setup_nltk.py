#!/usr/bin/env python3

import nltk
import os

def setup_nltk():
    """
    Download required NLTK data for WordNet and text processing
    """
    print("Setting up NLTK data...")

    # Create NLTK data directory if it doesn't exist
    nltk_data_dir = os.path.expanduser('~/nltk_data')
    os.makedirs(nltk_data_dir, exist_ok=True)

    # Download required NLTK datasets
    datasets = [
        'wordnet',      # WordNet lexical database
        'omw-1.4',      # Open Multilingual Wordnet
        'punkt',        # Punkt tokenizer
        'stopwords',    # Stop words corpus
        'averaged_perceptron_tagger'  # POS tagger
    ]

    for dataset in datasets:
        try:
            print(f"Downloading {dataset}...")
            nltk.download(dataset, quiet=False)
            print(f"✓ {dataset} downloaded successfully")
        except Exception as e:
            print(f"✗ Failed to download {dataset}: {e}")

    print("NLTK setup completed!")

    # Test WordNet availability
    try:
        from nltk.corpus import wordnet as wn
        synsets = wn.synsets('dog')
        print(f"✓ WordNet test successful - found {len(synsets)} synsets for 'dog'")
    except Exception as e:
        print(f"✗ WordNet test failed: {e}")

if __name__ == "__main__":
    setup_nltk()