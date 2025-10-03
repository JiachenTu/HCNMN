# WordNet Integration

**Last Updated**: 2025-10-03

## Overview

WordNet provides the semantic ontology backbone for hierarchical scene graph abstraction. This document explains how WordNet is used, what hypernym paths are, and why depth ranges matter.

## What is WordNet?

WordNet is a large lexical database of English that groups words into synsets (synonym sets) and organizes them into a semantic hierarchy using hypernym (is-a) relationships.

**Example**:
```
"clock" is-a "timepiece"
"timepiece" is-a "measuring instrument"
"measuring instrument" is-a "instrument"
...
"physical entity" is-a "entity"
```

## Synsets

### Definition
A synset represents a concept, not just a word.

```python
>>> wn.synsets("clock")
[
    Synset('clock.n.01'),  # Timepiece device
    Synset('clock.n.02'),  # Time shown on clock
    Synset('clock.v.01'),  # Measure time with clock
]
```

### Our Usage
We use the **first noun synset** (most common meaning):

```python
synset = wn.synsets("clock", pos=wn.NOUN)[0]
# → clock.n.01: "a timepiece that shows the time of day"
```

## Hypernym Paths

### Definition
A hypernym is a more general concept ("is-a" relationship).
A hypernym path traces from specific to abstract.

### Example: "clock"

```
clock.n.01
  ↓ hypernym
timepiece.n.01
  ↓
measuring_instrument.n.01
  ↓
instrument.n.01
  ↓
device.n.01
  ↓
instrumentality.n.03
  ↓
artifact.n.01
  ↓
whole.n.02
  ↓
object.n.01
  ↓
physical_entity.n.01
  ↓
entity.n.01
```

### Depth Annotation

We assign depths from root to leaf:

```
entity (depth 0)           ← Root
  ↓
physical entity (depth 1)
  ↓
object (depth 2)
  ↓
whole (depth 3)
  ↓
artifact (depth 4)
  ↓
instrumentality (depth 5)  ← Mid-level range starts
  ↓
device (depth 6)
  ↓
instrument (depth 7)
  ↓
measuring instrument (depth 8)
  ↓
timepiece (depth 9)
  ↓
clock (depth 10)           ← Leaf
```

## Depth Ranges and Semantics

### Depth 0: Root
```
entity - everything is an entity
```
**Semantics**: Too abstract, not useful

### Depth 1: Very Abstract Domains
```
physical entity, abstraction, psychological feature
```
**Semantics**: Broad philosophical categories
**Use**: Coarse-level fallback (when depth 2 unavailable)

### Depth 2: ⭐ Coarse-Level Sweet Spot
```
object, matter, process, communication, event, state
```
**Semantics**: Meaningful high-level domains
**Use**: **Preferred coarse-level** selection

### Depth 3: Specific Domains
```
whole, living thing, artifact, substance, natural object
```
**Semantics**: More specific than depth 2, sometimes overlaps with mid
**Use**: Coarse-level fallback (when depth 2 too broad)

### Depth 4: Broad Categories
```
artifact, living thing, natural object, location
```
**Semantics**: Broad categorical groupings
**Use**: Mid-level fallback

### Depth 5: ⭐ Mid-Level Sweet Spot
```
instrumentality, organism, structure, covering, equipment,
container, conveyance, facility
```
**Semantics**: Clear functional/semantic categories
**Use**: **Preferred mid-level** selection

### Depth 6: Specific Categories
```
device, building, clothing, vehicle, plant organ, implement
```
**Semantics**: More specific than depth 5, still categorical
**Use**: Mid-level fallback

### Depth 7+: Object-Specific
```
measuring instrument, timepiece, clock, ...
```
**Semantics**: Too specific for abstraction
**Use**: Fine-grained level only

## How Each Method Uses WordNet

