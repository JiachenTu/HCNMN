# Merged Multi-Granularity Scene Graph Report

## Image ID: 2330893

**Total Objects**: 26
**Hierarchy Levels**: 3 (Fine → Mid → Coarse)

---

## Merged Scene Graph Statistics

At each granularity level, objects with the same concept are merged into a single node with a combined bounding box.

| Granularity | Original Objects | Merged Nodes | Compression Ratio |
|-------------|------------------|--------------|-------------------|
| Fine | 26 | 11 | 2.36x |
| Mid | 26 | 10 | 2.60x |
| Coarse | 26 | 8 | 3.25x |

---

## Fine-Grained Merged Nodes

**Node Count**: 11

### bag
- **Merged Objects**: 1
- **Original Objects**: bag
- **Merged BBox**: x=63, y=203, w=62, h=127

### board
- **Merged Objects**: 2
- **Original Objects**: board, board
- **Merged BBox**: x=67, y=4, w=432, h=327

### broccoli
- **Merged Objects**: 11
- **Original Objects**: broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli (+1 more)
- **Merged BBox**: x=197, y=38, w=269, h=255

### brocolli
- **Merged Objects**: 2
- **Original Objects**: brocolli, brocolli
- **Merged BBox**: x=186, y=0, w=300, h=291

### can
- **Merged Objects**: 2
- **Original Objects**: can, can
- **Merged BBox**: x=1, y=169, w=136, h=158

### cutting board
- **Merged Objects**: 1
- **Original Objects**: cutting board
- **Merged BBox**: x=67, y=0, w=432, h=331

### floor
- **Merged Objects**: 1
- **Original Objects**: floor
- **Merged BBox**: x=1, y=144, w=159, h=170

### ground
- **Merged Objects**: 1
- **Original Objects**: ground
- **Merged BBox**: x=148, y=286, w=36, h=45

### knife
- **Merged Objects**: 2
- **Original Objects**: knife, knife
- **Merged BBox**: x=359, y=104, w=139, h=194

### piece
- **Merged Objects**: 1
- **Original Objects**: piece
- **Merged BBox**: x=281, y=112, w=32, h=28

### table
- **Merged Objects**: 2
- **Original Objects**: table, table
- **Merged BBox**: x=4, y=2, w=494, h=329

---

## Mid-Grained Merged Nodes

**Node Count**: 10

### array
- **Merged Objects**: 2
- **Original Objects**: table, table
- **Merged BBox**: x=4, y=2, w=494, h=329

### brocolli
- **Merged Objects**: 2
- **Original Objects**: brocolli, brocolli
- **Merged BBox**: x=186, y=0, w=300, h=291

### committee
- **Merged Objects**: 2
- **Original Objects**: board, board
- **Merged BBox**: x=67, y=4, w=432, h=327

### container
- **Merged Objects**: 3
- **Original Objects**: can, bag, can
- **Merged BBox**: x=1, y=169, w=136, h=161

### crucifer
- **Merged Objects**: 11
- **Original Objects**: broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli (+1 more)
- **Merged BBox**: x=197, y=38, w=269, h=255

### cutting board
- **Merged Objects**: 1
- **Original Objects**: cutting board
- **Merged BBox**: x=67, y=0, w=432, h=331

### edge tool
- **Merged Objects**: 2
- **Original Objects**: knife, knife
- **Merged BBox**: x=359, y=104, w=139, h=194

### horizontal surface
- **Merged Objects**: 1
- **Original Objects**: floor
- **Merged BBox**: x=1, y=144, w=159, h=170

### object
- **Merged Objects**: 1
- **Original Objects**: ground
- **Merged BBox**: x=148, y=286, w=36, h=45

### part
- **Merged Objects**: 1
- **Original Objects**: piece
- **Merged BBox**: x=281, y=112, w=32, h=28

---

## Coarse-Grained Merged Nodes

**Node Count**: 8

### array
- **Merged Objects**: 2
- **Original Objects**: table, table
- **Merged BBox**: x=4, y=2, w=494, h=329

### artifact
- **Merged Objects**: 6
- **Original Objects**: knife, can, floor, bag, can, knife
- **Merged BBox**: x=1, y=104, w=497, h=226

### brocolli
- **Merged Objects**: 2
- **Original Objects**: brocolli, brocolli
- **Merged BBox**: x=186, y=0, w=300, h=291

### cutting board
- **Merged Objects**: 1
- **Original Objects**: cutting board
- **Merged BBox**: x=67, y=0, w=432, h=331

### land
- **Merged Objects**: 1
- **Original Objects**: ground
- **Merged BBox**: x=148, y=286, w=36, h=45

### living thing
- **Merged Objects**: 11
- **Original Objects**: broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli, broccoli (+1 more)
- **Merged BBox**: x=197, y=38, w=269, h=255

### organization
- **Merged Objects**: 2
- **Original Objects**: board, board
- **Merged BBox**: x=67, y=4, w=432, h=327

### piece
- **Merged Objects**: 1
- **Original Objects**: piece
- **Merged BBox**: x=281, y=112, w=32, h=28

---

## Visualization Files

- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: Side-by-side comparison of all 3 levels

---

**Generated**: /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/v5/sample_2330893
