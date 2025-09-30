# Merged Multi-Granularity Scene Graph Approach

## Overview

This document explains the **merged scene graph** approach where objects with the same concept at each granularity level are combined into single nodes with merged bounding boxes.

## Motivation

### Problem with Original Approach
In the original visualization, objects that map to the same concept were displayed separately:

```
Fine-Grained Level:
- helmet (object 1) → bbox [x=440, y=393, w=50, h=45]
- helmet (object 2) → bbox [x=520, y=405, w=40, h=42]
- helmet (object 3) → bbox [x=585, y=398, w=36, h=42]

Result: 3 separate bounding boxes with identical label "helmet"
```

### Solution: Merged Scene Graph
Objects with the same concept are merged into a single node:

```
Fine-Grained Level (Merged):
- helmet → merged_bbox [x=440, y=393, w=166, h=99]
  - object_count: 3
  - original_objects: [helmet, helmet, helmet]

Result: 1 combined bounding box representing all 3 helmets
```

## Technical Implementation

### 1. Bounding Box Merging Algorithm

```python
def merge_bounding_boxes(bboxes):
    """
    Merge multiple bounding boxes into minimum enclosing rectangle.

    Input: [{x: 440, y: 393, w: 50, h: 45},
            {x: 520, y: 405, w: 40, h: 42},
            {x: 585, y: 398, w: 36, h: 42}]

    Output: {x: 440, y: 393, w: 181, h: 54}
    """
    x_min = min(bbox['x'] for bbox in bboxes)
    y_min = min(bbox['y'] for bbox in bboxes)
    x_max = max(bbox['x'] + bbox['w'] for bbox in bboxes)
    y_max = max(bbox['y'] + bbox['h'] for bbox in bboxes)

    return {
        'x': x_min,
        'y': y_min,
        'w': x_max - x_min,
        'h': y_max - y_min
    }
```

### 2. Concept Grouping at Each Granularity

```python
def create_merged_scene_graph(objects, object_to_levels, granularity):
    """
    Group objects by concept at specified granularity and merge bboxes.
    """
    concept_groups = {}

    for obj in objects:
        obj_name = obj['names'][0]

        # Map object to concept at this granularity
        concept = object_to_levels[obj_name].get(granularity, obj_name)

        # Group objects by concept
        if concept not in concept_groups:
            concept_groups[concept] = {'bboxes': [], 'original_objects': []}

        concept_groups[concept]['bboxes'].append(obj['bbox'])
        concept_groups[concept]['original_objects'].append(obj_name)

    # Merge bboxes for each concept
    merged_nodes = {}
    for concept, group in concept_groups.items():
        merged_nodes[concept] = {
            'concept': concept,
            'bbox': merge_bounding_boxes(group['bboxes']),
            'object_count': len(group['bboxes']),
            'original_objects': group['original_objects']
        }

    return merged_nodes
```

## Example: Image 107899

### Original Scene: 45 Objects

```
Objects in scene:
- helmet (3 instances)
- glasses (2 instances)
- arm (2 instances)
- foot (2 instances)
- building (1 instance)
- field (1 instance)
... and 34 more
```

### Merged Scene Graphs

#### Fine-Grained (24 merged nodes)

**Compression**: 45 objects → 24 nodes (1.88x)

Example merges:
- `helmet` (3 objects) → 1 node, bbox [x=440, y=393, w=166, h=99]
- `glasses` (2 objects) → 1 node, bbox [x=463, y=438, w=75, h=36]
- `arm` (2 objects) → 1 node, bbox [x=271, y=329, w=238, h=238]
- `foot` (2 objects) → 1 node, bbox [x=428, y=906, w=188, h=62]

#### Mid-Grained (22 merged nodes)

**Compression**: 45 objects → 22 nodes (2.05x)

Example merges:
- `protective covering` (3 helmets) → 1 node
- `optical instrument` (2 glasses + 1 eyeglasses) → 1 node
- `limb` (2 arms + 2 feet) → 1 node
- `edifice` (1 building + 1 home) → 1 node

#### Coarse-Grained (20 merged nodes)

**Compression**: 45 objects → 20 nodes (2.25x)

