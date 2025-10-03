# WordNet Hierarchy Path Analysis Report

## Overview

**Total Objects**: 9
**Total Unique Nodes**: 39
**Merge Points**: 7

---

## Depth Statistics

### Overall Distribution

| Depth | Node Count |
|-------|------------|
| 0 | 2 |
| 1 | 1 |
| 2 | 2 |
| 3 | 2 |
| 4 | 2 |
| 5 | 5 |
| 6 | 8 |
| 7 | 7 |
| 8 | 5 |
| 9 | 2 |
| 10 | 2 |
| 11 | 1 |

### Granularity Depth Mapping


| Granularity | Depth Range | Average Depth | Concept Count |
|-------------|-------------|---------------|---------------|
| Fine | 0-11 | 7.2 | 8 |
| Mid | 0-5 | 3.8 | 5 |
| Coarse | 0-2 | 1.3 | 3 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | street, building, emblem, car, steps (+3 more) | 8 |
| physical entity | 1 | street, building, emblem, car, steps (+3 more) | 8 |
| object | 2 | street, building, emblem, car, steps (+2 more) | 7 |
| whole | 3 | street, building, emblem, car, steps (+2 more) | 7 |
| artifact | 4 | street, building, emblem, car, steps (+2 more) | 7 |
| way | 5 | street, steps, sidewalk | 3 |
| structure | 5 | building, window | 2 |

---

## Sample Object Paths


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

### building

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ structure (d=5)
              └─ building (d=6)
```

### emblem

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ decoration (d=5)
              └─ design (d=6)
                └─ emblem (d=7)
```

### car

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ conveyance (d=6)
                └─ vehicle (d=7)
                  └─ wheeled vehicle (d=8)
                    └─ self-propelled vehicle (d=9)
                      └─ motor vehicle (d=10)
                        └─ car (d=11)
```

### steps

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

### window

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ structure (d=5)
              └─ supporting structure (d=6)
                └─ framework (d=7)
                  └─ window (d=8)
```

### street.

Path to root:
```
  └─ street. (d=0)
```

### sidewalk

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ way (d=5)
              └─ path (d=6)
                └─ walk (d=7)
                  └─ sidewalk (d=8)
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

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_713619/sample_713619/WORDNET_ANALYSIS_REPORT.md
