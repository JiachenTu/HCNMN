# WordNet Hierarchy Path Analysis Report

## Overview

**Total Objects**: 14
**Total Unique Nodes**: 41
**Merge Points**: 10

---

## Depth Statistics

### Overall Distribution

| Depth | Node Count |
|-------|------------|
| 0 | 7 |
| 1 | 2 |
| 2 | 3 |
| 3 | 5 |
| 4 | 6 |
| 5 | 6 |
| 6 | 5 |
| 7 | 4 |
| 8 | 3 |

### Granularity Depth Mapping


| Granularity | Depth Range | Average Depth | Concept Count |
|-------------|-------------|---------------|---------------|
| Fine | 0-8 | 3.5 | 12 |
| Mid | 0-5 | 2.5 | 13 |
| Coarse | 0-3 | 0.7 | 9 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | shoes, beach, surfboard, tracks, sand (+3 more) | 8 |
| physical entity | 1 | beach, surfboard, tracks, woman, man (+1 more) | 6 |
| object | 2 | beach, surfboard, tracks, woman, man (+1 more) | 6 |
| whole | 3 | skirt, surfboard, man, woman | 4 |
| abstraction | 1 | shoes, sand | 2 |
| artifact | 4 | surfboard, skirt | 2 |
| living thing | 4 | man, woman | 2 |
| organism | 5 | man, woman | 2 |
| person | 6 | man, woman | 2 |
| adult | 7 | man, woman | 2 |

---

## Sample Object Paths


### shoes

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ attribute (d=2)
        └─ state (d=3)
          └─ condition (d=4)
            └─ situation (d=5)
              └─ place (d=6)
```

### beach

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ geological formation (d=3)
          └─ beach (d=4)
```

### surfboard

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ sheet (d=5)
              └─ board (d=6)
                └─ surfboard (d=7)
```

### surf board

Path to root:
```
  └─ surf board (d=0)
```

### no motorcycle

Path to root:
```
  └─ no motorcycle (d=0)
```

### long hair

Path to root:
```
  └─ long hair (d=0)
```

### tracks

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ location (d=3)
          └─ line (d=4)
            └─ path (d=5)
```

### sand

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ relation (d=2)
        └─ part (d=3)
          └─ substance (d=4)
            └─ material (d=5)
              └─ earth (d=6)
                └─ soil (d=7)
                  └─ sand (d=8)
```

### woman

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ living thing (d=4)
            └─ organism (d=5)
              └─ person (d=6)
                └─ adult (d=7)
                  └─ woman (d=8)
```

### short hair

Path to root:
```
  └─ short hair (d=0)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2326885/sample_2326885/WORDNET_ANALYSIS_REPORT.md
