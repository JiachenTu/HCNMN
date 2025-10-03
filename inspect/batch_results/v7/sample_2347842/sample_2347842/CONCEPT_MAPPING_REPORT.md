# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 19
**Unique Fine Concepts**: 19
**Unique Mid Concepts**: 10
**Unique Coarse Concepts**: 5

**Compression Ratios**:
- Fine → Mid: **1.90x**
- Fine → Coarse: **3.80x**
- Mid → Coarse: **2.00x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| instrumentality | 4 | bench, bicycle, ramp, skateboard |
| organism | 4 | boy, grass, person, skateboarder |
| artifact | 3 | concrete, pants, shirt |
| covering | 2 | hair, shoe |
| people | 1 | people |
| dark | 1 | shadow |
| external body part | 1 | leg |
| skate park | 1 | skate park |
| activity | 1 | writing |
| extremity | 1 | edge |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 5 | 14 | artifact, covering, extremity, instrumentality, organism |
| abstraction | 2 | 2 | activity, people |
| state | 1 | 1 | dark |
| thing | 1 | 1 | external body part |
| skate park | 1 | 1 | skate park |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| writing | activity | abstraction |
| people | people | abstraction |
| concrete | artifact | object |
| pants | artifact | object |
| shirt | artifact | object |
| hair | covering | object |
| shoe | covering | object |
| edge | extremity | object |
| bench | instrumentality | object |
| bicycle | instrumentality | object |
| ramp | instrumentality | object |
| skateboard | instrumentality | object |
| boy | organism | object |
| grass | organism | object |
| person | organism | object |
| skateboarder | organism | object |
| skate park | skate park | skate park |
| shadow | dark | state |
| leg | external body part | thing |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2347842/sample_2347842/CONCEPT_MAPPING_REPORT.md
