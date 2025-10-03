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
| Mid | 0-5 | 4.3 | 14 |
| Coarse | 0-2 | 1.0 | 5 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | tops, drawer, board, table, handle (+12 more) | 17 |
| physical entity | 1 | tops, drawer, handle, flower, chairs (+8 more) | 13 |
| object | 2 | drawer, tops, handle, flower, chairs (+7 more) | 12 |
| whole | 3 | drawer, flower, chairs, flowers, dining table (+4 more) | 9 |
| artifact | 4 | drawer, chairs, dining table, chair, vase (+2 more) | 7 |
| instrumentality | 5 | chairs, dining table, chair, vase, cabinet | 5 |
| abstraction | 1 | crack, pink, board, table | 4 |
| furnishing | 6 | chairs, chair, dining table, cabinet | 4 |
| furniture | 7 | chairs, chair, dining table, cabinet | 4 |
| living thing | 4 | flower, flowers | 2 |
| organism | 5 | flower, flowers | 2 |
| plant | 6 | flower, flowers | 2 |
| vascular plant | 7 | flower, flowers | 2 |
| spermatophyte | 8 | flower, flowers | 2 |
| angiosperm | 9 | flower, flowers | 2 |
| flower | 10 | flower, flowers | 2 |
| attribute | 2 | crack, pink | 2 |
| seat | 8 | chairs, chair | 2 |
| chair | 9 | chairs, chair | 2 |
| part | 3 | handle, back | 2 |

---

## Sample Object Paths


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

### pink

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ attribute (d=2)
        └─ property (d=3)
          └─ visual property (d=4)
            └─ color (d=5)
              └─ chromatic color (d=6)
                └─ pink (d=7)
```

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

### chair back

Path to root:
```
  └─ chair back (d=0)
```

### back

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ back (d=5)
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

### babys breath

Path to root:
```
  └─ babys breath (d=0)
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

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2364859/sample_2364859/WORDNET_ANALYSIS_REPORT.md
