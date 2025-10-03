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
| Mid | 4-6 | 5.3 | 15 |
| Coarse | 1-2 | 1.5 | 4 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | clock, sign, flower, stairs, pot (+13 more) | 18 |
| physical entity | 1 | clock, flower, stairs, pot, edge (+9 more) | 14 |
| object | 2 | clock, flower, stairs, pot, edge (+7 more) | 12 |
| whole | 3 | clock, flower, stairs, pot, letter (+6 more) | 11 |
| artifact | 4 | clock, stairs, pot, letter, street (+4 more) | 9 |
| abstraction | 1 | words, lot, sign, background | 4 |
| instrumentality | 5 | clock, pole, pot | 3 |
| structure | 5 | billboard, railing, balcony | 3 |
| communication | 2 | words, sign | 2 |
| living thing | 4 | flower, flowers | 2 |
| organism | 5 | flower, flowers | 2 |
| plant | 6 | flower, flowers | 2 |
| vascular plant | 7 | flower, flowers | 2 |
| spermatophyte | 8 | flower, flowers | 2 |
| angiosperm | 9 | flower, flowers | 2 |
| flower | 10 | flower, flowers | 2 |
| implement | 6 | pole, pot | 2 |
| way | 5 | street, stairs | 2 |

---

## Sample Object Paths


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

### sign

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ communication (d=2)
        └─ indication (d=3)
          └─ evidence (d=4)
            └─ clue (d=5)
              └─ sign (d=6)
```

### flower

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

### pot

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ implement (d=6)
                └─ utensil (d=7)
                  └─ kitchen utensil (d=8)
                    └─ cooking utensil (d=9)
                      └─ pot (d=10)
```

### stairs

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ way (d=5)
              └─ stairway (d=6)
                └─ stairs (d=7)
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

### background

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ attribute (d=2)
        └─ inheritance (d=3)
          └─ background (d=4)
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

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_498335/sample_498335/WORDNET_ANALYSIS_REPORT.md
