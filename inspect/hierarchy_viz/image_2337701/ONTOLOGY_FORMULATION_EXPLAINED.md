# WordNet Ontology Formulation for VG Image 2337701

## Executive Summary

**Image**: Beach scene with seagulls (VG_100K/2337701.jpg)
**Base Objects**: 11 unique types (shells, bird, wing, dirt, sand, seagull, wood, ground, etc.)
**Ontology Expansion**: **42.5x** (11 → 467 concepts)
**Hierarchy Depth**: 14 levels (specific → abstract)

---

## What is Ontology Formulation?

**Ontology formulation** is the process of organizing concepts into a **hierarchical knowledge structure** that captures relationships from **specific instances** to **abstract categories**.

```
Example: "seagull" concept

Specific (Fine-grained):
  seagull (the actual bird in the image)
    ↓
  bird (category of flying animals)
    ↓
  vertebrate (animals with backbones)
    ↓
  animal (living organisms)
    ↓
  organism (biological entities)
    ↓
Abstract (Coarse-grained):
  living thing (all life forms)
    ↓
  entity (most abstract concept)
```

### Why Multi-Granularity Matters

Different reasoning tasks require different levels of abstraction:

| Question | Granularity Level | Concept Used |
|----------|-------------------|--------------|
| "Is this a seagull?" | **Fine-grained** | seagull (specific) |
| "Is there a bird?" | **Mid-level** | bird (category) |
| "Are there living things?" | **Coarse-grained** | organism, entity |

The model can reason at **any level** depending on the question!

---

## 1️⃣ BASE CONCEPTS (VG Object Annotations)

### Input: 11 Object Types from Visual Genome

```
VG Image 2337701 Objects:
┌────────────┬──────────────────┬─────────────────────┐
│ Object ID  │ Name             │ Synset              │
├────────────┼──────────────────┼─────────────────────┤
│ 1058549    │ shells           │ shell.n.01          │
│ 1058534    │ piece            │ piece.n.01          │
│ 1058508    │ wing             │ wing.n.01           │
│ 5077       │ dirt             │ soil.n.02           │
│ 1058539    │ sand             │ sand.n.01           │
│ 1058543    │ seagull          │ seagull.n.01        │
│ 1058545    │ wood             │ wood.n.01           │
│ 1058542    │ ground           │ ground.n.01         │
│ 1058498    │ pebble           │ pebble.n.01         │
│ 3798579    │ head             │ head.n.01           │
│ 3798576    │ beach            │ beach.n.01          │
└────────────┴──────────────────┴─────────────────────┘
```

These are the **fine-grained, specific concepts** directly annotated in the image.

---

## 2️⃣ WORDNET HYPERNYM TRAVERSAL

### Process: For Each Concept, Climb the Hierarchy

**Example 1: "seagull" → abstract entity**

```
seagull.n.01 (The actual bird)
  ↓ IsA (hypernym)
larid.n.01 (Family of gulls)
  ↓ IsA
coastal diving bird.n.01 (Birds that dive for fish)
  ↓ IsA
seabird.n.01 (Birds that live near the ocean)
  ↓ IsA
aquatic bird.n.01 (Water-dwelling birds)
  ↓ IsA
bird.n.01 (All birds)
  ↓ IsA
vertebrate.n.01 (Animals with backbones)
  ↓ IsA
chordate.n.01 (Phylum Chordata)
  ↓ IsA
animal.n.01 (All animals)
  ↓ IsA
organism.n.01 (Living beings)
  ↓ IsA
living thing.n.01 (Biological entities)
  ↓ IsA
whole.n.02 (Complete entities)
  ↓ IsA
object.n.01 (Physical objects)
  ↓ IsA
physical entity.n.01 (Things with physical form)
  ↓ IsA
entity.n.01 (MOST ABSTRACT - everything that exists)
```

**14 levels of hierarchy!**

---

**Example 2: "sand" → abstract entity**

```
sand.n.01 (Beach sand)
  ↓ IsA
soil.n.02 (Earth material)
  ↓ IsA
material.n.01 (Physical substance)
  ↓ IsA
substance.n.07 (Matter)
  ↓ IsA
part.n.01 (Portion of something)
  ↓ IsA
relation.n.01 (Connection between things)
  ↓ IsA
abstraction.n.06 (Non-physical concept)
  ↓ IsA
entity.n.01 (Most abstract)
```

