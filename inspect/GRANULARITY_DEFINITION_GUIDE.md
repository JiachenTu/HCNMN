# Multi-Granularity Concept Hierarchy: Complete Definition Guide

**Version**: v6.1/v6.2
**Last Updated**: 2025-10-03

---

## Overview

The HCNMN system uses a **3-level hierarchical concept taxonomy** to enable multi-granularity visual reasoning:

1. **Fine-Grained (L0)**: Specific objects from Visual Genome annotations
2. **Mid-Level (L1)**: Semantic categories via custom keyword matching
3. **Coarse-Grained (L2)**: High-level domains via WordNet depth-based traversal

This guide provides complete implementation details with code examples from the actual codebase.

---

## Level 0: Fine-Grained Concepts

### Definition

**Original object names from Visual Genome annotations** with no transformation or abstraction.

### Code Implementation

**Location**: `visualize_scene_graph_hierarchy.py:147-152`

```python
for obj_name in unique_objects:
    # Add to fine-grained level - NO TRANSFORMATION
    hierarchy['fine'].append(obj_name)
    object_to_levels[obj_name] = {'fine': obj_name}
```

### Characteristics

- **Direct mapping**: Object name from VG → Fine concept (identity function)
- **No WordNet lookup**: Uses raw annotation strings
- **Example**: VG object "clock" → Fine concept "clock"

### Examples from Image 498335

| VG Object | Fine Concept | Notes |
|-----------|--------------|-------|
| clock | clock | No change |
| pot | pot | No change |
| letter | letter | No change |
| flower | flower | No change |
| flowers | flowers | Different from "flower" |
| sign | sign | No change |
| street | street | No change |

### When Objects Have No WordNet Entry

If an object has no WordNet synset, it remains at all 3 levels:

```python
synsets = wn.synsets(obj_clean)
if not synsets:
    # Use object name for ALL levels
    hierarchy['mid'].append(obj_name)      # Same as fine
    hierarchy['coarse'].append(obj_name)   # Same as fine
    object_to_levels[obj_name] = {
        'fine': obj_name,
        'mid': obj_name,
        'coarse': obj_name
    }
```

---

## Level 1: Mid-Level Semantic Categories

### Definition

**Semantic categories** determined by matching WordNet hypernym paths against **predefined keyword lists**.

This is the **key innovation** in v6.1 that improved Fine→Mid compression from 1.06x (v6.0) to **1.54x** (v6.1).

### The 13 Semantic Categories

**Location**: `visualize_scene_graph_hierarchy.py:69-83`

```python
SEMANTIC_CATEGORIES = {
    'person': [
        'person', 'adult', 'child', 'juvenile', 'human',
        'man', 'woman', 'organism', 'people'
    ],
    'animal': [
        'animal', 'mammal', 'bird', 'fish', 'reptile',
        'insect', 'fauna', 'domestic_animal', 'ruminant'
    ],
    'plant': [
        'plant', 'tree', 'woody_plant', 'vascular_plant',
        'angiosperm', 'flora', 'herb', 'gramineous_plant'
    ],
    'vehicle': [
        'vehicle', 'motor_vehicle', 'conveyance',
        'wheeled_vehicle', 'craft', 'public_transport'
    ],
    'building': [
        'building', 'structure', 'construction',
        'edifice', 'housing'
    ],
    'furniture': [
        'furniture', 'furnishing', 'table', 'seat',
        'bed', 'supporting_structure'
    ],
    'body_part': [
        'body_part', 'external_body_part', 'organ',
        'limb', 'extremity', 'process'
    ],
    'clothing': [
        'clothing', 'garment', 'wear', 'attire',
        'footwear', 'armor_plate'
    ],
    'food': [
        'food', 'foodstuff', 'nutrient', 'dish', 'produce'
    ],
    'tool': [
        'tool', 'implement', 'instrument', 'device',
        'equipment', 'instrumentality', 'machine'
    ],
    'nature': [
        'sky', 'cloud', 'water', 'ground', 'land',
        'geological_formation', 'natural_object', 'soil', 'earth'
    ],
    'material': [
        'material', 'substance', 'matter', 'solid', 'liquid', 'gas'
    ],
    'text': [
        'writing', 'text', 'document', 'sign', 'symbol',
        'trademark', 'representation'
    ]
}
```

### Algorithm: Semantic Category Matching

