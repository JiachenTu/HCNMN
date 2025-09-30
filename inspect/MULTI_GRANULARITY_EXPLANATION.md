# Multi-Granularity Scene Graph Generation - Complete Guide

## Overview

Multi-granularity scene graphs enable visual reasoning at different levels of abstraction: **Fine** (specific objects), **Mid** (categories), and **Coarse** (high-level groups). This document explains how these levels are defined and which scripts generate them.

---

## Granularity Level Definitions

### Conceptual Framework

The 3-level hierarchy is based on **WordNet hypernym paths**:

```
Fine-grained (L0)    →    Mid-level (L1)         →    Coarse-grained (L2)
─────────────────         ─────────────────           ──────────────────
Original object           Immediate parent            Grandparent
Specific instance         Category                    High-level group
Most detailed             Moderate abstraction        Highest abstraction
```

### How Levels Are Computed

#### 1. **Fine-Grained Level** (L0: Original Objects)
- **Definition**: Direct object names from Visual Genome annotations
- **Source**: VG `objects[].names[0]` field
- **Examples**:
  - `"dog"` - specific animal
  - `"car"` - specific vehicle
  - `"tree"` - specific plant
  - `"person"` - specific human

**Code Implementation** (`visualize_scene_graph_hierarchy.py:79-81`):
```python
# Add to fine-grained
hierarchy['fine'].append(obj_name)
object_to_levels[obj_name] = {'fine': obj_name}
```

#### 2. **Mid-Level** (L1: Immediate Categories)
- **Definition**: First hypernym (parent) from WordNet
- **Source**: `synset.hypernyms()[0]`
- **Semantic Meaning**: Category or immediate generalization
- **Examples**:
  - `"dog"` → `"domestic animal"` (category)
  - `"car"` → `"motor vehicle"` (category)
  - `"tree"` → `"woody plant"` (category)
  - `"person"` → `"adult"` or `"human"` (category)

**Code Implementation** (`visualize_scene_graph_hierarchy.py:101-108`):
```python
# Get parent (mid-level)
if synset.hypernyms():
    parent = synset.hypernyms()[0]
    parent_name = parent.name().split('.')[0].replace('_', ' ')
    path.append(parent_name)

    if parent_name not in hierarchy['mid']:
        hierarchy['mid'].append(parent_name)
    object_to_levels[obj_name]['mid'] = parent_name
```

#### 3. **Coarse-Grained Level** (L2: High-Level Groups)
- **Definition**: Second hypernym (grandparent) from WordNet
- **Source**: `parent.hypernyms()[0]`
- **Semantic Meaning**: Abstract concept or domain
- **Examples**:
  - `"dog"` → `"domestic animal"` → `"animal"` (life form)
  - `"car"` → `"motor vehicle"` → `"self-propelled vehicle"` (artifact type)
  - `"tree"` → `"woody plant"` → `"vascular plant"` (organism type)
  - `"person"` → `"adult"` → `"person"` (entity type)

**Code Implementation** (`visualize_scene_graph_hierarchy.py:110-118`):
```python
# Get grandparent (coarse-level)
if parent.hypernyms():
    grandparent = parent.hypernyms()[0]
    grandparent_name = grandparent.name().split('.')[0].replace('_', ' ')
    path.append(grandparent_name)

    if grandparent_name not in hierarchy['coarse']:
        hierarchy['coarse'].append(grandparent_name)
    object_to_levels[obj_name]['coarse'] = grandparent_name
```

---

## Real-World Examples

### Example 1: Urban Street Scene (Image 498202)

| Fine-Grained | Mid-Level | Coarse-Grained |
|--------------|-----------|----------------|
| person (×4) | organism | living thing |
| car | motor vehicle | artifact |
| building | structure | artifact |
| tree | woody plant | vascular plant |
| sidewalk | walk | artifact |
| sign | communication | abstraction |
| umbrella | canopy | artifact |
| shirt | garment | clothing |
| road | way | artifact |

**Compression**: 30 objects → 20 mid-level → 19 coarse-level

### Example 2: Hierarchy Path Visualization

