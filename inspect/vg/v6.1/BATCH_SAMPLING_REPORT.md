# Visual Genome Batch Sampling Report

**Generated**: 2025-10-01 10:05:34

**Processing Time**: 840.43 seconds (14.01 minutes)

---

## Summary Statistics

- **Total Samples**: 10
- **Successful**: 10 (100.0%)
- **Failed**: 0 (0.0%)

### Object Statistics
- **Min Objects**: 11
- **Max Objects**: 30
- **Mean Objects**: 21.4

### Relationship Statistics
- **Min Relationships**: 4
- **Max Relationships**: 32
- **Mean Relationships**: 17.9

---

## Successful Samples

| Image ID | Objects | Relationships | Output Directory |
|----------|---------|---------------|------------------|
| 498335 | 30 | 15 | `sample_498335/` |
| 2323145 | 16 | 5 | `sample_2323145/` |
| 2333264 | 12 | 4 | `sample_2333264/` |
| 2339206 | 11 | 15 | `sample_2339206/` |
| 2341540 | 20 | 31 | `sample_2341540/` |
| 2349422 | 27 | 11 | `sample_2349422/` |
| 2357195 | 26 | 19 | `sample_2357195/` |
| 2363870 | 24 | 19 | `sample_2363870/` |
| 2368545 | 30 | 32 | `sample_2368545/` |
| 2368954 | 18 | 28 | `sample_2368954/` |

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