**Location**: `visualize_scene_graph_hierarchy.py:86-109`

**Step 1**: Get all hypernyms from object to WordNet root

```python
def get_semantic_mid_level(synset):
    # Get all hypernyms in the path to root
    paths = synset.hypernym_paths()
    if not paths:
        return synset.name().split('.')[0].replace('_', ' ')

    # Use longest path (most specific)
    longest_path = max(paths, key=len)

    # Extract synset names from path
    hypernym_names = [s.name().split('.')[0] for s in longest_path]
```

**Example for "clock"**:
```
hypernym_names = [
    'entity',           # Root (depth 0)
    'physical_entity',  # depth 1
    'object',           # depth 2
    'whole',            # depth 3
    'artifact',         # depth 4
    'instrumentality',  # depth 5
    'device',           # depth 6
    'instrument',       # depth 7
    'measuring_instrument',  # depth 8
    'timepiece',        # depth 9
    'clock'             # Leaf (depth 10)
]
```

**Step 2**: Match against semantic categories (most specific first)

```python
    # Match from MOST SPECIFIC to MOST GENERAL
    for hypernym in reversed(hypernym_names):  # Start from 'clock', go to 'entity'
        for category, keywords in SEMANTIC_CATEGORIES.items():
            if hypernym in keywords:
                return category  # Return FIRST match
```

**For "clock"**:
- Check `clock` → Not in any keyword list
- Check `timepiece` → Not in any keyword list
- Check `measuring_instrument` → Not in any keyword list
- Check `instrument` → Not in any keyword list
- Check `device` → **Found in `'tool'` keywords!** ✅
- **Return**: `"tool"`

**Step 3**: Fallback if no category matches

```python
    # Fallback: Use 1-hop WordNet hypernym
    if synset.hypernyms():
        return synset.hypernyms()[0].name().split('.')[0].replace('_', ' ')

    # Last resort: Use the object name itself
    return synset.name().split('.')[0].replace('_', ' ')
```

### Why Semantic Categories Work Better Than WordNet Hops

**Problem with pure WordNet traversal**:

Different objects with similar semantics end up at different mid-levels:

| Object | 1-hop WordNet | 2-hop WordNet | Result |
|--------|---------------|---------------|--------|
| car | motor_vehicle | self-propelled_vehicle | ❌ Don't merge |
| truck | motor_vehicle | self-propelled_vehicle | ❌ Don't merge |
| bus | public_transport | conveyance | ❌ DIFFERENT! |
| bike | wheeled_vehicle | vehicle | ❌ DIFFERENT! |

**Solution with semantic categories**:

All match against `'vehicle'` keyword list:

| Object | WordNet Path Contains | Semantic Category |
|--------|----------------------|-------------------|
| car | "motor_vehicle" | ✅ **vehicle** |
| truck | "motor_vehicle" | ✅ **vehicle** |
| bus | "public_transport" | ✅ **vehicle** |
| bike | "wheeled_vehicle" | ✅ **vehicle** |

**Result**: All 4 objects merge to same mid-level → Better compression!

### Mid-Level Assignment Examples (Image 498335)

| Fine Object | WordNet Path (partial) | Matched Keyword | Mid Category |
|-------------|------------------------|-----------------|--------------|
| clock | ...→ instrumentality → device → ... | device | **tool** |
| pot | ...→ instrumentality → implement → ... | implement | **tool** |
| pole | ...→ instrumentality → ... | instrumentality | **tool** |
| letter | ...→ writing → text → document → ... | text | **text** |
| sign | ...→ sign → symbol → ... | sign | **text** |
| flower | ...→ plant → ... | plant | **plant** |
| balcony | ...→ building → structure → ... | building | **building** |
| railing | ...→ structure → ... | structure | **building** |
| face | ...→ body_part → ... | body_part | **body_part** |

---

## Level 2: Coarse-Grained Concepts

### Definition

**WordNet hypernym at depth 4 from root** (with fallbacks to depths 3, 5, 6 if path is too short).

This provides high-level domain classification: `artifact`, `living_thing`, `substance`, etc.

### Code Implementation

**Location**: `visualize_scene_graph_hierarchy.py:179-200`

**Step 1**: Try depth-based traversal (prefer depth 4)

