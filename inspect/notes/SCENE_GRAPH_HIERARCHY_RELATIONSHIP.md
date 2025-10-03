# Scene Graph Hierarchy Relationship

**Last Updated**: 2025-10-03

## Overview

This document explains how hierarchical scene graphs relate to the original Visual Genome annotations, how objects are processed, and how relationships are inherited across granularity levels.

## Visual Genome Scene Graph Structure

### Original VG Format

```json
{
  "image_id": 498335,
  "objects": [
    {
      "object_id": 1,
      "names": ["clock"],
      "x": 100,
      "y": 50,
      "w": 80,
      "h": 120,
      "synsets": ["clock.n.01"]
    },
    {
      "object_id": 2,
      "names": ["wall"],
      "x": 0,
      "y": 0,
      "w": 800,
      "h": 600
    }
  ],
  "relationships": [
    {
      "relationship_id": 1,
      "subject_id": 1,      ← clock
      "predicate": "on",
      "object_id": 2        ← wall
    }
  ]
}
```

### Key Components

**Objects**:
- `object_id`: Unique identifier
- `names`: List of names (usually 1)
- `x, y, w, h`: Bounding box coordinates
- `synsets`: WordNet synset (optional, we compute if missing)

**Relationships**:
- `subject_id`: Source object ID
- `predicate`: Relationship type ("on", "in", "near", "has", etc.)
- `object_id`: Target object ID

## Hierarchy Construction Process

### Step 1: Object Extraction

```python
# From VG objects
vg_objects = [
    {"object_id": 1, "names": ["clock"], "x": 100, ...},
    {"object_id": 2, "names": ["wall"], "x": 0, ...},
    {"object_id": 3, "names": ["flower"], "x": 200, ...},
    # ... 30 total objects
]

# Extract unique object names (fine-grained level)
unique_objects = ["clock", "wall", "flower", ...]  # 18 unique names
```

**Note**: VG has 30 object instances with duplicates (e.g., "pot" appears 3 times). After deduplication: 18 unique fine-grained concepts.

### Step 2: WordNet Synset Lookup

```python
for obj_name in unique_objects:
    # Look up in WordNet
    synsets = wn.synsets(obj_name, pos=wn.NOUN)

    if not synsets:
        # No WordNet mapping → use object name for all levels
        fine = mid = coarse = obj_name
        continue

    # Use first (most common) synset
    synset = synsets[0]

    # Get hypernym path
    path = synset.hypernym_paths()[0]  # Longest path
    # Example: clock.n.01 →
    #   [(entity, 0), (physical entity, 1), ..., (clock, 10)]
```

### Step 3: Granularity Selection

**V7 (Rules)**:
```python
# Score candidates at each depth range
mid_concept = select_best(path, depths=[4,5,6])      # instrumentality
coarse_concept = select_best(path, depths=[1,2,3])   # object
```

**V8.1 (LLM)**:
```python
# Provide context + two-stage selection
context = {
    'objects': all_objects_with_bboxes,
    'relationships': relevant_relationships,
    'current_bbox': current_object_position
}
result = llm_select(obj_name, path, context)
# → {"mid": "instrumentality", "coarse": "object", "reasoning": "..."}
```

### Step 4: Mapping Storage

```python
object_to_levels = {
    "clock": {
        "fine": "clock",
        "mid": "instrumentality",
        "coarse": "object"
    },
    "wall": {
        "fine": "wall",
        "mid": "structure",
        "coarse": "object"
    },
    # ... for all 18 objects
}
```

## Relationship Inheritance

### Original Fine-Grained Relationships

```
clock -on-> wall
flower -in-> pot
sign -near-> street
```

### Mid-Level Relationships (Inherited)

Objects map to mid-level concepts, relationships preserved:

```
clock → instrumentality
wall → structure
flower → organism
pot → artifact
sign → clue
street → road

Inherited relationships:
instrumentality -on-> structure      (clock on wall)
organism -in-> artifact              (flower in pot)
clue -near-> road                    (sign near street)
```

### Coarse-Level Relationships (Inherited)

Objects map to coarse concepts:

```
instrumentality → object
structure → object
organism → object
artifact → object
clue → communication
road → physical entity

Inherited relationships:
object -on-> object                  (self-loop, from clock-wall merge)
object -in-> object                  (self-loop, from flower-pot merge)
communication -near-> physical entity (sign near street)
```

**Self-loops**: When both subject and object map to same coarse concept, relationship becomes a self-loop. These are preserved in mappings but typically removed in graph visualizations.

## Complete Example: Image 498335

### Original VG Scene Graph (Simplified)

```
Objects (30 instances, 18 unique):
- clock (1x) at (100,50)
- flower (1x) at (200,300)
- flowers (1x) at (325,851)  ← Different instance
- pot (3x) at multiple positions
- wall (1x), railing (2x), ...

Relationships (15 total):
- clock -on-> wall
- flower -in-> pot
- flowers -in-> pot
- billboard -on-> building
- sign -near-> street
- ...
```

### Fine-Grained Hierarchy

```
Objects: 18 unique concepts
[clock, flower, flowers, pot, wall, railing, billboard,
 sign, street, background, lot, light, words, ...]

Relationships: All 15 preserved
clock -on-> wall
flower -in-> pot
flowers -in-> pot
...
```

### Mid-Level Hierarchy

