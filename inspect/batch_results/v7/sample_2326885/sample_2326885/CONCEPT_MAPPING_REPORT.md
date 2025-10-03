# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 14
**Unique Fine Concepts**: 14
**Unique Mid Concepts**: 13
**Unique Coarse Concepts**: 9

**Compression Ratios**:
- Fine → Mid: **1.08x**
- Fine → Coarse: **1.56x**
- Mid → Coarse: **1.44x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| organism | 2 | man, woman |
| situation | 1 | shoes |
| beach | 1 | beach |
| artifact | 1 | surfboard |
| surf board | 1 | surf board |
| no motorcycle | 1 | no motorcycle |
| long hair | 1 | long hair |
| path | 1 | tracks |
| material | 1 | sand |
| short hair | 1 | short hair |
| bad sentence | 1 | bad sentence |
| covering | 1 | skirt |
| white motorcycle | 1 | white motorcycle |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 5 | 6 | artifact, beach, covering, organism, path |
| state | 1 | 1 | situation |
| surf board | 1 | 1 | surf board |
| no motorcycle | 1 | 1 | no motorcycle |
| long hair | 1 | 1 | long hair |
| abstraction | 1 | 1 | material |
| short hair | 1 | 1 | short hair |
| bad sentence | 1 | 1 | bad sentence |
| white motorcycle | 1 | 1 | white motorcycle |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| sand | material | abstraction |
| bad sentence | bad sentence | bad sentence |
| long hair | long hair | long hair |
| no motorcycle | no motorcycle | no motorcycle |
| surfboard | artifact | object |
| beach | beach | object |
| skirt | covering | object |
| man | organism | object |
| woman | organism | object |
| tracks | path | object |
| short hair | short hair | short hair |
| shoes | situation | state |
| surf board | surf board | surf board |
| white motorcycle | white motorcycle | white motorcycle |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2326885/sample_2326885/CONCEPT_MAPPING_REPORT.md
