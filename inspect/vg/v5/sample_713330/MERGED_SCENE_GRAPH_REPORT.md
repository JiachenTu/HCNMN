# Merged Multi-Granularity Scene Graph Report

## Image ID: 713330

**Total Objects**: 24
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 24 | 5 | 4.80x |
| Mid | 24 | 3 | 8.00x |
| Coarse | 24 | 1 | 24.00x |

---

## Fine-Grained Merged Nodes

**Node Count**: 5

### key
- **Merged Objects**: 12
- **Original Objects**: key, key, key, key, key, key, key, key, key, key (+2 more)
- **Merged BBox**: x=402, y=562, w=360, h=72

### keyboard
- **Merged Objects**: 8
- **Original Objects**: keyboard, keyboard, keyboard, keyboard, keyboard, keyboard, keyboard, keyboard
- **Merged BBox**: x=269, y=532, w=545, h=148

### keys
- **Merged Objects**: 2
- **Original Objects**: keys, keys
- **Merged BBox**: x=356, y=562, w=95, h=61

### screen
- **Merged Objects**: 1
- **Original Objects**: screen
- **Merged BBox**: x=356, y=156, w=301, h=245

### walls
- **Merged Objects**: 1
- **Original Objects**: walls
- **Merged BBox**: x=5, y=11, w=1014, h=402

---

## Mid-Grained Merged Nodes

**Node Count**: 3

### device
- **Merged Objects**: 22
- **Original Objects**: key, keyboard, keyboard, key, key, keyboard, key, keyboard, key, key (+12 more)
- **Merged BBox**: x=269, y=532, w=545, h=148

### partition
- **Merged Objects**: 1
- **Original Objects**: walls
- **Merged BBox**: x=5, y=11, w=1014, h=402

### surface
- **Merged Objects**: 1
- **Original Objects**: screen
- **Merged BBox**: x=356, y=156, w=301, h=245

---

## Coarse-Grained Merged Nodes

**Node Count**: 1

### artifact
- **Merged Objects**: 24
- **Original Objects**: key, keyboard, keyboard, key, key, keyboard, key, keyboard, key, key (+14 more)
- **Merged BBox**: x=5, y=11, w=1014, h=669

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v5/sample_713330
