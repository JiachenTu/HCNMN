# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 9
**Unique Fine Concepts**: 9
**Unique Mid Concepts**: 5
**Unique Coarse Concepts**: 3

**Compression Ratios**:
- Fine → Mid: **1.80x**
- Fine → Coarse: **3.00x**
- Mid → Coarse: **1.67x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| artifact | 4 | emblem, sidewalk, steps, street |
| structure | 2 | building, window |
| instrumentality | 1 | car |
| street. | 1 | street. |
| physical phenomenon | 1 | light |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 3 | 7 | artifact, instrumentality, structure |
| street. | 1 | 1 | street. |
| process | 1 | 1 | physical phenomenon |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| emblem | artifact | object |
| sidewalk | artifact | object |
| steps | artifact | object |
| street | artifact | object |
| car | instrumentality | object |
| building | structure | object |
| window | structure | object |
| light | physical phenomenon | process |
| street. | street. | street. |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_713619/sample_713619/CONCEPT_MAPPING_REPORT.md