**8 levels of hierarchy**

---

**Example 3: "wing" → abstract entity**

```
wing.n.01 (Bird wing)
  ↓ IsA
appendage.n.01 (Body part extending from main body)
  ↓ IsA
external body part.n.01 (Outer body structures)
  ↓ IsA
body part.n.01 (Anatomical structure)
  ↓ IsA
part.n.02 (Component of a whole)
  ↓ IsA
natural object.n.01 (Naturally occurring object)
  ↓ IsA
whole.n.02 (Complete entity)
  ↓ IsA
object.n.01 (Physical thing)
  ↓ IsA
physical entity.n.01 (Has physical form)
  ↓ IsA
entity.n.01 (Most abstract)
```

**10 levels of hierarchy**

---

## 3️⃣ MULTI-GRANULARITY STRUCTURE

### Hierarchy Distribution Across 14 Levels

```
Level │ Concepts │ Granularity │ Examples
──────┼──────────┼─────────────┼─────────────────────────────────
  0   │    23    │ SPECIFIC    │ seagull, shell, wing, sand, pebble
  1   │    39    │    ↓        │ bird, shell, husk, ground
  2   │    36    │    ↓        │ bird, object, shell, ground
  3   │    43    │    ↓        │ piece, shell, foundation
  4   │    54    │ MID-LEVEL   │ piece, content, natural phenomenon
  5   │    62    │    ↓        │ animal material, top, earth, rock
  6   │    64    │    ↓        │ animal material, earth, actor
  7   │    58    │    ↓        │ piece, shell, fecal matter
  8   │    40    │ ABSTRACT    │ shell, mechanical device, focal point
  9   │    27    │    ↓        │ cause, action, gift
 10   │    13    │    ↓        │ living thing, whole
 11   │     3    │    ↓        │ substance, world, smell bark
 12   │     2    │    ↓        │ substance, object
 13   │     2    │    ↓        │ physical entity
 14   │     1    │ MOST        │ entity (everything)
      │         │ ABSTRACT    │
──────┴──────────┴─────────────┴─────────────────────────────────
Total: 467 concepts (42.5x expansion from 11 base)
```

### Granularity Breakdown

```
┌─────────────────────┬──────────┬─────────┬────────────────────┐
│ Granularity Level   │ Levels   │ Concepts│ Description        │
├─────────────────────┼──────────┼─────────┼────────────────────┤
│ FINE-GRAINED        │ L0 - L2  │  98     │ Specific instances │
│ (21.0%)             │          │         │ seagull, sand      │
├─────────────────────┼──────────┼─────────┼────────────────────┤
│ MID-LEVEL           │ L3 - L5  │ 159     │ Categories         │
│ (34.0%)             │          │         │ bird, material     │
├─────────────────────┼──────────┼─────────┼────────────────────┤
│ COARSE-GRAINED      │ L6 - L14 │ 210     │ Abstract concepts  │
│ (45.0%)             │          │         │ entity, object     │
└─────────────────────┴──────────┴─────────┴────────────────────┘
```

**Key Insight**: The hierarchy is **bottom-heavy** (more abstract concepts than specific ones) because multiple specific concepts converge to shared abstract parents.

---

## 4️⃣ HIERARCHY CONVERGENCE

### How Multiple Concepts Converge to Abstract Nodes

```
Fine-grained concepts:
    seagull    bird    wing
       │        │       │
       └────────┴───────┘
              ↓
      vertebrate (L3)
              ↓
       animal (L5)
              ↓
      organism (L7)
              ↓
    living thing (L10)
              ↓
      entity (L14)


    sand    dirt    ground
      │      │        │
      └──────┴────────┘
             ↓
       material (L4)
             ↓
      substance (L5)
             ↓
        part (L6)
             ↓
      abstraction (L7)
             ↓
       entity (L14)
```

**Convergence creates a diamond structure**: Many specific concepts → Fewer mid-level categories → Single root (entity)

---

## 5️⃣ ONTOLOGY FORMULATION STATISTICS

### Expansion Metrics

```
Base Concepts (VG):           11
Expanded Concepts (WordNet):  467
Expansion Ratio:              42.5x
```

**Why such high expansion?**
- Each concept has **multiple synsets** (word senses)
- Each synset has **multiple hypernym paths** (different ways to generalize)
- Paths are **long** (up to 14 levels deep)

