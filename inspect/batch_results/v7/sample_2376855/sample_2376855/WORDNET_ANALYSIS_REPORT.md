# WordNet Hierarchy Path Analysis Report

## Overview

**Total Objects**: 23
**Total Unique Nodes**: 76
**Merge Points**: 24

---

## Depth Statistics

### Overall Distribution

| Depth | Node Count |
|-------|------------|
| 0 | 6 |
| 1 | 3 |
| 2 | 5 |
| 3 | 5 |
| 4 | 6 |
| 5 | 9 |
| 6 | 9 |
| 7 | 11 |
| 8 | 10 |
| 9 | 8 |
| 10 | 4 |

### Granularity Depth Mapping


| Granularity | Depth Range | Average Depth | Concept Count |
|-------------|-------------|---------------|---------------|
| Fine | 0-10 | 6.1 | 16 |
| Mid | 0-5 | 3.3 | 13 |
| Coarse | 0-2 | 0.9 | 8 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | latch, picture, buttons, shirt, speaker (+13 more) | 18 |
| physical entity | 1 | latch, picture, buttons, shirt, speaker (+11 more) | 16 |
| object | 2 | latch, picture, buttons, shirt, speaker (+5 more) | 10 |
| whole | 3 | latch, picture, buttons, shirt, speaker (+5 more) | 10 |
| artifact | 4 | latch, picture, buttons, shirt, phone (+3 more) | 8 |
| thing | 2 | ear, hand, thumb, fingernail, left hand (+1 more) | 6 |
| part | 3 | ear, hand, thumb, fingernail, left hand (+1 more) | 6 |
| body part | 4 | ear, hand, thumb, fingernail, left hand (+1 more) | 6 |
| instrumentality | 5 | latch, buttons, phone, keypad, watch (+1 more) | 6 |
| external body part | 5 | thumb, left hand, hand, finger | 4 |
| extremity | 6 | thumb, left hand, hand, finger | 4 |
| device | 6 | latch, buttons, watch | 3 |
| equipment | 6 | keypad, phone, cellphone | 3 |
| electronic equipment | 7 | keypad, phone, cellphone | 3 |
| hand | 7 | left hand, hand | 2 |
| restraint | 7 | latch, buttons | 2 |
| fastener | 8 | latch, buttons | 2 |
| abstraction | 1 | oscar, band | 2 |
| telephone | 8 | phone, cellphone | 2 |
| digit | 7 | thumb, finger | 2 |

---

## Sample Object Paths


### shirt

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ commodity (d=5)
              └─ consumer goods (d=6)
                └─ clothing (d=7)
                  └─ garment (d=8)
                    └─ shirt (d=9)
```

### cell phone

Path to root:
```
  └─ act (d=0)
    └─ interact (d=1)
      └─ communicate (d=2)
        └─ telecommunicate (d=3)
          └─ call (d=4)
            └─ cell phone (d=5)
```

### hand

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ external body part (d=5)
              └─ extremity (d=6)
                └─ hand (d=7)
```

### watch strap

Path to root:
```
  └─ watch strap (d=0)
```

### left hand

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ external body part (d=5)
              └─ extremity (d=6)
                └─ hand (d=7)
                  └─ left (d=8)
```

### buttons

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ device (d=6)
                └─ restraint (d=7)
                  └─ fastener (d=8)
                    └─ button (d=9)
```

### pointer finger

Path to root:
```
  └─ pointer finger (d=0)
```

### picture

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ creation (d=5)
              └─ representation (d=6)
                └─ picture (d=7)
```

### ear

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ organ (d=5)
              └─ sense organ (d=6)
                └─ ear (d=7)
```

### keypad

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ equipment (d=6)
                └─ electronic equipment (d=7)
                  └─ peripheral (d=8)
                    └─ data input device (d=9)
                      └─ computer keyboard (d=10)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2376855/sample_2376855/WORDNET_ANALYSIS_REPORT.md