```
Fine:    "golden retriever"  "sedan"    "oak tree"    "woman"
         ↓                   ↓          ↓             ↓
Mid:     "dog"               "car"      "tree"        "person"
         ↓                   ↓          ↓             ↓
Coarse:  "animal"            "vehicle"  "plant"       "entity"
```

This creates a **taxonomic abstraction ladder** where:
- **Fine**: Answers "What specific object is this?"
- **Mid**: Answers "What category does it belong to?"
- **Coarse**: Answers "What domain or type is it?"

---

## Key Scripts for Multi-Granularity Generation

### 1. **`visualize_scene_graph_hierarchy.py`**
**Location**: `/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/visualize_scene_graph_hierarchy.py`

**Purpose**: Build clean 3-level hierarchy and visualize ontology tree

**Key Functions**:

#### `build_clean_hierarchy(objects, max_depth=3)` (lines 51-145)
- **Input**: VG object annotations
- **Output**: 3-level hierarchy dictionary
- **Algorithm**:
  ```python
  for each object in VG:
      # Level 0: Fine
      fine = object.name

      # Level 1: Mid
      synsets = wordnet.synsets(object.name)
      if synsets:
          mid = synsets[0].hypernyms()[0].name()

      # Level 2: Coarse
      if mid_synset.hypernyms():
          coarse = mid_synset.hypernyms()[0].name()
  ```

**Outputs**:
- `hierarchical_ontology_tree.png` - 3-column hierarchy visualization
- `original_scene_graph.png` - VG scene graph with relationships
- `combined_visualization.png` - Scene graph + hierarchy panel
- `ontology_data.json` - Hierarchy structure data

**Usage**:
```bash
conda run -n hcnmn python visualize_scene_graph_hierarchy.py \
  --vg_dir /path/to/vg \
  --output_dir vg \
  --image_id 498202
```

---

### 2. **`visualize_merged_granularity.py`**
**Location**: `/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/visualize_merged_granularity.py`

**Purpose**: Create merged scene graphs where objects with same concept combine into single nodes

**Key Functions**:

#### `build_clean_hierarchy(objects)` (lines 51-98)
- Same hierarchy construction as above
- Returns `object_to_levels` mapping for merging

#### `merge_bounding_boxes(bboxes)` (lines 100-124)
- **Purpose**: Combine multiple bounding boxes into minimum enclosing rectangle
- **Algorithm**:
  ```python
  x_min = min(bbox.x for all bboxes)
  y_min = min(bbox.y for all bboxes)
  x_max = max(bbox.x + bbox.w for all bboxes)
  y_max = max(bbox.y + bbox.h for all bboxes)

  merged_bbox = {
      'x': x_min, 'y': y_min,
      'w': x_max - x_min, 'h': y_max - y_min
  }
  ```

#### `create_merged_scene_graph(objects, object_to_levels, granularity)` (lines 126-182)
- **Purpose**: Merge objects by concept at specific granularity level
- **Algorithm**:
  ```python
  # Group objects by concept at this granularity
  for obj in objects:
      concept = object_to_levels[obj.name][granularity]
      concept_groups[concept].append(obj)

  # Merge bounding boxes for each concept group
  for concept, obj_list in concept_groups:
      merged_bbox = merge_bounding_boxes([obj.bbox for obj in obj_list])
      merged_nodes[concept] = {
          'bbox': merged_bbox,
          'object_count': len(obj_list),
          'original_objects': [obj.name for obj in obj_list]
      }
  ```

**Outputs**:
- `merged_fine.png` - Fine-grained merged scene graph
- `merged_mid.png` - Mid-level merged scene graph
- `merged_coarse.png` - Coarse-grained merged scene graph
- `merged_comparison.png` - Side-by-side 3-panel comparison
- `merged_scene_graph_data.json` - Merged graph structure
- `MERGED_SCENE_GRAPH_REPORT.md` - Statistics and compression ratios

**Usage**:
```bash
conda run -n hcnmn python visualize_merged_granularity.py \
  --vg_dir /path/to/vg \
  --output_dir vg \
  --image_id 498202
```

