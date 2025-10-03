# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 19
**Unique Fine Concepts**: 19
**Unique Mid Concepts**: 16
**Unique Coarse Concepts**: 6

**Compression Ratios**:
- Fine → Mid: **1.19x**
- Fine → Coarse: **3.17x**
- Mid → Coarse: **2.67x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| artifact | 3 | bench, ramp, skateboard |
| person | 2 | boy, skateboarder |
| organism | 1 | person |
| footwear | 1 | shoe |
| body part | 1 | leg |
| illumination | 1 | shadow |
| covering | 1 | hair |
| consumer goods | 1 | pants |
| creation | 1 | writing |
| plant | 1 | grass |
| skate park | 1 | skate park |
| commodity | 1 | shirt |
| conveyance | 1 | bicycle |
| region | 1 | edge |
| concrete | 1 | concrete |
| people | 1 | people |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 9 | 10 | artifact, commodity, concrete, consumer goods, conveyance, footwear, organism, person, region |
| physical entity | 3 | 5 | body part, covering, plant |
| state | 1 | 1 | illumination |
| abstraction | 1 | 1 | creation |
| skate park | 1 | 1 | skate park |
| group | 1 | 1 | people |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| writing | creation | abstraction |
| people | people | group |
| bench | artifact | object |
| skateboard | artifact | object |
| shirt | commodity | object |
| concrete | concrete | object |
| pants | consumer goods | object |
| bicycle | conveyance | object |
| shoe | footwear | object |
| person | organism | object |
| boy | person | object |
| edge | region | object |
| ramp | artifact | physical entity |
| leg | body part | physical entity |
| hair | covering | physical entity |
| skateboarder | person | physical entity |
| grass | plant | physical entity |
| skate park | skate park | skate park |
| shadow | illumination | state |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2347842/sample_2347842/CONCEPT_MAPPING_REPORT.md
