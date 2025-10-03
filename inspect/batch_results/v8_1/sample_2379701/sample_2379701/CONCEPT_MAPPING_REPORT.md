# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 18
**Unique Fine Concepts**: 18
**Unique Mid Concepts**: 17
**Unique Coarse Concepts**: 3

**Compression Ratios**:
- Fine → Mid: **1.06x**
- Fine → Coarse: **6.00x**
- Mid → Coarse: **5.67x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| artifact | 2 | ball, shirt |
| external body part | 1 | leg |
| air | 1 | air |
| land | 1 | ground |
| band | 1 | headband |
| basic cognitive process | 1 | letters |
| material | 1 | dirt |
| extremity | 1 | foot |
| person | 1 | woman |
| footwear | 1 | shoe |
| natural object | 1 | hair |
| sound | 1 | racket |
| activity | 1 | writing |
| partition | 1 | wall |
| trouser | 1 | shorts |
| assembly | 1 | court |
| background | 1 | background |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| physical entity | 6 | 6 | air, band, external body part, extremity, natural object, partition |
| abstraction | 6 | 6 | activity, assembly, background, basic cognitive process, material, sound |
| object | 5 | 6 | artifact, footwear, land, person, trouser |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| writing | activity | abstraction |
| court | assembly | abstraction |
| background | background | abstraction |
| letters | basic cognitive process | abstraction |
| dirt | material | abstraction |
| racket | sound | abstraction |
| ball | artifact | object |
| shirt | artifact | object |
| shoe | footwear | object |
| ground | land | object |
| woman | person | object |
| shorts | trouser | object |
| air | air | physical entity |
| headband | band | physical entity |
| leg | external body part | physical entity |
| foot | extremity | physical entity |
| hair | natural object | physical entity |
| wall | partition | physical entity |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2379701/sample_2379701/CONCEPT_MAPPING_REPORT.md
