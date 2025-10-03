# WordNet Hierarchy Path Analysis Report

## Overview

**Total Objects**: 21
**Total Unique Nodes**: 80
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
| 9 | 7 |
| 10 | 3 |
| 11 | 2 |

### Granularity Depth Mapping


| Granularity | Depth Range | Average Depth | Concept Count |
|-------------|-------------|---------------|---------------|
| Fine | 2-11 | 7.6 | 16 |
| Mid | 2-5 | 4.5 | 15 |
| Coarse | 1-3 | 2.0 | 5 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | spot, sticker, shape, stem, oranges (+16 more) | 21 |
| physical entity | 1 | spot, sticker, fruit, tip, lemon (+8 more) | 13 |
| object | 2 | spot, fruit, tip, lemon, banana (+6 more) | 11 |
| abstraction | 1 | table, shape, bump, group, pile (+3 more) | 8 |
| whole | 3 | fruit, lemon, banana, orange, oranges (+1 more) | 6 |
| location | 3 | spot, tip, middle, bottom, top | 5 |
| natural object | 4 | fruit, lemon, orange, oranges, apple | 5 |
| plant part | 5 | fruit, lemon, orange, oranges, apple | 5 |
| plant organ | 6 | fruit, lemon, orange, oranges, apple | 5 |
| reproductive structure | 7 | fruit, lemon, orange, oranges, apple | 5 |
| fruit | 8 | fruit, lemon, orange, oranges, apple | 5 |
| region | 4 | middle, top, bottom, tip | 4 |
| group | 2 | pile, group, table, branch | 4 |
| attribute | 2 | bruise, shape, bump | 3 |
| edible fruit | 9 | lemon, oranges, orange | 3 |
| citrus | 10 | lemon, oranges, orange | 3 |
| part | 3 | sticker, stem | 2 |
| process | 2 | sticker, light | 2 |
| orange | 11 | orange, oranges | 2 |
| extremity | 5 | bottom, tip | 2 |

---

## Sample Object Paths


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

### spot

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ location (d=3)
          └─ point (d=4)
            └─ topographic point (d=5)
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

### stem

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ relation (d=2)
        └─ part (d=3)
          └─ language unit (d=4)
            └─ word (d=5)
              └─ form (d=6)
                └─ root (d=7)
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
                    └─ pome (d=9)
                      └─ apple (d=10)
```

### fruit

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

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2396558/sample_2396558/WORDNET_ANALYSIS_REPORT.md
