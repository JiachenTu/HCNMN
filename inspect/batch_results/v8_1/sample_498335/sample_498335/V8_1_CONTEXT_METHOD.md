# V8.1: Context-Aware LLM-Guided Granularity Selection

**Image ID**: 498335
**Date**: 2025-10-03

## Method Overview

V8.1 uses **context-aware Qwen3 LLM** with full scene graph information:
- **LLM Model**: Qwen3-0.6B (Apache 2.0 license)
- **Context**: Full scene graph (objects, relationships, spatial bboxes)
- **Selection**: Two-stage (mid first, then coarse)
- **Goal**: Traceable abstraction levels (coarse → mid → fine)
- **Key Fix**: `enable_thinking=False` in tokenizer
- **Fallback**: V7 adaptive rules if LLM fails
- **Success Rate**: 15/18 (83.3%)

### Why Context-Aware?

1. **Scene Understanding**: LLM sees all objects and relationships
2. **Spatial Awareness**: Bbox positions inform semantic decisions
3. **Relational Context**: Relationships guide abstraction choices
4. **Goal-Oriented**: Emphasizes traceable hierarchy not just compression
5. **Two-Stage Selection**: Mid-level first, then coarse for consistency
6. **Reasoning**: LLM provides explanation for each decision

## Granularity Definitions

### Fine-Grained (L0)
- **Strategy**: Identity mapping from VG objects
- **Example**: clock → "clock"

### Mid-Level (L1) - Stage 1
- **Strategy**: LLM selects best from **depth 4-6** with scene context
- **Prompt**: "Which concept best represents this object as a mid-level category in this scene?"
- **Context Provided**:
  - All objects in scene with bboxes
  - Current object's position and size
  - Relationships involving this object
- **LLM considers**: Functional/semantic category, scene role
- **Fallback**: V7 adaptive scoring if LLM fails

### Coarse-Grained (L2) - Stage 2
- **Strategy**: LLM selects best from **depth 1-3** based on mid selection
- **Prompt**: "Which concept provides appropriate high-level abstraction?"
- **Context Provided**: Same as mid-level plus mid selection
- **LLM considers**: General domain, meaningful grouping
- **Fallback**: V7 adaptive scoring if LLM fails

## Results for Image 498335

### Statistics
- **Objects**: 30
- **Fine concepts**: 18
- **Mid concepts**: 15
- **Coarse concepts**: 4

### Compression
- **Fine → Mid**: 1.20x
- **Fine → Coarse**: 4.50x
- **Mid → Coarse**: 3.75x

### Top Concepts

**Coarse level**:
- physical entity: 10 objects
- object: 4 objects
- abstraction: 3 objects
- communication: 1 objects

**Mid level**:
- artifact: 2 objects
- structure: 2 objects
- instrumentality: 2 objects
- sign: 1 objects
- road: 1 objects

## Advantages Over Previous Versions

| Aspect | V6.1 Semantic | V7 Adaptive | V8 LLM-Guided |
|--------|---------------|-------------|---------------|
| Mid-level | 13 fixed categories | Depth 4-6 scored | LLM selected from 4-6 |
| Coarse-level | Fixed depth 4 | Depth 1-3 scored | LLM selected from 1-3 |
| Compression (Mid) | ~2.57x | ~1.64x | 1.20x |
| Speed | Fast | Ultra-fast (~0.16ms) | Moderate (~500ms) |
| Intelligence | Rule-based | Heuristic | **LLM-guided** ✨ |
| Success Rate | 100% | 100% | 83% |

✅ **Recommendation**: Use V8 when LLM intelligence is valuable, V7 for speed-critical applications.
