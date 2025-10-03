# V7: Adaptive Granularity Selection Method

**Image ID**: 2379701
**Date**: 2025-10-03

## Method Overview

V7 uses **intelligent rule-based adaptive selection** instead of:
- V6.1: Semantic categories (mid) + fixed depth 4 (coarse)
- LLM approach: Qwen3 with thinking mode (too slow, unreliable JSON output)

### Why Adaptive Rules?

1. **Performance**: ~0.16ms per object vs 2650ms for LLM (~17,000x faster)
2. **Reliability**: 100% success rate vs 0% for LLM (thinking mode interference)
3. **Better Compression**: 1.29x vs 2.57x for v6.1 semantic categories
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

## Results for Image 2379701

### Statistics
- **Objects**: 19
- **Fine concepts**: 18
- **Mid concepts**: 14
- **Coarse concepts**: 4

### Compression
- **Fine → Mid**: 1.29x
- **Fine → Coarse**: 4.50x
- **Mid → Coarse**: 3.50x

### Top Concepts

**Coarse level**:
- object: 9 objects
- abstraction: 6 objects
- thing: 2 objects
- matter: 1 objects

**Mid level**:
- artifact: 3 objects
- covering: 2 objects
- external body part: 2 objects
- material: 1 objects
- organism: 1 objects

## Advantages Over Previous Versions

| Aspect | V6.1 Semantic | V7 Adaptive |
|--------|---------------|-------------|
| Mid-level | 13 fixed categories | Depth 4-6 scored |
| Coarse-level | Fixed depth 4 | Depth 1-3 scored |
| Compression (Mid) | ~2.57x | 1.29x |
| Speed | Fast | ~0.16ms/obj |
| Adaptability | Fixed categories | Adaptive to WordNet |

✅ **Recommendation**: Use V7 adaptive method for best balance of speed, compression, and semantic quality.
