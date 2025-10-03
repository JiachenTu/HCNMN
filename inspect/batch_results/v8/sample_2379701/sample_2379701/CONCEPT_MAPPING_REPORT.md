# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 18
**Unique Fine Concepts**: 18
**Unique Mid Concepts**: 16
**Unique Coarse Concepts**: 6

**Compression Ratios**:
- Fine → Mid: **1.12x**
- Fine → Coarse: **3.00x**
- Mid → Coarse: **2.67x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| body part | 2 | foot, leg |
| commodity | 2 | shirt, shorts |
| covering | 1 | hair |
| land | 1 | ground |
| act | 1 | writing |
| process | 1 | letters |
| assembly | 1 | court |
| background | 1 | background |
| substance | 1 | dirt |
| sound | 1 | racket |
| footwear | 1 | shoe |
| living thing | 1 | woman |
| air | 1 | air |
| partition | 1 | wall |
| artifact | 1 | ball |
| band | 1 | headband |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 6 | 7 | artifact, band, commodity, footwear, land, partition |
| abstraction | 4 | 4 | act, process, sound, substance |
| physical entity | 3 | 4 | body part, covering, living thing |
| group | 1 | 1 | assembly |
| attribute | 1 | 1 | background |
| matter | 1 | 1 | air |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| writing | act | abstraction |
| letters | process | abstraction |
| racket | sound | abstraction |
| dirt | substance | abstraction |
| background | background | attribute |
| court | assembly | group |
| air | air | matter |
| ball | artifact | object |
| headband | band | object |
| shirt | commodity | object |
| shorts | commodity | object |
| shoe | footwear | object |
| ground | land | object |
| wall | partition | object |
| foot | body part | physical entity |
| leg | body part | physical entity |
| hair | covering | physical entity |
| woman | living thing | physical entity |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2379701/sample_2379701/CONCEPT_MAPPING_REPORT.md
