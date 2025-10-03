# WordNet Hierarchy Path Analysis Report

## Overview

**Total Objects**: 22
**Total Unique Nodes**: 80
**Merge Points**: 22

---

## Depth Statistics

### Overall Distribution

| Depth | Node Count |
|-------|------------|
| 0 | 5 |
| 1 | 2 |
| 2 | 9 |
| 3 | 10 |
| 4 | 10 |
| 5 | 12 |
| 6 | 12 |
| 7 | 9 |
| 8 | 7 |
| 9 | 3 |
| 10 | 1 |

### Granularity Depth Mapping


| Granularity | Depth Range | Average Depth | Concept Count |
|-------------|-------------|---------------|---------------|
| Fine | 0-10 | 5.4 | 16 |
| Mid | 0-5 | 3.4 | 18 |
| Coarse | 0-2 | 1.0 | 9 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | woman, bag, shirt, cones, people (+13 more) | 18 |
| physical entity | 1 | woman, bag, shirt, cones, sky (+6 more) | 11 |
| object | 2 | woman, bag, shirt, cones, man (+3 more) | 8 |
| whole | 3 | woman, bag, shirt, cones, man (+2 more) | 7 |
| abstraction | 1 | people, hands, kite, down, blue (+2 more) | 7 |
| artifact | 4 | building, shirt, bag, cones | 4 |
| living thing | 4 | man, woman, boy | 3 |
| organism | 5 | man, woman, boy | 3 |
| person | 6 | man, woman, boy | 3 |
| process | 2 | tail, clouds | 2 |
| adult | 7 | man, woman | 2 |
| part | 3 | tail, down | 2 |
| communication | 2 | kite, kites | 2 |
| written communication | 3 | kite, kites | 2 |
| writing | 4 | kite, kites | 2 |
| document | 5 | kite, kites | 2 |
| legal document | 6 | kite, kites | 2 |
| negotiable instrument | 7 | kite, kites | 2 |
| draft | 8 | kite, kites | 2 |
| check | 9 | kite, kites | 2 |

---

## Sample Object Paths


### woman and boy

Path to root:
```
  └─ woman and boy (d=0)
```

### bag

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ container (d=6)
                └─ bag (d=7)
```

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

### clouds

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ process (d=2)
        └─ phenomenon (d=3)
          └─ natural phenomenon (d=4)
            └─ physical phenomenon (d=5)
              └─ cloud (d=6)
```

### ladybug kites

Path to root:
```
  └─ ladybug kites (d=0)
```

### woman

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
                  └─ woman (d=8)
```

### hands

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ psychological feature (d=2)
        └─ event (d=3)
          └─ act (d=4)
            └─ group action (d=5)
              └─ social control (d=6)
                └─ duty (d=7)
                  └─ guardianship (d=8)
                    └─ hands (d=9)
```

### sky

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ matter (d=2)
        └─ fluid (d=3)
          └─ gas (d=4)
            └─ atmosphere (d=5)
              └─ sky (d=6)
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

### tail

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ process (d=5)
              └─ tail (d=6)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2342105/sample_2342105/WORDNET_ANALYSIS_REPORT.md