Example merges:
- `covering` (3 helmets + clothing items) → 1 node
- `device` (glasses + other tools) → 1 node
- `body part` (arms + feet + head) → 1 node
- `structure` (buildings + fence) → 1 node

## Compression Statistics

| Image ID | Objects | Fine (Merged) | Mid (Merged) | Coarse (Merged) |
|----------|---------|---------------|--------------|-----------------|
| 107899   | 45      | 24 (1.88x)    | 22 (2.05x)   | 20 (2.25x)      |
| 107920   | 6       | 2 (3.00x)     | 2 (3.00x)    | 2 (3.00x)       |
| 107945   | 29      | 16 (1.81x)    | 14 (2.07x)   | 14 (2.07x)      |
| 107980   | 4       | 4 (1.00x)     | 4 (1.00x)    | 4 (1.00x)       |

**Observations**:
- Higher compression at coarser granularities (as expected)
- More compression when many duplicate objects exist (e.g., 107920: 3.00x)
- Minimal compression when objects are all unique (e.g., 107980: 1.00x)

## Visualization Features

### 1. Merged Bounding Boxes

Each merged node is visualized with:
- **Single bounding box**: Minimum enclosing rectangle of all merged objects
- **Concept label**: Shows the concept name (not individual object names)
- **Object count**: Shows how many objects were merged, e.g., "helmet (3)"
- **Unique color**: Each concept gets a distinct color from tab20 colormap

### 2. Three-Panel Comparison

Side-by-side visualization showing:
- **Left**: Merged fine-grained (green theme, 24 nodes)
- **Center**: Merged mid-grained (blue theme, 22 nodes)
- **Right**: Merged coarse-grained (red theme, 20 nodes)

### 3. Compression Statistics Overlay

Each panel shows:
- Number of merged nodes
- Compression ratio vs original objects

## Use Cases

### 1. Scene Understanding
**Question**: "How many distinct concepts are in this scene at different abstraction levels?"

**Answer**:
- Fine: 24 specific object types
- Mid: 22 category types
- Coarse: 20 high-level concept types

### 2. Spatial Reasoning
**Question**: "Where are all the protective gear items located?"

**Answer**: Query the merged "protective covering" node at mid-level to get combined spatial extent of all helmets, pads, etc.

### 3. Object Counting
**Question**: "How many helmet instances are in the scene?"

**Answer**: Check `object_count` field of "helmet" merged node: 3 instances

### 4. Hierarchical Grouping
**Question**: "Show me all body parts as a single spatial region"

**Answer**: Visualize merged "body part" node at coarse-level with combined bbox covering arms, feet, head, etc.

## Advantages Over Original Approach

✅ **Cleaner Visualizations**: No overlapping labels for duplicate concepts
✅ **Compression Metrics**: Quantify semantic grouping at each level
✅ **Spatial Extent**: Combined bbox shows total area occupied by concept instances
✅ **Scalable**: Works well even with 100+ objects by reducing visual clutter
✅ **Semantic Grouping**: Explicitly shows which objects map to same concept

## Limitations

⚠️ **Loss of Instance Information**: Individual object locations are merged
⚠️ **Large Bboxes**: Merged boxes can be very large when objects are spatially dispersed
⚠️ **Occlusion**: Merged bbox may include empty space between objects

## Future Enhancements

- [ ] **Convex Hull**: Use convex hull instead of minimum bounding rectangle
- [ ] **Instance Preservation**: Show individual objects as dots within merged bbox
- [ ] **Spatial Clustering**: Create multiple merged nodes if objects are spatially separated
- [ ] **Hierarchical Visualization**: Show parent-child relationships between granularities
- [ ] **Interactive Mode**: Click merged node to see individual object instances

## Related Files

- **Script**: `visualize_merged_granularity.py`
- **Documentation**: `MERGED_SCENE_GRAPH_REPORT.md` (per-sample)
- **Data**: `merged_scene_graph_data.json` (per-sample)
- **Visualizations**: `merged_fine.png`, `merged_mid.png`, `merged_coarse.png`, `merged_comparison.png`

---

**Generated**: 2025-09-30
**Location**: `/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg/`
**Samples Generated**: 107899, 107920, 107945, 107980