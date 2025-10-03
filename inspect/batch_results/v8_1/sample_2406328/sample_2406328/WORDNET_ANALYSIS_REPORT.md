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
| Mid | 5-6 | 5.4 | 10 |
| Coarse | 1-2 | 1.3 | 3 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | faucet, door, overflow, cubby, wall (+8 more) | 13 |
| physical entity | 1 | faucet, door, cubby, lid, wall (+7 more) | 12 |
| object | 2 | faucet, door, cubby, wall, toilet (+6 more) | 11 |
| whole | 3 | faucet, door, cubby, wall, toilet (+5 more) | 10 |
| artifact | 4 | faucet, door, cubby, wall, toilet (+5 more) | 10 |
| structure | 5 | wall, door, toilet, cubby | 4 |
| instrumentality | 5 | faucet, cabinet | 2 |
| area | 6 | cubby, toilet | 2 |
| room | 7 | cubby, toilet | 2 |
| part | 3 | lid, handle | 2 |

---

## Sample Object Paths


### faucet

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ device (d=6)
                └─ mechanism (d=7)
                  └─ control (d=8)
                    └─ regulator (d=9)
                      └─ faucet (d=10)
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

### cubby

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
                  └─ cubby (d=8)
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

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2406328/sample_2406328/WORDNET_ANALYSIS_REPORT.md
