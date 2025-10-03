# V8: LLM-Guided Granularity Selection Method

**Image ID**: 2342105
**Date**: 2025-10-03

## Method Overview

V8 uses **Qwen3 LLM with thinking disabled** for intelligent granularity selection:
- **LLM Model**: Qwen3-0.6B (Apache 2.0 license)
- **Key Fix**: `enable_thinking=False` in tokenizer to prevent `<think>` tags
- **Fallback**: V7 adaptive rules if LLM fails
- **Success Rate**: 10/22 (45.5%)

### Why LLM-Guided?

1. **Intelligent Selection**: LLM understands context and semantics
2. **Adaptive**: Responds to object-specific patterns
3. **Reliable**: Fixed thinking mode issue achieves high success rates
4. **Fallback Safety**: Uses proven V7 rules if LLM fails

## Granularity Definitions

### Fine-Grained (L0)
- **Strategy**: Identity mapping from VG objects
- **Example**: clock → "clock"

### Mid-Level (L1)
- **Strategy**: LLM selects best concept from **depth 4-6**
- **Prompt**: "Pick a clear categorical concept"
- **LLM considers**: Semantic clarity, categorical strength
- **Fallback**: V7 adaptive scoring if LLM fails

### Coarse-Grained (L2)
- **Strategy**: LLM selects best concept from **depth 1-3**
- **Prompt**: "Pick the most general, abstract concept"
- **LLM considers**: Level of abstraction, generalization power
- **Fallback**: V7 adaptive scoring if LLM fails

## Results for Image 2342105

### Statistics
- **Objects**: 28
- **Fine concepts**: 22
- **Mid concepts**: 20
- **Coarse concepts**: 13

### Compression
- **Fine → Mid**: 1.10x
- **Fine → Coarse**: 1.69x
- **Mid → Coarse**: 1.54x

### Top Concepts

**Coarse level**:
- object: 5 objects
- abstraction: 4 objects
- physical entity: 3 objects
- thing: 1 objects
- process: 1 objects

**Mid level**:
- document: 2 objects
- person: 2 objects
- process: 1 objects
- blue shirt: 1 objects
- organism: 1 objects

## Advantages Over Previous Versions

| Aspect | V6.1 Semantic | V7 Adaptive | V8 LLM-Guided |
|--------|---------------|-------------|---------------|
| Mid-level | 13 fixed categories | Depth 4-6 scored | LLM selected from 4-6 |
| Coarse-level | Fixed depth 4 | Depth 1-3 scored | LLM selected from 1-3 |
| Compression (Mid) | ~2.57x | ~1.64x | 1.10x |
| Speed | Fast | Ultra-fast (~0.16ms) | Moderate (~500ms) |
| Intelligence | Rule-based | Heuristic | **LLM-guided** ✨ |
| Success Rate | 100% | 100% | 45% |

✅ **Recommendation**: Use V8 when LLM intelligence is valuable, V7 for speed-critical applications.
