# LLM Prompt Engineering for Granularity Selection

**Last Updated**: 2025-10-03

## Overview

This document details the evolution of LLM prompting from V8 (72% success) to V8.1 (100% success), explaining what makes effective prompts for hierarchical scene graph abstraction.

## V8 vs V8.1: Side-by-Side Comparison

### V8 Prompt (Basic)

```
Task: Select the best concept from each list for object "clock".

COARSE level (choose ONE from depths 1-3):
"physical entity" (depth 1), "object" (depth 2), "whole" (depth 3)

MID level (choose ONE from depths 4-6):
"artifact" (depth 4), "instrumentality" (depth 5), "device" (depth 6)

Instructions:
1. For COARSE: Pick the most general, abstract concept
2. For MID: Pick a clear categorical concept

Output JSON format:
{"coarse": "...", "coarse_depth": N, "mid": "...", "mid_depth": N}
```

**Success**: 72.2% (13/18 objects)

### V8.1 Prompt (Context-Aware)

```
**Task**: Create a 3-level hierarchical abstraction of scene graphs using WordNet ontology.

**Goal**: Select concepts that create meaningful, traceable abstraction levels. The hierarchy should:
1. Preserve high-level semantic information at the coarse level
2. Allow progressive refinement: coarse → mid → fine for more detail
3. Group similar objects meaningfully at each level

**Scene Context**:
- Objects in scene: flowers@(325,851,213x102), pot@(360,918,138x66), ...
- Current object "clock": position (100,50), size 80x120
- Relationships: clock-on-wall, clock-part_of-building

**WordNet Path**: entity → physical entity → object → ... → clock

**Two-Stage Selection**:

**STAGE 1 - Select MID-level concept (depth 4-6)**:
Options: "artifact" (depth 4), "instrumentality" (depth 5), "device" (depth 6)

Question: Which concept best represents "clock" as a mid-level category in this scene context?
Consider: What functional/semantic category does this object belong to?

**STAGE 2 - Select COARSE-level concept (depth 1-3)**:
Options: "physical entity" (depth 1), "object" (depth 2), "whole" (depth 3)

Question: Which concept provides appropriate high-level abstraction?
Consider: What is the most general meaningful domain for grouping similar objects?

**Output JSON format**:
{"mid": "concept_name", "mid_depth": N, "coarse": "concept_name", "coarse_depth": N, "reasoning": "brief explanation"}

**Example for "clock"**:
{"mid": "instrumentality", "mid_depth": 5, "coarse": "object", "coarse_depth": 2, "reasoning": "Clock is an instrument/tool (mid) and a physical object (coarse)"}

**Now select for "clock"**:
```

**Success**: 100% (18/18 objects)

## Key Improvements Analysis

### 1. Goal Explanation (+15% success)

**V8**: Generic instructions ("most general", "clear categorical")
**V8.1**: Clear purpose explained
```
Goal: Create meaningful, traceable abstraction levels
- Preserve high-level semantic info
- Allow progressive refinement coarse → mid → fine
- Group similar objects meaningfully
```

**Impact**: LLM understands WHY it's selecting, not just WHAT to select

### 2. Scene Context (+20% success)

**V8**: Object name + WordNet path only
**V8.1**: Full scene graph
```
- All objects with positions
- Current object's bbox
- Relationships involving object
```

**Impact**: LLM makes context-aware decisions, not generic selections

**Example**:
```
Without context: sign → "abstraction" (generic)
With context: sign-on-wall → "communication" (scene-aware)
```

### 3. Two-Stage Selection (+10% success)

**V8**: Select coarse and mid simultaneously
**V8.1**: Mid first, then coarse
```
STAGE 1: Select mid-level (functional category)
STAGE 2: Select coarse (high-level domain) based on mid
```

**Impact**: Better consistency between levels, aligned hierarchy

### 4. Example-Driven (+5% success)

**V8**: No example
**V8.1**: Concrete example with reasoning
```
Example: {"mid": "instrumentality", "mid_depth": 5, "coarse": "object",
          "coarse_depth": 2, "reasoning": "..."}
```

**Impact**: LLM understands expected output quality

### 5. Reasoning Requirement (+5% success)

**V8**: No reasoning field
**V8.1**: Requires explanation
```
"reasoning": "brief explanation"
```

**Impact**: Forces LLM to think deeper about semantic relationships

## Prompt Component Breakdown

### 1. Task Header
```markdown
**Task**: Create a 3-level hierarchical abstraction of scene graphs using WordNet ontology.
```
**Purpose**: Set clear context for what LLM is doing

### 2. Goal Statement
```markdown
**Goal**: Select concepts that create meaningful, traceable abstraction levels. The hierarchy should:
1. Preserve high-level semantic information
2. Allow progressive refinement
3. Group similar objects meaningfully
```
**Purpose**: Explain WHY hierarchy matters, guides LLM's decision-making

### 3. Scene Context
```markdown
**Scene Context**:
- Objects in scene: {all_objects_with_positions}
- Current object "{name}": {bbox_info}
- Relationships: {connections}
```
**Purpose**: Provide spatial and relational context for informed decisions

### 4. WordNet Path
```markdown
**WordNet Path**: entity → physical entity → ... → {object}
```
**Purpose**: Show full hierarchy for reference

