# Merged Multi-Granularity Scene Graph Report

## Image ID: 2349289

**Total Objects**: 14
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 14 | 7 | 2.00x |
| Mid | 14 | 6 | 2.33x |
| Coarse | 14 | 5 | 2.80x |

---

## Fine-Grained Merged Nodes

**Node Count**: 7

### cream
- **Merged Objects**: 3
- **Original Objects**: cream, cream, cream
- **Merged BBox**: x=108, y=47, w=323, h=166

### crumb
- **Merged Objects**: 2
- **Original Objects**: crumb, crumb
- **Merged BBox**: x=121, y=227, w=206, h=12

### dessert
- **Merged Objects**: 1
- **Original Objects**: dessert
- **Merged BBox**: x=98, y=31, w=341, h=197

### leaf
- **Merged Objects**: 5
- **Original Objects**: leaf, leaf, leaf, leaf, leaf
- **Merged BBox**: x=314, y=30, w=105, h=77

### leaves
- **Merged Objects**: 1
- **Original Objects**: leaves
- **Merged BBox**: x=312, y=32, w=106, h=75

### plate
- **Merged Objects**: 1
- **Original Objects**: plate
- **Merged BBox**: x=0, y=82, w=499, h=250

### sauce
- **Merged Objects**: 1
- **Original Objects**: sauce
- **Merged BBox**: x=78, y=206, w=347, h=101

---

## Mid-Grained Merged Nodes

**Node Count**: 6

### base
- **Merged Objects**: 1
- **Original Objects**: plate
- **Merged BBox**: x=0, y=82, w=499, h=250

### condiment
- **Merged Objects**: 1
- **Original Objects**: sauce
- **Merged BBox**: x=78, y=206, w=347, h=101

### course
- **Merged Objects**: 1
- **Original Objects**: dessert
- **Merged BBox**: x=98, y=31, w=341, h=197

### elite
- **Merged Objects**: 3
- **Original Objects**: cream, cream, cream
- **Merged BBox**: x=108, y=47, w=323, h=166

### plant organ
- **Merged Objects**: 6
- **Original Objects**: leaves, leaf, leaf, leaf, leaf, leaf
- **Merged BBox**: x=312, y=30, w=107, h=77

### small indefinite quantity
- **Merged Objects**: 2
- **Original Objects**: crumb, crumb
- **Merged BBox**: x=121, y=227, w=206, h=12

---

## Coarse-Grained Merged Nodes

**Node Count**: 5

### artifact
- **Merged Objects**: 1
- **Original Objects**: plate
- **Merged BBox**: x=0, y=82, w=499, h=250

### class
- **Merged Objects**: 3
- **Original Objects**: cream, cream, cream
- **Merged BBox**: x=108, y=47, w=323, h=166

### food
- **Merged Objects**: 2
- **Original Objects**: dessert, sauce
- **Merged BBox**: x=78, y=31, w=361, h=276

### natural object
- **Merged Objects**: 6
- **Original Objects**: leaves, leaf, leaf, leaf, leaf, leaf
- **Merged BBox**: x=312, y=30, w=107, h=77

### small indefinite quantity
- **Merged Objects**: 2
- **Original Objects**: crumb, crumb
- **Merged BBox**: x=121, y=227, w=206, h=12

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v5/sample_2349289
