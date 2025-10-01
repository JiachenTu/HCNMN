# Merged Multi-Granularity Scene Graph Report

## Image ID: 2317206

**Total Objects**: 15
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 15 | 15 | 1.00x |
| Mid | 15 | 13 | 1.15x |
| Coarse | 15 | 7 | 2.14x |

---

## Fine-Grained Merged Nodes

**Node Count**: 15

### back
- **Merged Objects**: 1
- **Original Objects**: back
- **Merged BBox**: x=211, y=97, w=109, h=22

### bear
- **Merged Objects**: 1
- **Original Objects**: bear
- **Merged BBox**: x=99, y=91, w=259, h=115

### ear
- **Merged Objects**: 1
- **Original Objects**: ear
- **Merged BBox**: x=175, y=111, w=18, h=15

### ears
- **Merged Objects**: 1
- **Original Objects**: ears
- **Merged BBox**: x=143, y=108, w=65, h=22

### eye
- **Merged Objects**: 1
- **Original Objects**: eye
- **Merged BBox**: x=171, y=138, w=12, h=18

### eyes
- **Merged Objects**: 1
- **Original Objects**: eyes
- **Merged BBox**: x=145, y=135, w=42, h=15

### grass
- **Merged Objects**: 1
- **Original Objects**: grass
- **Merged BBox**: x=381, y=229, w=51, h=35

### ground
- **Merged Objects**: 1
- **Original Objects**: ground
- **Merged BBox**: x=213, y=279, w=99, h=39

### head
- **Merged Objects**: 1
- **Original Objects**: head
- **Merged BBox**: x=146, y=113, w=59, h=62

### leg
- **Merged Objects**: 1
- **Original Objects**: leg
- **Merged BBox**: x=208, y=180, w=15, h=26

### nose
- **Merged Objects**: 1
- **Original Objects**: nose
- **Merged BBox**: x=150, y=164, w=12, h=8

### snout
- **Merged Objects**: 1
- **Original Objects**: snout
- **Merged BBox**: x=153, y=152, w=24, h=24

### sun
- **Merged Objects**: 1
- **Original Objects**: sun
- **Merged BBox**: x=264, y=109, w=50, h=37

### weeds
- **Merged Objects**: 1
- **Original Objects**: weeds
- **Merged BBox**: x=444, y=192, w=34, h=30

### white mark
- **Merged Objects**: 1
- **Original Objects**: white mark
- **Merged BBox**: x=208, y=112, w=22, h=51

---

## Mid-Grained Merged Nodes

**Node Count**: 13

### body part
- **Merged Objects**: 1
- **Original Objects**: back
- **Merged BBox**: x=211, y=97, w=109, h=22

### carnivore
- **Merged Objects**: 1
- **Original Objects**: bear
- **Merged BBox**: x=99, y=91, w=259, h=115

### chemoreceptor
- **Merged Objects**: 1
- **Original Objects**: nose
- **Merged BBox**: x=150, y=164, w=12, h=8

### external body part
- **Merged Objects**: 1
- **Original Objects**: head
- **Merged BBox**: x=146, y=113, w=59, h=62

### garment
- **Merged Objects**: 1
- **Original Objects**: weeds
- **Merged BBox**: x=444, y=192, w=34, h=30

### gramineous plant
- **Merged Objects**: 1
- **Original Objects**: grass
- **Merged BBox**: x=381, y=229, w=51, h=35

### limb
- **Merged Objects**: 1
- **Original Objects**: leg
- **Merged BBox**: x=208, y=180, w=15, h=26

### nose
- **Merged Objects**: 1
- **Original Objects**: snout
- **Merged BBox**: x=153, y=152, w=24, h=24

### object
- **Merged Objects**: 1
- **Original Objects**: ground
- **Merged BBox**: x=213, y=279, w=99, h=39

### opinion
- **Merged Objects**: 1
- **Original Objects**: eyes
- **Merged BBox**: x=145, y=135, w=42, h=15

### sense organ
- **Merged Objects**: 3
- **Original Objects**: ears, ear, eye
- **Merged BBox**: x=143, y=108, w=65, h=48

### sun
- **Merged Objects**: 1
- **Original Objects**: sun
- **Merged BBox**: x=264, y=109, w=50, h=37

### white mark
- **Merged Objects**: 1
- **Original Objects**: white mark
- **Merged BBox**: x=208, y=112, w=22, h=51

---

## Coarse-Grained Merged Nodes

**Node Count**: 7

### artifact
- **Merged Objects**: 1
- **Original Objects**: weeds
- **Merged BBox**: x=444, y=192, w=34, h=30

### body part
- **Merged Objects**: 8
- **Original Objects**: ears, nose, snout, head, ear, eye, leg, back
- **Merged BBox**: x=143, y=97, w=177, h=109

### content
- **Merged Objects**: 1
- **Original Objects**: eyes
- **Merged BBox**: x=145, y=135, w=42, h=15

### land
- **Merged Objects**: 1
- **Original Objects**: ground
- **Merged BBox**: x=213, y=279, w=99, h=39

### living thing
- **Merged Objects**: 2
- **Original Objects**: bear, grass
- **Merged BBox**: x=99, y=91, w=333, h=173

### natural object
- **Merged Objects**: 1
- **Original Objects**: sun
- **Merged BBox**: x=264, y=109, w=50, h=37

### white mark
- **Merged Objects**: 1
- **Original Objects**: white mark
- **Merged BBox**: x=208, y=112, w=22, h=51

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v5/sample_2317206
