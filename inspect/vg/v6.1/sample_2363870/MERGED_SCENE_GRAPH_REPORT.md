# Merged Multi-Granularity Scene Graph Report

## Image ID: 2363870

**Total Objects**: 24
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 24 | 12 | 2.00x |
| Mid | 24 | 9 | 2.67x |
| Coarse | 24 | 8 | 3.00x |

---

## Fine-Grained Merged Nodes

**Node Count**: 12

### barn
- **Merged Objects**: 1
- **Original Objects**: barn
- **Merged BBox**: x=4, y=2, w=475, h=240

### cow
- **Merged Objects**: 4
- **Original Objects**: cow, cow, cow, cow
- **Merged BBox**: x=29, y=120, w=451, h=155

### ear
- **Merged Objects**: 6
- **Original Objects**: ear, ear, ear, ear, ear, ear
- **Merged BBox**: x=66, y=126, w=348, h=51

### forest
- **Merged Objects**: 1
- **Original Objects**: forest
- **Merged BBox**: x=197, y=66, w=221, h=28

### hay
- **Merged Objects**: 2
- **Original Objects**: hay, hay
- **Merged BBox**: x=317, y=65, w=177, h=77

### head
- **Merged Objects**: 4
- **Original Objects**: head, head, head, head
- **Merged BBox**: x=12, y=126, w=475, h=129

### holes
- **Merged Objects**: 1
- **Original Objects**: holes
- **Merged BBox**: x=1, y=104, w=490, h=156

### nose
- **Merged Objects**: 1
- **Original Objects**: nose
- **Merged BBox**: x=135, y=192, w=37, h=21

### roof
- **Merged Objects**: 1
- **Original Objects**: roof
- **Merged BBox**: x=3, y=1, w=474, h=58

### sun
- **Merged Objects**: 1
- **Original Objects**: sun
- **Merged BBox**: x=475, y=5, w=19, h=18

### tarp
- **Merged Objects**: 1
- **Original Objects**: tarp
- **Merged BBox**: x=429, y=41, w=70, h=43

### trough
- **Merged Objects**: 1
- **Original Objects**: trough
- **Merged BBox**: x=2, y=213, w=490, h=161

---

## Mid-Grained Merged Nodes

**Node Count**: 9

### animal
- **Merged Objects**: 4
- **Original Objects**: cow, cow, cow, cow
- **Merged BBox**: x=29, y=120, w=451, h=155

### body_part
- **Merged Objects**: 11
- **Original Objects**: head, head, head, head, nose, ear, ear, ear, ear, ear (+1 more)
- **Merged BBox**: x=12, y=126, w=475, h=129

### building
- **Merged Objects**: 1
- **Original Objects**: barn
- **Merged BBox**: x=4, y=2, w=475, h=240

### canvas
- **Merged Objects**: 1
- **Original Objects**: tarp
- **Merged BBox**: x=429, y=41, w=70, h=43

### food
- **Merged Objects**: 2
- **Original Objects**: hay, hay
- **Merged BBox**: x=317, y=65, w=177, h=77

### nature
- **Merged Objects**: 2
- **Original Objects**: trough, sun
- **Merged BBox**: x=2, y=5, w=492, h=369

### opening
- **Merged Objects**: 1
- **Original Objects**: holes
- **Merged BBox**: x=1, y=104, w=490, h=156

### protective covering
- **Merged Objects**: 1
- **Original Objects**: roof
- **Merged BBox**: x=3, y=1, w=474, h=58

### vegetation
- **Merged Objects**: 1
- **Original Objects**: forest
- **Merged BBox**: x=197, y=66, w=221, h=28

---

## Coarse-Grained Merged Nodes

**Node Count**: 8

### amorphous shape
- **Merged Objects**: 1
- **Original Objects**: holes
- **Merged BBox**: x=1, y=104, w=490, h=156

### artifact
- **Merged Objects**: 3
- **Original Objects**: roof, tarp, barn
- **Merged BBox**: x=3, y=1, w=496, h=241

### body part
- **Merged Objects**: 11
- **Original Objects**: head, head, head, head, nose, ear, ear, ear, ear, ear (+1 more)
- **Merged BBox**: x=12, y=126, w=475, h=129

### food
- **Merged Objects**: 2
- **Original Objects**: hay, hay
- **Merged BBox**: x=317, y=65, w=177, h=77

### living thing
- **Merged Objects**: 4
- **Original Objects**: cow, cow, cow, cow
- **Merged BBox**: x=29, y=120, w=451, h=155

### natural depression
- **Merged Objects**: 1
- **Original Objects**: trough
- **Merged BBox**: x=2, y=213, w=490, h=161

### natural object
- **Merged Objects**: 1
- **Original Objects**: sun
- **Merged BBox**: x=475, y=5, w=19, h=18

### vegetation
- **Merged Objects**: 1
- **Original Objects**: forest
- **Merged BBox**: x=197, y=66, w=221, h=28

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v6.1/sample_2363870
