# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 13
**Unique Fine Concepts**: 13
**Unique Mid Concepts**: 10
**Unique Coarse Concepts**: 3

**Compression Ratios**:
- Fine → Mid: **1.30x**
- Fine → Coarse: **4.33x**
- Mid → Coarse: **3.33x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| structure | 4 | cubby, door, toilet, wall |
| device | 1 | faucet |
| action | 1 | overflow |
| tissue | 1 | lid |
| way | 1 | pipe |
| horizontal surface | 1 | floor |
| furnishing | 1 | cabinet |
| strip | 1 | towel ring |
| plumbing fixture | 1 | sink |
| handle | 1 | handle |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| physical entity | 7 | 8 | furnishing, handle, horizontal surface, strip, structure, tissue, way |
| object | 2 | 4 | device, plumbing fixture |
| abstraction | 1 | 1 | action |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| overflow | action | abstraction |
| faucet | device | object |
| sink | plumbing fixture | object |
| cubby | structure | object |
| toilet | structure | object |
| cabinet | furnishing | physical entity |
| handle | handle | physical entity |
| floor | horizontal surface | physical entity |
| towel ring | strip | physical entity |
| door | structure | physical entity |
| wall | structure | physical entity |
| lid | tissue | physical entity |
| pipe | way | physical entity |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2406328/sample_2406328/CONCEPT_MAPPING_REPORT.md
