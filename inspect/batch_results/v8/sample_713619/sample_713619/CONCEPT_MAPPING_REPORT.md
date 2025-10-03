# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 9
**Unique Fine Concepts**: 9
**Unique Mid Concepts**: 7
**Unique Coarse Concepts**: 3

**Compression Ratios**:
- Fine → Mid: **1.29x**
- Fine → Coarse: **3.00x**
- Mid → Coarse: **2.33x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| structure | 2 | building, window |
| way | 2 | sidewalk, steps |
| physical phenomenon | 1 | light |
| conveyance | 1 | car |
| road | 1 | street |
| street. | 1 | street. |
| decoration | 1 | emblem |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 5 | 7 | conveyance, decoration, road, structure, way |
| phenomenon | 1 | 1 | physical phenomenon |
| street. | 1 | 1 | street. |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| car | conveyance | object |
| emblem | decoration | object |
| street | road | object |
| building | structure | object |
| window | structure | object |
| sidewalk | way | object |
| steps | way | object |
| light | physical phenomenon | phenomenon |
| street. | street. | street. |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_713619/sample_713619/CONCEPT_MAPPING_REPORT.md
