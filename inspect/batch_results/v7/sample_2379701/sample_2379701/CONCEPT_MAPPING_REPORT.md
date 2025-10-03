# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 18
**Unique Fine Concepts**: 18
**Unique Mid Concepts**: 14
**Unique Coarse Concepts**: 4

**Compression Ratios**:
- Fine → Mid: **1.29x**
- Fine → Coarse: **4.50x**
- Mid → Coarse: **3.50x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| artifact | 3 | headband, shirt, shorts |
| external body part | 2 | foot, leg |
| covering | 2 | hair, shoe |
| structure | 1 | wall |
| sound | 1 | racket |
| instrumentality | 1 | ball |
| organism | 1 | woman |
| background | 1 | background |
| basic cognitive process | 1 | letters |
| material | 1 | dirt |
| air | 1 | air |
| land | 1 | ground |
| activity | 1 | writing |
| assembly | 1 | court |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 6 | 9 | artifact, covering, instrumentality, land, organism, structure |
| abstraction | 6 | 6 | activity, assembly, background, basic cognitive process, material, sound |
| thing | 1 | 2 | external body part |
| matter | 1 | 1 | air |

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
| air | air | matter |
| headband | artifact | object |
| shirt | artifact | object |
| shorts | artifact | object |
| hair | covering | object |
| shoe | covering | object |
| ball | instrumentality | object |
| ground | land | object |
| woman | organism | object |
| wall | structure | object |
| foot | external body part | thing |
| leg | external body part | thing |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2379701/sample_2379701/CONCEPT_MAPPING_REPORT.md
