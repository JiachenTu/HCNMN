# Multi-Granularity Hierarchical Ontology Visualization Pipeline

## Overview

This pipeline generates multi-granularity hierarchical concept graphs (HCG) from Visual Genome annotations using WordNet-based ontology formulation. It creates comprehensive visualizations showing how objects in images can be organized at different levels of abstraction (fine/mid/coarse).

## Pipeline Architecture

### 1. Data Input
- **Source**: Visual Genome dataset annotations
- **Location**: `/home/jiachen/scratch/graph_reasoning/HCNMN/data/vg/`
- **Components**:
  - Images: `images/VG_100K/` and `images/VG_100K_2/`
  - Scene graphs: `scene_graphs.json`
  - Image metadata: `image_data.json`

### 2. Pipeline Stages

#### Stage 1: Scene Graph Extraction
- Load Visual Genome annotations for selected image
- Extract objects with bounding boxes and names
- Extract relationships between objects
- Overlay scene graph on original image with colored bounding boxes and relationship arrows

#### Stage 2: Concept Hierarchy Construction
- For each object, use WordNet to build 3-level hierarchy:
  - **Fine-grained (L0)**: Original object names from annotations
  - **Mid-level (L1)**: Immediate hypernyms (parent concepts)
  - **Coarse-grained (L2)**: Second-level hypernyms (grandparent concepts)
- Remove duplicates and synonyms to avoid redundancy
- Build concept paths showing traversal from fine to coarse

**Key Design Decision**: Limited to 3 levels to avoid massive concept expansion
- ❌ Original approach: 11 objects → 467 concepts (14 levels deep)
- ✅ Clean approach: 23 objects → 42 concepts (3 levels)
- Result: 93% reduction in concept bloat while maintaining multi-granularity reasoning

#### Stage 3: Granularity-Specific Visualization
Generate 5 visualization types per sample:

1. **granularity_fine.png**: Green overlay showing objects grouped by fine-grained concepts
2. **granularity_mid.png**: Blue overlay showing objects grouped by mid-level categories
3. **granularity_coarse.png**: Red overlay showing objects grouped by coarse abstractions
4. **multi_granularity_comparison.png**: Side-by-side comparison of all 3 levels
5. **hierarchical_graph_overlay.png**: Combined view with scene graph network and hierarchical tree

#### Stage 4: Documentation Generation
- Generate `VISUALIZATION_REPORT.md` with comprehensive documentation
- Export `ontology_data.json` with complete hierarchy data
- Include statistics, concept paths, and usage examples

## Key Scripts

### `visualize_merged_granularity.py` ⭐ **NEW: Merged Scene Graph Visualization**
**Purpose**: Generate merged scene graphs where objects with the same concept at each granularity level are combined into single nodes with merged bounding boxes

**Key Features**:
- **Bounding Box Merging**: Multiple objects → single merged node with combined bbox
- **Compression Statistics**: Track how many objects merge at each level
- **VG_100K Only**: Samples exclusively from VG_100K (not VG_100K_2)

**Key Functions**:
```python
load_vg_data(vg_dir, image_id)                    # Load VG scene graph annotations
build_clean_hierarchy(objects)                    # Construct 3-level hierarchy
merge_bounding_boxes(bboxes)                      # Merge multiple bboxes into one
create_merged_scene_graph(objects, levels, gran)  # Merge objects by concept
visualize_merged_granularity(...)                 # Visualize merged graph
```

**Usage**:
```bash
conda run -n hcnmn python visualize_merged_granularity.py \
    --vg_dir /home/jiachen/scratch/graph_reasoning/HCNMN/data/vg \
    --output_dir vg \
    --image_id <IMAGE_ID>
```

**Example**: 45 objects → 24 fine / 22 mid / 20 coarse merged nodes

**Outputs**:
- `merged_fine.png`: Merged fine-grained scene graph
- `merged_mid.png`: Merged mid-level scene graph
- `merged_coarse.png`: Merged coarse-grained scene graph
- `merged_comparison.png`: 3-panel side-by-side comparison
- `merged_scene_graph_data.json`: Complete merged graph data
- `MERGED_SCENE_GRAPH_REPORT.md`: Detailed documentation

---

### `visualize_granularity_overlay.py`
**Purpose**: Generate granularity overlays (original version without merging)

**Key Functions**:
```python
load_vg_data(vg_dir, image_id)          # Load VG annotations
build_clean_hierarchy(objects)          # Construct 3-level hierarchy
create_granularity_overlay(...)         # Generate granularity-specific overlays
create_multi_granularity_comparison(...)  # Generate comparison view
create_hierarchical_graph_overlay(...)  # Generate combined view
generate_visualization_report(...)      # Generate markdown documentation
```

**Usage**:
```bash
conda run -n hcnmn python visualize_granularity_overlay.py \
    --vg_dir /home/jiachen/scratch/graph_reasoning/HCNMN/data/vg \
    --output_dir /home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg \
    --image_id <IMAGE_ID>
```

