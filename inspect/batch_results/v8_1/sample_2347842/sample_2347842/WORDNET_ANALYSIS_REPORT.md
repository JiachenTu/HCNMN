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
| Mid | 0-9 | 5.1 | 15 |
| Coarse | 0-2 | 1.2 | 5 |

---

## Top Merge Points

Nodes where multiple object paths converge:

| Node | Depth | Merged Objects | Count |
|------|-------|----------------|-------|
| entity | 0 | leg, bicycle, ramp, bench, shadow (+13 more) | 18 |
| physical entity | 1 | leg, bicycle, ramp, bench, edge (+10 more) | 15 |
| object | 2 | bicycle, ramp, bench, edge, skateboarder (+9 more) | 14 |
| whole | 3 | bicycle, ramp, bench, skateboarder, person (+8 more) | 13 |
| artifact | 4 | bicycle, ramp, bench, pants, shoe (+3 more) | 8 |
| instrumentality | 5 | bench, bicycle, skateboard, ramp | 4 |
| living thing | 4 | boy, grass, skateboarder, person | 4 |
| organism | 5 | boy, grass, skateboarder, person | 4 |
| person | 6 | boy, skateboarder, person | 3 |
| abstraction | 1 | shadow, people, writing | 3 |
| extremity | 5 | leg, edge | 2 |
| conveyance | 6 | bicycle, skateboard | 2 |
| vehicle | 7 | bicycle, skateboard | 2 |
| wheeled vehicle | 8 | bicycle, skateboard | 2 |
| commodity | 5 | pants, shirt | 2 |
| consumer goods | 6 | pants, shirt | 2 |
| clothing | 7 | pants, shirt | 2 |
| garment | 8 | pants, shirt | 2 |
| covering | 5 | hair, shoe | 2 |

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

### bench

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ instrumentality (d=5)
              └─ furnishing (d=6)
                └─ furniture (d=7)
                  └─ seat (d=8)
                    └─ bench (d=9)
```

### edge

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ location (d=3)
          └─ region (d=4)
            └─ extremity (d=5)
              └─ boundary (d=6)
                └─ edge (d=7)
```

### person

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ living thing (d=4)
            └─ organism (d=5)
              └─ person (d=6)
```

### skateboarder

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ living thing (d=4)
            └─ organism (d=5)
              └─ person (d=6)
                └─ contestant (d=7)
                  └─ athlete (d=8)
                    └─ skater (d=9)
                      └─ skateboarder (d=10)
```

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

### concrete

Path to root:
```
  └─ entity (d=0)
    └─ physical entity (d=1)
      └─ object (d=2)
        └─ whole (d=3)
          └─ artifact (d=4)
            └─ building material (d=5)
              └─ concrete (d=6)
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

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2347842/sample_2347842/WORDNET_ANALYSIS_REPORT.md
