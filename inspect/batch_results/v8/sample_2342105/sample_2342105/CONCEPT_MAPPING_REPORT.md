# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 22
**Unique Fine Concepts**: 22
**Unique Mid Concepts**: 20
**Unique Coarse Concepts**: 13

**Compression Ratios**:
- Fine → Mid: **1.10x**
- Fine → Coarse: **1.69x**
- Mid → Coarse: **1.54x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| document | 2 | kite, kites |
| person | 2 | boy, woman |
| physical phenomenon | 1 | clouds |
| blue shirt | 1 | blue shirt |
| organism | 1 | man |
| act | 1 | hands |
| woman and boy | 1 | woman and boy |
| structure | 1 | building |
| ladybug kites | 1 | ladybug kites |
| people | 1 | people |
| red kite | 1 | red kite |
| container | 1 | bag |
| process | 1 | tail |
| atmosphere | 1 | sky |
| organization | 1 | strings |
| land | 1 | ground |
| cone | 1 | cones |
| commodity | 1 | shirt |
| color | 1 | blue |
| substance | 1 | down |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 4 | 5 | commodity, cone, land, structure |
| physical entity | 3 | 3 | container, organism, person |
| abstraction | 3 | 4 | act, organization, substance |
| process | 1 | 1 | physical phenomenon |
| blue shirt | 1 | 1 | blue shirt |
| woman and boy | 1 | 1 | woman and boy |
| ladybug kites | 1 | 1 | ladybug kites |
| communication | 1 | 1 | document |
| group | 1 | 1 | people |
| red kite | 1 | 1 | red kite |
| thing | 1 | 1 | process |
| matter | 1 | 1 | atmosphere |
| attribute | 1 | 1 | color |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| hands | act | abstraction |
| kites | document | abstraction |
| strings | organization | abstraction |
| down | substance | abstraction |
| blue | color | attribute |
| blue shirt | blue shirt | blue shirt |
| kite | document | communication |
| people | people | group |
| ladybug kites | ladybug kites | ladybug kites |
| sky | atmosphere | matter |
| shirt | commodity | object |
| cones | cone | object |
| ground | land | object |
| boy | person | object |
| building | structure | object |
| bag | container | physical entity |
| man | organism | physical entity |
| woman | person | physical entity |
| clouds | physical phenomenon | process |
| red kite | red kite | red kite |
| tail | process | thing |
| woman and boy | woman and boy | woman and boy |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2342105/sample_2342105/CONCEPT_MAPPING_REPORT.md