---

### `visualize_scene_graph_hierarchy.py`
**Purpose**: Generate basic scene graph and hierarchical tree visualizations (predecessor to granularity overlay script)

**Outputs**:
- `original_scene_graph.png`: Scene with objects and relationships
- `hierarchical_ontology_tree.png`: 3-column tree structure
- `combined_visualization.png`: Side-by-side view

## Output Structure

Each sample generates a directory with the following structure:

```
sample_<IMAGE_ID>/
├── granularity_fine.png                 # Fine-grained overlay (green)
├── granularity_mid.png                  # Mid-level overlay (blue)
├── granularity_coarse.png               # Coarse-grained overlay (red)
├── multi_granularity_comparison.png     # 3-panel comparison
├── hierarchical_graph_overlay.png       # Scene + network + tree
├── ontology_data.json                   # Complete hierarchy data
├── VISUALIZATION_REPORT.md              # Comprehensive documentation
├── original_scene_graph.png             # Basic scene graph
├── hierarchical_ontology_tree.png       # Tree structure
└── combined_visualization.png           # Scene + tree
```

## Sample Statistics

| Image ID | Objects | Relationships | Fine | Mid | Coarse | Total Concepts | Expansion |
|----------|---------|---------------|------|-----|--------|----------------|-----------|
| 2337701  | 11      | 9             | 10   | 9   | 9      | 28             | 2.5x      |
| 2368573  | 31      | 38            | 24   | 24  | 24     | 72             | 2.3x      |
| 2368901  | 25      | 26            | 19   | 18  | 16     | 53             | 2.1x      |
| 724      | 24      | 24            | 23   | 20  | 19     | 62             | 2.6x      |
| 118      | 15      | 16            | 12   | 12  | 10     | 34             | 2.3x      |
| 27       | 21      | 19            | 16   | 15  | 13     | 44             | 2.1x      |
| 858      | 24      | 29            | 13   | 12  | 11     | 36             | 1.5x      |
| 291      | 23      | 28            | 16   | 13  | 13     | 42             | 1.8x      |

**Average Expansion**: 2.2x (vs 42.5x with deep WordNet traversal)

## Multi-Granularity Reasoning Examples

### Example 1: Fine-Grained Query
**Question**: "Is there a seagull in the image?"

**Reasoning**:
1. Query at fine-grained level (L0)
2. Search for exact match: "seagull"
3. Check if present in image
4. **Answer**: Based on specific object detection

**Use Case**: Specific object identification tasks

### Example 2: Mid-Level Query
**Question**: "Is there a bird in the image?"

**Reasoning**:
1. Query at mid-level (L1)
2. Search for category: "bird", "vertebrate", "larid"
3. OR traverse from fine: "seagull" → parent category
4. **Answer**: Based on category membership

**Use Case**: Category-level recognition tasks

### Example 3: Coarse-Grained Query
**Question**: "Are there living things in the image?"

**Reasoning**:
1. Query at coarse level (L2)
2. Search for high-level groups: "chordate", "organism"
3. Traverse from mid: "vertebrate" → "chordate"
4. **Answer**: Based on abstract grouping

**Use Case**: Scene understanding and high-level reasoning

### Example 4: Cross-Granularity Query
**Question**: "What type of bird is it?"

**Reasoning**:
1. Start at mid-level: Identify "bird" category
2. Traverse DOWN to fine-grained level
3. Find specific instances: "seagull", "pigeon", etc.
4. **Answer**: Most specific concept available

**Use Case**: Fine-grained classification within categories

## Visualization Color Coding

| Granularity | Color | Hex Code | Represents |
|-------------|-------|----------|------------|
| Fine-grained | 🟢 Green | #2ecc71 | Specific objects |
| Mid-level | 🔵 Blue | #3498db | Categories |
| Coarse-grained | 🔴 Red | #e74c3c | High-level groups |

## Technical Details

### Ontology Construction Algorithm

```python
def build_clean_hierarchy(objects, max_depth=3):
    """
    Build 3-level hierarchy from Visual Genome objects using WordNet

    Args:
        objects: List of VG object annotations
        max_depth: Maximum hierarchy depth (default: 3)

    Returns:
        hierarchy: Dict with fine/mid/coarse concept lists
        concept_paths: Dict mapping objects to their hierarchy paths
    """
    hierarchy = {'fine': [], 'mid': [], 'coarse': []}
    concept_paths = {}

    for obj in objects:
        obj_name = obj['names'][0]
        obj_clean = obj_name.replace('_', ' ')

        # L0: Fine-grained (original object)
        hierarchy['fine'].append(obj_name)
        path = [obj_name]

        # L1: Mid-level (immediate hypernym)
        synsets = wn.synsets(obj_clean)
        if synsets:
            synset = synsets[0]
            if synset.hypernyms():
                parent = synset.hypernyms()[0]
                parent_name = parent.name().split('.')[0].replace('_', ' ')
                hierarchy['mid'].append(parent_name)
                path.append(parent_name)

                # L2: Coarse-grained (second-level hypernym)
                if parent.hypernyms():
                    grandparent = parent.hypernyms()[0]
                    grandparent_name = grandparent.name().split('.')[0].replace('_', ' ')
                    hierarchy['coarse'].append(grandparent_name)
                    path.append(grandparent_name)

        concept_paths[obj_name] = path

    # Remove duplicates
    hierarchy['fine'] = list(set(hierarchy['fine']))
    hierarchy['mid'] = list(set(hierarchy['mid']))
    hierarchy['coarse'] = list(set(hierarchy['coarse']))

    return hierarchy, concept_paths
```

