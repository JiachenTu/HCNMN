# Merged Multi-Granularity Scene Graph Report

## Image ID: 713869

**Total Objects**: 14
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 14 | 10 | 1.40x |
| Mid | 14 | 9 | 1.56x |
| Coarse | 14 | 3 | 4.67x |

---

## Fine-Grained Merged Nodes

**Node Count**: 10

### bike
- **Merged Objects**: 4
- **Original Objects**: bike, bike, bike, bike
- **Merged BBox**: x=71, y=33, w=858, h=633

### container
- **Merged Objects**: 1
- **Original Objects**: container
- **Merged BBox**: x=75, y=37, w=230, h=132

### engine
- **Merged Objects**: 1
- **Original Objects**: engine
- **Merged BBox**: x=380, y=355, w=210, h=171

### grass
- **Merged Objects**: 1
- **Original Objects**: grass
- **Merged BBox**: x=771, y=141, w=221, h=318

### helmet
- **Merged Objects**: 1
- **Original Objects**: helmet
- **Merged BBox**: x=548, y=39, w=74, h=55

### logo
- **Merged Objects**: 1
- **Original Objects**: logo
- **Merged BBox**: x=550, y=262, w=50, h=33

### motorcycle
- **Merged Objects**: 2
- **Original Objects**: motorcycle, motorcycle
- **Merged BBox**: x=84, y=44, w=856, h=631

### pole
- **Merged Objects**: 1
- **Original Objects**: pole
- **Merged BBox**: x=823, y=14, w=78, h=193

### symbol
- **Merged Objects**: 1
- **Original Objects**: symbol
- **Merged BBox**: x=548, y=258, w=50, h=40

### tire
- **Merged Objects**: 1
- **Original Objects**: tire
- **Merged BBox**: x=618, y=415, w=322, h=260

---

## Mid-Grained Merged Nodes

**Node Count**: 9

### armor plate
- **Merged Objects**: 1
- **Original Objects**: helmet
- **Merged BBox**: x=548, y=39, w=74, h=55

### gramineous plant
- **Merged Objects**: 1
- **Original Objects**: grass
- **Merged BBox**: x=771, y=141, w=221, h=318

### hoop
- **Merged Objects**: 1
- **Original Objects**: tire
- **Merged BBox**: x=618, y=415, w=322, h=260

### instrumentality
- **Merged Objects**: 1
- **Original Objects**: container
- **Merged BBox**: x=75, y=37, w=230, h=132

### motor
- **Merged Objects**: 1
- **Original Objects**: engine
- **Merged BBox**: x=380, y=355, w=210, h=171

### motor vehicle
- **Merged Objects**: 6
- **Original Objects**: motorcycle, motorcycle, bike, bike, bike, bike
- **Merged BBox**: x=71, y=33, w=869, h=642

### rod
- **Merged Objects**: 1
- **Original Objects**: pole
- **Merged BBox**: x=823, y=14, w=78, h=193

### signal
- **Merged Objects**: 1
- **Original Objects**: symbol
- **Merged BBox**: x=548, y=258, w=50, h=40

### trademark
- **Merged Objects**: 1
- **Original Objects**: logo
- **Merged BBox**: x=550, y=262, w=50, h=33

---

## Coarse-Grained Merged Nodes

**Node Count**: 3

### artifact
- **Merged Objects**: 11
- **Original Objects**: motorcycle, tire, container, motorcycle, helmet, bike, bike, bike, bike, pole (+1 more)
- **Merged BBox**: x=71, y=14, w=869, h=661

### living thing
- **Merged Objects**: 1
- **Original Objects**: grass
- **Merged BBox**: x=771, y=141, w=221, h=318

### symbol
- **Merged Objects**: 2
- **Original Objects**: symbol, logo
- **Merged BBox**: x=548, y=258, w=52, h=40

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v5/sample_713869
