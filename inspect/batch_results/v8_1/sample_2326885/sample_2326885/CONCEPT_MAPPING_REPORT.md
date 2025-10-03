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
| surf board | 1 | surf board |
| path | 1 | tracks |
| long hair | 1 | long hair |
| cloth covering | 1 | skirt |
| beach | 1 | beach |
| bad sentence | 1 | bad sentence |
| board | 1 | surfboard |
| white motorcycle | 1 | white motorcycle |
| short hair | 1 | short hair |
| no motorcycle | 1 | no motorcycle |
| material | 1 | sand |
| situation | 1 | shoes |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| physical entity | 3 | 4 | beach, organism, path |
| object | 2 | 2 | board, cloth covering |
| abstraction | 2 | 2 | material, situation |
| surf board | 1 | 1 | surf board |
| long hair | 1 | 1 | long hair |
| bad sentence | 1 | 1 | bad sentence |
| white motorcycle | 1 | 1 | white motorcycle |
| short hair | 1 | 1 | short hair |
| no motorcycle | 1 | 1 | no motorcycle |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| sand | material | abstraction |
| shoes | situation | abstraction |
| bad sentence | bad sentence | bad sentence |
| long hair | long hair | long hair |
| no motorcycle | no motorcycle | no motorcycle |
| surfboard | board | object |
| skirt | cloth covering | object |
| beach | beach | physical entity |
| man | organism | physical entity |
| woman | organism | physical entity |
| tracks | path | physical entity |
| short hair | short hair | short hair |
| surf board | surf board | surf board |
| white motorcycle | white motorcycle | white motorcycle |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2326885/sample_2326885/CONCEPT_MAPPING_REPORT.md