### V6.1: Fixed Depth (Superseded)
```python
# Always depth 4 for coarse
coarse = get_hypernym_at_depth(synset, depth=4)

# Fixed 13 semantic categories for mid
if obj in ["car", "bicycle", ...]: mid = "vehicle"
elif obj in ["dog", "cat", ...]: mid = "animal"
# ... hard-coded mappings
```
**Problem**: Inflexible, poor depth choice (4 for coarse)

### V7: Adaptive Rules
```python
# Extract candidates from depth ranges
coarse_candidates = [c for c, d in path if 1 <= d <= 3]
mid_candidates = [c for c, d in path if 4 <= d <= 6]

# Score each candidate
score = depth_score + semantic_bonus

# Example scores for clock:
#   Coarse: object (d=2) → score 20  ⭐
#           physical entity (d=1) → score 14
#           whole (d=3) → score 12
#
#   Mid: instrumentality (d=5) → score 20  ⭐
#        artifact (d=4) → score 14
#        device (d=6) → score 16

# Select highest scoring
```
**Advantage**: Adaptive within ranges, semantic awareness

### V8: Basic LLM
```python
# Extract same candidates
coarse_candidates = [c for c, d in path if 1 <= d <= 3]
mid_candidates = [c for c, d in path if 4 <= d <= 6]

# Prompt LLM to select
prompt = f"""
COARSE (1-3): {coarse_candidates}
MID (4-6): {mid_candidates}
Pick the most general (coarse) and clear categorical (mid)
"""

# LLM selects based on semantic understanding
```
**Advantage**: Semantic reasoning, no manual tuning
**Problem**: 72% success, no context

### V8.1: Context-Aware LLM
```python
# Same candidates + scene context
context = {
    'objects': all_objects_with_bboxes,
    'relationships': relevant_connections,
    'current_bbox': current_object_position
}

# Two-stage prompt with context
prompt = f"""
Goal: Create traceable hierarchy
Context: {scene_info}

STAGE 1 - MID (4-6): {mid_candidates}
Which represents "{obj}" in this scene?

STAGE 2 - COARSE (1-3): {coarse_candidates}
High-level domain?

Reasoning required.
"""

# LLM selects with full scene understanding
```
**Advantage**: 100% success, context-aware, with reasoning

## WordNet Path Extraction

### Code Implementation

```python
def format_wordnet_path(synset):
    """Extract WordNet path with depth annotations."""
    paths = synset.hypernym_paths()
    if not paths:
        return []

    # Use longest path (most specific)
    longest_path = max(paths, key=len)

    formatted_path = []
    for idx, s in enumerate(longest_path):
        concept_name = s.name().split('.')[0].replace('_', ' ')
        formatted_path.append((concept_name, idx))

    return formatted_path

# Example output:
# [(entity, 0), (physical entity, 1), ..., (clock, 10)]
```

### Multiple Paths Handling

Some synsets have multiple hypernym paths:

```python
>>> synset = wn.synset("dog.n.01")
>>> synset.hypernym_paths()
[
    [entity.n.01, physical_entity.n.01, object.n.01, ...],  # Path 1
    [entity.n.01, physical_entity.n.01, thing.n.12, ...]    # Path 2
]
```

**Our approach**: Use **longest path** (most specific/detailed)

## Common WordNet Concepts

### Coarse-Level (Depth 1-3)

| Concept | Depth | Count in Image 498335 | Description |
|---------|-------|----------------------|-------------|
| physical entity | 1 | 9 | Physical/tangible objects |
| object | 2 | 5 | Concrete physical objects |
| abstraction | 1 | 3 | Non-physical concepts |
| communication | 2 | 1 | Information exchange |
| process | 2 | 1 | Physical/chemical processes |
| thing | 2 | 1 | General objects/parts |

### Mid-Level (Depth 4-6)

