# Merged Multi-Granularity Scene Graph Report

## Image ID: 107980

**Total Objects**: 4
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 4 | 4 | 1.00x |
| Mid | 4 | 4 | 1.00x |
| Coarse | 4 | 4 | 1.00x |

---

## Fine-Grained Merged Nodes

**Node Count**: 4

### grass
- **Merged Objects**: 1
- **Original Objects**: grass
- **Merged BBox**: x=3, y=491, w=687, h=526

### sheep
- **Merged Objects**: 1
- **Original Objects**: sheep
- **Merged BBox**: x=5, y=478, w=658, h=236

### sky
- **Merged Objects**: 1
- **Original Objects**: sky
- **Merged BBox**: x=0, y=3, w=690, h=410

### trees
- **Merged Objects**: 1
- **Original Objects**: trees
- **Merged BBox**: x=5, y=147, w=686, h=346

---

## Mid-Grained Merged Nodes

**Node Count**: 4

### atmosphere
- **Merged Objects**: 1
- **Original Objects**: sky
- **Merged BBox**: x=0, y=3, w=690, h=410

### bovid
- **Merged Objects**: 1
- **Original Objects**: sheep
- **Merged BBox**: x=5, y=478, w=658, h=236

### gramineous plant
- **Merged Objects**: 1
- **Original Objects**: grass
- **Merged BBox**: x=3, y=491, w=687, h=526

### woody plant
- **Merged Objects**: 1
- **Original Objects**: trees
- **Merged BBox**: x=5, y=147, w=686, h=346

---

## Coarse-Grained Merged Nodes

**Node Count**: 4

### gas
- **Merged Objects**: 1
- **Original Objects**: sky
- **Merged BBox**: x=0, y=3, w=690, h=410

### herb
- **Merged Objects**: 1
- **Original Objects**: grass
- **Merged BBox**: x=3, y=491, w=687, h=526

### ruminant
- **Merged Objects**: 1
- **Original Objects**: sheep
- **Merged BBox**: x=5, y=478, w=658, h=236

### vascular plant
- **Merged Objects**: 1
- **Original Objects**: trees
- **Merged BBox**: x=5, y=147, w=686, h=346

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: vg/sample_107980
