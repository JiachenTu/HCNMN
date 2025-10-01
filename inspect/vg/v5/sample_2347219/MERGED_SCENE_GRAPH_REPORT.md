# Merged Multi-Granularity Scene Graph Report

## Image ID: 2347219

**Total Objects**: 30
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 30 | 18 | 1.67x |
| Mid | 30 | 16 | 1.88x |
| Coarse | 30 | 6 | 5.00x |

---

## Fine-Grained Merged Nodes

**Node Count**: 18

### arm
- **Merged Objects**: 1
- **Original Objects**: arm
- **Merged BBox**: x=174, y=4, w=127, h=355

### blue jeans
- **Merged Objects**: 1
- **Original Objects**: blue jeans
- **Merged BBox**: x=46, y=45, w=274, h=266

### car
- **Merged Objects**: 1
- **Original Objects**: car
- **Merged BBox**: x=2, y=24, w=87, h=105

### cone
- **Merged Objects**: 1
- **Original Objects**: cone
- **Merged BBox**: x=276, y=59, w=54, h=87

### floor
- **Merged Objects**: 1
- **Original Objects**: floor
- **Merged BBox**: x=176, y=426, w=132, h=65

### grey marks
- **Merged Objects**: 1
- **Original Objects**: grey marks
- **Merged BBox**: x=56, y=1, w=209, h=108

### lace
- **Merged Objects**: 1
- **Original Objects**: lace
- **Merged BBox**: x=219, y=287, w=38, h=35

### laces
- **Merged Objects**: 1
- **Original Objects**: laces
- **Merged BBox**: x=214, y=293, w=58, h=27

### man
- **Merged Objects**: 1
- **Original Objects**: man
- **Merged BBox**: x=46, y=2, w=273, h=384

### pants
- **Merged Objects**: 1
- **Original Objects**: pants
- **Merged BBox**: x=48, y=60, w=268, h=248

### person
- **Merged Objects**: 3
- **Original Objects**: person, person, person
- **Merged BBox**: x=34, y=1, w=297, h=397

### shirt
- **Merged Objects**: 3
- **Original Objects**: shirt, shirt, shirt
- **Merged BBox**: x=51, y=0, w=228, h=119

### shoe
- **Merged Objects**: 5
- **Original Objects**: shoe, shoe, shoe, shoe, shoe
- **Merged BBox**: x=39, y=270, w=247, h=125

### skateboard
- **Merged Objects**: 2
- **Original Objects**: skateboard, skateboard
- **Merged BBox**: x=17, y=336, w=314, h=104

### sock
- **Merged Objects**: 4
- **Original Objects**: sock, sock, sock, sock
- **Merged BBox**: x=59, y=262, w=169, h=61

### street
- **Merged Objects**: 1
- **Original Objects**: street
- **Merged BBox**: x=40, y=129, w=45, h=73

### trouser
- **Merged Objects**: 1
- **Original Objects**: trouser
- **Merged BBox**: x=37, y=58, w=291, h=241

### writing
- **Merged Objects**: 1
- **Original Objects**: writing
- **Merged BBox**: x=168, y=13, w=76, h=99

---

## Mid-Grained Merged Nodes

**Node Count**: 16

### artifact
- **Merged Objects**: 1
- **Original Objects**: cone
- **Merged BBox**: x=276, y=59, w=54, h=87

### blue jeans
- **Merged Objects**: 1
- **Original Objects**: blue jeans
- **Merged BBox**: x=46, y=45, w=274, h=266

### board
- **Merged Objects**: 2
- **Original Objects**: skateboard, skateboard
- **Merged BBox**: x=17, y=336, w=314, h=104

### causal agent
- **Merged Objects**: 3
- **Original Objects**: person, person, person
- **Merged BBox**: x=34, y=1, w=297, h=397

### cord
- **Merged Objects**: 2
- **Original Objects**: lace, laces
- **Merged BBox**: x=214, y=287, w=58, h=35

### footwear
- **Merged Objects**: 5
- **Original Objects**: shoe, shoe, shoe, shoe, shoe
- **Merged BBox**: x=39, y=270, w=247, h=125

### garment
- **Merged Objects**: 4
- **Original Objects**: trouser, shirt, shirt, shirt
- **Merged BBox**: x=37, y=0, w=291, h=299

### grey marks
- **Merged Objects**: 1
- **Original Objects**: grey marks
- **Merged BBox**: x=56, y=1, w=209, h=108

### horizontal surface
- **Merged Objects**: 1
- **Original Objects**: floor
- **Merged BBox**: x=176, y=426, w=132, h=65

### hosiery
- **Merged Objects**: 4
- **Original Objects**: sock, sock, sock, sock
- **Merged BBox**: x=59, y=262, w=169, h=61

### limb
- **Merged Objects**: 1
- **Original Objects**: arm
- **Merged BBox**: x=174, y=4, w=127, h=355

### male
- **Merged Objects**: 1
- **Original Objects**: man
- **Merged BBox**: x=46, y=2, w=273, h=384

### motor vehicle
- **Merged Objects**: 1
- **Original Objects**: car
- **Merged BBox**: x=2, y=24, w=87, h=105

### thoroughfare
- **Merged Objects**: 1
- **Original Objects**: street
- **Merged BBox**: x=40, y=129, w=45, h=73

### underpants
- **Merged Objects**: 1
- **Original Objects**: pants
- **Merged BBox**: x=48, y=60, w=268, h=248

### verbal creation
- **Merged Objects**: 1
- **Original Objects**: writing
- **Merged BBox**: x=168, y=13, w=76, h=99

---

## Coarse-Grained Merged Nodes

**Node Count**: 6

### act
- **Merged Objects**: 1
- **Original Objects**: writing
- **Merged BBox**: x=168, y=13, w=76, h=99

### artifact
- **Merged Objects**: 22
- **Original Objects**: floor, shoe, shoe, trouser, sock, sock, shirt, lace, shoe, shoe (+12 more)
- **Merged BBox**: x=2, y=0, w=329, h=491

### blue jeans
- **Merged Objects**: 1
- **Original Objects**: blue jeans
- **Merged BBox**: x=46, y=45, w=274, h=266

### body part
- **Merged Objects**: 1
- **Original Objects**: arm
- **Merged BBox**: x=174, y=4, w=127, h=355

### grey marks
- **Merged Objects**: 1
- **Original Objects**: grey marks
- **Merged BBox**: x=56, y=1, w=209, h=108

### living thing
- **Merged Objects**: 4
- **Original Objects**: man, person, person, person
- **Merged BBox**: x=34, y=1, w=297, h=397

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v5/sample_2347219