### Advantages of 3-Level Structure

✅ **Balanced**: Even distribution of concepts across levels
✅ **Meaningful**: Each level has clear semantic purpose
✅ **Efficient**: Fast traversal (max 2 hops)
✅ **Interpretable**: Easy to understand and visualize
✅ **Practical**: Directly usable for model training
✅ **No bloat**: Avoids irrelevant abstract concepts

## Usage Guidelines

### For Visual Question Answering (VQA)

1. **Encode question** to determine required granularity
   - "What is this?" → Fine-grained
   - "What kind of...?" → Mid-level
   - "Is there any...?" → Coarse-grained

2. **Query appropriate level** of hierarchy

3. **Use spatial information** from bounding boxes for location queries

### For Scene Understanding

1. **Start at coarse level**: Get high-level scene composition
2. **Drill down** to mid-level for categories
3. **Refine** to fine-grained for specific objects

### For Object Detection

1. **Train at multiple levels**: Use all 3 granularities
2. **Coarse → Fine**: Hierarchical detection pipeline
3. **Benefit**: Better generalization across abstraction levels

## Comparison to Alternative Approaches

### vs. Flat Object List
❌ **Flat**: No abstraction, only specific objects
✅ **Hierarchical**: Multiple levels of reasoning

### vs. Deep WordNet Tree (14 levels)
❌ **Deep**: Too many abstract concepts (467 total for 11 objects)
✅ **3-Level**: Only meaningful concepts (28-72 total)

### vs. Single Granularity
❌ **Single**: Fixed abstraction level
✅ **Multi**: Flexible reasoning at any level

## Environment Setup

```bash
# Activate conda environment
conda activate hcnmn

# Required packages
- Python 3.x
- nltk (with wordnet corpus)
- matplotlib
- PIL (Pillow)
- numpy
- json
```

## Generating New Samples

```bash
# Navigate to inspect directory
cd /home/jiachen/scratch/graph_reasoning/HCNMN/inspect

# Run pipeline for specific image
conda run -n hcnmn python visualize_granularity_overlay.py \
    --vg_dir /home/jiachen/scratch/graph_reasoning/HCNMN/data/vg \
    --output_dir vg \
    --image_id <IMAGE_ID>

# Batch process multiple images
for img_id in 724 118 27 858 291; do
    conda run -n hcnmn python visualize_granularity_overlay.py \
        --vg_dir /home/jiachen/scratch/graph_reasoning/HCNMN/data/vg \
        --output_dir vg \
        --image_id $img_id
done
```

## Integration with HCNMN Model

The generated hierarchical ontologies can be integrated with the HCNMN model for multi-granularity reasoning:

1. **Topology Matrix**: Encode parent-child relationships between concepts
2. **Property Vectors**: Binary vectors indicating visual attributes
3. **Multi-level Queries**: Route questions to appropriate granularity level
4. **Hierarchical Attention**: Attend to relevant abstraction levels

See the main HCNMN repository for model training details.

## References

- **Paper**: "Toward Multi-Granularity Decision-Making: Explicit Visual Reasoning with Hierarchical Knowledge" (ICCV 2023)
- **Dataset**: Visual Genome (Krishna et al., 2017)
- **Knowledge Base**: WordNet 3.0
- **Repository**: `/home/jiachen/scratch/graph_reasoning/HCNMN`

## Known Issues

1. **Concept Count Display**: The VISUALIZATION_REPORT.md may show "0 unique concepts" due to template rendering issue, but actual counts are correct in ontology_data.json
2. **Missing Images**: Some VG images may not render properly if image files are missing or corrupted
3. **WordNet Coverage**: Some object names may not have WordNet synsets, resulting in incomplete hierarchies

## Future Improvements

- [ ] Add VLM-based concept validation
- [ ] Integrate ConceptNet for additional semantic relationships
- [ ] Support for custom granularity levels beyond 3
- [ ] Aggregate statistics across all Visual Genome images
- [ ] Interactive visualization with web interface
- [ ] Export to formats compatible with graph databases

---

**Generated**: 2025-09-30
**Location**: `/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/`
**Total Samples**: 8 (2337701, 2368573, 2368901, 724, 118, 27, 858, 291)