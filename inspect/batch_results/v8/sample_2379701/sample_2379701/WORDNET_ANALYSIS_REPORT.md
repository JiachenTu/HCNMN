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
| Mid | 3-6 | 4.6 | 16 |
| Coarse | 1-2 | 1.7 | 6 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | hair, ground, writing, letters, court (+13 more) | 18 |
| physical entity | 1 | hair, ground, leg, shirt, shoe (+7 more) | 12 |
| object | 2 | hair, ground, shirt, shoe, shorts (+4 more) | 9 |
| whole | 3 | hair, shirt, shoe, shorts, woman (+3 more) | 8 |
| abstraction | 1 | writing, letters, court, background, dirt (+1 more) | 6 |
| artifact | 4 | shirt, shoe, shorts, wall, ball (+1 more) | 6 |
| psychological feature | 2 | writing, racket, letters | 3 |
| part | 3 | leg, foot, dirt | 3 |
| covering | 5 | hair, shoe | 2 |
| event | 3 | writing, racket | 2 |
| thing | 2 | leg, foot | 2 |
| body part | 4 | leg, foot | 2 |
| external body part | 5 | leg, foot | 2 |
| extremity | 6 | leg, foot | 2 |
| commodity | 5 | shorts, shirt | 2 |
| consumer goods | 6 | shorts, shirt | 2 |
| clothing | 7 | shorts, shirt | 2 |
| garment | 8 | shorts, shirt | 2 |

---

## Sample Object Paths


### hair

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ natural object (d=4)
            └─ covering (d=5)
              └─ body covering (d=6)
                └─ hair (d=7)
```

### ground

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ land (d=3)
```

### writing

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ psychological feature (d=2)
        └─ event (d=3)
          └─ act (d=4)
            └─ activity (d=5)
              └─ creation (d=6)
                └─ creating by mental acts (d=7)
                  └─ verbal creation (d=8)
                    └─ writing (d=9)
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

### court

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ group (d=2)
        └─ social group (d=3)
          └─ gathering (d=4)
            └─ assembly (d=5)
              └─ court (d=6)
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

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2379701/sample_2379701/WORDNET_ANALYSIS_REPORT.md
