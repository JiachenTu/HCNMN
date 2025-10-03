# WordNet Hierarchy Path Analysis Report

## Overview

**Total Objects**: 18
**Total Unique Nodes**: 80
**Merge Points**: 18

---

## Depth Statistics

### Overall Distribution

| Depth | Node Count |
|-------|------------|
| 0 | 1 |
| 1 | 2 |
| 2 | 7 |
| 3 | 8 |
| 4 | 11 |
| 5 | 13 |
| 6 | 13 |
| 7 | 13 |
| 8 | 7 |
| 9 | 4 |
| 10 | 1 |

### Granularity Depth Mapping


| Granularity | Depth Range | Average Depth | Concept Count |
|-------------|-------------|---------------|---------------|
| Fine | 4-9 | 7.3 | 15 |
| Mid | 3-5 | 4.7 | 14 |
| Coarse | 1-2 | 1.8 | 4 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | hair, wall, headband, woman, ball (+13 more) | 18 |
| physical entity | 1 | wall, headband, woman, ball, shorts (+7 more) | 12 |
| object | 2 | wall, headband, woman, ball, shorts (+4 more) | 9 |
| whole | 3 | wall, headband, woman, ball, shorts (+3 more) | 8 |
| artifact | 4 | wall, headband, ball, shorts, shirt (+1 more) | 6 |
| abstraction | 1 | dirt, background, letters, writing, racket (+1 more) | 6 |
| psychological feature | 2 | writing, letters, racket | 3 |
| part | 3 | foot, leg, dirt | 3 |
| event | 3 | writing, racket | 2 |
| commodity | 5 | shorts, shirt | 2 |
| consumer goods | 6 | shorts, shirt | 2 |
| clothing | 7 | shorts, shirt | 2 |
| garment | 8 | shorts, shirt | 2 |
| thing | 2 | foot, leg | 2 |
| body part | 4 | foot, leg | 2 |
| external body part | 5 | foot, leg | 2 |
| extremity | 6 | foot, leg | 2 |
| covering | 5 | shoe, hair | 2 |

---

## Sample Object Paths


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

### racket

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ psychological feature (d=2)
        └─ event (d=3)
          └─ happening (d=4)
            └─ sound (d=5)
              └─ noise (d=6)
                └─ racket (d=7)
```

### headband

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ strip (d=5)
              └─ band (d=6)
                └─ headband (d=7)
```

### ball

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ equipment (d=6)
                └─ game equipment (d=7)
                  └─ ball (d=8)
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

### shorts

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
                    └─ trouser (d=9)
                      └─ short pants (d=10)
```

### foot

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ external body part (d=5)
              └─ extremity (d=6)
                └─ vertebrate foot (d=7)
                  └─ foot (d=8)
```

### leg

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ thing (d=2)
        └─ part (d=3)
          └─ body part (d=4)
            └─ external body part (d=5)
              └─ extremity (d=6)
                └─ limb (d=7)
                  └─ leg (d=8)
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

### background

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ attribute (d=2)
        └─ inheritance (d=3)
          └─ background (d=4)
```

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2379701/sample_2379701/WORDNET_ANALYSIS_REPORT.md
