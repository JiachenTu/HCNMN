# Merged Multi-Granularity Scene Graph Report

## Image ID: 2341540

**Total Objects**: 20
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 20 | 15 | 1.33x |
| Mid | 20 | 12 | 1.67x |
| Coarse | 20 | 5 | 4.00x |

---

## Fine-Grained Merged Nodes

**Node Count**: 15

### arm
- **Merged Objects**: 2
- **Original Objects**: arm, arm
- **Merged BBox**: x=16, y=203, w=327, h=117

### blanket
- **Merged Objects**: 1
- **Original Objects**: blanket
- **Merged BBox**: x=0, y=290, w=375, h=210

### ear
- **Merged Objects**: 2
- **Original Objects**: ear, ear
- **Merged BBox**: x=88, y=36, w=194, h=66

### eye
- **Merged Objects**: 2
- **Original Objects**: eye, eye
- **Merged BBox**: x=109, y=133, w=136, h=44

### foot
- **Merged Objects**: 2
- **Original Objects**: foot, foot
- **Merged BBox**: x=5, y=321, w=354, h=133

### head
- **Merged Objects**: 1
- **Original Objects**: head
- **Merged BBox**: x=68, y=28, w=223, h=203

### leg
- **Merged Objects**: 2
- **Original Objects**: leg, leg
- **Merged BBox**: x=3, y=293, w=358, h=161

### mouth
- **Merged Objects**: 1
- **Original Objects**: mouth
- **Merged BBox**: x=144, y=199, w=48, h=34

### nose
- **Merged Objects**: 1
- **Original Objects**: nose
- **Merged BBox**: x=167, y=177, w=42, h=34

### pillow
- **Merged Objects**: 1
- **Original Objects**: pillow
- **Merged BBox**: x=2, y=1, w=373, h=313

### plastic
- **Merged Objects**: 1
- **Original Objects**: plastic
- **Merged BBox**: x=276, y=98, w=24, h=44

### scarf
- **Merged Objects**: 1
- **Original Objects**: scarf
- **Merged BBox**: x=114, y=213, w=180, h=175

### snout
- **Merged Objects**: 1
- **Original Objects**: snout
- **Merged BBox**: x=125, y=139, w=113, h=95

### teddy bear
- **Merged Objects**: 1
- **Original Objects**: teddy bear
- **Merged BBox**: x=1, y=28, w=358, h=423

### writing
- **Merged Objects**: 1
- **Original Objects**: writing
- **Merged BBox**: x=55, y=416, w=42, h=26

---

## Mid-Grained Merged Nodes

**Node Count**: 12

### body part
- **Merged Objects**: 1
- **Original Objects**: head
- **Merged BBox**: x=68, y=28, w=223, h=203

### chemoreceptor
- **Merged Objects**: 1
- **Original Objects**: snout
- **Merged BBox**: x=125, y=139, w=113, h=95

### cloth covering
- **Merged Objects**: 1
- **Original Objects**: blanket
- **Merged BBox**: x=0, y=290, w=375, h=210

### clothing
- **Merged Objects**: 1
- **Original Objects**: scarf
- **Merged BBox**: x=114, y=213, w=180, h=175

### creating by mental acts
- **Merged Objects**: 1
- **Original Objects**: writing
- **Merged BBox**: x=55, y=416, w=42, h=26

### extremity
- **Merged Objects**: 6
- **Original Objects**: leg, leg, foot, arm, arm, foot
- **Merged BBox**: x=3, y=203, w=358, h=251

### matter
- **Merged Objects**: 1
- **Original Objects**: plastic
- **Merged BBox**: x=276, y=98, w=24, h=44

### organ
- **Merged Objects**: 4
- **Original Objects**: eye, eye, ear, ear
- **Merged BBox**: x=88, y=36, w=194, h=141

### orifice
- **Merged Objects**: 1
- **Original Objects**: mouth
- **Merged BBox**: x=144, y=199, w=48, h=34

### padding
- **Merged Objects**: 1
- **Original Objects**: pillow
- **Merged BBox**: x=2, y=1, w=373, h=313

### sense organ
- **Merged Objects**: 1
- **Original Objects**: nose
- **Merged BBox**: x=167, y=177, w=42, h=34

### teddy bear
- **Merged Objects**: 1
- **Original Objects**: teddy bear
- **Merged BBox**: x=1, y=28, w=358, h=423

---

## Coarse-Grained Merged Nodes

**Node Count**: 5

### act
- **Merged Objects**: 1
- **Original Objects**: writing
- **Merged BBox**: x=55, y=416, w=42, h=26

### artifact
- **Merged Objects**: 3
- **Original Objects**: scarf, blanket, pillow
- **Merged BBox**: x=0, y=1, w=375, h=499

### body part
- **Merged Objects**: 14
- **Original Objects**: eye, eye, leg, leg, nose, ear, ear, foot, snout, arm (+4 more)
- **Merged BBox**: x=3, y=28, w=358, h=426

### plastic
- **Merged Objects**: 1
- **Original Objects**: plastic
- **Merged BBox**: x=276, y=98, w=24, h=44

### teddy bear
- **Merged Objects**: 1
- **Original Objects**: teddy bear
- **Merged BBox**: x=1, y=28, w=358, h=423

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v6/sample_2341540
