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
| Mid | 0-6 | 3.6 | 16 |
| Coarse | 0-3 | 1.1 | 9 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | picture, buttons, cellphone, oscar, thumb (+13 more) | 18 |
| physical entity | 1 | picture, buttons, cellphone, thumb, hand (+11 more) | 16 |
| object | 2 | buttons, cellphone, keypad, speaker, shirt (+5 more) | 10 |
| whole | 3 | buttons, cellphone, keypad, speaker, shirt (+5 more) | 10 |
| artifact | 4 | buttons, cellphone, keypad, shirt, latch (+3 more) | 8 |
| thing | 2 | thumb, hand, ear, finger, fingernail (+1 more) | 6 |
| part | 3 | thumb, hand, ear, finger, fingernail (+1 more) | 6 |
| body part | 4 | thumb, hand, ear, finger, fingernail (+1 more) | 6 |
| instrumentality | 5 | buttons, cellphone, keypad, latch, watch (+1 more) | 6 |
| external body part | 5 | finger, thumb, hand, left hand | 4 |
| extremity | 6 | finger, thumb, hand, left hand | 4 |
| device | 6 | latch, buttons, watch | 3 |
| equipment | 6 | keypad, cellphone, phone | 3 |
| electronic equipment | 7 | keypad, cellphone, phone | 3 |
| digit | 7 | finger, thumb | 2 |
| finger | 8 | finger, thumb | 2 |
| living thing | 4 | speaker, man | 2 |
| organism | 5 | speaker, man | 2 |
| person | 6 | speaker, man | 2 |
| restraint | 7 | latch, buttons | 2 |

---

## Sample Object Paths


### thumb

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ external body part (d=5)
              └─ extremity (d=6)
                └─ digit (d=7)
                  └─ finger (d=8)
                    └─ thumb (d=9)
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

### man

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ living thing (d=4)
            └─ organism (d=5)
              └─ person (d=6)
                └─ adult (d=7)
                  └─ man (d=8)
```

### latch

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
                    └─ lock (d=9)
                      └─ latch (d=10)
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

### watch

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ device (d=6)
                └─ instrument (d=7)
                  └─ measuring instrument (d=8)
                    └─ timepiece (d=9)
                      └─ watch (d=10)
```

### watch strap

Path to root:
```
  └─ watch strap (d=0)
```

### copyright symbol

Path to root:
```
  └─ copyright symbol (d=0)
```

### finger

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ external body part (d=5)
              └─ extremity (d=6)
                └─ digit (d=7)
                  └─ finger (d=8)
```

### fingernail

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ structure (d=5)
              └─ horny structure (d=6)
                └─ nail (d=7)
                  └─ fingernail (d=8)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2376855/sample_2376855/WORDNET_ANALYSIS_REPORT.md