### Depth Analysis

```
Maximum Depth:     14 levels (entity at root)
Average Depth:     ~6.5 levels per concept
Deepest Concepts:  "seagull" (14 levels), "wing" (10 levels)
Shallowest:        "entity" itself (1 level)
```

### Coverage Metrics

```
Synsets with paths:         11/11 (100%)
Concepts without hierarchy:  0/11 (0%)
Coverage rate:              100%
```

**All VG objects successfully mapped to WordNet!**

---

## 6️⃣ VISUALIZATION BREAKDOWN

### Panel 1: WordNet Hierarchy Levels
**Shows**: 15 horizontal bars colored by depth
- **Purple/Dark** (L0-L2): Fine-grained (seagull, sand, pebble)
- **Teal/Green** (L3-L6): Mid-level (bird, material, object)
- **Yellow** (L7-L14): Coarse-grained (entity, abstraction)

**Key Insight**: Most concepts accumulate in mid-levels (L4-L6)

---

### Panel 2: Sample Hypernym Paths
**Shows**: Specific examples of concept → abstract chains
- **bird**: physical entity → object → whole
- **dirt**: abstraction → relation → part → substance
- **ground**: abstraction → psychological feature → cognition

**Key Insight**: Different concepts take different paths to "entity"

---

### Panel 3: Concepts per Hierarchy Level (Bar Chart)
**Shows**: Distribution of 467 concepts across 15 levels
- **Peak at L5-L6**: 62-64 concepts (maximum convergence)
- **L0**: 23 concepts (base objects + immediate hypernyms)
- **L14**: 1 concept (entity - the root)

**Key Insight**: Classic hierarchy pyramid shape

---

### Panel 4: Multi-Granularity Pyramid
**Shows**: Visual representation of abstraction levels
- **Wide base** (green): Many specific concepts
- **Narrowing middle** (teal): Fewer mid-level categories
- **Narrow top** (yellow): Few abstract concepts
- **Single point**: entity

**Key Insight**: Ontology naturally forms inverted pyramid

---

### Panel 5: Concept → Abstract Hierarchy (Table)
**Shows**: Explicit paths for each base concept

Example row:
```
bird → entity → physical entity → object → whole → living thing
```

**Key Insight**: Shows exact reasoning chains the model can follow

---

### Panel 6: Hierarchy Statistics
**Shows**: Complete numerical summary
- Expansion ratio: 42.5x
- Depth distribution: 14 levels
- Granularity breakdown: 21% fine / 34% mid / 45% coarse
- Coverage: 100%

---

## 7️⃣ IMAGE VISUALIZATION INSIGHTS

### Objects Colored by Hierarchy Depth

In the left panel of `image_with_hierarchy.png`:
- **Bounding boxes** are colored by their **maximum hierarchy depth**
- **Purple boxes**: Shallow hierarchy (e.g., "ground" - 8 levels)
- **Yellow boxes**: Deep hierarchy (e.g., "seagull" - 14 levels)

**Visual Pattern**: Living things (seagull, bird) have **deeper hierarchies** than inanimate objects (sand, pebble)

### Why Depth Varies

| Object Type | Depth | Reason |
|-------------|-------|--------|
| **seagull** | 14    | Rich biological taxonomy (species → genus → family → order → ...) |
| **wing** | 10    | Anatomical structure with many parent categories |
| **sand** | 8     | Material substance (shorter path to abstraction) |
| **pebble** | 9     | Physical object (moderate complexity) |
| **ground** | 8     | Spatial concept (direct to abstraction) |

---

## 8️⃣ HOW THE MODEL USES THIS HIERARCHY

### Multi-Granularity Reasoning Examples

**Question 1**: "Is there a seagull?"
```
Reasoning:
1. Look for concept "seagull" at L0 (fine-grained)
2. Match with image annotation → YES
```

**Question 2**: "Is there a bird?"
```
Reasoning:
1. Look for concept "bird" at L5 (mid-level)
2. Traverse up from "seagull" → "bird" → YES
```

**Question 3**: "Are there living things?"
```
Reasoning:
1. Look for concept "living thing" at L10 (coarse)
2. Traverse up from "seagull" → "organism" → "living thing" → YES
```

