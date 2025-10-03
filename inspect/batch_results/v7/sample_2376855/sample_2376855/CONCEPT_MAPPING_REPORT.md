# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 23
**Unique Fine Concepts**: 23
**Unique Mid Concepts**: 13
**Unique Coarse Concepts**: 8

**Compression Ratios**:
- Fine → Mid: **1.77x**
- Fine → Coarse: **2.88x**
- Mid → Coarse: **1.62x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| instrumentality | 6 | buttons, cellphone, keypad, latch, phone, watch |
| external body part | 4 | finger, hand, left hand, thumb |
| artifact | 2 | picture, shirt |
| organism | 2 | man, speaker |
| cell phone | 1 | cell phone |
| watch strap | 1 | watch strap |
| pointer finger | 1 | pointer finger |
| organ | 1 | ear |
| set | 1 | band |
| copyright symbol | 1 | copyright symbol |
| award | 1 | oscar |
| key pad | 1 | key pad |
| structure | 1 | fingernail |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 3 | 10 | artifact, instrumentality, organism |
| thing | 3 | 6 | external body part, organ, structure |
| abstraction | 2 | 2 | award, set |
| communicate | 1 | 1 | cell phone |
| watch strap | 1 | 1 | watch strap |
| pointer finger | 1 | 1 | pointer finger |
| copyright symbol | 1 | 1 | copyright symbol |
| key pad | 1 | 1 | key pad |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| oscar | award | abstraction |
| band | set | abstraction |
| cell phone | cell phone | communicate |
| copyright symbol | copyright symbol | copyright symbol |
| key pad | key pad | key pad |
| picture | artifact | object |
| shirt | artifact | object |
| buttons | instrumentality | object |
| cellphone | instrumentality | object |
| keypad | instrumentality | object |
| latch | instrumentality | object |
| phone | instrumentality | object |
| watch | instrumentality | object |
| man | organism | object |
| speaker | organism | object |
| pointer finger | pointer finger | pointer finger |
| finger | external body part | thing |
| hand | external body part | thing |
| left hand | external body part | thing |
| thumb | external body part | thing |
| ear | organ | thing |
| fingernail | structure | thing |
| watch strap | watch strap | watch strap |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2376855/sample_2376855/CONCEPT_MAPPING_REPORT.md
