# WordNet Hierarchy Path Analysis Report

## Overview

**Total Objects**: 13
**Total Unique Nodes**: 59
**Merge Points**: 10

---

## Depth Statistics

### Overall Distribution

| Depth | Node Count |
|-------|------------|
| 0 | 1 |
| 1 | 2 |
| 2 | 3 |
| 3 | 3 |
| 4 | 4 |
| 5 | 9 |
| 6 | 11 |
| 7 | 11 |
| 8 | 9 |
| 9 | 5 |
| 10 | 1 |

### Granularity Depth Mapping


| Granularity | Depth Range | Average Depth | Concept Count |
|-------------|-------------|---------------|---------------|
| Fine | 5-10 | 7.8 | 11 |
| Mid | 4-5 | 4.8 | 6 |
| Coarse | 1-2 | 1.7 | 3 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | cabinet, lid, overflow, wall, floor (+8 more) | 13 |
| physical entity | 1 | cabinet, lid, wall, handle, floor (+7 more) | 12 |
| object | 2 | cabinet, wall, handle, floor, toilet (+6 more) | 11 |
| whole | 3 | cabinet, wall, floor, toilet, towel ring (+5 more) | 10 |
| artifact | 4 | cabinet, wall, floor, toilet, towel ring (+5 more) | 10 |
| structure | 5 | door, wall, cubby, toilet | 4 |
| instrumentality | 5 | cabinet, faucet | 2 |
| part | 3 | lid, handle | 2 |
| area | 6 | cubby, toilet | 2 |
| room | 7 | cubby, toilet | 2 |

---

## Sample Object Paths


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

### lid

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ tissue (d=5)
              └─ animal tissue (d=6)
                └─ flap (d=7)
                  └─ protective fold (d=8)
                    └─ eyelid (d=9)
```

### overflow

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ psychological feature (d=2)
        └─ event (d=3)
          └─ act (d=4)
            └─ action (d=5)
              └─ change (d=6)
                └─ motion (d=7)
                  └─ flow (d=8)
                    └─ flood (d=9)
```

### wall

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ structure (d=5)
              └─ partition (d=6)
                └─ wall (d=7)
```

### floor

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ surface (d=5)
              └─ horizontal surface (d=6)
                └─ floor (d=7)
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

### toilet

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ structure (d=5)
              └─ area (d=6)
                └─ room (d=7)
                  └─ toilet (d=8)
```

### towel ring

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ strip (d=5)
              └─ band (d=6)
                └─ hoop (d=7)
                  └─ towel ring (d=8)
```

### pipe

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ way (d=5)
              └─ passage (d=6)
                └─ conduit (d=7)
                  └─ tube (d=8)
                    └─ pipe (d=9)
```

### door

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
                  └─ movable barrier (d=8)
                    └─ door (d=9)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2406328/sample_2406328/WORDNET_ANALYSIS_REPORT.md
