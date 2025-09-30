# Merged Multi-Granularity Scene Graph Report

## Image ID: 107920

**Total Objects**: 6
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 6 | 2 | 3.00x |
| Mid | 6 | 2 | 3.00x |
| Coarse | 6 | 2 | 3.00x |

---

## Fine-Grained Merged Nodes

**Node Count**: 2

### hill
- **Merged Objects**: 1
- **Original Objects**: hill
- **Merged BBox**: x=2, y=34, w=1016, h=305

### tree
- **Merged Objects**: 5
- **Original Objects**: tree, tree, tree, tree, tree
- **Merged BBox**: x=185, y=1, w=677, h=369

---

## Mid-Grained Merged Nodes

**Node Count**: 2

### natural elevation
- **Merged Objects**: 1
- **Original Objects**: hill
- **Merged BBox**: x=2, y=34, w=1016, h=305

### woody plant
- **Merged Objects**: 5
- **Original Objects**: tree, tree, tree, tree, tree
- **Merged BBox**: x=185, y=1, w=677, h=369

---

## Coarse-Grained Merged Nodes

**Node Count**: 2

### geological formation
- **Merged Objects**: 1
- **Original Objects**: hill
- **Merged BBox**: x=2, y=34, w=1016, h=305

### vascular plant
- **Merged Objects**: 5
- **Original Objects**: tree, tree, tree, tree, tree
- **Merged BBox**: x=185, y=1, w=677, h=369

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: vg/sample_107920
