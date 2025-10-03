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
| Mid | 0-6 | 2.8 | 13 |
| Coarse | 0-2 | 0.4 | 9 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | tracks, woman, skirt, beach, surfboard (+3 more) | 8 |
| physical entity | 1 | tracks, woman, skirt, beach, surfboard (+1 more) | 6 |
| object | 2 | tracks, woman, skirt, beach, surfboard (+1 more) | 6 |
| whole | 3 | woman, surfboard, man, skirt | 4 |
| living thing | 4 | woman, man | 2 |
| organism | 5 | woman, man | 2 |
| person | 6 | woman, man | 2 |
| adult | 7 | woman, man | 2 |
| artifact | 4 | skirt, surfboard | 2 |
| abstraction | 1 | shoes, sand | 2 |

---

## Sample Object Paths


### surf board

Path to root:
```
  └─ surf board (d=0)
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

### long hair

Path to root:
```
  └─ long hair (d=0)
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

### skirt

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ covering (d=5)
              └─ cloth covering (d=6)
                └─ skirt (d=7)
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

### bad sentence

Path to root:
```
  └─ bad sentence (d=0)
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

### white motorcycle

Path to root:
```
  └─ white motorcycle (d=0)
```

### short hair

Path to root:
```
  └─ short hair (d=0)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2326885/sample_2326885/WORDNET_ANALYSIS_REPORT.md
