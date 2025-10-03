# WordNet Hierarchy Path Analysis Report

## Overview

**Total Objects**: 19
**Total Unique Nodes**: 66
**Merge Points**: 24

---

## Depth Statistics

### Overall Distribution

| Depth | Node Count |
|-------|------------|
| 0 | 3 |
| 1 | 2 |
| 2 | 4 |
| 3 | 7 |
| 4 | 9 |
| 5 | 12 |
| 6 | 9 |
| 7 | 9 |
| 8 | 6 |
| 9 | 4 |
| 10 | 1 |

### Granularity Depth Mapping


| Granularity | Depth Range | Average Depth | Concept Count |
|-------------|-------------|---------------|---------------|
| Fine | 0-10 | 6.5 | 15 |
| Mid | 0-6 | 4.3 | 15 |
| Coarse | 0-10 | 2.4 | 8 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | chairs, table, vase, mat, dining table (+12 more) | 17 |
| physical entity | 1 | chairs, vase, mat, dining table, back (+8 more) | 13 |
| object | 2 | chairs, vase, mat, dining table, drawer (+7 more) | 12 |
| whole | 3 | chairs, vase, dining table, cabinet, drawer (+4 more) | 9 |
| artifact | 4 | chairs, vase, dining table, cabinet, drawer (+2 more) | 7 |
| instrumentality | 5 | chairs, vase, dining table, cabinet, chair | 5 |
| furnishing | 6 | chairs, chair, dining table, cabinet | 4 |
| furniture | 7 | chairs, chair, dining table, cabinet | 4 |
| abstraction | 1 | board, table, crack, pink | 4 |
| seat | 8 | chairs, chair | 2 |
| chair | 9 | chairs, chair | 2 |
| group | 2 | board, table | 2 |
| part | 3 | back, handle | 2 |
| location | 3 | tops, tips | 2 |
| region | 4 | tops, tips | 2 |
| attribute | 2 | crack, pink | 2 |
| living thing | 4 | flower, flowers | 2 |
| organism | 5 | flower, flowers | 2 |
| plant | 6 | flower, flowers | 2 |
| vascular plant | 7 | flower, flowers | 2 |

---

## Sample Object Paths


### chairs

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ furnishing (d=6)
                └─ furniture (d=7)
                  └─ seat (d=8)
                    └─ chair (d=9)
```

### vase

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ container (d=6)
                └─ vessel (d=7)
                  └─ jar (d=8)
                    └─ vase (d=9)
```

### board

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ group (d=2)
        └─ social group (d=3)
          └─ organization (d=4)
            └─ unit (d=5)
              └─ administrative unit (d=6)
                └─ committee (d=7)
                  └─ board (d=8)
```

### chair back

Path to root:
```
  └─ chair back (d=0)
```

### handle

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ part (d=3)
          └─ appendage (d=4)
            └─ handle (d=5)
```

### tops

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ location (d=3)
          └─ region (d=4)
            └─ top (d=5)
```

### crack

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ attribute (d=2)
        └─ shape (d=3)
          └─ amorphous shape (d=4)
            └─ space (d=5)
              └─ opening (d=6)
                └─ crack (d=7)
```

### tips

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

### drawer

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ structure (d=5)
              └─ area (d=6)
                └─ storage space (d=7)
                  └─ drawer (d=8)
```

### cabinet

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ furnishing (d=6)
                └─ furniture (d=7)
                  └─ cabinet (d=8)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2364859/sample_2364859/WORDNET_ANALYSIS_REPORT.md
