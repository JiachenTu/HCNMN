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
| Mid | 0-6 | 4.0 | 19 |
| Coarse | 0-3 | 1.1 | 10 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | bag, ground, kites, tail, strings (+13 more) | 18 |
| physical entity | 1 | bag, ground, tail, clouds, building (+6 more) | 11 |
| object | 2 | bag, ground, building, boy, cones (+3 more) | 8 |
| whole | 3 | bag, building, boy, cones, woman (+2 more) | 7 |
| abstraction | 1 | kites, strings, blue, kite, down (+2 more) | 7 |
| artifact | 4 | bag, shirt, building, cones | 4 |
| living thing | 4 | boy, woman, man | 3 |
| organism | 5 | boy, woman, man | 3 |
| person | 6 | boy, woman, man | 3 |
| adult | 7 | woman, man | 2 |
| group | 2 | strings, people | 2 |
| part | 3 | tail, down | 2 |
| process | 2 | tail, clouds | 2 |
| communication | 2 | kite, kites | 2 |
| written communication | 3 | kite, kites | 2 |
| writing | 4 | kite, kites | 2 |
| document | 5 | kite, kites | 2 |
| legal document | 6 | kite, kites | 2 |
| negotiable instrument | 7 | kite, kites | 2 |
| draft | 8 | kite, kites | 2 |

---

## Sample Object Paths


### ground

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ land (d=3)
```

### blue shirt

Path to root:
```
  └─ blue shirt (d=0)
```

### red kite

Path to root:
```
  └─ red kite (d=0)
```

### woman and boy

Path to root:
```
  └─ woman and boy (d=0)
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

### people

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ group (d=2)
        └─ people (d=3)
```

### strings

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ group (d=2)
        └─ social group (d=3)
          └─ organization (d=4)
            └─ musical organization (d=5)
              └─ section (d=6)
                └─ string section (d=7)
```

### down

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ relation (d=2)
        └─ part (d=3)
          └─ substance (d=4)
            └─ material (d=5)
              └─ animal material (d=6)
                └─ feather (d=7)
                  └─ down (d=8)
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

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2342105/sample_2342105/WORDNET_ANALYSIS_REPORT.md
