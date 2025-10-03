# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 9
**Unique Fine Concepts**: 9
**Unique Mid Concepts**: 8
**Unique Coarse Concepts**: 3

**Compression Ratios**:
- Fine → Mid: **1.12x**
- Fine → Coarse: **3.00x**
- Mid → Coarse: **2.67x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| structure | 2 | building, window |
| physical phenomenon | 1 | light |
| decoration | 1 | emblem |
| road | 1 | street |
| artifact | 1 | car |
| way | 1 | sidewalk |
| stairway | 1 | steps |
| street. | 1 | street. |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| physical entity | 5 | 6 | artifact, physical phenomenon, road, stairway, way |
| object | 2 | 2 | decoration, structure |
| street. | 1 | 1 | street. |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| emblem | decoration | object |
| window | structure | object |
| car | artifact | physical entity |
| light | physical phenomenon | physical entity |
| street | road | physical entity |
| steps | stairway | physical entity |
| building | structure | physical entity |
| sidewalk | way | physical entity |
| street. | street. | street. |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_713619/sample_713619/CONCEPT_MAPPING_REPORT.md
