# V8: Basic LLM-Guided Granularity Selection

**Method**: Qwen3-0.6B LLM with simple prompting
**Implementation**: `llm_granularity_selector.py`
**Performance**: 72.2% success rate (13/18), ~500ms per object

## Overview

V8 replaces V7's rule-based scoring with LLM-based semantic understanding. The LLM analyzes WordNet paths and selects optimal concepts based on semantic meaning rather than heuristic scores.

**Key Innovation**: Fixed Qwen3's thinking mode issue by adding `enable_thinking=False`

## Method

### 1. WordNet Path Extraction
Same as V7:
```python
synset = wn.synsets("clock")[0]
path = synset.hypernym_paths()[0]
# [(entity, 0), ..., (instrumentality, 5), ..., (clock, 10)]
```

### 2. Extract Candidates
```python
coarse_candidates = [(c, d) for c, d in path if 1 <= d <= 3]
mid_candidates = [(c, d) for c, d in path if 4 <= d <= 6]
```

### 3. Construct LLM Prompt

```python
prompt = f"""Task: Select the best concept from each list for object "{object_name}".

COARSE level (choose ONE from depths 1-3):
{', '.join(coarse_options)}

MID level (choose ONE from depths 4-6):
{', '.join(mid_options)}

Instructions:
1. For COARSE: Pick the most general, abstract concept
2. For MID: Pick a clear categorical concept

Output JSON format (fill in actual concept names and depths):
{{"coarse": "concept_name_here", "coarse_depth": depth_number, "mid": "concept_name_here", "mid_depth": depth_number}}"""
```

### 4. LLM Inference

**Critical Fix**: `enable_thinking=False`

```python
# Apply chat template with thinking disabled
text = self.tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False  # ⚠ CRITICAL: Prevents <think> tags
)

# Generate
outputs = self.model.generate(
    **inputs,
    max_new_tokens=80,
    temperature=0.7,  # Non-thinking mode setting
    top_p=0.8,
    top_k=20,
    do_sample=True,   # Required for non-thinking mode
    pad_token_id=self.tokenizer.eos_token_id
)
```

**Why `enable_thinking=False` is Critical**:
- Qwen3 has built-in "thinking mode" that generates reasoning in `<think>` tags
- With thinking enabled: `<think>Let me analyze...</think>{"coarse": "...", ...}`
- This breaks JSON parsing → 0% success rate
- With thinking disabled: `{"coarse": "...", ...}` → Clean JSON

### 5. Parse JSON Response

```python
def extract_json_from_response(self, response):
    # Try direct parse
    try:
        return json.loads(response.strip())
    except:
        pass

    # Try regex extraction
    json_pattern = r'\{[^}]*"coarse"[^}]*"mid"[^}]*\}'
    matches = re.findall(json_pattern, response, re.DOTALL)
    # ... fallback parsing logic
```

### 6. Validate and Fallback

```python
if selection and self.validate_selection(selection, wordnet_path):
    return {**selection, 'method': 'llm'}
else:
    # Fall back to V7 adaptive rules
    return self.fallback_selection(wordnet_path)
```

## Complete Example: "clock"

### Input
```
Object: clock
WordNet path: entity → physical entity → object → whole → artifact →
              instrumentality → device → ... → clock

Coarse candidates (1-3): physical entity (1), object (2), whole (3)
Mid candidates (4-6): artifact (4), instrumentality (5), device (6)
```

