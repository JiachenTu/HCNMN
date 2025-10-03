# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 19
**Unique Fine Concepts**: 19
**Unique Mid Concepts**: 16
**Unique Coarse Concepts**: 6

**Compression Ratios**:
- Fine → Mid: **1.19x**
- Fine → Coarse: **3.17x**
- Mid → Coarse: **2.67x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| furnishing | 4 | cabinet, chair, chairs, dining table |
| container | 1 | vase |
| organism | 1 | flower |
| unit | 1 | board |
| color | 1 | pink |
| back | 1 | back |
| plant | 1 | flowers |
| covering | 1 | mat |
| extremity | 1 | tips |
| babys breath | 1 | babys breath |
| amorphous shape | 1 | crack |
| table | 1 | table |
| top | 1 | tops |
| chair back | 1 | chair back |
| structure | 1 | drawer |
| handle | 1 | handle |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| physical entity | 6 | 9 | back, container, covering, furnishing, handle, structure |
| object | 4 | 4 | extremity, organism, plant, top |
| abstraction | 3 | 3 | amorphous shape, table, unit |
| attribute | 1 | 1 | color |
| babys breath | 1 | 1 | babys breath |
| chair back | 1 | 1 | chair back |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| crack | amorphous shape | abstraction |
| table | table | abstraction |
| board | unit | abstraction |
| pink | color | attribute |
| babys breath | babys breath | babys breath |
| chair back | chair back | chair back |
| tips | extremity | object |
| flower | organism | object |
| flowers | plant | object |
| tops | top | object |
| back | back | physical entity |
| vase | container | physical entity |
| mat | covering | physical entity |
| cabinet | furnishing | physical entity |
| chair | furnishing | physical entity |
| chairs | furnishing | physical entity |
| dining table | furnishing | physical entity |
| handle | handle | physical entity |
| drawer | structure | physical entity |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1/sample_2364859/sample_2364859/CONCEPT_MAPPING_REPORT.md