---

### 3. **`batch_sample_vg.py`**
**Location**: `/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/batch_sample_vg.py`

**Purpose**: Batch processing - sample N images and run both pipelines automatically

**Key Functions**:

#### `filter_good_samples(scene_graphs, vg_dir, min_objects, max_objects)`
- Filters VG images by object count (default: 10-30 objects)
- Requires images to have relationships
- Verifies image files exist

#### `stratified_sample(object_count_bins, num_samples, seed)`
- Performs stratified sampling across object count bins
- Ensures diverse representation
- Reproducible with fixed seed

#### `process_sample(image_id, vg_dir, output_dir, inspect_dir)`
- Runs both visualization pipelines sequentially:
  1. `visualize_merged_granularity.py`
  2. `visualize_scene_graph_hierarchy.py`
- Handles errors gracefully
- Returns success/failure status

**Outputs**:
- N sample directories (each with 10 visualization files)
- `BATCH_SAMPLING_REPORT.md` - Processing summary
- `batch_sampling_data.json` - Complete metadata

**Usage**:
```bash
conda run -n hcnmn python batch_sample_vg.py \
  --num_samples 25 \
  --min_objects 10 \
  --max_objects 30 \
  --seed 42
```

---

## Merging Mechanism

### Concept-Based Merging

At each granularity level, objects with the **same concept name** are merged:

#### Fine-Grained Merging
```
Objects:        person, person, person, person (4 instances)
Concept:        "person"
Merged Node:    1 node labeled "person" (4 obj)
Merged BBox:    Enclosing rectangle of all 4 person bboxes
```

#### Mid-Level Merging
```
Objects:        tree, bush, flower (3 different objects)
Concepts:       woody plant, woody plant, plant
Merged Nodes:
  - "woody plant" (tree + bush, 2 obj)
  - "plant" (flower, 1 obj)
```

#### Coarse-Grained Merging
```
Objects:        tree, bush, flower, grass (4 objects)
Mid Concepts:   woody plant, woody plant, plant, plant
Coarse Concept: vascular plant, vascular plant, vascular plant, vascular plant
Merged Node:    1 node labeled "vascular plant" (4 obj)
```

### Compression Ratios

Real example from sample_498202:

| Granularity | Objects | Merged Nodes | Compression |
|-------------|---------|--------------|-------------|
| Fine | 30 | 21 | 1.43x |
| Mid | 30 | 20 | 1.50x |
| Coarse | 30 | 19 | 1.58x |

**Note**: Low compression indicates high object diversity (many unique object types)

High compression example:
| Granularity | Objects | Merged Nodes | Compression |
|-------------|---------|--------------|-------------|
| Fine | 30 | 30 | 1.00x (all unique) |
| Mid | 30 | 12 | 2.50x (categories merge) |
| Coarse | 30 | 5 | 6.00x (high-level groups) |

---

## Visual Output Comparison

### 1. Hierarchical Ontology Tree
**File**: `hierarchical_ontology_tree.png`
**Shows**: 3-column tree structure
```
Fine               Mid                 Coarse
────────────────   ─────────────────   ──────────────
tree        ───→   woody plant   ───→  vascular plant
bush        ───→   woody plant   ───→  vascular plant
flower      ───→   plant         ───→  vascular plant
car         ───→   motor vehicle ───→  artifact
person      ───→   adult         ───→  living thing
```

### 2. Merged Scene Graphs
**Files**: `merged_fine.png`, `merged_mid.png`, `merged_coarse.png`
**Shows**: Image with bounding boxes at each level

**Fine-grained**:
- Many separate boxes for each object
- Labels: "tree", "tree", "bush", "flower"

**Mid-level**:
- Fewer, larger boxes
- Labels: "woody plant (2 obj)", "plant (1 obj)"

**Coarse-grained**:
- Fewest, largest boxes
- Labels: "vascular plant (4 obj)"

### 3. Comparison Panel
**File**: `merged_comparison.png`
**Shows**: Side-by-side 3-panel view
- Visualizes compression visually
- Shows how abstraction reduces scene complexity

