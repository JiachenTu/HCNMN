#!/usr/bin/env python3

import argparse
import pickle
import numpy as np
from tqdm import tqdm
import os

def process_glove(input_file, output_file):
    """
    Convert GloVe text format to pickle format for faster loading

    Args:
        input_file: Path to GloVe text file (e.g., glove.840B.300d.txt)
        output_file: Path to output pickle file (e.g., glove.pt)
    """
    print(f"Processing GloVe embeddings from {input_file}")
    print(f"Output will be saved to {output_file}")

    embeddings = {}
    vocab = []

    # Count total lines for progress bar
    print("Counting lines...")
    with open(input_file, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)

    print(f"Processing {total_lines} embeddings...")

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in tqdm(f, total=total_lines, desc="Processing"):
            values = line.strip().split()
            word = values[0]
            try:
                vector = np.array(values[1:], dtype='float32')
                embeddings[word] = vector
                vocab.append(word)
            except ValueError:
                print(f"Skipping malformed line for word: {word}")
                continue

    print(f"Processed {len(embeddings)} word embeddings")
    print(f"Embedding dimension: {len(next(iter(embeddings.values())))}")

    # Save as pickle
    data = {
        'embeddings': embeddings,
        'vocab': vocab,
        'dim': len(next(iter(embeddings.values())))
    }

    print(f"Saving to {output_file}...")
    with open(output_file, 'wb') as f:
        pickle.dump(data, f)

    print("GloVe processing completed!")
    print(f"Output file size: {os.path.getsize(output_file) / (1024**3):.2f} GB")

def main():
    parser = argparse.ArgumentParser(description='Process GloVe embeddings to pickle format')
    parser.add_argument('--input', required=True, help='Input GloVe text file')
    parser.add_argument('--output', required=True, help='Output pickle file')

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} does not exist")
        return

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    process_glove(args.input, args.output)

if __name__ == "__main__":
    main()