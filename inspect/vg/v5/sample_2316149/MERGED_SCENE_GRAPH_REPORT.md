# Merged Multi-Granularity Scene Graph Report

## Image ID: 2316149

**Total Objects**: 28
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 28 | 15 | 1.87x |
| Mid | 28 | 14 | 2.00x |
| Coarse | 28 | 5 | 5.60x |

---

## Fine-Grained Merged Nodes

**Node Count**: 15

### bat
- **Merged Objects**: 1
- **Original Objects**: bat
- **Merged BBox**: x=341, y=114, w=16, h=52

### batter
- **Merged Objects**: 2
- **Original Objects**: batter, batter
- **Merged BBox**: x=324, y=106, w=78, h=191

### batter box
- **Merged Objects**: 1
- **Original Objects**: batter box
- **Merged BBox**: x=274, y=270, w=225, h=59

### batters
- **Merged Objects**: 1
- **Original Objects**: batters
- **Merged BBox**: x=332, y=103, w=21, h=63

### cages
- **Merged Objects**: 1
- **Original Objects**: cages
- **Merged BBox**: x=1, y=0, w=497, h=237

### catcher
- **Merged Objects**: 3
- **Original Objects**: catcher, catcher, catcher
- **Merged BBox**: x=138, y=187, w=95, h=120

### field
- **Merged Objects**: 2
- **Original Objects**: field, field
- **Merged BBox**: x=0, y=174, w=498, h=157

### head
- **Merged Objects**: 1
- **Original Objects**: head
- **Merged BBox**: x=357, y=123, w=44, h=35

### helmet
- **Merged Objects**: 2
- **Original Objects**: helmet, helmet
- **Merged BBox**: x=357, y=123, w=43, h=32

### human
- **Merged Objects**: 4
- **Original Objects**: human, human, human, human
- **Merged BBox**: x=394, y=77, w=98, h=131

### man
- **Merged Objects**: 3
- **Original Objects**: man, man, man
- **Merged BBox**: x=404, y=85, w=87, h=118

### pants
- **Merged Objects**: 1
- **Original Objects**: pants
- **Merged BBox**: x=341, y=212, w=57, h=50

### plate
- **Merged Objects**: 1
- **Original Objects**: plate
- **Merged BBox**: x=381, y=301, w=64, h=21

### shorts
- **Merged Objects**: 4
- **Original Objects**: shorts, shorts, shorts, shorts
- **Merged BBox**: x=404, y=143, w=85, h=34

### umpire
- **Merged Objects**: 1
- **Original Objects**: umpire
- **Merged BBox**: x=42, y=126, w=122, h=148

---

## Mid-Grained Merged Nodes

**Node Count**: 14

### adult
- **Merged Objects**: 3
- **Original Objects**: man, man, man
- **Merged BBox**: x=404, y=85, w=87, h=118

### armor plate
- **Merged Objects**: 2
- **Original Objects**: helmet, helmet
- **Merged BBox**: x=357, y=123, w=43, h=32

### ballplayer
- **Merged Objects**: 3
- **Original Objects**: batter, batter, batters
- **Merged BBox**: x=324, y=103, w=78, h=194

### base
- **Merged Objects**: 1
- **Original Objects**: plate
- **Merged BBox**: x=381, y=301, w=64, h=21

### batter box
- **Merged Objects**: 1
- **Original Objects**: batter box
- **Merged BBox**: x=274, y=270, w=225, h=59

### enclosure
- **Merged Objects**: 1
- **Original Objects**: cages
- **Merged BBox**: x=1, y=0, w=497, h=237

### external body part
- **Merged Objects**: 1
- **Original Objects**: head
- **Merged BBox**: x=357, y=123, w=44, h=35

### hominid
- **Merged Objects**: 4
- **Original Objects**: human, human, human, human
- **Merged BBox**: x=394, y=77, w=98, h=131

### infielder
- **Merged Objects**: 3
- **Original Objects**: catcher, catcher, catcher
- **Merged BBox**: x=138, y=187, w=95, h=120

### official
- **Merged Objects**: 1
- **Original Objects**: umpire
- **Merged BBox**: x=42, y=126, w=122, h=148

### placental
- **Merged Objects**: 1
- **Original Objects**: bat
- **Merged BBox**: x=341, y=114, w=16, h=52

### tract
- **Merged Objects**: 2
- **Original Objects**: field, field
- **Merged BBox**: x=0, y=174, w=498, h=157

### trouser
- **Merged Objects**: 4
- **Original Objects**: shorts, shorts, shorts, shorts
- **Merged BBox**: x=404, y=143, w=85, h=34

### underpants
- **Merged Objects**: 1
- **Original Objects**: pants
- **Merged BBox**: x=341, y=212, w=57, h=50

---

## Coarse-Grained Merged Nodes

**Node Count**: 5

### artifact
- **Merged Objects**: 9
- **Original Objects**: cages, plate, pants, helmet, shorts, shorts, shorts, shorts, helmet
- **Merged BBox**: x=1, y=0, w=497, h=322

### batter box
- **Merged Objects**: 1
- **Original Objects**: batter box
- **Merged BBox**: x=274, y=270, w=225, h=59

### body part
- **Merged Objects**: 1
- **Original Objects**: head
- **Merged BBox**: x=357, y=123, w=44, h=35

### living thing
- **Merged Objects**: 15
- **Original Objects**: catcher, umpire, catcher, batter, batter, bat, man, man, man, human (+5 more)
- **Merged BBox**: x=42, y=77, w=450, h=230

### region
- **Merged Objects**: 2
- **Original Objects**: field, field
- **Merged BBox**: x=0, y=174, w=498, h=157

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v5/sample_2316149