---

## Integration with HCNMN Model

### How the Model Uses Multi-Granularity

The HCNMN model (`model/hierarchical_module.py`) operates on hierarchical concept graphs:

```python
HCG = {
    'concept_vis': (batch, CONCEPT_NUM, CV_DIM),      # Visual features
    'concept_lin': (batch, CONCEPT_NUM, CL_DIM),      # Linguistic features
    'mono_mask': (batch, CONCEPT_NUM, CONCEPT_NUM),   # Same-level relations
    'cross_mask': (batch, CONCEPT_NUM, CONCEPT_NUM),  # Cross-level relations
}
```

**Module Operations**:
1. **FindModule**: Locates objects at appropriate granularity
   - Fine: Find specific "golden retriever"
   - Mid: Find category "dog"
   - Coarse: Find domain "animal"

2. **FilterModule**: Filters using hierarchical properties
   - Fine: "red car" (specific property)
   - Mid: "vehicle" (category-level)
   - Coarse: "artifact" (domain-level)

3. **RelateModule**: Reasons about relationships
   - Fine: "man next to woman"
   - Mid: "person next to person"
   - Coarse: "entity near entity"

---

## WordNet Technical Details

### Synset Selection
- Uses `wn.synsets(word)[0]` - most common meaning
- Example: "bank" has multiple meanings (financial, riverbank)
- First synset is typically most frequent usage

### Hypernym Path
```python
from nltk.corpus import wordnet as wn

synsets = wn.synsets('dog')
synset = synsets[0]  # dog.n.01

# L1: Parent
parent = synset.hypernyms()[0]  # domestic_animal.n.01
parent_name = parent.name().split('.')[0]  # "domestic animal"

# L2: Grandparent
grandparent = parent.hypernyms()[0]  # animal.n.01
grandparent_name = grandparent.name().split('.')[0]  # "animal"
```

### Edge Cases

#### No WordNet Entry
```python
if not synsets:
    # Use object name for all levels
    object_to_levels[obj_name] = {
        'fine': obj_name,
        'mid': obj_name,
        'coarse': obj_name
    }
```

#### No Hypernyms (Root Concept)
```python
if not synset.hypernyms():
    # Use fine-level for mid and coarse
    object_to_levels[obj_name]['mid'] = obj_name
    object_to_levels[obj_name]['coarse'] = obj_name
```

---

## Summary

### Key Points

1. **Granularity Definition**:
   - Fine = Original VG objects
   - Mid = WordNet immediate hypernym (1 level up)
   - Coarse = WordNet second hypernym (2 levels up)

2. **Key Scripts**:
   - `visualize_scene_graph_hierarchy.py` - Build hierarchy + ontology tree
   - `visualize_merged_granularity.py` - Create merged scene graphs
   - `batch_sample_vg.py` - Batch processing pipeline

3. **Merging Algorithm**:
   - Group objects by concept name at each level
   - Merge bounding boxes (minimum enclosing rectangle)
   - Track compression ratios

4. **Purpose**:
   - Enable reasoning at multiple abstraction levels
   - Support compositional VQA (fine details + high-level scene)
   - Demonstrate hierarchical knowledge integration

---

## Quick Reference Commands

```bash
# Generate single sample with all visualizations
cd /home/jiachen/scratch/graph_reasoning/HCNMN/inspect

# Run merged granularity pipeline
conda run -n hcnmn python visualize_merged_granularity.py \
  --image_id 498202

# Run scene graph + hierarchy pipeline
conda run -n hcnmn python visualize_scene_graph_hierarchy.py \
  --image_id 498202

# Batch process 25 samples
conda run -n hcnmn python batch_sample_vg.py \
  --num_samples 25 \
  --seed 42
```

---

**Generated**: October 1, 2025
**Repository**: HCNMN - Hierarchical Cross-Modality Neural Module Network
**Paper**: "Toward Multi-Granularity Decision-Making: Explicit Visual Reasoning with Hierarchical Knowledge" (ICCV 2023)
