# Multi-Granularity Hierarchical Ontology Visualization

## Image ID: 2337701

**Scene Type**: Visual Genome Image 2337701
**Total Objects**: 15
**Total Relationships**: 12
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Executive Summary

This document presents a **multi-granularity hierarchical ontology** constructed from Visual Genome annotations. The ontology organizes 15 objects into 34 concepts across 3 levels of abstraction.

**Key Statistics**:
- **Fine-grained**: 12 specific concepts
- **Mid-level**: 12 category concepts
- **Coarse-grained**: 10 high-level concepts
- **Expansion ratio**: 2.3x

---

## Visualization Overview

### 1. **Single-Granularity Overlays**

Each visualization shows objects grouped and labeled by their concept at a specific granularity level:

#### Fine-Grained Overlay (`granularity_fine.png`)
- **Concept Count**: 12 unique concepts
- **Abstraction Level**: Specific objects as they appear in the scene
- **Examples**: bird, dirt, ground, head, pebble...
- **Use Case**: "Is there a seagull?" (specific object queries)

**Visual Features**:
- Green color theme
- Each unique object type has its own color
- Bounding boxes show exact object locations
- Labels show specific object names

---

#### Mid-Level Overlay (`granularity_mid.png`)
- **Concept Count**: 12 unique concepts
- **Abstraction Level**: Category-level groupings
- **Examples**: ammunition, earth, external body part, larid, object...
- **Use Case**: "Is there a bird?" (category queries)

**Visual Features**:
- Blue color theme
- Objects grouped by category (e.g., all birds same color)
- Shows semantic relationships between objects
- Labels show category names

---

#### Coarse-Grained Overlay (`granularity_coarse.png`)
- **Concept Count**: 10 unique concepts
- **Abstraction Level**: High-level abstract groupings
- **Examples**: body part, chordate, coastal diving bird, earth, material...
- **Use Case**: "Are there living things?" (abstract queries)

**Visual Features**:
- Red color theme
- Broad groupings (e.g., all animals, all materials)
- Shows high-level scene composition
- Labels show abstract concept names

---

### 2. **Multi-Granularity Comparison** (`multi_granularity_comparison.png`)

Side-by-side view of all three granularity levels on the same image.

**Purpose**: Compare how objects are grouped differently at each abstraction level

**Key Observations**:
- **Fine → Mid**: Objects merge into categories
- **Mid → Coarse**: Categories merge into high-level groups
- **Concept Reduction**: 12 → 12 → 10

---

### 3. **Hierarchical Graph Overlay** (`hierarchical_graph_overlay.png`)

Combined visualization showing:
- **Top**: Original image with all objects labeled
- **Bottom Left**: Concept network at fine-grained level
- **Bottom Right**: Hierarchical tree structure

**Purpose**: Show both spatial layout (image) and taxonomic structure (tree)

---

## Hierarchical Structure Details

### Complete Hierarchy