```python
# Coarse-level: depth 3-5 from root for better merging
coarse_synset = None
for depth in [4, 3, 5, 6]:  # Try in order of preference
    coarse_synset = get_hypernym_at_depth_from_root(synset, depth)
    if coarse_synset:
        break  # Use first successful depth
```

**Step 2**: Extract synset at target depth

```python
def get_hypernym_at_depth_from_root(synset, target_depth):
    """Get hypernym at specific depth from root."""
    paths = synset.hypernym_paths()
    if not paths:
        return None

    # Use longest path (most specific)
    longest_path = max(paths, key=len)

    # Check if path is long enough
    if len(longest_path) <= target_depth:
        return None  # Path too short

    # Return synset at target depth from root
    # longest_path[0] = root ('entity.n.01')
    # longest_path[1] = depth 1
    # longest_path[target_depth] = depth 'target_depth'
    return longest_path[target_depth]
```

**Example for "clock"**:

```python
# Path: [entity, physical_entity, object, whole, artifact, instrumentality, ...]
# Length: 11

# Try depth 4:
longest_path = [entity, physical_entity, object, whole, artifact, ...]
coarse_synset = longest_path[4]  # = artifact ✅
```

**Step 3**: Convert to string and add to hierarchy

```python
if coarse_synset:
    coarse_name = coarse_synset.name().split('.')[0].replace('_', ' ')
    # coarse_name = "artifact"

    if coarse_name not in hierarchy['coarse']:
        hierarchy['coarse'].append(coarse_name)
    object_to_levels[obj_name]['coarse'] = coarse_name
```

**Step 4**: Fallback if path too short

```python
else:
    # Use mid-level as coarse if path too short
    mid_name = object_to_levels[obj_name].get('mid', obj_name)
    if mid_name not in hierarchy['coarse']:
        hierarchy['coarse'].append(mid_name)
    object_to_levels[obj_name]['coarse'] = mid_name
```

### Why Depth 4?

**Empirical analysis** (from v6.2 WordNet path analysis) shows:

- Depth 0: `entity` (100% of objects - useless)
- Depth 1: `physical_entity`, `abstraction` (2 categories - still too general)
- Depth 2: `object`, `communication` (6 categories - getting better)
- Depth 3: `whole`, `part`, `location` (11 categories - moderate)
- **Depth 4**: `artifact`, `living_thing`, `substance` (9-12 categories - ✅ OPTIMAL)
- Depth 5: Too specific, poor compression

**Merge statistics** (Image 498335):
- Depth 4 `artifact` merges **9 objects** (clock, pot, street, letter, balcony, railing, billboard, pole, stairs)
- Depth 4 `living_thing` merges **2 objects** (flower, flowers)
- Average compression: **2.0x** (18 fine → 9 coarse)

### Coarse-Level Assignment Examples (Image 498335)

| Fine | Mid | WordNet Depth 4 | Coarse |
|------|-----|-----------------|--------|
| clock | tool | artifact | **artifact** |
| pot | tool | artifact | **artifact** |
| pole | tool | artifact | **artifact** |
| street | thoroughfare | artifact | **artifact** |
| letter | text | artifact | **artifact** |
| balcony | building | artifact | **artifact** |
| railing | building | artifact | **artifact** |
| billboard | building | artifact | **artifact** |
| stairs | stairway | artifact | **artifact** |
| flower | plant | living_thing | **living_thing** |
| flowers | plant | living_thing | **living_thing** |
| face | body_part | body_part | **body part** (too short) |
| sign | text | evidence | **evidence** (depth 4) |

---

## Complete Example: "clock"

### Full Hierarchy Traversal

```
VG Annotation: "clock"
│
├─ FINE LEVEL (L0)
│  └─ "clock" (no transformation)
│
├─ MID LEVEL (L1)
│  ├─ Get WordNet synset: clock.n.01
│  ├─ Get hypernym path to root:
│  │  [entity, physical_entity, object, whole, artifact,
│  │   instrumentality, device, instrument, measuring_instrument,
│  │   timepiece, clock]
│  ├─ Check each hypernym against semantic categories:
│  │  - clock: not in keywords
│  │  - timepiece: not in keywords
│  │  - measuring_instrument: not in keywords
│  │  - instrument: not in keywords
│  │  - device: FOUND in 'tool' keywords ✅
│  └─ Mid = "tool"
│
└─ COARSE LEVEL (L2)
   ├─ Try depth 4 from root:
   │  - Path length: 11 (✓ long enough)
   │  - longest_path[4] = artifact
   └─ Coarse = "artifact"

Final Mapping:
  Fine: "clock"
  Mid: "tool"
  Coarse: "artifact"
```