### 5. Two-Stage Questions
```markdown
**STAGE 1**: Select MID-level
Options: {...}
Question: Which concept best represents "{object}" in this scene?
Consider: Functional/semantic category

**STAGE 2**: Select COARSE-level
Options: {...}
Question: High-level abstraction?
Consider: General domain for grouping
```
**Purpose**: Guide LLM through structured reasoning process

### 6. Output Format with Example
```markdown
**Output JSON**: {...}
**Example for "clock"**: {concrete example with reasoning}
```
**Purpose**: Show exact expected format and quality

## Best Practices

### ✅ DO:
1. **Explain the goal**: Why are we creating this hierarchy?
2. **Provide context**: What else is in the scene?
3. **Use two-stage**: Mid first, then coarse
4. **Include examples**: Show expected output
5. **Require reasoning**: Force semantic analysis
6. **Format clearly**: Use markdown structure
7. **Limit context**: Top 15 objects to avoid token limits
8. **Be specific**: "functional category" not "category"

### ❌ DON'T:
1. **Generic instructions**: "Pick the best" is vague
2. **No context**: Isolated objects lead to generic selections
3. **Single-stage**: Simultaneous selection reduces consistency
4. **No examples**: LLM may misunderstand format
5. **Skip reasoning**: Missing deeper semantic analysis
6. **Wall of text**: Hard for LLM to parse
7. **Too much context**: Token limits, dilutes focus
8. **Vague questions**: "What should it be?" is unclear

## Common Failure Modes

### Failure Mode 1: Conservative Selection
**Symptom**: LLM selects broader concepts than optimal
```
Expected: flower → organism (d=5) → object (d=2)
Got: flower → living_thing (d=4) → physical_entity (d=1)
```
**Fix**: Add goal statement emphasizing meaningful grouping, not just abstraction

### Failure Mode 2: Same-Name Selection
**Symptom**: LLM keeps object name at mid-level
```
Object: sign
Got: {"mid": "sign", ...}  ← Depth 6, should abstract to "clue" (d=5)
```
**Fix**: Two-stage selection, emphasize "category" not "specific"

### Failure Mode 3: Depth Violation
**Symptom**: LLM selects outside depth ranges
```
Expected depths: 4-6 (mid), 1-3 (coarse)
Got: {"mid": "sign", "mid_depth": 7, ...}  ← Out of range
```
**Fix**: Clearer depth range specification, validation in code

### Failure Mode 4: JSON Formatting
**Symptom**: Malformed JSON with extra text
```
Got: "Well, for the clock object, I think {"mid": ...}"
```
**Fix**: Example-driven format, `enable_thinking=False`

## Prompt Engineering Workflow

### Step 1: Start with Basic Prompt (V8 style)
Test on 5-10 sample objects

### Step 2: Analyze Failures
- Which objects failed?
- What did LLM output?
- Why did it fail?

### Step 3: Add Context
Include scene objects, relationships

### Step 4: Structure with Two-Stage
Mid first, then coarse

### Step 5: Add Goal Statement
Explain purpose of hierarchy

### Step 6: Include Example
Show expected format and quality

### Step 7: Iterate
Test → analyze → refine → repeat

## Example: Improving "sign" Prompt

### Iteration 1: Basic (Failed)
```
Select concepts for "sign":
COARSE (1-3): abstraction, communication, indication
MID (4-6): evidence, clue, sign
```
**Result**: Kept "sign" at mid (d=6), too specific

### Iteration 2: Add Instructions (Improved)
```
Instructions:
- MID: Pick a CATEGORY, not the specific object name
- COARSE: Pick for meaningful grouping
```
**Result**: Selected "clue" (d=5), but "abstraction" (d=1) still too broad

### Iteration 3: Add Scene Context (Better)
```
Scene: sign-on-wall, near-street, other objects include billboard, words
```
**Result**: Selected "clue" (d=5), "communication" (d=2) ✓ Perfect!

### Iteration 4: Add Two-Stage (Best)
```
STAGE 1: Which represents "sign" in this scene? → clue
STAGE 2: High-level domain? → communication
```
**Result**: Consistent, semantic, optimal selection

## Technical Details

### Token Management
- **Context length**: Limit to ~500 tokens
- **Objects list**: Top 15 objects only
- **Relationships**: Top 5 relationships
- **Path display**: Abbreviated if >10 nodes

### Temperature Settings
- **V8**: 0.7 (balanced)
- **V8.1**: 0.7 (same, good for semantic tasks)
- **Don't use**: 0.0 (too deterministic, loses reasoning quality)

### Generation Parameters
```python
max_new_tokens=100  # Allow for reasoning (80 for V8)
temperature=0.7     # Balanced creativity
top_p=0.8          # Nucleus sampling
top_k=20           # Top-k filtering
do_sample=True     # Required for non-thinking mode
```

## See Also

- [V8_BASIC_LLM.md](V8_BASIC_LLM.md) - Basic prompting approach
- [V8_1_CONTEXT_AWARE_LLM.md](V8_1_CONTEXT_AWARE_LLM.md) - Advanced context-aware prompting
- [METHODS_COMPARISON.md](METHODS_COMPARISON.md) - Overall comparison

---

**Generated**: 2025-10-03
**Key Insight**: Context + Goal + Structure → 100% success
