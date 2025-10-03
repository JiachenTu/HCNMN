# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 21
**Unique Fine Concepts**: 21
**Unique Mid Concepts**: 17
**Unique Coarse Concepts**: 10

**Compression Ratios**:
- Fine → Mid: **1.24x**
- Fine → Coarse: **2.10x**
- Mid → Coarse: **1.70x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| plant organ | 4 | fruit, lemon, orange, oranges |
| physical condition | 2 | bruise, bump |
| region | 1 | bottom |
| group | 1 | group |
| extremity | 1 | tip |
| organization | 1 | branch |
| shape | 1 | shape |
| body part | 1 | sticker |
| plant | 1 | banana |
| center | 1 | middle |
| point | 1 | spot |
| language unit | 1 | stem |
| top | 1 | top |
| pile | 1 | pile |
| table | 1 | table |
| plant part | 1 | apple |
| natural phenomenon | 1 | light |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 5 | 7 | center, extremity, plant organ, plant part, top |
| group | 3 | 3 | group, organization, table |
| location | 2 | 2 | point, region |
| attribute | 2 | 3 | physical condition, shape |
| physical entity | 1 | 1 | body part |
| banana | 1 | 1 | plant |
| part | 1 | 1 | language unit |
| collection | 1 | 1 | pile |
| phenomenon | 1 | 1 | natural phenomenon |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| bruise | physical condition | attribute |
| bump | physical condition | attribute |
| shape | shape | attribute |
| banana | plant | banana |
| pile | pile | collection |
| fruit | plant organ | fruit |
| group | group | group |
| branch | organization | group |
| table | table | group |
| spot | point | location |
| bottom | region | location |
| middle | center | object |
| tip | extremity | object |
| lemon | plant organ | object |
| orange | plant organ | object |
| oranges | plant organ | object |
| apple | plant part | object |
| top | top | object |
| stem | language unit | part |
| light | natural phenomenon | phenomenon |
| sticker | body part | physical entity |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2396558/sample_2396558/CONCEPT_MAPPING_REPORT.md
