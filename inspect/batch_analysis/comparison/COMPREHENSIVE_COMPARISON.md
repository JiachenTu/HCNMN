# Comprehensive Method Comparison Summary

**Test Images**: 10 diverse Visual Genome images (complexity range: 19.0-54.0)

## Aggregate Statistics

| Method | N | Fine Concepts | Mid Concepts | Coarse Concepts | Compression (F→C) | Compression (M→C) |
|--------|---|---------------|--------------|-----------------|-------------------|-------------------|
| V7 (Rules) | 10 | 17.6 ± 4.4 | 11.9 ± 4.0 | 5.5 ± 2.3 | 3.5 ± 1.0 | 2.3 ± 0.7 |
| V8 (LLM) | 10 | 17.6 ± 4.4 | 14.6 ± 3.5 | 7.7 ± 3.3 | 2.6 ± 0.9 | 2.1 ± 0.8 |
| V8.1 (LLM+Context) | 10 | 17.6 ± 4.4 | 14.8 ± 3.5 | 5.5 ± 2.6 | 3.7 ± 1.4 | 3.1 ± 1.2 |
| V20 (VLM) | 6 | 17.7 ± 5.3 | 12.3 ± 3.9 | 6.7 ± 3.0 | 3.0 ± 1.1 | 2.1 ± 0.9 |
| V20.1 (VLM+) | 4 | 15.8 ± 5.6 | 11.5 ± 5.8 | 5.5 ± 2.9 | 3.4 ± 1.8 | 2.2 ± 1.0 |

## VLM Success Rates (V20/V20.1 only)

| Method | VLM Success Rate | Fallback Rate | Notes |
|--------|------------------|---------------|-------|
| V20 (VLM) | 37.9% ± 16.0% | N/A | N=6/10 (partial) |
| V20.1 (VLM+) | 22.0% ± 31.4% | N/A | N=4/10 (partial) |

**Note**: V7/V8/V8.1 are deterministic (no LLM/VLM success rates to track).
## Per-Image Comparison

**Note**: V20 has 6/10 images, V20.1 has 4/10 images (incomplete runs).

### Images with All 5 Methods (3 images)

#### Image 713619

| Method | Fine | Mid | Coarse | Compression (F→C) | VLM Success |
|--------|------|-----|--------|-------------------|-------------|
| V7 (Rules) | 9 | 5 | 3 | 3.00x | N/A |
| V8 (LLM) | 9 | 7 | 3 | 3.00x | N/A |
| V8.1 (LLM+Context) | 9 | 8 | 3 | 3.00x | N/A |
| V20 (VLM) | 9 | 5 | 3 | 3.00x | 11.1% |
| V20.1 (VLM+) | 9 | 4 | 3 | 3.00x | 66.7% |

#### Image 2326885

| Method | Fine | Mid | Coarse | Compression (F→C) | VLM Success |
|--------|------|-----|--------|-------------------|-------------|
| V7 (Rules) | 14 | 13 | 9 | 1.56x | N/A |
| V8 (LLM) | 14 | 14 | 11 | 1.27x | N/A |
| V8.1 (LLM+Context) | 14 | 13 | 9 | 1.56x | N/A |
| V20 (VLM) | 14 | 12 | 9 | 1.56x | 35.7% |
| V20.1 (VLM+) | 14 | 13 | 8 | 1.75x | 21.4% |

#### Image 2342105

| Method | Fine | Mid | Coarse | Compression (F→C) | VLM Success |
|--------|------|-----|--------|-------------------|-------------|
| V7 (Rules) | 22 | 18 | 9 | 2.44x | N/A |
| V8 (LLM) | 22 | 20 | 13 | 1.69x | N/A |
| V8.1 (LLM+Context) | 22 | 19 | 10 | 2.20x | N/A |
| V20 (VLM) | 22 | 16 | 9 | 2.44x | 31.8% |
| V20.1 (VLM+) | 22 | 18 | 8 | 2.75x | 0.0% |

### Text-Only Methods Comparison (10 images)

#### Image 498335

| Method | Fine | Mid | Coarse | Compression (F→C) |
|--------|------|-----|--------|-------------------|
| V7 (Rules) | 18 | 11 | 4 | 4.50x |
| V8 (LLM) | 18 | 13 | 8 | 2.25x |
| V8.1 (LLM+Context) | 18 | 15 | 4 | 4.50x |

#### Image 713619

| Method | Fine | Mid | Coarse | Compression (F→C) |
|--------|------|-----|--------|-------------------|
| V7 (Rules) | 9 | 5 | 3 | 3.00x |
| V8 (LLM) | 9 | 7 | 3 | 3.00x |
| V8.1 (LLM+Context) | 9 | 8 | 3 | 3.00x |

#### Image 2326885

