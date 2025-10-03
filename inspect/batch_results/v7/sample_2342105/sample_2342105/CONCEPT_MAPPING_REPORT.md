# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 22
**Unique Fine Concepts**: 22
**Unique Mid Concepts**: 18
**Unique Coarse Concepts**: 9

**Compression Ratios**:
- Fine → Mid: **1.22x**
- Fine → Coarse: **2.44x**
- Mid → Coarse: **2.00x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| organism | 3 | boy, man, woman |
| artifact | 2 | cones, shirt |
| document | 2 | kite, kites |
| woman and boy | 1 | woman and boy |
| instrumentality | 1 | bag |
| physical phenomenon | 1 | clouds |
| ladybug kites | 1 | ladybug kites |
| group action | 1 | hands |
| atmosphere | 1 | sky |
| process | 1 | tail |
| color | 1 | blue |
| red kite | 1 | red kite |
| structure | 1 | building |
| musical organization | 1 | strings |
| land | 1 | ground |
| people | 1 | people |
| material | 1 | down |
| blue shirt | 1 | blue shirt |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| abstraction | 6 | 7 | color, document, group action, material, musical organization, people |
| object | 5 | 8 | artifact, instrumentality, land, organism, structure |
| woman and boy | 1 | 1 | woman and boy |
| process | 1 | 1 | physical phenomenon |
| ladybug kites | 1 | 1 | ladybug kites |
| matter | 1 | 1 | atmosphere |
| thing | 1 | 1 | process |
| red kite | 1 | 1 | red kite |
| blue shirt | 1 | 1 | blue shirt |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| blue | color | abstraction |
| kite | document | abstraction |
| kites | document | abstraction |
| hands | group action | abstraction |
| down | material | abstraction |
| strings | musical organization | abstraction |
| people | people | abstraction |
| blue shirt | blue shirt | blue shirt |
| ladybug kites | ladybug kites | ladybug kites |
| sky | atmosphere | matter |
| cones | artifact | object |
| shirt | artifact | object |
| bag | instrumentality | object |
| ground | land | object |
| boy | organism | object |
| man | organism | object |
| woman | organism | object |
| building | structure | object |
| clouds | physical phenomenon | process |
| red kite | red kite | red kite |
| tail | process | thing |
| woman and boy | woman and boy | woman and boy |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2342105/sample_2342105/CONCEPT_MAPPING_REPORT.md