---

## Decision Tree Flowchart

```
Start: VG Object "X"
│
├─ [FINE LEVEL]
│  └─ Fine = X (always)
│
├─ [MID LEVEL]
│  ├─ Does X have WordNet synset?
│  │  ├─ NO → Mid = X (fallback)
│  │  └─ YES ↓
│  ├─ Get hypernym path to root
│  ├─ For each hypernym (from leaf to root):
│  │  ├─ Is hypernym in any SEMANTIC_CATEGORIES keyword list?
│  │  │  ├─ YES → Mid = category name ✅
│  │  │  └─ NO → Continue to next hypernym
│  │  └─ All checked, none matched?
│  │     ├─ Has 1-hop hypernym? → Mid = hypernym name
│  │     └─ No hypernym → Mid = X
│
└─ [COARSE LEVEL]
   ├─ Does X have WordNet synset?
   │  ├─ NO → Coarse = X (fallback)
   │  └─ YES ↓
   ├─ Try depth 4:
   │  ├─ Path long enough? → Coarse = synset at depth 4 ✅
   │  └─ Path too short? ↓
   ├─ Try depth 3:
   │  ├─ Path long enough? → Coarse = synset at depth 3
   │  └─ Path too short? ↓
   ├─ Try depths 5, 6:
   │  ├─ Path long enough? → Coarse = synset at that depth
   │  └─ All too short → Coarse = Mid (fallback)
```

---

## Comparison Table: V5 vs V6 vs V6.1

| Feature | V5 (1-hop) | V6 (2-3 hop) | V6.1 (Semantic) |
|---------|-----------|--------------|-----------------|
| **Fine** | VG object | VG object | VG object |
| **Mid** | 1-hop WordNet | 2-hop WordNet | **Semantic categories** |
| **Coarse** | 2-hop WordNet | Depth 4 | Depth 4 |
| **F→M Compression** | 1.09x | 1.06x ❌ | **1.54x** ✅ |
| **F→C Compression** | 2.33x | 1.95x | 1.95x |
| **Mid Concepts** | Too specific | Even worse | Meaningful categories |
| **Issue** | Poor merging | Worse merging | **Solved!** ✅ |

---

## Code Locations Quick Reference

| Component | File | Lines |
|-----------|------|-------|
| Semantic categories | `visualize_scene_graph_hierarchy.py` | 69-83 |
| Mid-level assignment | `visualize_scene_graph_hierarchy.py` | 86-109 |
| Coarse depth traversal | `visualize_scene_graph_hierarchy.py` | 51-65, 179-200 |
| Complete hierarchy builder | `visualize_scene_graph_hierarchy.py` | 112-212 |
| WordNet path extraction | `visualize_wordnet_paths.py` | 15-50 |
| Depth analysis | `visualize_wordnet_paths.py` | 53-95 |

---

## Summary

### Fine-Grained (L0)
- **What**: Original VG object names
- **How**: Identity mapping (no transformation)
- **Code**: `hierarchy['fine'].append(obj_name)`

### Mid-Level (L1)
- **What**: Semantic categories via keyword matching
- **How**: Match WordNet hypernyms against 13 predefined categories
- **Code**: `get_semantic_mid_level(synset)` with `SEMANTIC_CATEGORIES`
- **Key Innovation**: v6.1 improvement (1.06x → 1.54x compression)

### Coarse-Grained (L2)
- **What**: High-level domains at WordNet depth 4
- **How**: Index into hypernym path at depth 4 (with fallbacks)
- **Code**: `get_hypernym_at_depth_from_root(synset, depth=4)`
- **Validation**: v6.2 WordNet path analysis confirms depth 4 is optimal

---

**For visualization of concept merging**, see:
- `merged_concepts_flow.png` (Sankey diagram)
- `concept_hierarchy_table.png` (Table view)
- `compression_analysis.png` (Statistics)

**For detailed path analysis**, see:
- `wordnet_paths_tree.png` (Complete WordNet paths)
- `WORDNET_ANALYSIS_REPORT.md` (Depth statistics)
