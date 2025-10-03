# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 19
**Unique Fine Concepts**: 19
**Unique Mid Concepts**: 14
**Unique Coarse Concepts**: 5

**Compression Ratios**:
- Fine → Mid: **1.36x**
- Fine → Coarse: **3.80x**
- Mid → Coarse: **2.80x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| instrumentality | 5 | cabinet, chair, chairs, dining table, vase |
| organism | 2 | flower, flowers |
| color | 1 | pink |
| chair back | 1 | chair back |
| back | 1 | back |
| top | 1 | tops |
| babys breath | 1 | babys breath |
| structure | 1 | drawer |
| unit | 1 | board |
| table | 1 | table |
| extremity | 1 | tips |
| space | 1 | crack |
| handle | 1 | handle |
| covering | 1 | mat |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 7 | 12 | covering, extremity, handle, instrumentality, organism, structure, top |
| abstraction | 4 | 4 | color, space, table, unit |
| chair back | 1 | 1 | chair back |
| thing | 1 | 1 | back |
| babys breath | 1 | 1 | babys breath |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| pink | color | abstraction |
| crack | space | abstraction |
| table | table | abstraction |
| board | unit | abstraction |
| babys breath | babys breath | babys breath |
| chair back | chair back | chair back |
| mat | covering | object |
| tips | extremity | object |
| handle | handle | object |
| cabinet | instrumentality | object |
| chair | instrumentality | object |
| chairs | instrumentality | object |
| dining table | instrumentality | object |
| vase | instrumentality | object |
| flower | organism | object |
| flowers | organism | object |
| drawer | structure | object |
| tops | top | object |
| back | back | thing |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2364859/sample_2364859/CONCEPT_MAPPING_REPORT.md
