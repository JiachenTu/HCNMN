# Granularity Level Definitions

**Last Updated**: 2025-10-03

## Overview

Multi-granularity hierarchical scene graphs consist of three abstraction levels, each representing the same visual scene at different semantic resolutions. This enables flexible reasoning: start with high-level understanding (coarse) and progressively drill down for details (mid → fine).

## Three Abstraction Levels

### Fine-Grained Level (L0)

**Definition**: Identity mapping from Visual Genome object annotations.

**Characteristics**:
- **Source**: Original VG object names (no transformation)
- **Purpose**: Maximum detail, direct correspondence to image regions
- **Granularity**: Object-specific (e.g., "clock", "bicycle", "dog")
- **WordNet Depth**: Typically 7-12 (most specific)
- **Use Case**: Detailed spatial reasoning, object localization

**Examples from Image 498335**:
```
clock, flower, street, sign, balcony, billboard, light, pot,
railing, edge, background, lot, words, letter, stairs, face, flowers, pole
```

**Relationship to VG Scene Graph**:
```json
{
  "object_id": 1234,
  "names": ["clock"],          ← Fine-grained: "clock"
  "x": 100, "y": 50,
  "w": 80, "h": 120
}
```

**Count**: 18 unique fine-grained concepts (from 30 total VG objects)

---

### Mid-Level (L1)

**Definition**: Semantic categories selected from WordNet depth range 4-6.

**Characteristics**:
- **Source**: WordNet hypernym paths, depths 4-6
- **Purpose**: Functional/categorical grouping
- **Granularity**: Category-level (e.g., "instrumentality", "organism", "structure")
- **WordNet Depth**: 4-6 (categorical level)
- **Selection**:
  - V7: Scoring algorithm (depth preference + semantic bonus)
  - V8/V8.1: LLM selection with context

**Why Depths 4-6?**
- **Depth 4**: Broad categories (artifact, living thing, natural object)
- **Depth 5**: ⭐ Sweet spot - clear categories (organism, instrumentality, structure, conveyance)
- **Depth 6**: More specific but still categorical (device, facility, clothing)
- **Depth 7+**: Too specific, approaching object-level

**Examples from Image 498335**:

| Fine Object | Mid Concept (V8.1) | WordNet Depth | Explanation |
|------------|-------------------|---------------|-------------|
| clock | instrumentality | 5 | Tool/instrument category |
| flower | plant | 6 | Biological organism type |
| street | road | 6 | Infrastructure/way type |
| sign | clue | 5 | Informational element |
| balcony | structure | 5 | Architectural structure |
| light | physical phenomenon | 5 | Physical process/effect |

**Mid-Level Concepts (V8.1)**: 15 unique concepts
```
plant, structure, instrumentality, physical phenomenon, signboard,
artifact, organism, boundary, clue, background, batch, words,
external body part, lot (batch), creation
```

**Compression**: 18 fine → 15 mid = **1.20x compression**

---

### Coarse-Grained Level (L2)

**Definition**: Abstract domains selected from WordNet depth range 1-3.

**Characteristics**:
- **Source**: WordNet hypernym paths, depths 1-3
- **Purpose**: High-level domain grouping
- **Granularity**: Domain-level (e.g., "object", "abstraction", "process")
- **WordNet Depth**: 1-3 (domain level)
- **Selection**: Same methods as mid-level

**Why Depths 1-3?**
- **Depth 0**: "entity" (too abstract, everything is an entity)
- **Depth 1**: Very abstract (physical entity, abstraction) - sometimes too general
- **Depth 2**: ⭐ Sweet spot - meaningful domains (object, matter, process, communication)
- **Depth 3**: More specific (whole, living thing, artifact) - sometimes overlaps with mid

**Examples from Image 498335**:

| Mid Concept | Coarse Domain (V8.1) | WordNet Depth | Explanation |
|------------|---------------------|---------------|-------------|
| instrumentality | physical entity | 1 | Physical objects domain |
| plant | object | 2 | Tangible objects domain |
| road | physical entity | 1 | Physical objects domain |
| clue | communication | 2 | Information/communication domain |
| structure | physical entity | 1 | Physical objects domain |
| physical phenomenon | physical entity | 1 | Physical processes domain |

**Coarse-Level Concepts (V8.1)**: 4 unique concepts
```
physical entity (9 objects)
object (5 objects)
abstraction (3 objects)
communication (1 object)
```

**Compression**: 18 fine → 4 coarse = **4.50x compression**

---

## Hierarchy Flow Diagram

