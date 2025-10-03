# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 13
**Unique Fine Concepts**: 13
**Unique Mid Concepts**: 12
**Unique Coarse Concepts**: 3

**Compression Ratios**:
- Fine → Mid: **1.08x**
- Fine → Coarse: **4.33x**
- Mid → Coarse: **4.00x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| structure | 2 | cubby, door |
| partition | 1 | wall |
| strip | 1 | towel ring |
| act | 1 | overflow |
| way | 1 | pipe |
| handle | 1 | handle |
| body part | 1 | lid |
| device | 1 | faucet |
| furnishing | 1 | cabinet |
| fixture | 1 | sink |
| surface | 1 | floor |
| area | 1 | toilet |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 7 | 8 | area, device, fixture, furnishing, handle, strip, structure |
| physical entity | 4 | 4 | body part, partition, surface, way |
| abstraction | 1 | 1 | act |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| overflow | act | abstraction |
| toilet | area | object |
| faucet | device | object |
| sink | fixture | object |
| cabinet | furnishing | object |
| handle | handle | object |
| towel ring | strip | object |
| cubby | structure | object |
| door | structure | object |
| lid | body part | physical entity |
| wall | partition | physical entity |
| floor | surface | physical entity |
| pipe | way | physical entity |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2406328/sample_2406328/CONCEPT_MAPPING_REPORT.md
