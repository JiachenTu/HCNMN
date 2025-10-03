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
| Mid | 0-6 | 4.5 | 16 |
| Coarse | 0-2 | 1.0 | 6 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | chair, crack, flowers, vase, mat (+12 more) | 17 |
| physical entity | 1 | chair, flowers, vase, mat, tips (+8 more) | 13 |
| object | 2 | chair, flowers, vase, mat, tips (+7 more) | 12 |
| whole | 3 | chair, flowers, vase, mat, flower (+4 more) | 9 |
| artifact | 4 | chair, mat, vase, chairs, dining table (+2 more) | 7 |
| instrumentality | 5 | chair, vase, chairs, dining table, cabinet | 5 |
| abstraction | 1 | crack, board, pink, table | 4 |
| furnishing | 6 | chair, dining table, cabinet, chairs | 4 |
| furniture | 7 | chair, dining table, cabinet, chairs | 4 |
| living thing | 4 | flower, flowers | 2 |
| organism | 5 | flower, flowers | 2 |
| plant | 6 | flower, flowers | 2 |
| vascular plant | 7 | flower, flowers | 2 |
| spermatophyte | 8 | flower, flowers | 2 |
| angiosperm | 9 | flower, flowers | 2 |
| flower | 10 | flower, flowers | 2 |
| group | 2 | board, table | 2 |
| seat | 8 | chair, chairs | 2 |
| chair | 9 | chair, chairs | 2 |
| attribute | 2 | crack, pink | 2 |

---

## Sample Object Paths


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

### chair

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

### mat

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ covering (d=5)
              └─ floor cover (d=6)
                └─ mat (d=7)
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

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2364859/sample_2364859/WORDNET_ANALYSIS_REPORT.md
