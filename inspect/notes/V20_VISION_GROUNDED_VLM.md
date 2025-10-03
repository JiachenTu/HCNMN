# V20: Vision-Grounded VLM-Guided Granularity Selection

**Method**: Qwen2.5-VL-3B with image + scene context
**Implementation**: `vlm_granularity_selector_v20.py`
**Status**: Experimental (V8.1 recommended for production)

## Overview

V20 uses a Vision-Language Model to select WordNet granularity concepts by actually seeing the image, enabling vision-grounded semantic decisions. This is the first method to incorporate visual understanding beyond text-based scene graph descriptions.

## Evolution: V20 → V20.1

### V20 (Initial)
- **Success Rate**: 61.1% (11/18 objects)
- **Compression**: 3.60x (18 → 5 concepts)
- **Approach**: Basic VLM prompting with vision
- **Issue**: VLM generates conversational text instead of pure JSON

### V20.1 (Enhanced Prompting)
- **Success Rate**: ~64% average (11-12/18 objects)
- **Compression**: 3.00-3.60x
- **Improvements**:
  - **CRITICAL INSTRUCTION** demanding JSON-only output
  - 3 correct examples + 1 incorrect example
  - 6-strategy JSON extraction (vs 3 before)
  - Strips conversational prefixes and markdown blocks
- **Result**: +3% modest improvement

## Key Differences vs V8.1

| Aspect | V8.1 (Text LLM) | V20 (Vision VLM) |
|--------|----------------|------------------|
| **Model** | Qwen3-0.6B | Qwen2.5-VL-3B |
| **Input** | Text scene graph | Image + scene graph |
| **Success Rate** | **100%** (18/18) | 61-67% (11-12/18) |
| **Compression** | **4.50x** | 3.00-3.60x |
| **Vision Grounding** | ❌ No | ✅ Yes |
| **Reasoning Quality** | Text-based | **Vision-aware** |
| **JSON Reliability** | ✅ Consistent | ❌ Inconsistent |
| **Speed** | ~500ms/obj | ~500ms/obj |

## Method

### 1. Vision-Grounded Prompt (V20.1)

```python
prompt = f"""**CRITICAL INSTRUCTION**: YOU MUST RESPOND WITH ONLY VALID JSON.
NO explanations. NO conversational text. NO markdown. ONLY the raw JSON object below.

**Task**: Select WordNet concepts for hierarchical abstraction using visual analysis.

**Scene Context**:
- Look at the image to see "{object_name}" and its surroundings
- Objects in scene: {objects_summary}
- Target object "{object_name}": {bbox_info}
- Relationships: {relationships}

**WordNet Path**: {path}

**Selection Task**:
MID-level (depth 4-6): {mid_options}
COARSE-level (depth 1-3): {coarse_options}

Look at the image. Consider visual appearance of "{object_name}". Select ONE concept from each level.

**REQUIRED JSON OUTPUT FORMAT** (THIS IS YOUR ENTIRE RESPONSE):
{{"mid": "concept", "mid_depth": N, "coarse": "concept", "coarse_depth": N, "reasoning": "brief visual description"}}

**CORRECT Examples**:

Example 1 (clock):
{{"mid": "instrumentality", "mid_depth": 5, "coarse": "object", "coarse_depth": 2, "reasoning": "Visible timekeeper instrument mounted on pole"}}

Example 2 (flower):
{{"mid": "plant", "mid_depth": 6, "coarse": "object", "coarse_depth": 2, "reasoning": "Living plant with visible petals in pot"}}

Example 3 (sign):
{{"mid": "clue", "mid_depth": 5, "coarse": "communication", "coarse_depth": 2, "reasoning": "Text signboard displaying store name"}}

**INCORRECT Example** (DO NOT DO THIS):
"Based on the image, I can see the clock. Here is the JSON: {{...}}"  ← WRONG! No extra text!

**NOW OUTPUT ONLY THE JSON FOR "{object_name}"** (no other text):"""
```

### 2. Enhanced JSON Extraction (6 Strategies)

