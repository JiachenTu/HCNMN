# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 21
**Unique Fine Concepts**: 21
**Unique Mid Concepts**: 17
**Unique Coarse Concepts**: 4

**Compression Ratios**:
- Fine → Mid: **1.24x**
- Fine → Coarse: **5.25x**
- Mid → Coarse: **4.25x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| plant organ | 4 | fruit, lemon, orange, oranges |
| physical condition | 2 | bruise, bump |
| top | 1 | top |
| area | 1 | middle |
| process | 1 | sticker |
| unit | 1 | branch |
| array | 1 | table |
| physical phenomenon | 1 | light |
| group | 1 | group |
| plant part | 1 | apple |
| shape | 1 | shape |
| plant | 1 | banana |
| point | 1 | spot |
| extremity | 1 | tip |
| region | 1 | bottom |
| collection | 1 | pile |
| word | 1 | stem |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| physical entity | 8 | 11 | area, extremity, physical phenomenon, plant organ, point, process, region, top |
| abstraction | 6 | 7 | array, group, physical condition, shape, unit, word |
| object | 2 | 2 | plant, plant part |
| collection | 1 | 1 | collection |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| table | array | abstraction |
| group | group | abstraction |
| bruise | physical condition | abstraction |
| bump | physical condition | abstraction |
| shape | shape | abstraction |
| branch | unit | abstraction |
| stem | word | abstraction |
| pile | collection | collection |
| banana | plant | object |
| apple | plant part | object |
| middle | area | physical entity |
| tip | extremity | physical entity |
| light | physical phenomenon | physical entity |
| fruit | plant organ | physical entity |
| lemon | plant organ | physical entity |
| orange | plant organ | physical entity |
| oranges | plant organ | physical entity |
| spot | point | physical entity |
| sticker | process | physical entity |
| bottom | region | physical entity |
| top | top | physical entity |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2396558/sample_2396558/CONCEPT_MAPPING_REPORT.md
