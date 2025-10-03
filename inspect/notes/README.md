# HCNMN Hierarchical Scene Graph Documentation

**Last Updated**: 2025-10-03
**Location**: `/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/notes/`

## Overview

Comprehensive documentation for three methods (V7, V8, V8.1) that create multi-granularity hierarchical scene graphs from Visual Genome annotations using WordNet ontology.

## Quick Start

**New users**: Start with [METHODS_COMPARISON.md](METHODS_COMPARISON.md)

**Need to understand levels**: Read [GRANULARITY_DEFINITIONS.md](GRANULARITY_DEFINITIONS.md)

**Choosing a method**:
- Speed-critical → [V7_ADAPTIVE_RULES.md](V7_ADAPTIVE_RULES.md)
- Semantic quality → [V8_1_CONTEXT_AWARE_LLM.md](V8_1_CONTEXT_AWARE_LLM.md)

## Documents

### Core Documentation

#### [METHODS_COMPARISON.md](METHODS_COMPARISON.md) ⭐ START HERE
High-level comparison of V7, V8, and V8.1 methods
- Performance summary table
- When to use each method
- Quick decision guide
- **Read this first!**

#### [GRANULARITY_DEFINITIONS.md](GRANULARITY_DEFINITIONS.md)
Clear explanation of fine, mid, and coarse levels
- What each level represents
- Relationship to WordNet depths
- Connection to Visual Genome scene graphs
- Complete examples

### Method Details

#### [V7_ADAPTIVE_RULES.md](V7_ADAPTIVE_RULES.md)
V7 adaptive rule-based scoring method
- Algorithm explanation with code
- Scoring functions and semantic bonuses
- Performance: 100% success, ~0.16ms per object
- When to use: Speed-critical applications

#### [V8_BASIC_LLM.md](V8_BASIC_LLM.md)
V8 basic LLM prompting method
- Qwen3-0.6B with simple prompts
- Critical fix: `enable_thinking=False`
- Performance: 72% success, ~500ms per object
- **Note**: Superseded by V8.1

#### [V8_1_CONTEXT_AWARE_LLM.md](V8_1_CONTEXT_AWARE_LLM.md) ⭐ RECOMMENDED LLM
V8.1 context-aware two-stage LLM method
- Full scene graph context
- Two-stage selection with reasoning
- Performance: 100% success, 4.50x compression
- When to use: Quality-critical, explainability needed

### Supporting Documentation

#### [PROMPT_ENGINEERING.md](PROMPT_ENGINEERING.md)
LLM prompting strategies and best practices
- V8 vs V8.1 prompt comparison
- Why context increases success 72% → 100%
- Component breakdown
- Common failure modes and fixes

#### [SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md](SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md)
How hierarchy relates to Visual Genome scene graphs
- VG format explanation
- Object extraction and processing
- Relationship inheritance across levels
- Complete example walkthrough

#### [WORDNET_INTEGRATION.md](WORDNET_INTEGRATION.md)
How WordNet provides semantic ontology
- Synsets and hypernym paths explained
- Depth ranges and semantics
- How each method uses WordNet
- Example walkthrough

## Reading Paths

### For Researchers
1. [METHODS_COMPARISON.md](METHODS_COMPARISON.md) - Overview
2. [GRANULARITY_DEFINITIONS.md](GRANULARITY_DEFINITIONS.md) - Understand levels
3. [V8_1_CONTEXT_AWARE_LLM.md](V8_1_CONTEXT_AWARE_LLM.md) - Best LLM method
4. [PROMPT_ENGINEERING.md](PROMPT_ENGINEERING.md) - Prompting strategies

### For Engineers
1. [METHODS_COMPARISON.md](METHODS_COMPARISON.md) - Overview
2. [V7_ADAPTIVE_RULES.md](V7_ADAPTIVE_RULES.md) - Fast implementation
3. [SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md](SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md) - Integration details
4. [WORDNET_INTEGRATION.md](WORDNET_INTEGRATION.md) - WordNet usage

