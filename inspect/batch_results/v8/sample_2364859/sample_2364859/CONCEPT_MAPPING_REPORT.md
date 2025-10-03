# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 19
**Unique Fine Concepts**: 19
**Unique Mid Concepts**: 15
**Unique Coarse Concepts**: 8

**Compression Ratios**:
- Fine → Mid: **1.27x**
- Fine → Coarse: **2.38x**
- Mid → Coarse: **1.88x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| furnishing | 4 | cabinet, chair, chairs, dining table |
| plant | 2 | flower, flowers |
| container | 1 | vase |
| organization | 1 | board |
| chair back | 1 | chair back |
| handle | 1 | handle |
| top | 1 | tops |
| amorphous shape | 1 | crack |
| extremity | 1 | tips |
| artifact | 1 | drawer |
| color | 1 | pink |
| covering | 1 | mat |
| table | 1 | table |
| babys breath | 1 | babys breath |
| back | 1 | back |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 6 | 9 | container, covering, extremity, handle, plant, top |
| physical entity | 3 | 3 | artifact, back, furnishing |
| group | 2 | 2 | organization, table |
| chair back | 1 | 1 | chair back |
| abstraction | 1 | 1 | amorphous shape |
| property | 1 | 1 | color |
| babys breath | 1 | 1 | babys breath |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| crack | amorphous shape | abstraction |
| babys breath | babys breath | babys breath |
| chair back | chair back | chair back |
| flower | plant | flower |
| board | organization | group |
| table | table | group |
| vase | container | object |
| mat | covering | object |
| tips | extremity | object |
| cabinet | furnishing | object |
| chair | furnishing | object |
| dining table | furnishing | object |
| handle | handle | object |
| flowers | plant | object |
| tops | top | object |
| drawer | artifact | physical entity |
| back | back | physical entity |
| chairs | furnishing | physical entity |
| pink | color | property |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8/sample_2364859/sample_2364859/CONCEPT_MAPPING_REPORT.md
