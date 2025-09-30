# Merged Multi-Granularity Scene Graph Report

## Image ID: 2337701

**Total Objects**: 18
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 18 | 13 | 1.38x |
| Mid | 18 | 13 | 1.38x |
| Coarse | 18 | 10 | 1.80x |

---

## Fine-Grained Merged Nodes

**Node Count**: 13

### beach
- **Merged Objects**: 1
- **Original Objects**: beach
- **Merged BBox**: x=4, y=1, w=494, h=332

### bird
- **Merged Objects**: 1
- **Original Objects**: bird
- **Merged BBox**: x=238, y=41, w=110, h=142

### dirt
- **Merged Objects**: 1
- **Original Objects**: dirt
- **Merged BBox**: x=212, y=205, w=250, h=107

### ground
- **Merged Objects**: 1
- **Original Objects**: ground
- **Merged BBox**: x=5, y=194, w=493, h=134

### head
- **Merged Objects**: 1
- **Original Objects**: head
- **Merged BBox**: x=152, y=127, w=19, h=32

### pebble
- **Merged Objects**: 1
- **Original Objects**: pebble
- **Merged BBox**: x=449, y=260, w=41, h=30

### piece
- **Merged Objects**: 1
- **Original Objects**: piece
- **Merged BBox**: x=227, y=159, w=109, h=52

### sand
- **Merged Objects**: 2
- **Original Objects**: sand, sand
- **Merged BBox**: x=0, y=195, w=498, h=135

### seagull
- **Merged Objects**: 1
- **Original Objects**: seagull
- **Merged BBox**: x=145, y=123, w=64, h=75

### shells
- **Merged Objects**: 1
- **Original Objects**: shells
- **Merged BBox**: x=451, y=194, w=46, h=28

### wing
- **Merged Objects**: 1
- **Original Objects**: wing
- **Merged BBox**: x=283, y=106, w=45, h=63

### wood
- **Merged Objects**: 5
- **Original Objects**: wood, wood, wood, wood, wood
- **Merged BBox**: x=140, y=158, w=309, h=148

### wood edges
- **Merged Objects**: 1
- **Original Objects**: wood edges
- **Merged BBox**: x=220, y=163, w=122, h=42

---

## Mid-Grained Merged Nodes

**Node Count**: 13

### ammunition
- **Merged Objects**: 1
- **Original Objects**: shells
- **Merged BBox**: x=451, y=194, w=46, h=28

### earth
- **Merged Objects**: 1
- **Original Objects**: dirt
- **Merged BBox**: x=212, y=205, w=250, h=107

### external body part
- **Merged Objects**: 1
- **Original Objects**: head
- **Merged BBox**: x=152, y=127, w=19, h=32

### geological formation
- **Merged Objects**: 1
- **Original Objects**: beach
- **Merged BBox**: x=4, y=1, w=494, h=332

### larid
- **Merged Objects**: 1
- **Original Objects**: seagull
- **Merged BBox**: x=145, y=123, w=64, h=75

### object
- **Merged Objects**: 1
- **Original Objects**: ground
- **Merged BBox**: x=5, y=194, w=493, h=134

### organ
- **Merged Objects**: 1
- **Original Objects**: wing
- **Merged BBox**: x=283, y=106, w=45, h=63

### part
- **Merged Objects**: 1
- **Original Objects**: piece
- **Merged BBox**: x=227, y=159, w=109, h=52

### plant material
- **Merged Objects**: 5
- **Original Objects**: wood, wood, wood, wood, wood
- **Merged BBox**: x=140, y=158, w=309, h=148

### rock
- **Merged Objects**: 1
- **Original Objects**: pebble
- **Merged BBox**: x=449, y=260, w=41, h=30

### soil
- **Merged Objects**: 2
- **Original Objects**: sand, sand
- **Merged BBox**: x=0, y=195, w=498, h=135

### vertebrate
- **Merged Objects**: 1
- **Original Objects**: bird
- **Merged BBox**: x=238, y=41, w=110, h=142

### wood edges
- **Merged Objects**: 1
- **Original Objects**: wood edges
- **Merged BBox**: x=220, y=163, w=122, h=42

---

## Coarse-Grained Merged Nodes

**Node Count**: 10

### body part
- **Merged Objects**: 2
- **Original Objects**: wing, head
- **Merged BBox**: x=152, y=106, w=176, h=63

### chordate
- **Merged Objects**: 1
- **Original Objects**: bird
- **Merged BBox**: x=238, y=41, w=110, h=142

### coastal diving bird
- **Merged Objects**: 1
- **Original Objects**: seagull
- **Merged BBox**: x=145, y=123, w=64, h=75

### earth
- **Merged Objects**: 2
- **Original Objects**: sand, sand
- **Merged BBox**: x=0, y=195, w=498, h=135

### material
- **Merged Objects**: 6
- **Original Objects**: wood, wood, wood, wood, dirt, wood
- **Merged BBox**: x=140, y=158, w=322, h=154

### natural object
- **Merged Objects**: 1
- **Original Objects**: pebble
- **Merged BBox**: x=449, y=260, w=41, h=30

### object
- **Merged Objects**: 2
- **Original Objects**: piece, beach
- **Merged BBox**: x=4, y=1, w=494, h=332

### physical entity
- **Merged Objects**: 1
- **Original Objects**: ground
- **Merged BBox**: x=5, y=194, w=493, h=134

### weaponry
- **Merged Objects**: 1
- **Original Objects**: shells
- **Merged BBox**: x=451, y=194, w=46, h=28

### wood edges
- **Merged Objects**: 1
- **Original Objects**: wood edges
- **Merged BBox**: x=220, y=163, w=122, h=42

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: vg/sample_2337701