### For Understanding LLM Methods
1. [V8_BASIC_LLM.md](V8_BASIC_LLM.md) - Basic approach (72% success)
2. [PROMPT_ENGINEERING.md](PROMPT_ENGINEERING.md) - What improves prompts
3. [V8_1_CONTEXT_AWARE_LLM.md](V8_1_CONTEXT_AWARE_LLM.md) - Advanced approach (100% success)

### For Scene Graph Integration
1. [GRANULARITY_DEFINITIONS.md](GRANULARITY_DEFINITIONS.md) - Level definitions
2. [SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md](SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md) - VG integration
3. [WORDNET_INTEGRATION.md](WORDNET_INTEGRATION.md) - Semantic foundation

## Key Concepts

### Three Granularity Levels
- **Fine (L0)**: Original VG objects (e.g., "clock")
- **Mid (L1)**: Semantic categories from WordNet depth 4-6 (e.g., "instrumentality")
- **Coarse (L2)**: Abstract domains from WordNet depth 1-3 (e.g., "object")

### Three Methods
- **V7**: Rule-based scoring (100% success, ultra-fast)
- **V8**: Basic LLM prompting (72% success, moderate speed)
- **V8.1**: Context-aware LLM (100% success, moderate speed, with reasoning)

### Key Results (Image 498335)
```
Objects: 18 unique
Compression: 18 → 15 → 4 concepts (4.50x fine→coarse)

Performance:
- V7: 100% success, ~0.16ms/obj, no reasoning
- V8: 72% success, ~500ms/obj, no reasoning
- V8.1: 100% success, ~500ms/obj, with reasoning
```

## File Structure

```
/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/notes/
├── README.md                               (this file)
├── METHODS_COMPARISON.md                   (⭐ start here)
├── GRANULARITY_DEFINITIONS.md             (level definitions)
├── V7_ADAPTIVE_RULES.md                   (rule-based method)
├── V8_BASIC_LLM.md                        (basic LLM, superseded)
├── V8_1_CONTEXT_AWARE_LLM.md              (⭐ recommended LLM)
├── PROMPT_ENGINEERING.md                  (LLM prompting guide)
├── SCENE_GRAPH_HIERARCHY_RELATIONSHIP.md  (VG integration)
└── WORDNET_INTEGRATION.md                 (semantic foundation)
```

## Related Files

### Code Implementations
- `inspect/adaptive_granularity_selector.py` - V7 implementation
- `inspect/llm_granularity_selector.py` - V8 implementation
- `inspect/llm_granularity_selector_v8_1.py` - V8.1 implementation

### Pipelines
- `inspect/visualize_scene_graph_hierarchy_v7.py` - V7 full pipeline
- `inspect/visualize_scene_graph_hierarchy_v8.py` - V8 full pipeline
- `inspect/visualize_scene_graph_hierarchy_v8_1.py` - V8.1 full pipeline

### Test Scripts
- `inspect/test_llm_v8_1_prompting.py` - V8.1 prompt testing

### Output Examples
- `inspect/vg/v7/sample_498335/` - V7 results (23 files)
- `inspect/vg/v8/sample_498335/` - V8 results (23 files)
- `inspect/vg/v8_1/sample_498335/` - V8.1 results (24 files with reasoning)

## Quick Reference

### Decision Matrix

| Need | Use | Why |
|------|-----|-----|
| Speed | V7 | 3000x faster than LLM |
| Quality | V8.1 | 100% success, semantic reasoning |
| Explainability | V8.1 | Natural language reasoning |
| Batch processing | V7 | Ultra-fast for thousands of images |
| Context-aware | V8.1 | Full scene understanding |
| Simple integration | V7 | No LLM infrastructure needed |

### Performance Summary

```
                V7        V8       V8.1
Success:       100%       72%      100%
Compression:   4.50x     2.25x    4.50x
Speed:         0.16ms    500ms    500ms
Reasoning:     No        No       Yes
Context:       No        No       Yes
```

## Contact & Issues

See main repository for issues, questions, or contributions.

---

**Generated**: 2025-10-03
**Repository**: HCNMN - Hierarchical Cross-Modality Neural Module Network
**Documentation Status**: Complete (8 documents)
