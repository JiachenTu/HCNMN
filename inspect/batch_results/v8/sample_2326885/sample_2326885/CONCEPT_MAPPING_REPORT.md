# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 14
**Unique Fine Concepts**: 14
**Unique Mid Concepts**: 14
**Unique Coarse Concepts**: 11

**Compression Ratios**:
- Fine → Mid: **1.00x**
- Fine → Coarse: **1.27x**
- Mid → Coarse: **1.27x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| no motorcycle | 1 | no motorcycle |
| long hair | 1 | long hair |
| surf board | 1 | surf board |
| person | 1 | woman |
| material | 1 | sand |
| white motorcycle | 1 | white motorcycle |
| short hair | 1 | short hair |
| cloth covering | 1 | skirt |
| living thing | 1 | man |
| condition | 1 | shoes |
| beach | 1 | beach |
| line | 1 | tracks |
| bad sentence | 1 | bad sentence |
| sheet | 1 | surfboard |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 3 | 3 | beach, cloth covering, sheet |
| physical entity | 2 | 2 | living thing, person |
| no motorcycle | 1 | 1 | no motorcycle |
| long hair | 1 | 1 | long hair |
| surf board | 1 | 1 | surf board |
| relation | 1 | 1 | material |
| white motorcycle | 1 | 1 | white motorcycle |
| short hair | 1 | 1 | short hair |
| abstraction | 1 | 1 | condition |
| location | 1 | 1 | line |
| bad sentence | 1 | 1 | bad sentence |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| shoes | condition | abstraction |
| bad sentence | bad sentence | bad sentence |
| tracks | line | location |
| long hair | long hair | long hair |
| no motorcycle | no motorcycle | no motorcycle |
| beach | beach | object |
| skirt | cloth covering | object |
| surfboard | sheet | object |
| man | living thing | physical entity |
| woman | person | physical entity |
| sand | material | relation |
| short hair | short hair | short hair |
| surf board | surf board | surf board |
| white motorcycle | white motorcycle | white motorcycle |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2326885/sample_2326885/CONCEPT_MAPPING_REPORT.md