```
Visual Genome Scene Graph
        ↓
┌───────────────────────────────────┐
│   Fine-Grained (L0) - 18 concepts │
│   clock, flower, street, sign,... │
└───────────┬───────────────────────┘
            │ WordNet depth 4-6
            ↓
┌───────────────────────────────────┐
│   Mid-Level (L1) - 15 concepts    │
│   instrumentality, plant, road,.. │
└───────────┬───────────────────────┘
            │ WordNet depth 1-3
            ↓
┌───────────────────────────────────┐
│   Coarse (L2) - 4 concepts        │
│   physical entity, object,...     │
└───────────────────────────────────┘

Compression: 18 → 15 → 4
Ratios: 1.20x → 3.75x
```

---

## Complete Example: "clock" Object

### WordNet Hypernym Path
```
clock (depth 10)
  ↓
timepiece (9)
  ↓
measuring instrument (8)
  ↓
instrument (7)
  ↓
device (6)  ← Mid candidate range starts
  ↓
instrumentality (5)  ← ⭐ Mid selected (all methods)
  ↓
artifact (4)
  ↓
whole (3)  ← Coarse candidate range starts
  ↓
object (2)  ← ⭐ Coarse selected (all methods)
  ↓
physical entity (1)
  ↓
entity (0)
```

### Three-Level Representation
```
Fine:   clock
Mid:    instrumentality  (depth 5)
Coarse: object          (depth 2)

Reasoning (V8.1): "Clock is an instrument/tool (mid-level functional category)
                   and a physical object (high-level domain)"
```

### Why These Selections?

**Mid = instrumentality (depth 5)**
- ✅ Clear functional category
- ✅ Depth 5 is preferred range
- ✅ More semantic than "device" (too technical)
- ✅ Less abstract than "artifact" (too broad)

**Coarse = object (depth 2)**
- ✅ Meaningful domain grouping
- ✅ Depth 2 is optimal
- ✅ More specific than "physical entity" (depth 1)
- ✅ More general than "whole" (depth 3)

---

## Relationship to Original Scene Graph

### Object Merging

Original VG has **30 object instances** with duplicates:
```
flowers (appears 2x), pot (appears 3x), clock (appears 1x), etc.
```

After deduplication: **18 unique fine-grained concepts**

### Relationship Inheritance

Relationships defined at fine-grained level are inherited:

```
Fine Level:
  clock -on-> wall
  flower -in-> pot

Mid Level (inherited & merged):
  instrumentality -on-> structure
  plant -in-> artifact

Coarse Level (inherited & merged):
  object -on-> object  (self-loop from merging)
  object -in-> object  (self-loop from merging)
```

**Note**: Self-loops are removed in graph visualizations but preserved in concept mappings.

---

## Method Differences in Granularity Selection

### V7: Adaptive Rules
```python
# Mid-level selection
mid_score = depth_score[5] + semantic_bonus("instrumentality")
          = 10         + 10
          = 20  ← Highest score wins

# Coarse-level selection
coarse_score = depth_score[2] + semantic_bonus("object")
             = 10         + 10
             = 20  ← Highest score wins
```

### V8: Basic LLM
```
LLM prompt: "Select most general (coarse) and clear categorical (mid) concepts"
LLM response: {"coarse": "object", "mid": "instrumentality"}
→ 72.2% success rate (sometimes fails, uses V7 fallback)
```

### V8.1: Context-Aware LLM
```
LLM prompt with scene context:
- All objects in scene
- Clock's position and size
- Clock's relationships (on-wall, part_of-building)

Two-stage selection:
1. Mid: "Which represents clock in this scene?" → instrumentality
2. Coarse: "High-level domain?" → object

LLM provides reasoning: "Clock is an instrument/tool and physical object"
→ 100% success rate
```

---

## Design Principles

### 1. Traceability
User can progressively drill down:
```
Coarse: "There's a physical entity in the scene"
  ↓ (refine)
Mid: "It's an instrumentality"
  ↓ (refine)
Fine: "It's a clock"
```

### 2. Meaningful Grouping
Coarse level groups semantically related objects:
```
object: {clock, pot, flower, street, railing, ...}
abstraction: {background, lot, words, sign}
process: {light}
```

### 3. Compression vs. Semantics
- **V7**: Optimizes compression (4 coarse concepts)
- **V8**: Conservative, poor compression (8 coarse concepts)
- **V8.1**: Balances both (4 coarse concepts with better semantics)

---

## Use Cases by Granularity

### Fine-Grained
- Object detection and localization
- Detailed spatial reasoning
- "Where is the clock in the image?"

### Mid-Level
- Categorical reasoning
- Scene understanding
- "What types of objects are present?" → instrumentality, organism, structure

### Coarse-Grained
- High-level scene classification
- Domain-specific reasoning
- "What domains does this scene contain?" → objects, abstractions

---

## See Also

- [METHODS_COMPARISON.md](METHODS_COMPARISON.md) - Compare V7/V8/V8.1 methods
- [WORDNET_INTEGRATION.md](WORDNET_INTEGRATION.md) - How WordNet depths are used
- [SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md](SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md) - Hierarchy construction details

---

**Generated**: 2025-10-03
**Repository**: HCNMN Documentation
