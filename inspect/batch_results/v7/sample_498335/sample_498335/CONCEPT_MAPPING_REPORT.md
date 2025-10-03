# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 18
**Unique Fine Concepts**: 18
**Unique Mid Concepts**: 11
**Unique Coarse Concepts**: 4

**Compression Ratios**:
- Fine → Mid: **1.64x**
- Fine → Coarse: **4.50x**
- Mid → Coarse: **2.75x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| artifact | 3 | letter, stairs, street |
| structure | 3 | balcony, billboard, railing |
| instrumentality | 3 | clock, pole, pot |
| organism | 2 | flower, flowers |
| background | 1 | background |
| clue | 1 | sign |
| words | 1 | words |
| physical phenomenon | 1 | light |
| extremity | 1 | edge |
| external body part | 1 | face |
| batch | 1 | lot |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 5 | 12 | artifact, extremity, instrumentality, organism, structure |
| abstraction | 4 | 4 | background, batch, clue, words |
| process | 1 | 1 | physical phenomenon |
| thing | 1 | 1 | external body part |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| background | background | abstraction |
| lot | batch | abstraction |
| sign | clue | abstraction |
| words | words | abstraction |
| letter | artifact | object |
| stairs | artifact | object |
| street | artifact | object |
| edge | extremity | object |
| clock | instrumentality | object |
| pole | instrumentality | object |
| pot | instrumentality | object |
| flower | organism | object |
| flowers | organism | object |
| balcony | structure | object |
| billboard | structure | object |
| railing | structure | object |
| light | physical phenomenon | process |
| face | external body part | thing |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_498335/sample_498335/CONCEPT_MAPPING_REPORT.md
