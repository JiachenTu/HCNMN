# WordNet Hierarchy Path Analysis Report

## Overview

**Total Objects**: 21
**Total Unique Nodes**: 79
**Merge Points**: 26

---

## Depth Statistics

### Overall Distribution

| Depth | Node Count |
|-------|------------|
| 0 | 1 |
| 1 | 2 |
| 2 | 6 |
| 3 | 9 |
| 4 | 12 |
| 5 | 12 |
| 6 | 10 |
| 7 | 9 |
| 8 | 7 |
| 9 | 6 |
| 10 | 3 |
| 11 | 2 |

### Granularity Depth Mapping


| Granularity | Depth Range | Average Depth | Concept Count |
|-------------|-------------|---------------|---------------|
| Fine | 2-11 | 7.6 | 16 |
| Mid | 2-6 | 4.6 | 17 |
| Coarse | 1-9 | 3.6 | 10 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | bottom, group, bump, tip, oranges (+16 more) | 21 |
| physical entity | 1 | fruit, middle, lemon, spot, top (+8 more) | 13 |
| object | 2 | fruit, middle, lemon, spot, top (+6 more) | 11 |
| abstraction | 1 | shape, bump, stem, pile, table (+3 more) | 8 |
| whole | 3 | fruit, lemon, apple, orange, oranges (+1 more) | 6 |
| location | 3 | spot, middle, top, bottom, tip | 5 |
| natural object | 4 | fruit, lemon, apple, orange, oranges | 5 |
| plant part | 5 | fruit, lemon, apple, orange, oranges | 5 |
| plant organ | 6 | fruit, lemon, apple, orange, oranges | 5 |
| reproductive structure | 7 | fruit, lemon, apple, orange, oranges | 5 |
| fruit | 8 | fruit, lemon, apple, orange, oranges | 5 |
| region | 4 | middle, bottom, top, tip | 4 |
| group | 2 | table, group, branch, pile | 4 |
| edible fruit | 9 | oranges, lemon, orange, apple | 4 |
| attribute | 2 | shape, bruise, bump | 3 |
| citrus | 10 | oranges, lemon, orange | 3 |
| extremity | 5 | bottom, tip | 2 |
| state | 3 | bruise, bump | 2 |
| condition | 4 | bruise, bump | 2 |
| physical condition | 5 | bruise, bump | 2 |

---

## Sample Object Paths


### bottom

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ location (d=3)
          └─ region (d=4)
            └─ extremity (d=5)
              └─ boundary (d=6)
                └─ surface (d=7)
                  └─ side (d=8)
                    └─ bottom (d=9)
```

### group

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ group (d=2)
```

### bump

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ attribute (d=2)
        └─ state (d=3)
          └─ condition (d=4)
            └─ physical condition (d=5)
              └─ pathological state (d=6)
                └─ ill health (d=7)
                  └─ injury (d=8)
                    └─ bump (d=9)
```

### tip

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ location (d=3)
          └─ region (d=4)
            └─ extremity (d=5)
              └─ end (d=6)
                └─ tip (d=7)
```

### oranges

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ natural object (d=4)
            └─ plant part (d=5)
              └─ plant organ (d=6)
                └─ reproductive structure (d=7)
                  └─ fruit (d=8)
                    └─ edible fruit (d=9)
                      └─ citrus (d=10)
                        └─ orange (d=11)
```

### branch

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ group (d=2)
        └─ social group (d=3)
          └─ organization (d=4)
            └─ unit (d=5)
              └─ administrative unit (d=6)
                └─ division (d=7)
                  └─ branch (d=8)
```

### bruise

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ attribute (d=2)
        └─ state (d=3)
          └─ condition (d=4)
            └─ physical condition (d=5)
              └─ pathological state (d=6)
                └─ ill health (d=7)
                  └─ injury (d=8)
                    └─ bruise (d=9)
```

### shape

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ attribute (d=2)
        └─ property (d=3)
          └─ spatial property (d=4)
            └─ shape (d=5)
```

### lemon

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ natural object (d=4)
            └─ plant part (d=5)
              └─ plant organ (d=6)
                └─ reproductive structure (d=7)
                  └─ fruit (d=8)
                    └─ edible fruit (d=9)
                      └─ citrus (d=10)
                        └─ lemon (d=11)
```

### orange

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ natural object (d=4)
            └─ plant part (d=5)
              └─ plant organ (d=6)
                └─ reproductive structure (d=7)
                  └─ fruit (d=8)
                    └─ edible fruit (d=9)
                      └─ citrus (d=10)
                        └─ orange (d=11)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2396558/sample_2396558/WORDNET_ANALYSIS_REPORT.md