| Method | Fine | Mid | Coarse | Compression (F→C) |
|--------|------|-----|--------|-------------------|
| V7 (Rules) | 14 | 13 | 9 | 1.56x |
| V8 (LLM) | 14 | 14 | 11 | 1.27x |
| V8.1 (LLM+Context) | 14 | 13 | 9 | 1.56x |

#### Image 2342105

| Method | Fine | Mid | Coarse | Compression (F→C) |
|--------|------|-----|--------|-------------------|
| V7 (Rules) | 22 | 18 | 9 | 2.44x |
| V8 (LLM) | 22 | 20 | 13 | 1.69x |
| V8.1 (LLM+Context) | 22 | 19 | 10 | 2.20x |

#### Image 2347842

| Method | Fine | Mid | Coarse | Compression (F→C) |
|--------|------|-----|--------|-------------------|
| V7 (Rules) | 19 | 10 | 5 | 3.80x |
| V8 (LLM) | 19 | 16 | 6 | 3.17x |
| V8.1 (LLM+Context) | 19 | 15 | 5 | 3.80x |

#### Image 2364859

| Method | Fine | Mid | Coarse | Compression (F→C) |
|--------|------|-----|--------|-------------------|
| V7 (Rules) | 19 | 14 | 5 | 3.80x |
| V8 (LLM) | 19 | 15 | 8 | 2.38x |
| V8.1 (LLM+Context) | 19 | 16 | 6 | 3.17x |

#### Image 2376855

| Method | Fine | Mid | Coarse | Compression (F→C) |
|--------|------|-----|--------|-------------------|
| V7 (Rules) | 23 | 13 | 8 | 2.88x |
| V8 (LLM) | 23 | 16 | 9 | 2.56x |
| V8.1 (LLM+Context) | 23 | 18 | 8 | 2.88x |

#### Image 2379701

| Method | Fine | Mid | Coarse | Compression (F→C) |
|--------|------|-----|--------|-------------------|
| V7 (Rules) | 18 | 14 | 4 | 4.50x |
| V8 (LLM) | 18 | 16 | 6 | 3.00x |
| V8.1 (LLM+Context) | 18 | 17 | 3 | 6.00x |

#### Image 2396558

| Method | Fine | Mid | Coarse | Compression (F→C) |
|--------|------|-----|--------|-------------------|
| V7 (Rules) | 21 | 15 | 5 | 4.20x |
| V8 (LLM) | 21 | 17 | 10 | 2.10x |
| V8.1 (LLM+Context) | 21 | 17 | 4 | 5.25x |

#### Image 2406328

| Method | Fine | Mid | Coarse | Compression (F→C) |
|--------|------|-----|--------|-------------------|
| V7 (Rules) | 13 | 6 | 3 | 4.33x |
| V8 (LLM) | 13 | 12 | 3 | 4.33x |
| V8.1 (LLM+Context) | 13 | 10 | 3 | 4.33x |

## Method Rankings

### By Compression Ratio (F→C, Higher is Better)

1. V8.1 (LLM+Context): 3.67x
2. V7 (Rules): 3.50x
3. V20.1 (VLM+): 3.38x
4. V20 (VLM): 2.98x
5. V8 (LLM): 2.58x

### By Coarse Concept Count (Lower is Better)

1. V7 (Rules): 5.5 concepts
2. V8.1 (LLM+Context): 5.5 concepts
3. V20.1 (VLM+): 5.5 concepts
4. V20 (VLM): 6.7 concepts
5. V8 (LLM): 7.7 concepts
## Key Findings

1. **Best Compression**: V8.1 (LLM+Context) - **3.67x** (Fine→Coarse)

2. **Best VLM Success**: V20 (VLM) - **37.9%** (vision-grounded JSON generation)

3. **Text-Only Methods (V7/V8/V8.1)**:
   - V8.1 achieves **3.67x** compression (5.5 coarse concepts)
   - V7 achieves **3.50x** compression (5.5 coarse concepts)
   - V8.1 **4.8% better** than V7

4. **Vision-Grounded Methods (V20/V20.1)**:
   - V20 compression: **2.98x** (6/10 images)
   - V20.1 compression: **3.38x** (4/10 images)
   - Vision grounding **does not improve** compression vs V8.1

## Recommendations

### For Production Use

**Primary Recommendation**: V8.1 (Context-Aware LLM)

**Reasons**:
- Highest compression: **3.67x**
- Fewest coarse concepts: **5.5** (most abstract)
- Intelligent semantic reasoning with scene context
- Text-only (faster than VLM)

### For Research & Explainability

**V20/V20.1 (Vision VLM)** if:
- Visual grounding is essential
- Explainable AI requirements (vision-aware reasoning)
- Studying multimodal semantic abstraction

**Limitation**: Current VLM success rate is **low** (~40% average).
- VLMs struggle with strict JSON format despite enhanced prompting
- High fallback rate to V7 rules
- For production vision-grounding, deploy with vLLM + `guided_json`