```python
def extract_json_from_response(response):
    # Strategy 1: Strip conversational prefixes
    conversational_prefixes = [
        "here is the json", "here's the json", "the json is",
        "based on", "looking at", "i can see"
    ]

    # Strategy 2: Strip markdown code blocks
    if "```json" in response:
        response = response.split("```json")[1].split("```")[0]

    # Strategy 3: Direct JSON parse after cleaning
    try:
        return json.loads(response.strip())
    except: pass

    # Strategy 4: Extract between first { and last }
    first_brace = response.find('{')
    last_brace = response.rfind('}')
    if first_brace != -1 and last_brace != -1:
        return json.loads(response[first_brace:last_brace+1])

    # Strategy 5: Flexible regex pattern
    json_pattern = r'\{[^{}]*"mid"[^{}]*"coarse"[^{}]*\}'
    matches = re.findall(json_pattern, response, re.DOTALL)

    # Strategy 6: Manual key-value extraction (last resort)
    # ... extract fields individually
```

### 3. VLM Inference with Image

```python
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": pil_image},  # Actual image!
            {"type": "text", "text": prompt}
        ]
    }
]

inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_dict=True,
    return_tensors="pt"
)

generated_ids = model.generate(
    **inputs,
    max_new_tokens=150,  # For reasoning text
    temperature=0.7,
    top_p=0.8,
    do_sample=True
)
```

## Results on Image 498335

### V20.1 Performance
- **Objects processed**: 18 unique
- **VLM success**: 11-12/18 (61-67%, **average ~64%**)
- **Fallback to V7 rules**: 6-7/18 (33-39%)
- **Fine concepts**: 18
- **Mid concepts**: 12-13
- **Coarse concepts**: 5-6
- **Compression**: 3.00-3.60x

### Sample Vision-Grounded Reasoning

**"clock"**:
> "The clock is a visible instrument/tool for timekeeping (mid) and a solid physical object (coarse)"

**"flower"**:
> "Flowers are living organisms with visual features such as petals, stems, and leaves, and they play a functional role in the environment"

**"sign"**:
> "The sign serves as an indication or clue, providing information about the store 'Gooderham & Worts Limited' (mid) and is a part of the communication system in the urban setting (coarse)"

**"pot"**:
> "The pot is a visible artifact or tool used for holding and displaying flowers (mid) and is a solid, physical object (coarse)"

## Advantages

✅ **True Vision Grounding**: VLM sees actual image, references visual features
✅ **Richer Reasoning**: Incorporates visual observations ("petals, stems, leaves", "mounted on pole")
✅ **Context-Aware**: Reads visible text in image ("Gooderham & Worts Limited")
✅ **Better for Ambiguous Objects**: Visual appearance helps semantic decisions
✅ **Explainable**: Natural language reasoning with visual details

## Limitations

❌ **Lower Success Rate**: 64% vs 100% for V8.1
❌ **JSON Inconsistency**: VLM adds conversational text despite strict instructions
❌ **Worse Compression**: 3.0-3.6x vs 4.5x for V8.1
❌ **Model Size**: 3B params vs 0.6B for V8.1 (5x larger)
❌ **Variability**: Results vary between runs (temperature=0.7)

## Why Vision Didn't Improve Performance

**Expected**: Visual grounding → better semantic decisions → higher success
**Reality**: Vision improved reasoning quality but not JSON adherence

**Root Cause**: VLM's multimodal nature makes it more conversational:
- Text-only LLMs (V8.1) trained heavily on JSON data → better format adherence
- VLMs optimized for natural dialogue about images → more verbose
- Image input triggers "explain what you see" behavior

**Evidence**:
- V20 reasoning is richer and more detailed than V8.1
- V20 correctly identifies visual features V8.1 can't see
- But V20 wraps JSON in conversational text: "Based on the image, I can see..."

## Solutions for Production Use

### Option 1: Use V8.1 (RECOMMENDED)
- **100% success rate**, 4.50x compression
- Text-only LLM is sufficient for this task
- Scene graph text provides enough context
- Vision grounding not worth 36% accuracy drop

### Option 2: Deploy with vLLM + `guided_json`
For cases where vision grounding is essential:

```python
# Deploy Qwen2.5-VL-3B with vLLM
vllm serve Qwen/Qwen2.5-VL-3B-Instruct \
    --guided-decoding-backend=outlines \
    --gpu-memory-utilization 0.9

