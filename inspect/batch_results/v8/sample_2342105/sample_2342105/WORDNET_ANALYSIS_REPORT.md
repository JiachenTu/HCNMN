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
| Mid | 0-6 | 3.6 | 20 |
| Coarse | 0-2 | 1.2 | 13 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | clouds, sky, kite, man, hands (+13 more) | 18 |
| physical entity | 1 | clouds, sky, woman, man, ground (+6 more) | 11 |
| object | 2 | woman, man, ground, boy, cones (+3 more) | 8 |
| whole | 3 | woman, man, boy, cones, bag (+2 more) | 7 |
| abstraction | 1 | kite, hands, strings, blue, people (+2 more) | 7 |
| artifact | 4 | bag, shirt, cones, building | 4 |
| living thing | 4 | woman, boy, man | 3 |
| organism | 5 | woman, boy, man | 3 |
| person | 6 | woman, boy, man | 3 |
| process | 2 | clouds, tail | 2 |
| adult | 7 | woman, man | 2 |
| communication | 2 | kite, kites | 2 |
| written communication | 3 | kite, kites | 2 |
| writing | 4 | kite, kites | 2 |
| document | 5 | kite, kites | 2 |
| legal document | 6 | kite, kites | 2 |
| negotiable instrument | 7 | kite, kites | 2 |
| draft | 8 | kite, kites | 2 |
| check | 9 | kite, kites | 2 |
| kite | 10 | kite, kites | 2 |

---

## Sample Object Paths


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

### blue shirt

Path to root:
```
  └─ blue shirt (d=0)
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

### woman and boy

Path to root:
```
  └─ woman and boy (d=0)
```

### building

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ structure (d=5)
              └─ building (d=6)
```

### ladybug kites

Path to root:
```
  └─ ladybug kites (d=0)
```

### kite

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ communication (d=2)
        └─ written communication (d=3)
          └─ writing (d=4)
            └─ document (d=5)
              └─ legal document (d=6)
                └─ negotiable instrument (d=7)
                  └─ draft (d=8)
                    └─ check (d=9)
                      └─ kite (d=10)
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

### people

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ group (d=2)
        └─ people (d=3)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2342105/sample_2342105/WORDNET_ANALYSIS_REPORT.md
