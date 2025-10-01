# Merged Multi-Granularity Scene Graph Report

## Image ID: 2323145

**Total Objects**: 16
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 16 | 11 | 1.45x |
| Mid | 16 | 10 | 1.60x |
| Coarse | 16 | 7 | 2.29x |

---

## Fine-Grained Merged Nodes

**Node Count**: 11

### chin
- **Merged Objects**: 1
- **Original Objects**: chin
- **Merged BBox**: x=154, y=213, w=87, h=22

### dress
- **Merged Objects**: 1
- **Original Objects**: dress
- **Merged BBox**: x=77, y=236, w=320, h=132

### girl
- **Merged Objects**: 4
- **Original Objects**: girl, girl, girl, girl
- **Merged BBox**: x=18, y=36, w=466, h=320

### hand
- **Merged Objects**: 1
- **Original Objects**: hand
- **Merged BBox**: x=20, y=237, w=66, h=84

### mantle
- **Merged Objects**: 1
- **Original Objects**: mantle
- **Merged BBox**: x=280, y=312, w=218, h=55

### mouth
- **Merged Objects**: 2
- **Original Objects**: mouth, mouth
- **Merged BBox**: x=155, y=174, w=78, h=50

### neck/part
- **Merged Objects**: 1
- **Original Objects**: neck/part
- **Merged BBox**: x=204, y=245, w=47, h=13

### nose
- **Merged Objects**: 1
- **Original Objects**: nose
- **Merged BBox**: x=178, y=142, w=29, h=33

### open sign
- **Merged Objects**: 1
- **Original Objects**: open sign
- **Merged BBox**: x=128, y=22, w=205, h=239

### shirt
- **Merged Objects**: 2
- **Original Objects**: shirt, shirt
- **Merged BBox**: x=70, y=242, w=362, h=130

### smile
- **Merged Objects**: 1
- **Original Objects**: smile
- **Merged BBox**: x=176, y=185, w=51, h=26

---

## Mid-Grained Merged Nodes

**Node Count**: 10

### adult
- **Merged Objects**: 4
- **Original Objects**: girl, girl, girl, girl
- **Merged BBox**: x=18, y=36, w=466, h=320

### body part
- **Merged Objects**: 1
- **Original Objects**: chin
- **Merged BBox**: x=154, y=213, w=87, h=22

### clothing
- **Merged Objects**: 3
- **Original Objects**: shirt, shirt, dress
- **Merged BBox**: x=70, y=236, w=362, h=136

### external body part
- **Merged Objects**: 1
- **Original Objects**: hand
- **Merged BBox**: x=20, y=237, w=66, h=84

### gesture
- **Merged Objects**: 1
- **Original Objects**: smile
- **Merged BBox**: x=176, y=185, w=51, h=26

### neck/part
- **Merged Objects**: 1
- **Original Objects**: neck/part
- **Merged BBox**: x=204, y=245, w=47, h=13

### open sign
- **Merged Objects**: 1
- **Original Objects**: open sign
- **Merged BBox**: x=128, y=22, w=205, h=239

### orifice
- **Merged Objects**: 2
- **Original Objects**: mouth, mouth
- **Merged BBox**: x=155, y=174, w=78, h=50

### sense organ
- **Merged Objects**: 1
- **Original Objects**: nose
- **Merged BBox**: x=178, y=142, w=29, h=33

### signal
- **Merged Objects**: 1
- **Original Objects**: mantle
- **Merged BBox**: x=280, y=312, w=218, h=55

---

## Coarse-Grained Merged Nodes

**Node Count**: 7

### artifact
- **Merged Objects**: 3
- **Original Objects**: shirt, shirt, dress
- **Merged BBox**: x=70, y=236, w=362, h=136

### body part
- **Merged Objects**: 5
- **Original Objects**: chin, hand, mouth, mouth, nose
- **Merged BBox**: x=20, y=142, w=221, h=179

### gesture
- **Merged Objects**: 1
- **Original Objects**: smile
- **Merged BBox**: x=176, y=185, w=51, h=26

### living thing
- **Merged Objects**: 4
- **Original Objects**: girl, girl, girl, girl
- **Merged BBox**: x=18, y=36, w=466, h=320

### neck/part
- **Merged Objects**: 1
- **Original Objects**: neck/part
- **Merged BBox**: x=204, y=245, w=47, h=13

### open sign
- **Merged Objects**: 1
- **Original Objects**: open sign
- **Merged BBox**: x=128, y=22, w=205, h=239

### symbol
- **Merged Objects**: 1
- **Original Objects**: mantle
- **Merged BBox**: x=280, y=312, w=218, h=55

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v6/sample_2323145