### Prompt Sent to LLM
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
{"coarse": "concept_name_here", "coarse_depth": depth_number, "mid": "concept_name_here", "mid_depth": depth_number}
```

### LLM Response
```json
{
  "coarse": "object",
  "coarse_depth": 2,
  "mid": "instrumentality",
  "mid_depth": 5
}
```

### Result
```
Fine: clock
Mid: instrumentality (LLM selected)
Coarse: object (LLM selected)
Method: llm ✓
```

##Results on Image 498335

### Performance Metrics
- **Objects processed**: 18 unique
- **LLM success**: 13/18 (72.2%)
- **Fallback to V7**: 5/18 (27.8%)
- **Processing time**: ~9 seconds total (~500ms per object)
- **Fine concepts**: 18
- **Mid concepts**: 15
- **Coarse concepts**: 8 (too conservative!)
- **Compression**: 2.25x (poor compared to V7's 4.50x)

### Failure Analysis

**Objects that fell back to V7 rules** (5/18):
1. flower → Chose depth 10 (too specific)
2-5. Other conservative selections outside depth ranges

**Problem**: LLM sometimes selects concepts outside depth ranges or fails JSON formatting

### Coarse-Level Distribution
```
physical entity: 9 objects (too broad, LLM conservative)
object: 5 objects
abstraction: 3 objects
communication: 1 object
... (8 total - poor compression)
```

Compare to V7: Only 4 coarse concepts

## Advantages

✅ **Semantic understanding**: LLM comprehends meaning, not just patterns
✅ **Flexible**: Can adapt to novel objects
✅ **No manual tuning**: No need to define semantic preference lists
✅ **Generalizable**: Works on any WordNet concepts

## Limitations

❌ **72.2% success rate**: 27.8% fallback to rules
❌ **Poor compression**: 2.25x vs V7's 4.50x
❌ **Conservative**: LLM tends to select broader concepts
❌ **No context**: Doesn't see scene, other objects, relationships
❌ **Slow**: ~500ms per object vs V7's 0.16ms (3000x slower)
❌ **No reasoning**: LLM doesn't explain choices
❌ **LLM infrastructure**: Requires GPU, model loading

## Why V8 Falls Short

### 1. Conservative Selections
LLM errs on side of caution → selects broader concepts → poor compression

Example:
```
V7:  flower → organism (d=5) → object (d=2)
V8:  flower → plant (d=6) → physical entity (d=1)  ← Too broad at coarse
```

### 2. No Scene Context
LLM only sees object name and WordNet path, not:
- Other objects in scene
- Spatial positions
- Relationships

This leads to generic selections.

### 3. No Goal Guidance
Prompt says "most general" and "clear categorical" but doesn't explain:
- Purpose of hierarchy (traceable abstraction)
- How concepts will be used
- Importance of meaningful grouping

## V8 → V8.1 Improvements

V8.1 addresses all limitations:

| Issue | V8 | V8.1 Fix |
|-------|-----|----------|
| Success rate | 72.2% | 100% (scene context helps) |
| Compression | 2.25x | 4.50x (goal-oriented prompt) |
| Context | None | Full scene graph |
| Reasoning | None | LLM explains decisions |
| Selection | Single-stage | Two-stage (mid first, then coarse) |

## When to Use V8

**Don't use V8 - use V8.1 instead** (same speed, better everything)

V8 kept only for historical comparison and understanding evolution of methods.

## Code Implementation

### Core Selection Function

```python
def select_granularity_concepts(self, object_name, synset):
    """LLM-based concept selection."""
    # 1. Get WordNet path
    wordnet_path = self.format_wordnet_path(synset)

    # 2. Create prompt
    prompt = self.create_selection_prompt(object_name, wordnet_path)

    # 3. LLM inference
    messages = [
        {"role": "system", "content": "You are a helpful assistant..."},
        {"role": "user", "content": prompt}
    ]

    text = self.tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False  # KEY FIX
    )

    inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
    outputs = self.model.generate(**inputs, max_new_tokens=80, ...)
    response = self.tokenizer.decode(...)

    # 4. Parse and validate
    selection = self.extract_json_from_response(response)
    if selection and self.validate_selection(selection, wordnet_path):
        return {**selection, 'fine': object_name, 'method': 'llm'}
    else:
        # Fallback to V7 rules
        return self.fallback_selection(wordnet_path)
```

## See Also

- [METHODS_COMPARISON.md](METHODS_COMPARISON.md) - Compare all methods
- [V7_ADAPTIVE_RULES.md](V7_ADAPTIVE_RULES.md) - Rule-based approach
- [V8_1_CONTEXT_AWARE_LLM.md](V8_1_CONTEXT_AWARE_LLM.md) - Improved LLM method
- [PROMPT_ENGINEERING.md](PROMPT_ENGINEERING.md) - Prompting strategies

---

**Generated**: 2025-10-03
**File**: `inspect/llm_granularity_selector.py`
**Note**: Superseded by V8.1