| Concept | Depth | Count in Image 498335 | Description |
|---------|-------|----------------------|-------------|
| plant | 6 | 2 | Botanical organisms |
| structure | 5 | 2 | Built structures |
| instrumentality | 5 | 2 | Tools/instruments |
| artifact | 4 | 2 | Man-made objects |
| organism | 5 | 2 | Living beings |
| physical phenomenon | 5 | 1 | Physical effects |

## Depth Distribution Analysis

### Image 498335 WordNet Paths

```
Depth Distribution (all nodes in paths):
Depth 0: 1 node (entity)
Depth 1: 2 nodes (physical entity, abstraction)
Depth 2: 6 nodes (object, process, communication, ...)
Depth 3: 8 nodes (whole, living thing, ...)
Depth 4: 9 nodes (artifact, ...)
Depth 5: 11 nodes (instrumentality, organism, structure, ...)  ⭐ Peak
Depth 6: 13 nodes (device, plant, ...)  ⭐ Peak
Depth 7: 11 nodes
Depth 8: 8 nodes
Depth 9: 4 nodes
Depth 10: 4 nodes
```

**Observation**: Depths 5-6 have most diversity → ideal for mid-level

## Handling Missing Synsets

Some objects may not be in WordNet:

```python
synsets = wn.synsets("clock")  # Found!
synsets = wn.synsets("qwerty")  # [] - Not found

# Fallback: Use object name for all levels
if not synsets:
    fine = mid = coarse = object_name
    # Skip WordNet path processing
```

## Advantages of WordNet

✅ **Comprehensive**: 155,000+ synsets covering most English nouns
✅ **Structured**: Clear hierarchy with is-a relationships
✅ **Semantic**: Captures meaning, not just words
✅ **Stable**: Well-established, not changing rapidly
✅ **Free**: Open-source, no licensing issues
✅ **NLTK integration**: Easy to use with Python

## Limitations

❌ **English-only**: No multilingual support
❌ **Noun-focused**: Verbs/adjectives less developed
❌ **Domain gaps**: Missing some technical/modern terms
❌ **Multiple senses**: Polysemy requires disambiguation
❌ **Flat in places**: Some areas lack depth/detail

## Alternative Ontologies (Not Used)

### ConceptNet
**Pros**: Multilingual, modern concepts
**Cons**: Less structured hierarchy, nosier

### BabelNet
**Pros**: Multilingual, comprehensive
**Cons**: More complex, heavier

### Custom Ontology
**Pros**: Domain-specific, tailored
**Cons**: Manual creation, maintenance overhead

**Decision**: WordNet provides best balance for Visual Genome scene graphs

## Example Walkthrough

### Object: "flower"

**Step 1**: Look up synset
```python
synset = wn.synsets("flower", pos=wn.NOUN)[0]
# → flower.n.03: "reproductive organ of angiosperm plants"
```

**Step 2**: Extract hypernym path
```python
path = synset.hypernym_paths()[0]
# → [entity, physical entity, object, whole, living thing,
#     organism, plant, vascular plant, spermatophyte,
#     angiosperm, flower]
```

**Step 3**: Annotate with depths
```
entity (0), physical entity (1), object (2), whole (3),
living thing (4), organism (5), plant (6), vascular plant (7),
spermatophyte (8), angiosperm (9), flower (10)
```

**Step 4**: Extract candidates
```
Coarse (1-3): physical entity, object, whole
Mid (4-6): living thing, organism, plant
```

**Step 5**: Select (V8.1)
```
LLM with context selects:
Mid: organism (d=5) - "biological organism type"
Coarse: object (d=2) - "physical object domain"
```

**Result**:
```
Fine: flower
Mid: organism
Coarse: object
```

## See Also

- [GRANULARITY_DEFINITIONS.md](GRANULARITY_DEFINITIONS.md) - Level definitions
- [SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md](SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md) - Scene graph integration
- [METHODS_COMPARISON.md](METHODS_COMPARISON.md) - How methods use WordNet

---

**Generated**: 2025-10-03
**Key**: WordNet provides structured semantic hierarchy for abstraction
