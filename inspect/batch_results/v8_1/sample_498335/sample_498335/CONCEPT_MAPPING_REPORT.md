# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 18
**Unique Fine Concepts**: 18
**Unique Mid Concepts**: 15
**Unique Coarse Concepts**: 4

**Compression Ratios**:
- Fine → Mid: **1.20x**
- Fine → Coarse: **4.50x**
- Mid → Coarse: **3.75x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| instrumentality | 2 | clock, pole |
| artifact | 2 | letter, pot |
| structure | 2 | billboard, railing |
| sign | 1 | sign |
| plant | 1 | flower |
| stairway | 1 | stairs |
| boundary | 1 | edge |
| background | 1 | background |
| road | 1 | street |
| organism | 1 | flowers |
| large indefinite quantity | 1 | lot |
| words | 1 | words |
| balcony | 1 | balcony |
| face | 1 | face |
| physical phenomenon | 1 | light |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| physical entity | 8 | 10 | artifact, balcony, boundary, face, physical phenomenon, road, stairway, structure |
| object | 3 | 4 | instrumentality, organism, plant |
| abstraction | 3 | 3 | background, large indefinite quantity, words |
| communication | 1 | 1 | sign |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| background | background | abstraction |
| lot | large indefinite quantity | abstraction |
| words | words | abstraction |
| sign | sign | communication |
| letter | artifact | object |
| clock | instrumentality | object |
| flowers | organism | object |
| flower | plant | object |
| pot | artifact | physical entity |
| balcony | balcony | physical entity |
| edge | boundary | physical entity |
| face | face | physical entity |
| pole | instrumentality | physical entity |
| light | physical phenomenon | physical entity |
| street | road | physical entity |
| stairs | stairway | physical entity |
| billboard | structure | physical entity |
| railing | structure | physical entity |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_498335/sample_498335/CONCEPT_MAPPING_REPORT.md
