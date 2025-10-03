# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 23
**Unique Fine Concepts**: 23
**Unique Mid Concepts**: 18
**Unique Coarse Concepts**: 8

**Compression Ratios**:
- Fine → Mid: **1.28x**
- Fine → Coarse: **2.88x**
- Mid → Coarse: **2.25x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| extremity | 4 | finger, hand, left hand, thumb |
| device | 2 | buttons, latch |
| equipment | 2 | cellphone, keypad |
| pointer finger | 1 | pointer finger |
| watch strap | 1 | watch strap |
| key pad | 1 | key pad |
| organism | 1 | speaker |
| instrumentality | 1 | watch |
| copyright symbol | 1 | copyright symbol |
| organ | 1 | ear |
| set | 1 | band |
| artifact | 1 | phone |
| structure | 1 | fingernail |
| cell phone | 1 | cell phone |
| commodity | 1 | shirt |
| person | 1 | man |
| representation | 1 | picture |
| academy award | 1 | oscar |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| physical entity | 6 | 9 | device, extremity, organ, organism, person, structure |
| object | 5 | 7 | artifact, commodity, equipment, instrumentality, representation |
| abstraction | 2 | 2 | academy award, set |
| pointer finger | 1 | 1 | pointer finger |
| watch strap | 1 | 1 | watch strap |
| key pad | 1 | 1 | key pad |
| copyright symbol | 1 | 1 | copyright symbol |
| communicate | 1 | 1 | cell phone |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| oscar | academy award | abstraction |
| band | set | abstraction |
| cell phone | cell phone | communicate |
| copyright symbol | copyright symbol | copyright symbol |
| key pad | key pad | key pad |
| phone | artifact | object |
| shirt | commodity | object |
| buttons | device | object |
| cellphone | equipment | object |
| keypad | equipment | object |
| watch | instrumentality | object |
| picture | representation | object |
| latch | device | physical entity |
| finger | extremity | physical entity |
| hand | extremity | physical entity |
| left hand | extremity | physical entity |
| thumb | extremity | physical entity |
| ear | organ | physical entity |
| speaker | organism | physical entity |
| man | person | physical entity |
| fingernail | structure | physical entity |
| pointer finger | pointer finger | pointer finger |
| watch strap | watch strap | watch strap |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2376855/sample_2376855/CONCEPT_MAPPING_REPORT.md
