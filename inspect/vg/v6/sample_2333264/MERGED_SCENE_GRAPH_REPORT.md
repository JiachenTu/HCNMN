# Merged Multi-Granularity Scene Graph Report

## Image ID: 2333264

**Total Objects**: 12
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 12 | 9 | 1.33x |
| Mid | 12 | 9 | 1.33x |
| Coarse | 12 | 6 | 2.00x |

---

## Fine-Grained Merged Nodes

**Node Count**: 9

### bracelet
- **Merged Objects**: 1
- **Original Objects**: bracelet
- **Merged BBox**: x=321, y=198, w=84, h=85

### finger
- **Merged Objects**: 3
- **Original Objects**: finger, finger, finger
- **Merged BBox**: x=204, y=71, w=118, h=73

### hand
- **Merged Objects**: 1
- **Original Objects**: hand
- **Merged BBox**: x=201, y=76, w=197, h=182

### key pad
- **Merged Objects**: 1
- **Original Objects**: key pad
- **Merged BBox**: x=122, y=186, w=135, h=141

### keyboard
- **Merged Objects**: 1
- **Original Objects**: keyboard
- **Merged BBox**: x=3, y=143, w=273, h=182

### mouse
- **Merged Objects**: 2
- **Original Objects**: mouse, mouse
- **Merged BBox**: x=205, y=55, w=218, h=124

### person
- **Merged Objects**: 1
- **Original Objects**: person
- **Merged BBox**: x=198, y=69, w=300, h=262

### ring finger
- **Merged Objects**: 1
- **Original Objects**: ring finger
- **Merged BBox**: x=280, y=88, w=41, h=32

### table top
- **Merged Objects**: 1
- **Original Objects**: table top
- **Merged BBox**: x=113, y=67, w=55, h=47

---

## Mid-Grained Merged Nodes

**Node Count**: 9

### external body part
- **Merged Objects**: 1
- **Original Objects**: hand
- **Merged BBox**: x=201, y=76, w=197, h=182

### extremity
- **Merged Objects**: 3
- **Original Objects**: finger, finger, finger
- **Merged BBox**: x=204, y=71, w=118, h=73

### instrumentality
- **Merged Objects**: 1
- **Original Objects**: keyboard
- **Merged BBox**: x=3, y=143, w=273, h=182

### key pad
- **Merged Objects**: 1
- **Original Objects**: key pad
- **Merged BBox**: x=122, y=186, w=135, h=141

### living thing
- **Merged Objects**: 1
- **Original Objects**: person
- **Merged BBox**: x=198, y=69, w=300, h=262

### placental
- **Merged Objects**: 2
- **Original Objects**: mouse, mouse
- **Merged BBox**: x=205, y=55, w=218, h=124

### ring finger
- **Merged Objects**: 1
- **Original Objects**: ring finger
- **Merged BBox**: x=280, y=88, w=41, h=32

### strip
- **Merged Objects**: 1
- **Original Objects**: bracelet
- **Merged BBox**: x=321, y=198, w=84, h=85

### table top
- **Merged Objects**: 1
- **Original Objects**: table top
- **Merged BBox**: x=113, y=67, w=55, h=47

---

## Coarse-Grained Merged Nodes

**Node Count**: 6

### artifact
- **Merged Objects**: 2
- **Original Objects**: bracelet, keyboard
- **Merged BBox**: x=3, y=143, w=402, h=182

### body part
- **Merged Objects**: 4
- **Original Objects**: hand, finger, finger, finger
- **Merged BBox**: x=201, y=71, w=197, h=187

### key pad
- **Merged Objects**: 1
- **Original Objects**: key pad
- **Merged BBox**: x=122, y=186, w=135, h=141

### living thing
- **Merged Objects**: 3
- **Original Objects**: mouse, mouse, person
- **Merged BBox**: x=198, y=55, w=300, h=276

### ring finger
- **Merged Objects**: 1
- **Original Objects**: ring finger
- **Merged BBox**: x=280, y=88, w=41, h=32

### table top
- **Merged Objects**: 1
- **Original Objects**: table top
- **Merged BBox**: x=113, y=67, w=55, h=47

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v6/sample_2333264
