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
| Mid | 2-6 | 4.5 | 17 |
| Coarse | 1-3 | 1.8 | 4 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | top, middle, bruise, sticker, oranges (+16 more) | 21 |
| physical entity | 1 | light, apple, lemon, spot, top (+8 more) | 13 |
| object | 2 | apple, lemon, spot, top, middle (+6 more) | 11 |
| abstraction | 1 | table, group, bruise, bump, branch (+3 more) | 8 |
| whole | 3 | apple, lemon, oranges, orange, banana (+1 more) | 6 |
| location | 3 | spot, top, middle, tip, bottom | 5 |
| natural object | 4 | apple, lemon, oranges, orange, fruit | 5 |
| plant part | 5 | apple, lemon, oranges, orange, fruit | 5 |
| plant organ | 6 | apple, lemon, oranges, orange, fruit | 5 |
| reproductive structure | 7 | apple, lemon, oranges, orange, fruit | 5 |
| fruit | 8 | apple, lemon, oranges, orange, fruit | 5 |
| region | 4 | bottom, top, middle, tip | 4 |
| edible fruit | 9 | oranges, orange, apple, lemon | 4 |
| group | 2 | table, group, pile, branch | 4 |
| attribute | 2 | bump, shape, bruise | 3 |
| citrus | 10 | oranges, orange, lemon | 3 |
| state | 3 | bump, bruise | 2 |
| condition | 4 | bump, bruise | 2 |
| physical condition | 5 | bump, bruise | 2 |
| pathological state | 6 | bump, bruise | 2 |

---

## Sample Object Paths


### top

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ location (d=3)
          └─ region (d=4)
            └─ top (d=5)
```

### middle

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ location (d=3)
          └─ region (d=4)
            └─ area (d=5)
              └─ center (d=6)
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

### sticker

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ process (d=5)
              └─ plant process (d=6)
                └─ aculeus (d=7)
                  └─ spine (d=8)
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

### table

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ group (d=2)
        └─ arrangement (d=3)
          └─ array (d=4)
            └─ table (d=5)
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

### group

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ group (d=2)
```

### apple

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
                      └─ apple (d=10)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2396558/sample_2396558/WORDNET_ANALYSIS_REPORT.md
