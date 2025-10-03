# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 22
**Unique Fine Concepts**: 22
**Unique Mid Concepts**: 19
**Unique Coarse Concepts**: 10

**Compression Ratios**:
- Fine → Mid: **1.16x**
- Fine → Coarse: **2.20x**
- Mid → Coarse: **1.90x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| person | 3 | boy, man, woman |
| document | 2 | kite, kites |
| land | 1 | ground |
| blue shirt | 1 | blue shirt |
| red kite | 1 | red kite |
| woman and boy | 1 | woman and boy |
| commodity | 1 | shirt |
| group | 1 | people |
| section | 1 | strings |
| material | 1 | down |
| group action | 1 | hands |
| structure | 1 | building |
| cloud | 1 | clouds |
| cone | 1 | cones |
| color | 1 | blue |
| ladybug kites | 1 | ladybug kites |
| container | 1 | bag |
| tail | 1 | tail |
| sky | 1 | sky |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 5 | 5 | commodity, cone, container, land, structure |
| physical entity | 4 | 6 | cloud, person, sky, tail |
| abstraction | 3 | 4 | document, group action, material |
| blue shirt | 1 | 1 | blue shirt |
| red kite | 1 | 1 | red kite |
| woman and boy | 1 | 1 | woman and boy |
| people | 1 | 1 | group |
| group | 1 | 1 | section |
| attribute | 1 | 1 | color |
| ladybug kites | 1 | 1 | ladybug kites |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| kite | document | abstraction |
| kites | document | abstraction |
| hands | group action | abstraction |
| down | material | abstraction |
| blue | color | attribute |
| blue shirt | blue shirt | blue shirt |
| strings | section | group |
| ladybug kites | ladybug kites | ladybug kites |
| shirt | commodity | object |
| cones | cone | object |
| bag | container | object |
| ground | land | object |
| building | structure | object |
| people | group | people |
| clouds | cloud | physical entity |
| boy | person | physical entity |
| man | person | physical entity |
| woman | person | physical entity |
| sky | sky | physical entity |
| tail | tail | physical entity |
| red kite | red kite | red kite |
| woman and boy | woman and boy | woman and boy |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2342105/sample_2342105/CONCEPT_MAPPING_REPORT.md
