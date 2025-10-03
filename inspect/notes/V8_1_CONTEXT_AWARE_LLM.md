# V8.1: Context-Aware LLM-Guided Granularity Selection

**Method**: Qwen3-0.6B with scene context + two-stage selection
**Implementation**: `llm_granularity_selector_v8_1.py`
**Performance**: 100% success rate (18/18), ~500ms per object, 4.50x compression

## Overview

V8.1 achieves perfect LLM success by providing full scene graph context and using goal-oriented two-stage prompting. This is the recommended LLM-based method.

## Key Improvements Over V8

| Aspect | V8 | V8.1 |
|--------|-----|------|
| **Context** | Object name + WordNet path only | Full scene graph |
| **Prompting** | Single-stage, generic | Two-stage, goal-oriented |
| **Success Rate** | 72.2% (13/18) | **100%** (18/18) ✨ |
| **Compression** | 2.25x | **4.50x** ✨ |
| **Reasoning** | None | ✅ Included |
| **Scene Awareness** | None | Spatial + relational |

## Method

### 1. Scene Context Formatting

**Extract scene information for LLM**:

```python
def format_scene_context(all_objects, relationships, current_object):
    """Format rich scene context for prompt."""

    # All objects with positions
    objects_summary = "flowers@(325,851,213x102), pot@(360,918,138x66), ..."

    # Current object's bbox
    current_bbox = "position (100,50), size 80x120"

    # Relationships involving current object
    relationships_summary = "clock-on-wall, clock-part_of-building"

    return {
        'objects_summary': objects_summary,
        'current_bbox': current_bbox,
        'relationships_summary': relationships_summary
    }
```

### 2. Two-Stage Prompt Structure

**Stage 1: Select Mid-Level (depth 4-6)**
**Stage 2: Select Coarse-Level (depth 1-3) based on mid**

```python
prompt = f"""**Task**: Create 3-level hierarchical abstraction using WordNet.

**Goal**: Select concepts that create meaningful, traceable abstraction levels:
1. Preserve high-level semantic info at coarse
2. Allow progressive refinement: coarse → mid → fine
3. Group similar objects meaningfully at each level

**Scene Context**:
- Objects in scene: {objects_summary}
- Current object "{object_name}": {current_bbox}
- Relationships: {relationships_summary}

**WordNet Path**: entity → physical entity → ... → {object_name}

**STAGE 1 - Select MID-level (depth 4-6)**:
Options: {mid_options}

Question: Which concept best represents "{object_name}" as a mid-level category
in this scene context?
Consider: What functional/semantic category does this object belong to?

**STAGE 2 - Select COARSE-level (depth 1-3)**:
Options: {coarse_options}

Question: Which concept provides appropriate high-level abstraction?
Consider: What is the most general meaningful domain for grouping similar objects?

**Output JSON**:
{{"mid": "concept_name", "mid_depth": N, "coarse": "concept_name", "coarse_depth": N, "reasoning": "explanation"}}

**Example for "clock"**:
{{"mid": "instrumentality", "mid_depth": 5, "coarse": "object", "coarse_depth": 2,
  "reasoning": "Clock is an instrument/tool (mid) and a physical object (coarse)"}}

**Now select for "{object_name}"**:"""
```

### 3. LLM Inference

Same as V8 but with richer input:

```python
text = self.tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False  # Still critical!
)

outputs = self.model.generate(
    **inputs,
    max_new_tokens=100,  # +20 for reasoning
    temperature=0.7,
    top_p=0.8,
    top_k=20,
    do_sample=True
)
```

### 4. Parse Response with Reasoning

```python
{
  "mid": "instrumentality",
  "mid_depth": 5,
  "coarse": "object",
  "coarse_depth": 2,
  "reasoning": "Clock is an instrument/tool (mid-level functional category) and a physical object (high-level domain)"
}
```

## Complete Example: "sign" Object

### Scene Context
```
Objects in scene: flowers@(325,851), pot@(360,918), billboard@(52,77),
                  street@(0,800), sign@(200,100), ...

Current object: "sign" at position (200,100), size 60x80

Relationships: sign-on-wall, sign-near-street
```

### WordNet Path
```
entity (0) → abstraction (1) → communication (2) → indication (3) →
evidence (4) → clue (5) → sign (6)
```

