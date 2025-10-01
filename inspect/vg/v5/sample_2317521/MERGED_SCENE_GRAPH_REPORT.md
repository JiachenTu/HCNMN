# Merged Multi-Granularity Scene Graph Report

## Image ID: 2317521

**Total Objects**: 10
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 10 | 6 | 1.67x |
| Mid | 10 | 6 | 1.67x |
| Coarse | 10 | 4 | 2.50x |

---

## Fine-Grained Merged Nodes

**Node Count**: 6

### brick
- **Merged Objects**: 1
- **Original Objects**: brick
- **Merged BBox**: x=28, y=23, w=197, h=72

### cheese
- **Merged Objects**: 2
- **Original Objects**: cheese, cheese
- **Merged BBox**: x=69, y=118, w=430, h=145

### cheese/pizza
- **Merged Objects**: 1
- **Original Objects**: cheese/pizza
- **Merged BBox**: x=178, y=180, w=317, h=94

### cloth
- **Merged Objects**: 1
- **Original Objects**: cloth
- **Merged BBox**: x=1, y=94, w=497, h=235

### pizza
- **Merged Objects**: 4
- **Original Objects**: pizza, pizza, pizza, pizza
- **Merged BBox**: x=31, y=81, w=468, h=244

### table
- **Merged Objects**: 1
- **Original Objects**: table
- **Merged BBox**: x=0, y=100, w=498, h=231

---

## Mid-Grained Merged Nodes

**Node Count**: 6

### array
- **Merged Objects**: 1
- **Original Objects**: table
- **Merged BBox**: x=0, y=100, w=498, h=231

### artifact
- **Merged Objects**: 1
- **Original Objects**: cloth
- **Merged BBox**: x=1, y=94, w=497, h=235

### building material
- **Merged Objects**: 1
- **Original Objects**: brick
- **Merged BBox**: x=28, y=23, w=197, h=72

### cheese/pizza
- **Merged Objects**: 1
- **Original Objects**: cheese/pizza
- **Merged BBox**: x=178, y=180, w=317, h=94

### dish
- **Merged Objects**: 4
- **Original Objects**: pizza, pizza, pizza, pizza
- **Merged BBox**: x=31, y=81, w=468, h=244

### food
- **Merged Objects**: 2
- **Original Objects**: cheese, cheese
- **Merged BBox**: x=69, y=118, w=430, h=145

---

## Coarse-Grained Merged Nodes

**Node Count**: 4

### array
- **Merged Objects**: 1
- **Original Objects**: table
- **Merged BBox**: x=0, y=100, w=498, h=231

### artifact
- **Merged Objects**: 2
- **Original Objects**: cloth, brick
- **Merged BBox**: x=1, y=23, w=497, h=306

### cheese/pizza
- **Merged Objects**: 1
- **Original Objects**: cheese/pizza
- **Merged BBox**: x=178, y=180, w=317, h=94

### food
- **Merged Objects**: 6
- **Original Objects**: pizza, pizza, cheese, cheese, pizza, pizza
- **Merged BBox**: x=31, y=81, w=468, h=244

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v5/sample_2317521
