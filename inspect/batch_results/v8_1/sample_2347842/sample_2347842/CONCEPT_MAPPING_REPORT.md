# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 19
**Unique Fine Concepts**: 19
**Unique Mid Concepts**: 15
**Unique Coarse Concepts**: 5

**Compression Ratios**:
- Fine → Mid: **1.27x**
- Fine → Coarse: **3.80x**
- Mid → Coarse: **3.00x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| artifact | 4 | concrete, pants, shirt, skateboard |
| organism | 2 | boy, person |
| extremity | 1 | leg |
| furnishing | 1 | bench |
| boundary | 1 | edge |
| skater | 1 | skateboarder |
| semidarkness | 1 | shadow |
| natural object | 1 | hair |
| footwear | 1 | shoe |
| group | 1 | people |
| skate park | 1 | skate park |
| conveyance | 1 | bicycle |
| device | 1 | ramp |
| plant | 1 | grass |
| activity | 1 | writing |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 6 | 8 | artifact, boundary, conveyance, footwear, plant, skater |
| physical entity | 5 | 7 | device, extremity, furnishing, natural object, organism |
| abstraction | 2 | 2 | activity, semidarkness |
| group | 1 | 1 | group |
| skate park | 1 | 1 | skate park |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| writing | activity | abstraction |
| shadow | semidarkness | abstraction |
| people | group | group |
| pants | artifact | object |
| skateboard | artifact | object |
| edge | boundary | object |
| bicycle | conveyance | object |
| shoe | footwear | object |
| boy | organism | object |
| grass | plant | object |
| skateboarder | skater | object |
| concrete | artifact | physical entity |
| shirt | artifact | physical entity |
| ramp | device | physical entity |
| leg | extremity | physical entity |
| bench | furnishing | physical entity |
| hair | natural object | physical entity |
| person | organism | physical entity |
| skate park | skate park | skate park |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2347842/sample_2347842/CONCEPT_MAPPING_REPORT.md