### Prompt to LLM
```
**Task**: Create 3-level hierarchical abstraction using WordNet.

**Goal**: Traceable hierarchy for scene understanding

**Scene Context**:
- Objects: flowers@(325,851), pot@(360,918), sign@(200,100), ...
- Current: "sign" at (200,100), size 60x80
- Relationships: sign-on-wall, sign-near-street

**WordNet Path**: entity → abstraction → communication → ... → sign

**STAGE 1 - Select MID (4-6)**:
Options: "evidence" (depth 4), "clue" (depth 5), "sign" (depth 6)

Which represents "sign" in this scene context?
Consider: Functional/semantic category

**STAGE 2 - Select COARSE (1-3)**:
Options: "abstraction" (depth 1), "communication" (depth 2), "indication" (depth 3)

High-level abstraction for grouping?

Output JSON with reasoning:
```

### LLM Response
```json
{
  "mid": "clue",
  "mid_depth": 5,
  "coarse": "communication",
  "coarse_depth": 2,
  "reasoning": "Sign is a functional element that provides a clue to its context,
aligning with mid-level concept 'clue'. It fits broader category 'communication'
which includes signs as a form of signaling."
}
```

### Result
```
Fine: sign
Mid: clue (LLM selected with context)
Coarse: communication (LLM selected, better than "abstraction")
Method: llm ✓
Reasoning: Context-aware semantic understanding
```

**Compare to V7/V8**:
- V7: clue (d=5) → abstraction (d=1) [rule-based, good]
- V8: sign (d=6) → abstraction (d=1) [kept same name, generic coarse]
- V8.1: clue (d=5) → communication (d=2) [⭐ best semantic quality]

## Results on Image 498335

### Performance Metrics
- **Objects processed**: 18 unique
- **LLM success**: 18/18 (100%) ⭐
- **Fallback**: 0/18 (0%) ⭐
- **Processing time**: ~9 seconds (~500ms per object)
- **Fine concepts**: 18
- **Mid concepts**: 15
- **Coarse concepts**: 4 ⭐ (optimal)
- **Compression**: 4.50x ⭐ (matches V7)

### Coarse-Level Distribution (Optimal)
```
physical entity: 9 objects (clock, pot, flower, railing, ...)
object: 5 objects (...)
abstraction: 3 objects (background, lot, words)
communication: 1 object (sign)

Total: 4 coarse concepts (perfect grouping)
```

### Sample Reasoning Outputs

**Edge**:
```
"The 'edge' represents a boundary between regions, aligning with mid-level
'boundary' (depth 6). It serves as a physical entity, matching coarse-level
'physical entity' (depth 1)."
```

**Light**:
```
"Light is a physical phenomenon (mid-level) that can be abstracted as a
physical entity (coarse-level) representing the object's physical properties
and behavior."
```

**Pot**:
```
"Pot is a physical object, and 'artifact' represents the most general category
that includes objects like pots, utensils, and tools. It captures both its
functional role as a cooking tool and its physical existence in the scene."
```

## Why 100% Success Rate?

### 1. Scene Context Helps LLM
LLM sees:
- **Spatial info**: Object positions help understand scene layout
- **Relationships**: Connections reveal semantic roles
- **Co-occurrence**: Other objects provide context

Example: "clock-on-wall" relationship helps LLM understand clock's role

### 2. Goal-Oriented Prompting
Clear explanation of purpose:
- Create traceable hierarchy
- Coarse → mid → fine for progressive refinement
- Group similar objects meaningfully

LLM understands WHY it's selecting concepts

### 3. Two-Stage Selection
Mid first, then coarse ensures:
- Consistency between levels
- Mid selection informs coarse choice
- Better alignment with hierarchy goals

### 4. Example-Driven
Including "clock" example shows expected format and reasoning quality

### 5. Reasoning Required
Forcing LLM to explain makes it think deeper about semantic relationships

## Advantages

