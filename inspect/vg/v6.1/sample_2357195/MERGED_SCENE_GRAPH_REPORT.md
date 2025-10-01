# Merged Multi-Granularity Scene Graph Report

## Image ID: 2357195

**Total Objects**: 26
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 26 | 25 | 1.04x |
| Mid | 26 | 16 | 1.62x |
| Coarse | 26 | 10 | 2.60x |

---

## Fine-Grained Merged Nodes

**Node Count**: 25

### backboard
- **Merged Objects**: 1
- **Original Objects**: backboard
- **Merged BBox**: x=55, y=1, w=50, h=36

### ball
- **Merged Objects**: 1
- **Original Objects**: ball
- **Merged BBox**: x=220, y=160, w=25, h=21

### basketball court
- **Merged Objects**: 1
- **Original Objects**: basketball court
- **Merged BBox**: x=3, y=1, w=497, h=240

### basketball hoop
- **Merged Objects**: 1
- **Original Objects**: basketball hoop
- **Merged BBox**: x=78, y=28, w=26, h=35

### basketball rim
- **Merged Objects**: 1
- **Original Objects**: basketball rim
- **Merged BBox**: x=76, y=29, w=31, h=10

### building
- **Merged Objects**: 1
- **Original Objects**: building
- **Merged BBox**: x=248, y=0, w=251, h=106

### car
- **Merged Objects**: 1
- **Original Objects**: car
- **Merged BBox**: x=2, y=120, w=37, h=30

### concrete
- **Merged Objects**: 1
- **Original Objects**: concrete
- **Merged BBox**: x=78, y=196, w=70, h=46

### fence
- **Merged Objects**: 1
- **Original Objects**: fence
- **Merged BBox**: x=1, y=1, w=499, h=260

### fingers
- **Merged Objects**: 1
- **Original Objects**: fingers
- **Merged BBox**: x=99, y=190, w=18, h=19

### girl
- **Merged Objects**: 1
- **Original Objects**: girl
- **Merged BBox**: x=99, y=21, w=196, h=313

### hair
- **Merged Objects**: 1
- **Original Objects**: hair
- **Merged BBox**: x=144, y=18, w=139, h=122

### hand
- **Merged Objects**: 1
- **Original Objects**: hand
- **Merged BBox**: x=95, y=177, w=21, h=34

### leaf
- **Merged Objects**: 1
- **Original Objects**: leaf
- **Merged BBox**: x=274, y=281, w=18, h=9

### net
- **Merged Objects**: 1
- **Original Objects**: net
- **Merged BBox**: x=82, y=38, w=20, h=25

### pole
- **Merged Objects**: 2
- **Original Objects**: pole, pole
- **Merged BBox**: x=30, y=1, w=112, h=208

### racket
- **Merged Objects**: 1
- **Original Objects**: racket
- **Merged BBox**: x=1, y=172, w=126, h=160

### shirt
- **Merged Objects**: 1
- **Original Objects**: shirt
- **Merged BBox**: x=130, y=90, w=137, h=114

### shoes
- **Merged Objects**: 1
- **Original Objects**: shoes
- **Merged BBox**: x=226, y=299, w=73, h=35

### shorts
- **Merged Objects**: 1
- **Original Objects**: shorts
- **Merged BBox**: x=150, y=180, w=89, h=56

### shoulder
- **Merged Objects**: 1
- **Original Objects**: shoulder
- **Merged BBox**: x=145, y=86, w=29, h=21

### side
- **Merged Objects**: 1
- **Original Objects**: side
- **Merged BBox**: x=8, y=121, w=33, h=29

### surface
- **Merged Objects**: 1
- **Original Objects**: surface
- **Merged BBox**: x=274, y=251, w=102, h=74

### wall
- **Merged Objects**: 1
- **Original Objects**: wall
- **Merged BBox**: x=254, y=0, w=244, h=120

### window
- **Merged Objects**: 1
- **Original Objects**: window
- **Merged BBox**: x=13, y=127, w=17, h=11

---

## Mid-Grained Merged Nodes

