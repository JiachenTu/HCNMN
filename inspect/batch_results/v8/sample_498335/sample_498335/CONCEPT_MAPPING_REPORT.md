# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 18
**Unique Fine Concepts**: 18
**Unique Mid Concepts**: 13
**Unique Coarse Concepts**: 8

**Compression Ratios**:
- Fine → Mid: **1.38x**
- Fine → Coarse: **2.25x**
- Mid → Coarse: **1.62x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| structure | 3 | balcony, billboard, railing |
| artifact | 3 | letter, pole, pot |
| plant | 2 | flower, flowers |
| region | 1 | edge |
| large indefinite quantity | 1 | lot |
| external body part | 1 | face |
| road | 1 | street |
| device | 1 | clock |
| natural phenomenon | 1 | light |
| clue | 1 | sign |
| background | 1 | background |
| words | 1 | words |
| stairway | 1 | stairs |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 4 | 9 | plant, road, stairway, structure |
| physical entity | 2 | 2 | artifact, device |
| communication | 2 | 2 | clue, words |
| location | 1 | 1 | region |
| indefinite quantity | 1 | 1 | large indefinite quantity |
| thing | 1 | 1 | external body part |
| phenomenon | 1 | 1 | natural phenomenon |
| abstraction | 1 | 1 | background |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| background | background | abstraction |
| sign | clue | communication |
| words | words | communication |
| lot | large indefinite quantity | indefinite quantity |
| edge | region | location |
| pole | artifact | object |
| pot | artifact | object |
| flower | plant | object |
| flowers | plant | object |
| street | road | object |
| stairs | stairway | object |
| balcony | structure | object |
| billboard | structure | object |
| railing | structure | object |
| light | natural phenomenon | phenomenon |
| letter | artifact | physical entity |
| clock | device | physical entity |
| face | external body part | thing |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_498335/sample_498335/CONCEPT_MAPPING_REPORT.md
