# Merged Multi-Granularity Scene Graph Report

## Image ID: 498335

**Total Objects**: 30
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 30 | 18 | 1.67x |
| Mid | 30 | 17 | 1.76x |
| Coarse | 30 | 9 | 3.33x |

---

## Fine-Grained Merged Nodes

**Node Count**: 18

### background
- **Merged Objects**: 1
- **Original Objects**: background
- **Merged BBox**: x=12, y=39, w=403, h=232

### balcony
- **Merged Objects**: 1
- **Original Objects**: balcony
- **Merged BBox**: x=105, y=333, w=358, h=85

### billboard
- **Merged Objects**: 1
- **Original Objects**: billboard
- **Merged BBox**: x=52, y=77, w=370, h=207

### clock
- **Merged Objects**: 1
- **Original Objects**: clock
- **Merged BBox**: x=403, y=20, w=222, h=902

### edge
- **Merged Objects**: 2
- **Original Objects**: edge, edge
- **Merged BBox**: x=78, y=381, w=386, h=285

### face
- **Merged Objects**: 1
- **Original Objects**: face
- **Merged BBox**: x=415, y=83, w=156, h=173

### flower
- **Merged Objects**: 1
- **Original Objects**: flower
- **Merged BBox**: x=331, y=846, w=43, h=40

### flowers
- **Merged Objects**: 2
- **Original Objects**: flowers, flowers
- **Merged BBox**: x=322, y=846, w=226, h=107

### letter
- **Merged Objects**: 6
- **Original Objects**: letter, letter, letter, letter, letter, letter
- **Merged BBox**: x=53, y=107, w=232, h=123

### light
- **Merged Objects**: 1
- **Original Objects**: light
- **Merged BBox**: x=97, y=89, w=50, h=38

### lot
- **Merged Objects**: 1
- **Original Objects**: lot
- **Merged BBox**: x=17, y=677, w=597, h=304

### pole
- **Merged Objects**: 1
- **Original Objects**: pole
- **Merged BBox**: x=99, y=54, w=48, h=31

### pot
- **Merged Objects**: 2
- **Original Objects**: pot, pot
- **Merged BBox**: x=282, y=759, w=216, h=225

### railing
- **Merged Objects**: 1
- **Original Objects**: railing
- **Merged BBox**: x=128, y=331, w=340, h=74

### sign
- **Merged Objects**: 5
- **Original Objects**: sign, sign, sign, sign, sign
- **Merged BBox**: x=0, y=15, w=475, h=323

### stairs
- **Merged Objects**: 1
- **Original Objects**: stairs
- **Merged BBox**: x=77, y=642, w=415, h=27

### street
- **Merged Objects**: 1
- **Original Objects**: street
- **Merged BBox**: x=110, y=624, w=389, h=74

### words
- **Merged Objects**: 1
- **Original Objects**: words
- **Merged BBox**: x=25, y=105, w=398, h=156

---

## Mid-Grained Merged Nodes

**Node Count**: 17

### artifact
- **Merged Objects**: 1
- **Original Objects**: balcony
- **Merged BBox**: x=105, y=333, w=358, h=85

### attribute
- **Merged Objects**: 1
- **Original Objects**: background
- **Merged BBox**: x=12, y=39, w=403, h=232

### auditory communication
- **Merged Objects**: 1
- **Original Objects**: words
- **Merged BBox**: x=25, y=105, w=398, h=156

### body part
- **Merged Objects**: 1
- **Original Objects**: face
- **Merged BBox**: x=415, y=83, w=156, h=173

### electromagnetic radiation
- **Merged Objects**: 1
- **Original Objects**: light
- **Merged BBox**: x=97, y=89, w=50, h=38

### evidence
- **Merged Objects**: 5
- **Original Objects**: sign, sign, sign, sign, sign
- **Merged BBox**: x=0, y=15, w=475, h=323

### extremity
- **Merged Objects**: 2
- **Original Objects**: edge, edge
- **Merged BBox**: x=78, y=381, w=386, h=285

### implement
- **Merged Objects**: 1
- **Original Objects**: pole
- **Merged BBox**: x=99, y=54, w=48, h=31

### indefinite quantity
- **Merged Objects**: 1
- **Original Objects**: lot
- **Merged BBox**: x=17, y=677, w=597, h=304

### kitchen utensil
- **Merged Objects**: 2
- **Original Objects**: pot, pot
- **Merged BBox**: x=282, y=759, w=216, h=225

### matter
- **Merged Objects**: 6
- **Original Objects**: letter, letter, letter, letter, letter, letter
- **Merged BBox**: x=53, y=107, w=232, h=123

### measuring instrument
- **Merged Objects**: 1
- **Original Objects**: clock
- **Merged BBox**: x=403, y=20, w=222, h=902

### obstruction
- **Merged Objects**: 1
- **Original Objects**: railing
- **Merged BBox**: x=128, y=331, w=340, h=74

### road
- **Merged Objects**: 1
- **Original Objects**: street
- **Merged BBox**: x=110, y=624, w=389, h=74

### spermatophyte
- **Merged Objects**: 3
- **Original Objects**: flowers, flower, flowers
- **Merged BBox**: x=322, y=846, w=226, h=107

### structure
- **Merged Objects**: 1
- **Original Objects**: billboard
- **Merged BBox**: x=52, y=77, w=370, h=207

### way
- **Merged Objects**: 1
- **Original Objects**: stairs
- **Merged BBox**: x=77, y=642, w=415, h=27

---

## Coarse-Grained Merged Nodes

**Node Count**: 9

### artifact
- **Merged Objects**: 15
- **Original Objects**: pot, billboard, street, pot, letter, letter, letter, letter, letter, letter (+5 more)
- **Merged BBox**: x=52, y=20, w=573, h=964

### background
- **Merged Objects**: 1
- **Original Objects**: background
- **Merged BBox**: x=12, y=39, w=403, h=232

### body part
- **Merged Objects**: 1
- **Original Objects**: face
- **Merged BBox**: x=415, y=83, w=156, h=173

### evidence
- **Merged Objects**: 5
- **Original Objects**: sign, sign, sign, sign, sign
- **Merged BBox**: x=0, y=15, w=475, h=323

### large indefinite quantity
- **Merged Objects**: 1
- **Original Objects**: lot
- **Merged BBox**: x=17, y=677, w=597, h=304

### living thing
- **Merged Objects**: 3
- **Original Objects**: flowers, flower, flowers
- **Merged BBox**: x=322, y=846, w=226, h=107

### natural phenomenon
- **Merged Objects**: 1
- **Original Objects**: light
- **Merged BBox**: x=97, y=89, w=50, h=38

### region
- **Merged Objects**: 2
- **Original Objects**: edge, edge
- **Merged BBox**: x=78, y=381, w=386, h=285

### speech
- **Merged Objects**: 1
- **Original Objects**: words
- **Merged BBox**: x=25, y=105, w=398, h=156

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v6/sample_498335
