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
| Mid | 4-5 | 4.8 | 11 |
| Coarse | 1-2 | 1.8 | 4 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | background, flowers, sign, words, street (+13 more) | 18 |
| physical entity | 1 | flowers, street, flower, pot, balcony (+9 more) | 14 |
| object | 2 | flowers, street, flower, pot, balcony (+7 more) | 12 |
| whole | 3 | flowers, street, flower, pot, balcony (+6 more) | 11 |
| artifact | 4 | street, pot, balcony, pole, billboard (+4 more) | 9 |
| abstraction | 1 | background, sign, words, lot | 4 |
| structure | 5 | balcony, billboard, railing | 3 |
| instrumentality | 5 | pole, pot, clock | 3 |
| living thing | 4 | flowers, flower | 2 |
| organism | 5 | flowers, flower | 2 |
| plant | 6 | flowers, flower | 2 |
| vascular plant | 7 | flowers, flower | 2 |
| spermatophyte | 8 | flowers, flower | 2 |
| angiosperm | 9 | flowers, flower | 2 |
| flower | 10 | flowers, flower | 2 |
| way | 5 | stairs, street | 2 |
| communication | 2 | sign, words | 2 |
| implement | 6 | pole, pot | 2 |

---

## Sample Object Paths


### background

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ attribute (d=2)
        └─ inheritance (d=3)
          └─ background (d=4)
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

### words

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ communication (d=2)
        └─ auditory communication (d=3)
          └─ speech (d=4)
            └─ words (d=5)
```

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

### light

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ process (d=2)
        └─ phenomenon (d=3)
          └─ natural phenomenon (d=4)
            └─ physical phenomenon (d=5)
              └─ energy (d=6)
                └─ radiation (d=7)
                  └─ electromagnetic radiation (d=8)
                    └─ actinic radiation (d=9)
                      └─ light (d=10)
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

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_498335/sample_498335/WORDNET_ANALYSIS_REPORT.md