**Node Count**: 16

### artifact
- **Merged Objects**: 1
- **Original Objects**: surface
- **Merged BBox**: x=274, y=251, w=102, h=74

### basketball court
- **Merged Objects**: 1
- **Original Objects**: basketball court
- **Merged BBox**: x=3, y=1, w=497, h=240

### basketball hoop
- **Merged Objects**: 1
- **Original Objects**: basketball hoop
- **Merged BBox**: x=78, y=28, w=26, h=35

### basketball rim
- **Merged Objects**: 1
- **Original Objects**: basketball rim
- **Merged BBox**: x=76, y=29, w=31, h=10

### body_part
- **Merged Objects**: 3
- **Original Objects**: shoulder, hand, fingers
- **Merged BBox**: x=95, y=86, w=79, h=125

### building
- **Merged Objects**: 3
- **Original Objects**: building, wall, fence
- **Merged BBox**: x=1, y=0, w=499, h=261

### building material
- **Merged Objects**: 1
- **Original Objects**: concrete
- **Merged BBox**: x=78, y=196, w=70, h=46

### clothing
- **Merged Objects**: 2
- **Original Objects**: shirt, shorts
- **Merged BBox**: x=130, y=90, w=137, h=146

### furniture
- **Merged Objects**: 1
- **Original Objects**: window
- **Merged BBox**: x=13, y=127, w=17, h=11

### nature
- **Merged Objects**: 2
- **Original Objects**: leaf, hair
- **Merged BBox**: x=144, y=18, w=148, h=272

### noise
- **Merged Objects**: 1
- **Original Objects**: racket
- **Merged BBox**: x=1, y=172, w=126, h=160

### person
- **Merged Objects**: 1
- **Original Objects**: girl
- **Merged BBox**: x=99, y=21, w=196, h=313

### region
- **Merged Objects**: 1
- **Original Objects**: side
- **Merged BBox**: x=8, y=121, w=33, h=29

### situation
- **Merged Objects**: 1
- **Original Objects**: shoes
- **Merged BBox**: x=226, y=299, w=73, h=35

### tool
- **Merged Objects**: 5
- **Original Objects**: pole, ball, pole, net, backboard
- **Merged BBox**: x=30, y=1, w=215, h=208

### vehicle
- **Merged Objects**: 1
- **Original Objects**: car
- **Merged BBox**: x=2, y=120, w=37, h=30

---

## Coarse-Grained Merged Nodes

**Node Count**: 10

### artifact
- **Merged Objects**: 14
- **Original Objects**: surface, car, window, building, wall, pole, concrete, ball, fence, pole (+4 more)
- **Merged BBox**: x=1, y=0, w=499, h=325

### basketball court
- **Merged Objects**: 1
- **Original Objects**: basketball court
- **Merged BBox**: x=3, y=1, w=497, h=240

### basketball hoop
- **Merged Objects**: 1
- **Original Objects**: basketball hoop
- **Merged BBox**: x=78, y=28, w=26, h=35

### basketball rim
- **Merged Objects**: 1
- **Original Objects**: basketball rim
- **Merged BBox**: x=76, y=29, w=31, h=10

### body part
- **Merged Objects**: 3
- **Original Objects**: shoulder, hand, fingers
- **Merged BBox**: x=95, y=86, w=79, h=125

### condition
- **Merged Objects**: 1
- **Original Objects**: shoes
- **Merged BBox**: x=226, y=299, w=73, h=35

### happening
- **Merged Objects**: 1
- **Original Objects**: racket
- **Merged BBox**: x=1, y=172, w=126, h=160

### living thing
- **Merged Objects**: 1
- **Original Objects**: girl
- **Merged BBox**: x=99, y=21, w=196, h=313

### natural object
- **Merged Objects**: 2
- **Original Objects**: leaf, hair
- **Merged BBox**: x=144, y=18, w=148, h=272

### region
- **Merged Objects**: 1
- **Original Objects**: side
- **Merged BBox**: x=8, y=121, w=33, h=29

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v6.1/sample_2357195
