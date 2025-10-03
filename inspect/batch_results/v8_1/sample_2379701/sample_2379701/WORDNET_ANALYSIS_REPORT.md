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
| Mid | 3-9 | 5.2 | 17 |
| Coarse | 1-2 | 1.3 | 3 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | leg, air, ground, shirt, headband (+13 more) | 18 |
| physical entity | 1 | leg, air, ground, shirt, headband (+7 more) | 12 |
| object | 2 | ground, shirt, headband, shoe, woman (+4 more) | 9 |
| whole | 3 | shirt, headband, shoe, woman, hair (+3 more) | 8 |
| artifact | 4 | shirt, headband, wall, shoe, shorts (+1 more) | 6 |
| abstraction | 1 | dirt, letters, racket, writing, court (+1 more) | 6 |
| part | 3 | leg, dirt, foot | 3 |
| psychological feature | 2 | racket, letters, writing | 3 |
| thing | 2 | leg, foot | 2 |
| body part | 4 | leg, foot | 2 |
| external body part | 5 | leg, foot | 2 |
| extremity | 6 | leg, foot | 2 |
| commodity | 5 | shirt, shorts | 2 |
| consumer goods | 6 | shirt, shorts | 2 |
| clothing | 7 | shirt, shorts | 2 |
| garment | 8 | shirt, shorts | 2 |
| covering | 5 | hair, shoe | 2 |
| event | 3 | racket, writing | 2 |

---

## Sample Object Paths


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

### air

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ matter (d=2)
        └─ fluid (d=3)
          └─ gas (d=4)
            └─ air (d=5)
```

### ground

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ land (d=3)
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

### letters

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ psychological feature (d=2)
        └─ cognition (d=3)
          └─ process (d=4)
            └─ basic cognitive process (d=5)
              └─ discrimination (d=6)
                └─ taste (d=7)
                  └─ culture (d=8)
                    └─ letters (d=9)
```

### dirt

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ relation (d=2)
        └─ part (d=3)
          └─ substance (d=4)
            └─ material (d=5)
              └─ earth (d=6)
                └─ soil (d=7)
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

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2379701/sample_2379701/WORDNET_ANALYSIS_REPORT.md
