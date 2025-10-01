# V5 vs V6 Comparison: Multi-Granularity Hierarchy Experiments

**Date**: 2025-10-01

---

## Summary

Tested two different strategies for mid-level concept merging:
- **V5**: 1-hop up + depth-4 coarse
- **V6**: 2-3 hops up + depth-4 coarse

**Result**: V5 performs better than V6 ❌

---

## Compression Statistics

| Version | Strategy | F→M Compression | M→C Compression | F→C Compression |
|---------|----------|----------------|-----------------|-----------------|
| **V5** | 1-hop mid | **1.09x** | **2.11x** | **2.33x** ✅ |
| **V6** | 2-3 hop mid | 1.06x | 1.80x | 1.95x ❌ |
| **Change** | | -2.5% | -14.3% | **-16.3%** |

---

## Problem Analysis

### Why V5→V6 Failed

**Hypothesis**: 2-3 hops would give better mid-level merging
**Reality**: Made compression worse across the board!

**Root causes**:

1. **Inconsistent hop depth**: The "2-3 hop" logic picks whichever is available, not whichever is semantically better
   - Some objects got 2 hops: still too specific
   - Some objects got 3 hops: better but inconsistent
   - Result: No systematic improvement

2. **Still too fine-grained**: 2-3 hops is not deep enough for most WordNet paths
   - Example: hands → duty → act (2 hops, but "duty" is still very specific)
   - Example: track → location → line (2 hops, "location" not a good category)

3. **Coarse level becomes harder to reach**: When mid is higher in the tree, there's less distance to coarse
   - V5: 1-hop mid → lots of room to depth-4 coarse (2.11x M→C compression)
   - V6: 2-3 hop mid → less room to depth-4 coarse (1.80x M→C compression)

### What We Learned

**The fundamental issue**: Fine→Mid compression is inherently difficult because:

1. **WordNet immediate hypernyms are very specific**: motor_vehicle, woody_plant, armor_plate, etc. are all distinct categories
2. **Visual Genome objects are diverse**: Even within scenes, objects come from many different semantic domains
3. **True category-level merging requires deeper abstraction**: But this conflicts with maintaining 3 distinct levels

**Example from V6 (Image 2368545)**:
```
Fine → Mid (2-3 hops) → Coarse (depth 4)

hands → duty → act
track → location → line
people → abstraction → people
shadow → semidarkness → illumination
child → person → living thing  ✓ (good merging!)
lamps → device → artifact
```

Only "person" related objects merge well. Everything else stays unique at mid-level.

---

## Conclusion

**V5 is the better choice:**
- Maintains 2.33x Fine→Coarse compression
- Clear 3-level hierarchy (even if F→M is minimal)
- Coarse level has excellent merging (2.11x M→C)

**Why mid-level compression is low (1.09x):**
- This is actually **expected behavior** given WordNet structure
- Visual Genome objects are semantically diverse
- 1-hop hypernyms are specific by design (motor_vehicle ≠ woody_plant)
- The value comes from coarse-level merging, not mid-level

**Recommendation**:
- **Keep V5 approach** (1-hop mid, depth-4 coarse)
- Accept that Fine→Mid will have minimal compression (~1.1x)
- Focus on coarse-level merging (2.1x) as the main value proposition
- The 3 levels serve different purposes:
  - Fine: Instance-level (original objects)
  - Mid: Type-level (immediate categories) - **distinction, not compression**
  - Coarse: Domain-level (high-level grouping) - **compression**

---

## Alternative Approaches (Future Work)

If better mid-level merging is needed:

1. **Semantic clustering**: Group objects by semantic field (vehicles, plants, people, buildings, etc.) rather than strict WordNet hierarchy

2. **Adaptive depth-from-root for mid**: Use depth 2-3 from root for mid (like we do for coarse at depth 4)
   - Risk: May make mid too similar to coarse

3. **Custom category mappings**: Manually define mid-level categories for common VG object types
   - Example: {car, truck, bus, bike} → "vehicle"
   - Example: {tree, bush, flower, grass} → "plant"

4. **Accept 2 levels instead of 3**: Fine + Coarse only
   - Fine: Original objects
   - Coarse: Depth-4 from root (2.3x compression)
   - Simpler and clearer!

---

## Version Details

### V5 (Recommended ✅)
```python
# Mid: 1 hop up
if synset.hypernyms():
    parent = synset.hypernyms()[0]

# Coarse: Depth 4 from root
for depth in [4, 3, 5, 6]:
    coarse_synset = get_hypernym_at_depth_from_root(synset, depth)
```

**Results**:
- 10/10 samples successful
- Average F→M: 1.09x
- Average M→C: 2.11x
- Average F→C: 2.33x

### V6 (Experiment - Failed ❌)
```python
# Mid: 2-3 hops up
for n_hops in [2, 3]:
    temp_synset = synset
    for _ in range(n_hops):
        if temp_synset.hypernyms():
            temp_synset = temp_synset.hypernyms()[0]
    if successful:
        mid_synset = temp_synset
        break

# Coarse: Depth 4 from root (same as V5)
```

**Results**:
- 10/10 samples successful
- Average F→M: 1.06x (worse!)
- Average M→C: 1.80x (worse!)
- Average F→C: 1.95x (worse!)

---

**Conclusion**: Use V5 for all future work. Accept that mid-level provides **distinction** rather than **compression**.
