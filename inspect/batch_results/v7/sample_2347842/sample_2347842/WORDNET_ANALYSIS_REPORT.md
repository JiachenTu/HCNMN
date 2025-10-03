# WordNet Hierarchy Path Analysis Report

## Overview

**Total Objects**: 19
**Total Unique Nodes**: 81
**Merge Points**: 19

---

## Depth Statistics

### Overall Distribution

| Depth | Node Count |
|-------|------------|
| 0 | 2 |
| 1 | 2 |
| 2 | 5 |
| 3 | 6 |
| 4 | 7 |
| 5 | 9 |
| 6 | 12 |
| 7 | 13 |
| 8 | 10 |
| 9 | 9 |
| 10 | 4 |
| 11 | 2 |

### Granularity Depth Mapping


| Granularity | Depth Range | Average Depth | Concept Count |
|-------------|-------------|---------------|---------------|
| Fine | 0-11 | 7.5 | 17 |
| Mid | 0-5 | 4.2 | 10 |
| Coarse | 0-3 | 1.6 | 5 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | skateboard, boy, pants, bicycle, shadow (+13 more) | 18 |
| physical entity | 1 | skateboard, boy, pants, bicycle, person (+10 more) | 15 |
| object | 2 | skateboard, boy, pants, bicycle, person (+9 more) | 14 |
| whole | 3 | skateboard, boy, pants, bicycle, person (+8 more) | 13 |
| artifact | 4 | skateboard, pants, bicycle, ramp, concrete (+3 more) | 8 |
| instrumentality | 5 | ramp, skateboard, bicycle, bench | 4 |
| living thing | 4 | person, boy, skateboarder, grass | 4 |
| organism | 5 | person, boy, skateboarder, grass | 4 |
| person | 6 | person, boy, skateboarder | 3 |
| abstraction | 1 | shadow, people, writing | 3 |
| conveyance | 6 | skateboard, bicycle | 2 |
| vehicle | 7 | skateboard, bicycle | 2 |
| wheeled vehicle | 8 | skateboard, bicycle | 2 |
| commodity | 5 | pants, shirt | 2 |
| consumer goods | 6 | pants, shirt | 2 |
| clothing | 7 | pants, shirt | 2 |
| garment | 8 | pants, shirt | 2 |
| covering | 5 | shoe, hair | 2 |
| extremity | 5 | leg, edge | 2 |

---

## Sample Object Paths


### skateboard

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ conveyance (d=6)
                └─ vehicle (d=7)
                  └─ wheeled vehicle (d=8)
                    └─ skateboard (d=9)
```

### boy

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ living thing (d=4)
            └─ organism (d=5)
              └─ person (d=6)
                └─ male (d=7)
                  └─ male child (d=8)
```

### pants

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
                    └─ undergarment (d=9)
                      └─ underpants (d=10)
                        └─ bloomers (d=11)
```

### concrete

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ paving (d=5)
              └─ concrete (d=6)
```

### people

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ group (d=2)
        └─ people (d=3)
```

### shoe

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ covering (d=5)
              └─ footwear (d=6)
                └─ shoe (d=7)
```

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

### bicycle

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ conveyance (d=6)
                └─ vehicle (d=7)
                  └─ wheeled vehicle (d=8)
                    └─ bicycle (d=9)
```

### shadow

Path to root:
```
  └─ entity (d=0)
    └─ abstraction (d=1)
      └─ attribute (d=2)
        └─ state (d=3)
          └─ illumination (d=4)
            └─ dark (d=5)
              └─ semidarkness (d=6)
                └─ shade (d=7)
                  └─ shadow (d=8)
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

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2347842/sample_2347842/WORDNET_ANALYSIS_REPORT.md
