# Merged Multi-Granularity Scene Graph Report

## Image ID: 2339206

**Total Objects**: 11
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 11 | 11 | 1.00x |
| Mid | 11 | 7 | 1.57x |
| Coarse | 11 | 7 | 1.57x |

---

## Fine-Grained Merged Nodes

**Node Count**: 11

### bank
- **Merged Objects**: 1
- **Original Objects**: bank
- **Merged BBox**: x=205, y=222, w=292, h=153

### bear
- **Merged Objects**: 1
- **Original Objects**: bear
- **Merged BBox**: x=58, y=222, w=85, h=123

### hill
- **Merged Objects**: 1
- **Original Objects**: hill
- **Merged BBox**: x=1, y=2, w=497, h=209

### knot
- **Merged Objects**: 1
- **Original Objects**: knot
- **Merged BBox**: x=277, y=185, w=14, h=13

### log
- **Merged Objects**: 1
- **Original Objects**: log
- **Merged BBox**: x=0, y=320, w=286, h=52

### mouth
- **Merged Objects**: 1
- **Original Objects**: mouth
- **Merged BBox**: x=118, y=308, w=13, h=12

### paw
- **Merged Objects**: 1
- **Original Objects**: paw
- **Merged BBox**: x=87, y=331, w=20, h=17

### rock
- **Merged Objects**: 1
- **Original Objects**: rock
- **Merged BBox**: x=233, y=90, w=45, h=38

### stump
- **Merged Objects**: 1
- **Original Objects**: stump
- **Merged BBox**: x=0, y=89, w=462, h=151

### tree
- **Merged Objects**: 1
- **Original Objects**: tree
- **Merged BBox**: x=251, y=0, w=22, h=83

### water
- **Merged Objects**: 1
- **Original Objects**: water
- **Merged BBox**: x=0, y=281, w=269, h=87

---

## Mid-Grained Merged Nodes

**Node Count**: 7

### animal
- **Merged Objects**: 1
- **Original Objects**: bear
- **Merged BBox**: x=58, y=222, w=85, h=123

### body_part
- **Merged Objects**: 1
- **Original Objects**: paw
- **Merged BBox**: x=87, y=331, w=20, h=17

### building
- **Merged Objects**: 1
- **Original Objects**: mouth
- **Merged BBox**: x=118, y=308, w=13, h=12

### bunch
- **Merged Objects**: 1
- **Original Objects**: knot
- **Merged BBox**: x=277, y=185, w=14, h=13

### material
- **Merged Objects**: 1
- **Original Objects**: log
- **Merged BBox**: x=0, y=320, w=286, h=52

### nature
- **Merged Objects**: 5
- **Original Objects**: stump, water, bank, rock, hill
- **Merged BBox**: x=0, y=2, w=498, h=373

### plant
- **Merged Objects**: 1
- **Original Objects**: tree
- **Merged BBox**: x=251, y=0, w=22, h=83

---

## Coarse-Grained Merged Nodes

**Node Count**: 7

### agglomeration
- **Merged Objects**: 1
- **Original Objects**: knot
- **Merged BBox**: x=277, y=185, w=14, h=13

### body part
- **Merged Objects**: 2
- **Original Objects**: paw, mouth
- **Merged BBox**: x=87, y=308, w=44, h=40

### living thing
- **Merged Objects**: 2
- **Original Objects**: bear, tree
- **Merged BBox**: x=58, y=0, w=215, h=345

### natural elevation
- **Merged Objects**: 1
- **Original Objects**: hill
- **Merged BBox**: x=1, y=2, w=497, h=209

### natural object
- **Merged Objects**: 2
- **Original Objects**: stump, rock
- **Merged BBox**: x=0, y=89, w=462, h=151

### slope
- **Merged Objects**: 1
- **Original Objects**: bank
- **Merged BBox**: x=205, y=222, w=292, h=153

### substance
- **Merged Objects**: 2
- **Original Objects**: log, water
- **Merged BBox**: x=0, y=281, w=286, h=91

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v6.1/sample_2339206