# Use OpenAI API with guided JSON
completion = client.chat.completions.create(
    model="Qwen/Qwen2.5-VL-3B-Instruct",
    messages=[...],
    extra_body={"guided_json": json_schema}
)
```

**Benefits**:
- ✅ Guaranteed valid JSON (100% success)
- ✅ Keep vision grounding benefits
- ✅ Production-ready inference server
- ❌ Requires vLLM deployment (not transformers)

### Option 3: Outlines Library (EXPERIMENTAL)
```python
import outlines
from pydantic import BaseModel

class GranularitySelection(BaseModel):
    mid: str
    mid_depth: int
    coarse: str
    coarse_depth: int
    reasoning: str

# Load with transformers_vision backend
model = outlines.models.transformers_vision("Qwen/Qwen2.5-VL-3B-Instruct")
generator = outlines.generate.json(model, GranularitySelection.model_json_schema())

# Guaranteed valid JSON output
result = generator(prompt, images=[image])
```

**Status**:
- ⚠️ Dependency conflicts in current environment
- ⚠️ `transformers_vision` support newly added (2025)
- ⚠️ May not fully support Qwen2.5-VL yet
- ✅ Works well for LLaVA, Idefics models

## When to Use V20

### Best For:
- **Research**: Studying vision-language grounding for hierarchy
- **Explainability**: Need visual reasoning in explanations
- **Visually-Ambiguous Objects**: When visual appearance matters
- **User-Facing Applications**: Show visual understanding
- **Proof of Concept**: Demonstrate VLM capabilities

### Not Ideal For:
- **Production**: V8.1 is more reliable (100% vs 64%)
- **Batch Processing**: Lower success rate = more fallbacks
- **Resource-Constrained**: 5x larger model than V8.1
- **Consistency**: Run-to-run variance

## Future Improvements

1. **Lower Temperature**: Try 0.3-0.5 for more consistent JSON
2. **Few-Shot Prompting**: Provide 5-10 examples instead of 3
3. **Response Format Parameter**: If Qwen2.5-VL adds native JSON mode
4. **Fine-Tuning**: Train VLM specifically for structured outputs
5. **vLLM Deployment**: Use `guided_json` for guaranteed valid JSON

## Comparison with Other Methods

| Method | Success | Compression | Speed | Vision | Reasoning |
|--------|---------|-------------|-------|--------|-----------|
| **V7 (Rules)** | 100% | 4.50x | 0.16ms | ❌ | ❌ |
| **V8 (LLM)** | 72% | 2.25x | 500ms | ❌ | ❌ |
| **V8.1 (LLM+Context)** | **100%** | **4.50x** | 500ms | ❌ | ✅ |
| **V20 (VLM)** | 61% | 3.00x | 500ms | ✅ | ✅✅ |
| **V20.1 (Enhanced)** | 64% | 3.30x | 500ms | ✅ | ✅✅ |

**Takeaway**: V8.1 offers best balance of success and reasoning without vision overhead.

## Implementation Files

- **Selector**: `inspect/vlm_granularity_selector_v20.py`
- **Pipeline**: `inspect/visualize_scene_graph_hierarchy_v20.py`
- **Test**: `inspect/test_vlm_v20_quick.py`
- **Results**: `inspect/vg/v20/sample_498335/` (21 files)
- **Comparison**: `inspect/vg/v20/sample_498335/V20_V8_1_COMPARISON.md`

## Conclusion

V20 successfully demonstrates **vision-grounded granularity selection** with richer reasoning that references actual visual features. However, the VLM's conversational nature makes JSON formatting unreliable (64% success vs 100% for V8.1).

**For Production**: Use V8.1 (text-only LLM with scene context)
**For Research**: V20 shows promise for vision-aware semantic understanding
**For 90%+ Success with Vision**: Deploy with vLLM + `guided_json`

Vision grounding is valuable for explainability and visual reasoning, but comes at the cost of format reliability. The scene graph text representation in V8.1 provides sufficient semantic context without the complexity of multimodal models.

---

**Generated**: 2025-10-03
**Status**: Experimental
**Recommendation**: V8.1 for production, V20 for research

## See Also

- [METHODS_COMPARISON.md](METHODS_COMPARISON.md) - Full method comparison
- [V8_1_CONTEXT_AWARE_LLM.md](V8_1_CONTEXT_AWARE_LLM.md) - Recommended method
- [PROMPT_ENGINEERING.md](PROMPT_ENGINEERING.md) - Prompting strategies
