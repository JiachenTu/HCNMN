import json
import numpy as np
import pickle
import os
"""
Utilities for preprocessing sequence data.

Special tokens that are in all dictionaries:

<NULL>: Extra parts of the sequence that we should ignore
<START>: Goes at the start of a sequence
<END>: Goes at the end of a sequence, before <NULL> tokens
<UNK>: Out-of-vocabulary words
"""

SPECIAL_TOKENS = {
  '<NULL>': 0,
  '<START>': 1,
  '<END>': 2,
  '<UNK>': 3,
}


def tokenize(s, delim=' ',
      add_start_token=True, add_end_token=True,
      punct_to_keep=None, punct_to_remove=None):
  """
  Tokenize a sequence, converting a string s into a list of (string) tokens by
  splitting on the specified delimiter. Optionally keep or remove certain
  punctuation marks and add start and end tokens.
  """
  if punct_to_keep is not None:
    for p in punct_to_keep:
      s = s.replace(p, '%s%s' % (delim, p))

  if punct_to_remove is not None:
    for p in punct_to_remove:
      s = s.replace(p, '')

  # if delim='' then regard the whole s as a token
  tokens = s.split(delim) if delim else [s]
  if add_start_token:
    tokens.insert(0, '<START>')
  if add_end_token:
    tokens.append('<END>')
  return tokens


def build_vocab(sequences, min_token_count=1, delim=' ',
                punct_to_keep=None, punct_to_remove=None, add_special=None):
  token_to_count = {}
  tokenize_kwargs = {
    'delim': delim,
    'punct_to_keep': punct_to_keep,
    'punct_to_remove': punct_to_remove,
  }
  for seq in sequences:
    seq_tokens = tokenize(seq, **tokenize_kwargs,
                    add_start_token=False, add_end_token=False)
    for token in seq_tokens:
      if token not in token_to_count:
        token_to_count[token] = 0
      token_to_count[token] += 1

  token_to_idx = {}
  if add_special:
    for token in SPECIAL_TOKENS:
      token_to_idx[token] = len(token_to_idx)
  for token, count in sorted(token_to_count.items()):
    if count >= min_token_count:
      token_to_idx[token] = len(token_to_idx)

  return token_to_idx


def encode(seq_tokens, token_to_idx, allow_unk=False):
  seq_idx = []
  for token in seq_tokens:
    if token not in token_to_idx:
      if allow_unk:
        token = '<UNK>'
      else:
        raise KeyError('Token "%s" not in vocab' % token)
    seq_idx.append(token_to_idx[token])
  return seq_idx


def decode(seq_idx, idx_to_token, delim=None, stop_at_end=True):
  tokens = []
  for idx in seq_idx:
    tokens.append(idx_to_token[idx])
    if stop_at_end and tokens[-1] == '<END>':
      break
  if delim is None:
    return tokens
  else:
    return delim.join(tokens)

def FindRelevantTerms():
  return

def MatchPropertyByVocab(args):
  # Handle different glove formats
  glove_data = pickle.load(open(args.glove_pt, 'rb'))
  if isinstance(glove_data, dict) and 'embeddings' in glove_data:
    glove = glove_data['embeddings']
  else:
    glove = glove_data

  # Use knowledge_dir if available, fallback to input_knowledge_folder
  knowledge_folder = getattr(args, 'knowledge_dir', args.input_knowledge_folder)
  if not knowledge_folder.endswith('/'):
    knowledge_folder += '/'

  p2c = knowledge_folder + 'conceptnet.json'
  p2w = knowledge_folder + 'wikitext.json'

  # Check if files exist, create dummy data if not
  if not os.path.exists(p2c):
    cn = {'hasProperty': {}, 'relation': {}}
  else:
    with open(p2c, 'r') as f:
      cn = json.load(f)

  if not os.path.exists(p2w):
    wi = {}
  else:
    with open(p2w, 'r') as f:
      wi = json.load(f)

  with open(args.input_vocab, 'r') as f:
    vocabs = json.load(f) 
  
  # we first create a dictionary to map each term with its relevant distinguishable property
  term2property={}
  for term in vocabs['terms']:
    cn_property = cn.get('hasProperty', {}).get(term, [])
    wi_text = wi.get(term, '')
    relevant_properties = [prop for prop in cn_property if prop in str(wi_text)]
    term2property[term] = relevant_properties

  property_vocab = {}
  # Flatten all properties and get unique sorted list
  all_properties = []
  for props in term2property.values():
    all_properties.extend(props)
  all_property_vocab = sorted(list(set(all_properties)))

  property_vocab['properties'] = all_property_vocab

  # convert term2property to vector
  for term in vocabs['terms']:
    pv = np.zeros(len(all_property_vocab))
    relevant_properties = term2property[term]
    for i, prop in enumerate(all_property_vocab):
      if prop in relevant_properties:
        pv[i] = 1
    term2property[term] = pv

  # next create a copy of property vectors corresponds to each concept per question.
  concept_property = {}
  concept_property['property_vector_per_question'] = []
  for terms in vocabs['term_per_question']:
    concept_property['property_vector_per_question'].append([term2property[term] for term in terms])

  # Get embeddings for properties if they exist in glove
  property_embeddings = []
  for prop in all_property_vocab:
    if prop in glove:
      property_embeddings.append(glove[prop])
    else:
      # Use random embedding if property not in glove
      if len(property_embeddings) > 0:
        dim = len(property_embeddings[0])
      else:
        dim = 300  # Default GloVe dimension
      property_embeddings.append(np.random.normal(0, 0.1, dim))

  property_vocab['property_embeddings'] = property_embeddings
  return concept_property, property_vocab

