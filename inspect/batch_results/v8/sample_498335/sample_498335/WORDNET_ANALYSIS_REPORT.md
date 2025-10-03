# WordNet Hierarchy Path Analysis Report

## Overview

**Total Objects**: 18
**Total Unique Nodes**: 77
**Merge Points**: 18

---

## Depth Statistics

### Overall Distribution

| Depth | Node Count |
|-------|------------|
| 0 | 1 |
| 1 | 2 |
| 2 | 6 |
| 3 | 8 |
| 4 | 9 |
| 5 | 11 |
| 6 | 13 |
| 7 | 11 |
| 8 | 8 |
| 9 | 4 |
| 10 | 4 |

### Granularity Depth Mapping


| Granularity | Depth Range | Average Depth | Concept Count |
|-------------|-------------|---------------|---------------|
| Fine | 4-10 | 7.5 | 16 |
| Mid | 4-6 | 4.9 | 13 |
| Coarse | 1-3 | 2.1 | 8 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | railing, letter, edge, pole, flowers (+13 more) | 18 |
| physical entity | 1 | railing, letter, edge, pole, flowers (+9 more) | 14 |
| object | 2 | railing, letter, edge, pole, flowers (+7 more) | 12 |
| whole | 3 | railing, letter, pole, flowers, balcony (+6 more) | 11 |
| artifact | 4 | railing, letter, pole, balcony, street (+4 more) | 9 |
| abstraction | 1 | words, background, sign, lot | 4 |
| structure | 5 | billboard, railing, balcony | 3 |
| instrumentality | 5 | pole, clock, pot | 3 |
| implement | 6 | pole, pot | 2 |
| living thing | 4 | flowers, flower | 2 |
| organism | 5 | flowers, flower | 2 |
| plant | 6 | flowers, flower | 2 |
| vascular plant | 7 | flowers, flower | 2 |
| spermatophyte | 8 | flowers, flower | 2 |
| angiosperm | 9 | flowers, flower | 2 |
| flower | 10 | flowers, flower | 2 |
| way | 5 | stairs, street | 2 |
| communication | 2 | words, sign | 2 |

---

## Sample Object Paths


### railing

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ structure (d=5)
              └─ obstruction (d=6)
                └─ barrier (d=7)
                  └─ railing (d=8)
```

### letter

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ creation (d=5)
              └─ representation (d=6)
                └─ document (d=7)
                  └─ letter (d=8)
```

### edge

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ location (d=3)
          └─ region (d=4)
            └─ extremity (d=5)
              └─ boundary (d=6)
                └─ edge (d=7)
```

### pole

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ implement (d=6)
                └─ rod (d=7)
                  └─ pole (d=8)
```

### flowers

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ living thing (d=4)
            └─ organism (d=5)
              └─ plant (d=6)
                └─ vascular plant (d=7)
                  └─ spermatophyte (d=8)
                    └─ angiosperm (d=9)
                      └─ flower (d=10)
```

### lot

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ measure (d=2)
        └─ indefinite quantity (d=3)
          └─ large indefinite quantity (d=4)
            └─ batch (d=5)
```

### balcony

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ structure (d=5)
              └─ balcony (d=6)
```

### face

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ external body part (d=5)
              └─ face (d=6)
```

### street

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ way (d=5)
              └─ road (d=6)
                └─ thoroughfare (d=7)
                  └─ street (d=8)
```

### clock

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ device (d=6)
                └─ instrument (d=7)
                  └─ measuring instrument (d=8)
                    └─ timepiece (d=9)
                      └─ clock (d=10)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_498335/sample_498335/WORDNET_ANALYSIS_REPORT.md
