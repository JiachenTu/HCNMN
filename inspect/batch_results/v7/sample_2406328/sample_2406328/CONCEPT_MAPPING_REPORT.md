# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 13
**Unique Fine Concepts**: 13
**Unique Mid Concepts**: 6
**Unique Coarse Concepts**: 3

**Compression Ratios**:
- Fine → Mid: **2.17x**
- Fine → Coarse: **4.33x**
- Mid → Coarse: **2.00x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| structure | 4 | cubby, door, toilet, wall |
| artifact | 4 | floor, pipe, sink, towel ring |
| instrumentality | 2 | cabinet, faucet |
| tissue | 1 | lid |
| action | 1 | overflow |
| handle | 1 | handle |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 4 | 11 | artifact, handle, instrumentality, structure |
| thing | 1 | 1 | tissue |
| abstraction | 1 | 1 | action |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| overflow | action | abstraction |
| floor | artifact | object |
| pipe | artifact | object |
| sink | artifact | object |
| towel ring | artifact | object |
| handle | handle | object |
| cabinet | instrumentality | object |
| faucet | instrumentality | object |
| cubby | structure | object |
| door | structure | object |
| toilet | structure | object |
| wall | structure | object |
| lid | tissue | thing |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2406328/sample_2406328/CONCEPT_MAPPING_REPORT.md
