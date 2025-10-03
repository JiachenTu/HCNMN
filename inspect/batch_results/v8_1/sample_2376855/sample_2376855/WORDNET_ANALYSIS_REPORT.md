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
| Mid | 0-6 | 4.1 | 18 |
| Coarse | 0-2 | 0.8 | 8 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | phone, thumb, fingernail, finger, latch (+13 more) | 18 |
| physical entity | 1 | phone, thumb, fingernail, finger, latch (+11 more) | 16 |
| object | 2 | phone, latch, shirt, cellphone, buttons (+5 more) | 10 |
| whole | 3 | phone, latch, shirt, cellphone, buttons (+5 more) | 10 |
| artifact | 4 | phone, latch, shirt, cellphone, buttons (+3 more) | 8 |
| instrumentality | 5 | phone, latch, cellphone, buttons, watch (+1 more) | 6 |
| thing | 2 | thumb, fingernail, finger, ear, left hand (+1 more) | 6 |
| part | 3 | thumb, fingernail, finger, ear, left hand (+1 more) | 6 |
| body part | 4 | thumb, fingernail, finger, ear, left hand (+1 more) | 6 |
| external body part | 5 | finger, left hand, hand, thumb | 4 |
| extremity | 6 | finger, left hand, hand, thumb | 4 |
| device | 6 | latch, watch, buttons | 3 |
| equipment | 6 | cellphone, phone, keypad | 3 |
| electronic equipment | 7 | cellphone, phone, keypad | 3 |
| restraint | 7 | latch, buttons | 2 |
| fastener | 8 | latch, buttons | 2 |
| hand | 7 | left hand, hand | 2 |
| telephone | 8 | cellphone, phone | 2 |
| living thing | 4 | speaker, man | 2 |
| organism | 5 | speaker, man | 2 |

---

## Sample Object Paths


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

### pointer finger

Path to root:
```
  └─ pointer finger (d=0)
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

### watch strap

Path to root:
```
  └─ watch strap (d=0)
```

### key pad

Path to root:
```
  └─ key pad (d=0)
```

### cellphone

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
                  └─ telephone (d=8)
                    └─ radiotelephone (d=9)
                      └─ cellular telephone (d=10)
```

### speaker

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ living thing (d=4)
            └─ organism (d=5)
              └─ person (d=6)
                └─ communicator (d=7)
                  └─ articulator (d=8)
                    └─ speaker (d=9)
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

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2376855/sample_2376855/WORDNET_ANALYSIS_REPORT.md