def MatchRelationByVocab(args):
  # Handle different glove formats
  glove_data = pickle.load(open(args.glove_pt, 'rb'))
  if isinstance(glove_data, dict) and 'embeddings' in glove_data:
    glove = glove_data['embeddings']
  else:
    glove = glove_data

  # Use knowledge_dir if available, fallback to input_knowledge_folder
  knowledge_folder = getattr(args, 'knowledge_dir', args.input_knowledge_folder)
  if not knowledge_folder.endswith('/'):
    knowledge_folder += '/'

  p2c = knowledge_folder + 'conceptnet.json'
  p2w = knowledge_folder + 'wikitext.json'

  # Check if files exist, create dummy data if not
  if not os.path.exists(p2c):
    cn = {'relation': {}}
  else:
    with open(p2c, 'r') as f:
      cn = json.load(f)

  if not os.path.exists(p2w):
    wi = {'relation': {}}
  else:
    with open(p2w, 'r') as f:
      wi = json.load(f)

  with open(args.input_vocab, 'r') as f:
    vocabs = json.load(f)

  # we first extract a list of all the relevant relationships
  all_relations = []
  if 'relation' in cn:
    if isinstance(cn['relation'], list):
      all_relations.extend(cn['relation'])
    elif isinstance(cn['relation'], dict):
      for term_rels in cn['relation'].values():
        if isinstance(term_rels, list):
          all_relations.extend(term_rels)
        elif isinstance(term_rels, dict):
          all_relations.extend(term_rels.keys())

  if 'relation' in wi:
    if isinstance(wi['relation'], list):
      all_relations.extend(wi['relation'])
    elif isinstance(wi['relation'], dict):
      for term_rels in wi['relation'].values():
        if isinstance(term_rels, list):
          all_relations.extend(term_rels)
        elif isinstance(term_rels, dict):
          all_relations.extend(term_rels.keys())

  relation_list = sorted(list(set(all_relations)))
  relation_vocab = {'relations': relation_list}

  # next create a copy of concept affinity matrix corresponds to each concept per question.
  topology_json = {}
  topology_by_questions = []

  for terms in vocabs['term_per_question']:
    affinity = np.zeros([len(terms), len(terms)])

    for i in range(len(terms)):
      term_i = terms[i]
      term_i_relations = cn.get('relation', {}).get(term_i, {})

      for j in range(len(terms)):
        if i != j:
          term_j = terms[j]
          # Check if there's a relation between term_i and term_j
          if term_j in term_i_relations:
            affinity[i][j] = 1.0  # Simple binary relation

    topology_by_questions.append(affinity)

  topology_json['topology_per_question'] = topology_by_questions

  # Get embeddings for relations if they exist in glove
  relation_embeddings = []
  for rel in relation_list:
    if rel in glove:
      relation_embeddings.append(glove[rel])
    else:
      # Use random embedding if relation not in glove
      if len(relation_embeddings) > 0:
        dim = len(relation_embeddings[0])
      else:
        dim = 300  # Default GloVe dimension
      relation_embeddings.append(np.random.normal(0, 0.1, dim))

  relation_vocab['relation_embeddings'] = relation_embeddings
  return topology_json, relation_vocab

def get_id_from_list(entry, full):
  for i in range(len(full)):
    if full[i] == entry:
        return i
  return -1

def get_ids_from_list(entry, full):
  ids = -np.ones(len(entry), dtype=int)
  for e in range(len(entry)):
    for i in range(len(full)):
      if full[i] == entry[e]:
          ids[e] = i
          break
  return ids