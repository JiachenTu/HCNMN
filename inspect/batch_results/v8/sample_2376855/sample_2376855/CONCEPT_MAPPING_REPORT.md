# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 23
**Unique Fine Concepts**: 23
**Unique Mid Concepts**: 16
**Unique Coarse Concepts**: 9

**Compression Ratios**:
- Fine → Mid: **1.44x**
- Fine → Coarse: **2.56x**
- Mid → Coarse: **1.78x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| body part | 5 | finger, fingernail, hand, left hand, thumb |
| equipment | 3 | cellphone, keypad, phone |
| artifact | 2 | latch, watch |
| cell phone | 1 | cell phone |
| living thing | 1 | man |
| watch strap | 1 | watch strap |
| copyright symbol | 1 | copyright symbol |
| device | 1 | buttons |
| symbol | 1 | oscar |
| key pad | 1 | key pad |
| commodity | 1 | shirt |
| representation | 1 | picture |
| pointer finger | 1 | pointer finger |
| organ | 1 | ear |
| organism | 1 | speaker |
| set | 1 | band |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| physical entity | 5 | 11 | artifact, body part, equipment, living thing, organ |
| object | 4 | 5 | commodity, device, organism, representation |
| communicate | 1 | 1 | cell phone |
| watch strap | 1 | 1 | watch strap |
| copyright symbol | 1 | 1 | copyright symbol |
| signal | 1 | 1 | symbol |
| key pad | 1 | 1 | key pad |
| pointer finger | 1 | 1 | pointer finger |
| group | 1 | 1 | set |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| cell phone | cell phone | communicate |
| copyright symbol | copyright symbol | copyright symbol |
| band | set | group |
| key pad | key pad | key pad |
| shirt | commodity | object |
| buttons | device | object |
| cellphone | equipment | object |
| speaker | organism | object |
| picture | representation | object |
| latch | artifact | physical entity |
| watch | artifact | physical entity |
| finger | body part | physical entity |
| fingernail | body part | physical entity |
| hand | body part | physical entity |
| left hand | body part | physical entity |
| thumb | body part | physical entity |
| keypad | equipment | physical entity |
| phone | equipment | physical entity |
| man | living thing | physical entity |
| ear | organ | physical entity |
| pointer finger | pointer finger | pointer finger |
| oscar | symbol | signal |
| watch strap | watch strap | watch strap |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2376855/sample_2376855/CONCEPT_MAPPING_REPORT.md
