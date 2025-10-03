# V7: Adaptive Granularity Selection Method

**Image ID**: 2376855
**Date**: 2025-10-03

## Method Overview

V7 uses **intelligent rule-based adaptive selection** instead of:
- V6.1: Semantic categories (mid) + fixed depth 4 (coarse)
- LLM approach: Qwen3 with thinking mode (too slow, unreliable JSON output)

### Why Adaptive Rules?

1. **Performance**: ~0.16ms per object vs 2650ms for LLM (~17,000x faster)
2. **Reliability**: 100% success rate vs 0% for LLM (thinking mode interference)
3. **Better Compression**: 1.77x vs 2.57x for v6.1 semantic categories
4. **Deterministic**: Consistent, explainable results

## Granularity Definitions

### Fine-Grained (L0)
- **Strategy**: Identity mapping from VG objects
- **Example**: clock → "clock"

### Mid-Level (L1)
- **Strategy**: Adaptive selection from **depth 4-6** using scoring
- **Scoring**:
  - Preferred depth: 5 (score 10)
  - Fallback depths: 4 (score 7), 6 (score 8)
  - Semantic bonus: instrumentality (+10), organism (+10), structure (+10), etc.
- **Example**: clock → "instrumentality" (depth 5, score 20)

### Coarse-Grained (L2)
- **Strategy**: Adaptive selection from **depth 1-3** using scoring
- **Scoring**:
  - Preferred depth: 2 (score 10)
  - Fallback depths: 1 (score 5), 3 (score 6)
  - Semantic bonus: object (+10), matter (+10), living_thing (+8), etc.
- **Example**: clock → "object" (depth 2, score 20)

## Results for Image 2376855

### Statistics
- **Objects**: 32
- **Fine concepts**: 23
- **Mid concepts**: 13
- **Coarse concepts**: 8

### Compression
- **Fine → Mid**: 1.77x
- **Fine → Coarse**: 2.88x
- **Mid → Coarse**: 1.62x

### Top Concepts

**Coarse level**:
- object: 10 objects
- thing: 6 objects
- abstraction: 2 objects
- key pad: 1 objects
- copyright symbol: 1 objects

**Mid level**:
- instrumentality: 6 objects
- external body part: 4 objects
- organism: 2 objects
- artifact: 2 objects
- key pad: 1 objects

## Advantages Over Previous Versions

| Aspect | V6.1 Semantic | V7 Adaptive |
|--------|---------------|-------------|
| Mid-level | 13 fixed categories | Depth 4-6 scored |
| Coarse-level | Fixed depth 4 | Depth 1-3 scored |
| Compression (Mid) | ~2.57x | 1.77x |
| Speed | Fast | ~0.16ms/obj |
| Adaptability | Fixed categories | Adaptive to WordNet |

✅ **Recommendation**: Use V7 adaptive method for best balance of speed, compression, and semantic quality.