**Question 4**: "What kind of bird is it?"
```
Reasoning:
1. Find "bird" at L5
2. Traverse DOWN to specific instances
3. Options: seagull (L0), larid (L1), coastal diving bird (L2)
4. Answer: "seagull" (most specific)
```

### Cross-Level Reasoning

**Question**: "Is the seagull on the beach?"

```
Step 1: Identify concepts
  - "seagull" → L0 (fine-grained)
  - "beach" → L0 (fine-grained)

Step 2: Check spatial topology
  - topology[seagull][beach] > 0 → spatially related

Step 3: Answer
  - YES (both concepts present and spatially connected)
```

---

## 9️⃣ COMPARISON TO PAPER'S APPROACH

### Paper (VQA-Based Ontology)

**Input**: VQA question tokens
- "What color is the bird?"
- Extract: "color", "bird"

**Hierarchy**: WordNet augmentation
- "color" → property → attribute → abstraction → entity
- "bird" → vertebrate → animal → organism → entity

**Result**: Hierarchy based on **linguistic question structure**

### This Demo (VG-Based Ontology)

**Input**: VG object annotations
- seagull, wing, sand, ground (from image)

**Hierarchy**: WordNet augmentation
- "seagull" → bird → vertebrate → animal → entity
- "sand" → soil → material → substance → entity

**Result**: Hierarchy based on **visual scene content**

### Key Difference

| Aspect | Paper (VQA) | This Demo (VG) |
|--------|-------------|----------------|
| **Source** | Question text | Image annotations |
| **Concepts** | Question-relevant | All visible objects |
| **Grounding** | Linguistic | Visual (bboxes) |
| **Hierarchy** | Task-specific | Scene-comprehensive |

---

## 🔟 IMPROVEMENTS & FUTURE WORK

### Current Limitations

1. **Multiple Synsets**: Each word can have multiple meanings
   - "bank" → financial institution OR river bank
   - Solution: Use context or LLM disambiguation

2. **Ambiguous Paths**: Multiple routes to root
   - "bird" → animal → entity (biological path)
   - "bird" → object → entity (physical path)
   - Solution: Choose longest/shortest path consistently

3. **No Visual Validation**: All concepts from WordNet accepted
   - May include irrelevant abstract concepts
   - Solution: Filter by visual relevance using VLMs

### Proposed Enhancements

#### 1. Add ConceptNet Relations
```
Current:  seagull → bird → animal (IsA only)
Enhanced: seagull → [HasPart] wings
          seagull → [AtLocation] beach
          seagull → [CapableOf] flying
```

#### 2. Visual Validation with VLMs
```python
# Prompt GPT-4V for each concept
prompt = f"Is '{concept}' visible in this image region?"
if vlm_confirms(image_crop, concept):
    add_to_hierarchy(concept)
```

#### 3. Hierarchy Pruning
```
Current:  467 concepts (many irrelevant abstractions)
Pruned:   ~100 concepts (visually-relevant only)
Method:   Remove concepts not mentioned in VG annotations or VLM descriptions
```

---

## 📊 SUMMARY

### What We Built

✅ **Ontology formulation** from 11 VG objects → 467 multi-granularity concepts
✅ **42.5x expansion** using WordNet hypernym traversal
✅ **14-level hierarchy** from specific (seagull) to abstract (entity)
✅ **Multi-granularity structure**: 21% fine / 34% mid / 45% coarse
✅ **Complete visualization**: 6-panel hierarchy + image overlay

### Key Achievements

1. **Automatic hierarchy generation** - No manual ontology engineering
2. **Multi-level reasoning** - Model can answer at any abstraction level
3. **100% coverage** - All VG objects successfully mapped
4. **Grounded in image** - Hierarchy tied to visual evidence

### Files Generated

```
hierarchy_viz/image_2337701/
├── wordnet_hierarchy_detailed.png  (6-panel hierarchy visualization)
├── image_with_hierarchy.png        (image + hierarchy paths)
├── hierarchy_data.json             (complete ontology data)
└── ONTOLOGY_FORMULATION_EXPLAINED.md (this document)
```

---

## 🎯 NEXT STEPS

1. **Run on more images** to see hierarchy variation
2. **Add VLM validation** to prune irrelevant concepts
3. **Integrate ConceptNet** for richer relations
4. **Compare to VQA-based ontology** from the paper
5. **Evaluate downstream** on VQA tasks