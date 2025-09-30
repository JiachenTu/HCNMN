#!/usr/bin/env python3
import re
import os
import argparse
import json
import numpy as np
import pickle
from collections import Counter
from utils import FindRelevantTerms
from nltk.corpus import wordnet as wn

def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])

parser = argparse.ArgumentParser()
parser.add_argument('--input_vocab', required=True, help='path to vocab.json')
parser.add_argument('--glove_pt', help='glove pickle file, should be a map whose key are words and value are word vectors represented by numpy arrays. Only needed in train mode')
parser.add_argument('--vocab_json', required=True, help='path to output vocab')
parser.add_argument('--hierarchy', required=True, help='path to output hierarchy')
args = parser.parse_args()
assert os.path.isfile(args.input_vocab)

augmentation_vocab = {}

print('Loading vocab')
with open(args.input_vocab, 'r') as f:
    vocab = json.load(f)

# Extract terms from question tokens (skip special tokens)
skip_tokens = {'<NULL>', '<UNK>'}
terms = [token for token in vocab['question_token_to_idx'].keys() if token not in skip_tokens]

print(f'Found {len(terms)} terms from question vocabulary')

# Build augmentation vocabulary with WordNet hypernyms
for term in terms:
    synsets = wn.synsets(term)
    if synsets:
        hyperpaths = []
        for synset in synsets:
            paths = synset.hypernym_paths()
            for path in paths:
                hyperpaths.extend([s.name().split(".")[0].replace('_',' ') for s in path])
        augmentation_vocab[term] = list(set(hyperpaths))
    else:
        augmentation_vocab[term] = [term]

# Create augmented vocabulary structure
vocab['terms'] = terms
vocab['term_per_question'] = []
vocab['hierarchy_per_question'] = []

# For each question token, create a list of augmented terms
for i, term in enumerate(terms):
    augmented_terms = augmentation_vocab[term]
    vocab['term_per_question'].append(augmented_terms)

    # Calculate hierarchy depth for each augmented term
    hierarchy_depths = []
    for aug_term in augmented_terms:
        synsets = wn.synsets(aug_term)
        if synsets:
            max_depth = max(len(path) for synset in synsets for path in synset.hypernym_paths())
            hierarchy_depths.append(max_depth)
        else:
            hierarchy_depths.append(0)
    vocab['hierarchy_per_question'].append(hierarchy_depths)

print('write vocab')
with open(args.vocab_json, 'w') as f:
    json.dump(vocab, f)

with open(args.hierarchy, 'w') as f:
    json.dump(augmentation_vocab, f)