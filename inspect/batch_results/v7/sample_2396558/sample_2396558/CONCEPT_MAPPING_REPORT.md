# Concept Merging Analysis Report

## Summary Statistics

**Total Objects**: 21
**Unique Fine Concepts**: 21
**Unique Mid Concepts**: 15
**Unique Coarse Concepts**: 5

**Compression Ratios**:
- Fine → Mid: **1.40x**
- Fine → Coarse: **4.20x**
- Mid → Coarse: **3.00x**

---

## Mid-Level Concept Merging

Shows how fine-grained objects merge into mid-level categories.

| Mid Concept | Object Count | Fine Objects |
|-------------|--------------|-------------|
| natural object | 5 | apple, fruit, lemon, orange, oranges |
| extremity | 2 | bottom, tip |
| physical condition | 2 | bruise, bump |
| process | 1 | sticker |
| topographic point | 1 | spot |
| shape | 1 | shape |
| word | 1 | stem |
| pile | 1 | pile |
| unit | 1 | branch |
| table | 1 | table |
| physical phenomenon | 1 | light |
| organism | 1 | banana |
| area | 1 | middle |
| top | 1 | top |
| group | 1 | group |

---

## Coarse-Level Concept Merging

Shows how mid-level categories merge into coarse-grained domains.

| Coarse Concept | Mid Count | Total Objects | Mid Concepts |
|----------------|-----------|---------------|-------------|
| object | 6 | 11 | area, extremity, natural object, organism, top, topographic point |
| abstraction | 6 | 6 | group, pile, shape, table, unit, word |
| thing | 1 | 1 | process |
| state | 1 | 2 | physical condition |
| process | 1 | 1 | physical phenomenon |

---

## Complete Object Mappings

| Fine Object | Mid Category | Coarse Domain |
|-------------|--------------|---------------|
| group | group | abstraction |
| pile | pile | abstraction |
| shape | shape | abstraction |
| table | table | abstraction |
| branch | unit | abstraction |
| stem | word | abstraction |
| middle | area | object |
| bottom | extremity | object |
| tip | extremity | object |
| apple | natural object | object |
| fruit | natural object | object |
| lemon | natural object | object |
| orange | natural object | object |
| oranges | natural object | object |
| banana | organism | object |
| top | top | object |
| spot | topographic point | object |
| light | physical phenomenon | process |
| bruise | physical condition | state |
| bump | physical condition | state |
| sticker | process | thing |

---

**Generated**: /nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v7/sample_2396558/sample_2396558/CONCEPT_MAPPING_REPORT.md