✅ **100% success**: No fallbacks needed
✅ **Optimal compression**: 4.50x (matches V7's quality)
✅ **Context-aware**: Understands scene, not just isolated objects
✅ **Explainable**: Natural language reasoning for each decision
✅ **Semantic quality**: Better abstraction choices than rules
✅ **Goal-aligned**: Follows traceable hierarchy principle
✅ **Two-stage**: Consistent mid/coarse selections

## Limitations

❌ **Speed**: ~500ms per object (3000x slower than V7)
❌ **LLM infrastructure**: Requires GPU, model loading
❌ **Determinism**: Slight variations possible (temperature=0.7)
❌ **Model dependency**: Requires Qwen3 or compatible LLM

## When to Use V8.1

### Best For:
- **Research**: Explainability and reasoning required
- **Quality-critical**: Semantic accuracy more important than speed
- **Context-dependent**: Decisions should consider full scene
- **User-facing**: Need to explain abstraction choices
- **Production hybrid**: Use V8.1 for critical paths, V7 for batch

### Not Ideal For:
- Real-time applications (use V7)
- Large-scale batch processing (use V7)
- Resource-constrained environments (use V7)
- Deterministic requirements (use V7)

## Implementation Details

### Scene Context Function

```python
def format_scene_context(self, all_objects, relationships, current_object_name):
    """Format rich scene context."""
    # Build objects list with spatial info
    objects_list = []
    current_bbox = None

    for obj in all_objects:
        obj_name = obj['names'][0]
        x, y, w, h = obj.get('x', 0), obj.get('y', 0), obj.get('w', 0), obj.get('h', 0)
        objects_list.append(f"{obj_name}@({x},{y},{w}x{h})")

        if obj_name == current_object_name:
            current_bbox = f"position ({x},{y}), size {w}x{h}"

    # Limit to first 15 objects (prompt length)
    objects_summary = ", ".join(objects_list[:15])
    if len(objects_list) > 15:
        objects_summary += f", ... (+{len(objects_list)-15} more)"

    # Extract relationships
    related_to = []
    for rel in relationships.get('relationships', []):
        # Find relationships involving current object
        # ...
    relationships_summary = ", ".join(related_to[:5])

    return {
        'objects_summary': objects_summary,
        'current_bbox': current_bbox,
        'relationships_summary': relationships_summary
    }
```

### Core Selection Function

```python
def select_granularity_with_context(self, object_name, synset, all_objects, relationships):
    """Context-aware LLM selection."""
    # 1. Get WordNet path
    wordnet_path = self.format_wordnet_path(synset)

    # 2. Format scene context
    scene_context = self.format_scene_context(all_objects, relationships, object_name)

    # 3. Create two-stage prompt
    prompt = self.create_two_stage_prompt(object_name, wordnet_path, scene_context)

    # 4. LLM inference (with enable_thinking=False)
    # ...

    # 5. Parse response (includes reasoning)
    selection = self.extract_json_from_response(response)

    if selection and self.validate_selection(selection, wordnet_path):
        return {**selection, 'method': 'llm'}
    else:
        return self.fallback_selection(wordnet_path)  # V7 rules
```

## Best Practices

### Prompt Design
1. **Clear goal**: Explain purpose of hierarchy
2. **Rich context**: Include spatial and relational info
3. **Two-stage**: Select mid first, then coarse
4. **Example-driven**: Show expected output format
5. **Require reasoning**: Force deeper semantic analysis

### Context Formatting
1. **Limit length**: Top 15 objects to avoid token limits
2. **Spatial info**: Include bboxes for positioning
3. **Relationships**: Show relevant connections only
4. **Current object**: Highlight target object clearly

### Error Handling
1. **Always have fallback**: Use V7 rules if LLM fails
2. **Validate output**: Check depth ranges, concept existence
3. **Timeout**: Set reasonable generation limits
4. **Robust parsing**: Handle malformed JSON gracefully

## See Also

- [METHODS_COMPARISON.md](METHODS_COMPARISON.md) - Compare all methods
- [V7_ADAPTIVE_RULES.md](V7_ADAPTIVE_RULES.md) - Fast rule-based alternative
- [V8_BASIC_LLM.md](V8_BASIC_LLM.md) - Why context matters (V8 comparison)
- [PROMPT_ENGINEERING.md](PROMPT_ENGINEERING.md) - Detailed prompting strategies
- [SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md](SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md) - Scene graph integration

---

**Generated**: 2025-10-03
**File**: `inspect/llm_granularity_selector_v8_1.py`
**Status**: Recommended LLM method ⭐