```
Objects: 15 concepts (V8.1)
[instrumentality, plant, artifact, structure,
 clue, road, physical phenomenon, ...]

Merged mappings:
- flower, flowers → plant (2 objects merged)
- clock, pole, pot → instrumentality (3 objects merged)
- railing, billboard, balcony → structure (3 objects merged)

Relationships: Inherited + merged
plant -in-> artifact              (flower in pot, flowers in pot → merged)
instrumentality -on-> structure   (clock on wall)
clue -near-> road                 (sign near street)
structure -on-> structure         (billboard on building)
```

### Coarse-Level Hierarchy

```
Objects: 4 concepts (V8.1)
[object, physical entity, abstraction, communication]

Merged mappings:
- instrumentality, plant, artifact, structure → object (12 objects)
- physical phenomenon, road, ... → physical entity (9 objects)
- background, lot, words → abstraction (3 objects)
- clue → communication (1 object)

Relationships: Inherited + heavily merged
object -in-> object               (many relationships merged)
object -on-> object              (self-loops from same-concept merging)
communication -near-> physical entity (sign near street)
abstraction -... (various)
```

**Compression**: 18 → 15 → 4 concepts

## Graph Topology Preservation

### Node Merging Rules

1. **Identity Mapping (Fine)**: One-to-one with VG objects
2. **Concept Merging (Mid/Coarse)**: Many-to-one mapping
   ```
   flower, flowers → plant
   clock, pole, pot → instrumentality
   ```

3. **Self-Loop Detection**: When subject and object merge to same concept
   ```
   Original: clock -on-> wall
   Mid: instrumentality -on-> structure  (preserved)
   Coarse: object -on-> object  (self-loop, both are "object")
   ```

### Edge Inheritance Rules

1. **Direct Inheritance**: Relationship type (predicate) preserved
   ```
   Fine: clock -on-> wall
   Mid: instrumentality -on-> structure
   ```

2. **Multiplicity**: Multiple fine relationships may map to single mid relationship
   ```
   Fine: flower -in-> pot, flowers -in-> pot
   Mid: plant -in-> artifact  (merged, count=2)
   ```

3. **Self-Loop Filtering**: In visualizations, self-loops typically removed for clarity
   ```
   Coarse: object -on-> object  (removed in graph viz)
   ```

## Bounding Box Handling

### Fine-Grained Bboxes
Direct from VG:
```json
{"object_id": 1, "names": ["clock"], "x": 100, "y": 50, "w": 80, "h": 120}
```

### Mid/Coarse Bboxes (Merged)
When multiple objects merge, compute union bbox:

```python
def merge_bounding_boxes(objects, concept_name):
    """Compute union bbox for merged concept."""
    filtered = [obj for obj in objects if maps_to(obj, concept_name)]

    x_min = min(obj['x'] for obj in filtered)
    y_min = min(obj['y'] for obj in filtered)
    x_max = max(obj['x'] + obj['w'] for obj in filtered)
    y_max = max(obj['y'] + obj['h'] for obj in filtered)

    return {
        'x': x_min,
        'y': y_min,
        'w': x_max - x_min,
        'h': y_max - y_min
    }
```

Example:
```
Fine: clock@(100,50,80x120), pot@(360,918,138x66)
Mid (instrumentality): merged_bbox@(100,50,398x934)  ← Union of all instrumentalities
```

## Use Cases

### 1. Progressive Refinement

Start coarse, drill down:
```
User: "What objects are in the scene?"
System (Coarse): "Objects, abstractions, physical entities"

User: "What kind of objects?"
System (Mid): "Instrumentalities, structures, organisms"

User: "Which instrumentalities?"
System (Fine): "Clock, pole, pot"
```

### 2. Spatial Reasoning at Multiple Levels

```
Fine: "Where is the clock?" → (100, 50)
Mid: "Where are instrumentalities?" → Union bbox of all instrumentalities
Coarse: "Where are physical entities?" → Large region covering most objects
```

### 3. Relationship Reasoning

```
Question: "What is the clock's relationship to its surroundings?"

Fine level: clock -on-> wall
Mid level: instrumentality -on-> structure
Coarse level: object -on-> object

Explanation: Clock (an instrument) is mounted on a wall (a structure),
both being physical objects in the scene.
```

## Data Flow Diagram

```
Visual Genome Annotations
        ↓
┌──────────────────────────┐
│ Objects (30 instances)   │
│ - names, bbox, synsets   │
│ Relationships (15)       │
│ - subject, pred, object  │
└──────────┬───────────────┘
           │
           ↓ Deduplication
┌──────────────────────────┐
│ Fine Level (18 unique)   │
│ - Identity mapping       │
│ - All relationships      │
└──────────┬───────────────┘
           │
           ↓ WordNet + V7/V8/V8.1
┌──────────────────────────┐
│ Mid Level (15 concepts)  │
│ - Depth 4-6 selection    │
│ - Inherited relationships│
│ - Merged bboxes          │
└──────────┬───────────────┘
           │
           ↓ Further abstraction
┌──────────────────────────┐
│ Coarse Level (4 concepts)│
│ - Depth 1-3 selection    │
│ - Inherited relationships│
│ - Union bboxes           │
└──────────────────────────┘
```

## See Also

- [GRANULARITY_DEFINITIONS.md](GRANULARITY_DEFINITIONS.md) - Level definitions
- [WORDNET_INTEGRATION.md](WORDNET_INTEGRATION.md) - WordNet usage
- [METHODS_COMPARISON.md](METHODS_COMPARISON.md) - Selection methods

---

**Generated**: 2025-10-03
**Key**: Hierarchy preserves VG structure while adding semantic abstraction
