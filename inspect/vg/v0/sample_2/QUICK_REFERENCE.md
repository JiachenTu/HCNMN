# Quick Reference: Topology & Properties

## TL;DR

**TOPOLOGY** = "What objects are spatially related?" (41×41 matrix, weights 0-0.5)
**PROPERTIES** = "What attributes do objects have?" (41×30 binary matrix)

---

## Topology Matrix (41×41)

### What It Measures
```
topology[i][j] = spatial relationship strength between concept i and j
```

### How It's Calculated
- **Overlap**: If bboxes intersect → weight = IoU (intersection/union)
- **Proximity**: If distance < 200px → weight = (1 - dist/200) × 0.5

### Example
```
Road bbox: (0, 345, 364×254)
Sidewalk bbox: (320, 347, 478×253)
→ Small overlap → topology[road][sidewalk] = 0.055
```

### Stats
- 142 connections out of 1,681 possible (8.4% density)
- Weights: 0.05 (weak) to 0.50 (strong), avg 0.20

---

## Property Matrix (41×30)

### What It Measures
```
properties[i][j] = 1 if concept i has property j, else 0
```

### The 30 Properties
```
Colors (8):    red, blue, green, yellow, black, white, brown, gray
Sizes (5):     large, small, medium, tiny, huge
Shapes (5):    round, square, rectangular, circular, linear
Materials (6): metal, wood, glass, plastic, fabric, stone
Context (6):   indoor, outdoor, natural, artificial, movable, fixed
```

### How It's Assigned
Keyword matching: if "car" in concept name → metal=1

### Current Stats
- Only 3 properties assigned total
- 38/41 concepts have ZERO properties
- Reason: Most concepts are abstract WordNet terms

---

## How To Improve

### Better Property Extraction
1. Use ConceptNet HasProperty relations
2. Use VG attribute annotations
3. Use VLM predictions (GPT-4V/Claude)

### Better Topology
1. Add VG relationship annotations ("on", "wearing", "holding")
2. Combine spatial + semantic relations
3. Add visual similarity edges

---

## File Locations

```
/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/sample_2/
├── hcg_data/topology.json           ← 41×41 spatial matrix
├── hcg_data/properties.json         ← 41×30 property matrix
├── TOPOLOGY_AND_PROPERTIES_EXPLAINED.md  ← Detailed explanation
└── RESULTS_SUMMARY.md               ← Full pipeline results
```
