# Visual Genome Batch Sampling Report

**Generated**: 2025-10-01 08:24:22

**Processing Time**: 839.33 seconds (13.99 minutes)

---

## Summary Statistics

- **Total Samples**: 10
- **Successful**: 10 (100.0%)
- **Failed**: 0 (0.0%)

### Object Statistics
- **Min Objects**: 14
- **Max Objects**: 30
- **Mean Objects**: 22.5

### Relationship Statistics
- **Min Relationships**: 3
- **Max Relationships**: 37
- **Mean Relationships**: 14.6

---

## Successful Samples

| Image ID | Objects | Relationships | Output Directory |
|----------|---------|---------------|------------------|
| 713869 | 14 | 3 | `sample_713869/` |
| 2316149 | 28 | 15 | `sample_2316149/` |
| 2330893 | 26 | 8 | `sample_2330893/` |
| 2331126 | 19 | 5 | `sample_2331126/` |
| 2337091 | 30 | 17 | `sample_2337091/` |
| 2342588 | 22 | 37 | `sample_2342588/` |
| 2347219 | 30 | 5 | `sample_2347219/` |
| 2349289 | 14 | 5 | `sample_2349289/` |
| 2365400 | 19 | 29 | `sample_2365400/` |
| 2372873 | 23 | 22 | `sample_2372873/` |

---

## Output Structure

Each sample directory contains:

```
sample_{image_id}/
├── merged_fine.png              # Merged fine-grained scene graph
├── merged_mid.png               # Merged mid-level scene graph
├── merged_coarse.png            # Merged coarse-grained scene graph
├── merged_comparison.png        # 3-panel comparison
├── merged_scene_graph_data.json # Merged graph data
├── MERGED_SCENE_GRAPH_REPORT.md # Detailed report
├── original_scene_graph.png     # Original VG scene graph
├── hierarchical_ontology_tree.png # Hierarchy tree
├── combined_visualization.png   # Combined view
└── ontology_data.json           # Ontology structure
```

---

**Pipeline**: HCNMN Hierarchical Concept Graph Generation
**Scripts Used**:
- `visualize_merged_granularity.py`
- `visualize_scene_graph_hierarchy.py`