```
Fine-Grained → Mid-Level → Coarse-Grained
───────────────────────────────────────────

### Example Concept Paths

```
wood            : wood → plant material → material
wing            : wing → organ → body part
seagull         : seagull → larid → coastal diving bird
shells          : shells → ammunition → weaponry
dirt            : dirt → earth → material
wood edges      : wood edges
bird            : bird → vertebrate → chordate
piece           : piece → part → object
```

### Concepts by Granularity Level

#### Fine-Grained (Specific Objects)
**Count**: 12 concepts

```
bird, dirt, ground, head, pebble, piece, sand, seagull, shells, wing, wood, wood edges
```

#### Mid-Level (Categories)
**Count**: 12 concepts

```
ammunition, earth, external body part, larid, object, organ, part, plant material, rock, soil, vertebrate, wood edges
```

#### Coarse-Grained (High-Level Groups)
**Count**: 10 concepts

```
body part, chordate, coastal diving bird, earth, material, natural object, object, physical entity, weaponry, wood edges
```

---

## Multi-Granularity Reasoning Examples

### Example 1: Fine-Grained Query
**Question**: "Is there a seagull in the image?"

**Reasoning**:
1. Query at fine-grained level (L0)
2. Search for exact match: "seagull"
3. Check if present in image
4. **Answer**: Based on object detection

**Applicable to**: Specific object identification tasks

---

### Example 2: Mid-Level Query
**Question**: "Is there a bird in the image?"

**Reasoning**:
1. Query at mid-level (L1)
2. Search for category: "bird", "vertebrate", "larid"
3. OR traverse from fine: "seagull" → parent category
4. **Answer**: Based on category membership

**Applicable to**: Category-level recognition tasks

---

### Example 3: Coarse-Grained Query
**Question**: "Are there living things in the image?"

**Reasoning**:
1. Query at coarse level (L2)
2. Search for high-level groups: "chordate", "organism"
3. Traverse from mid: "vertebrate" → "chordate"
4. **Answer**: Based on abstract grouping

**Applicable to**: Scene understanding and high-level reasoning

---

### Example 4: Cross-Granularity Query
**Question**: "What type of bird is it?"

**Reasoning**:
1. Start at mid-level: Identify "bird" category
2. Traverse DOWN to fine-grained level
3. Find specific instances: "seagull", "pigeon", etc.
4. **Answer**: Most specific concept available

**Applicable to**: Fine-grained classification within categories

---

## Visualization Legend

### Color Coding

| Granularity | Color | Hex Code | Represents |
|-------------|-------|----------|------------|
| Fine-grained | 🟢 Green | #2ecc71 | Specific objects |
| Mid-level | 🔵 Blue | #3498db | Categories |
| Coarse-grained | 🔴 Red | #e74c3c | High-level groups |

### Bounding Box Interpretation

- **Solid colored boxes**: Objects grouped by their concept at the displayed granularity
- **Same color = Same concept**: Objects with the same color belong to the same concept group
- **Label position**: Above bounding box shows concept name (not object name)

### Legend (in each image)

- **Top right**: Shows mapping between colors and concepts
- **Limited to 15 entries**: For readability (full list in this document)

---

## Technical Details

### Ontology Construction Method

1. **Input**: Visual Genome object annotations with names and synsets
2. **WordNet Traversal**: For each object, traverse hypernym hierarchy up to 2 levels
3. **Deduplication**: Remove redundant concepts and synonyms
4. **Categorization**: Organize into fine/mid/coarse levels based on abstraction

### Hierarchy Traversal Algorithm

```python
def build_hierarchy(object_name):
    synset = wordnet.synsets(object_name)[0]  # First sense

    fine = object_name                        # L0: Original
    mid = synset.hypernyms()[0].name()       # L1: Parent
    coarse = mid.hypernyms()[0].name()       # L2: Grandparent

    return [fine, mid, coarse]
```

### Advantages of 3-Level Structure

✅ **Balanced**: Even distribution of concepts across levels
✅ **Meaningful**: Each level has clear semantic purpose
✅ **Efficient**: Fast traversal (max 2 hops)
✅ **Interpretable**: Easy to understand and visualize
✅ **Practical**: Directly usable for model training

---

## Usage Guidelines

### For Visual Question Answering (VQA)

1. **Encode question** to determine required granularity
   - "What is this?" → Fine-grained
   - "What kind of...?" → Mid-level
   - "Is there any...?" → Coarse-grained

2. **Query appropriate level** of hierarchy

3. **Use spatial information** from bounding boxes for location queries

### For Scene Understanding

1. **Start at coarse level**: Get high-level scene composition
2. **Drill down** to mid-level for categories
3. **Refine** to fine-grained for specific objects

### For Object Detection

1. **Train at multiple levels**: Use all 3 granularities
2. **Coarse → Fine**: Hierarchical detection pipeline
3. **Benefit**: Better generalization across abstraction levels

---

## Files Generated

### Visualizations
```
granularity_fine.png              - Fine-grained overlay
granularity_mid.png               - Mid-level overlay
granularity_coarse.png            - Coarse-grained overlay
multi_granularity_comparison.png  - All 3 side-by-side
hierarchical_graph_overlay.png    - Image + network + tree
```

### Data Files
```
ontology_data.json                - Complete hierarchy data
VISUALIZATION_REPORT.md           - This document
```

---

## Comparison to Alternative Approaches

### vs. Flat Object List
❌ **Flat**: No abstraction, only specific objects
✅ **Hierarchical**: Multiple levels of reasoning

### vs. Deep WordNet Tree (14 levels)
❌ **Deep**: Too many abstract concepts (467 total)
✅ **3-Level**: Only meaningful concepts (30-75 total)

### vs. Single Granularity
❌ **Single**: Fixed abstraction level
✅ **Multi**: Flexible reasoning at any level

---

## Conclusion

This multi-granularity hierarchical ontology provides:

✅ **3 levels** of abstraction (fine/mid/coarse)
✅ **{statistics['total_concepts']} concepts** (clean, no bloat)
✅ **Visual overlays** showing groupings at each level
✅ **Clear hierarchy** with example paths
✅ **Practical structure** for VQA and scene understanding

The visualizations demonstrate how the same scene can be understood at different levels of abstraction, enabling flexible multi-granularity reasoning.

---

**Generated**: {output_path}
**Image ID**: {image_id}
**Total Concepts**: {statistics['total_concepts']}
