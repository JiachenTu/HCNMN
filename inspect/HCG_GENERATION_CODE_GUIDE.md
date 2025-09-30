# HCG Generation Code Guide for Visual Genome

## Overview

This guide explains the **key code** for generating Hierarchical Concept Graphs (HCG) from Visual Genome dataset samples. The main script is `test_vg_hcg_generation.py` which demonstrates the complete HCG generation pipeline.

---

## Core Pipeline: 5 Steps

```python
# Main Pipeline (test_vg_hcg_generation.py:533-609)
def main():
    # Step 1: Extract concepts from VG objects
    concepts, hierarchies, objects = extract_concepts_from_objects(
        vg_sample, vocab_data, hierarchy_data)

    # Step 2: Build spatial topology matrix
    topology_matrix = build_spatial_topology(objects, concepts)

    # Step 3: Generate object properties
    property_vectors, properties = generate_object_properties(objects, concepts, property_data)

    # Step 4: Create visualizations
    create_vg_visualization(vg_sample, objects, concepts, topology_matrix,
                           property_vectors, properties, sample_output_dir)

    # Step 5: Save HCG data
    save_vg_hcg_data(vg_sample, objects, concepts, topology_matrix,
                     property_vectors, properties, sample_output_dir)
```

---

## Step 1: Concept Extraction

**Function**: `extract_concepts_from_objects()` (lines 100-159)

**Purpose**: Extract and expand concepts from VG object names using hierarchical knowledge

### Algorithm

```python
def extract_concepts_from_objects(vg_sample, vocab_data, hierarchy_data):
    """
    Extract hierarchical concepts from VG object annotations.

    Args:
        vg_sample: VG annotation with objects list
        vocab_data: Vocabulary from VQA (question_token_to_idx)
        hierarchy_data: WordNet hierarchies from vocab_augmentation

    Returns:
        concepts: List of expanded concept names
        hierarchies: Hierarchy depth for each concept
        objects: Original VG objects
    """
    objects = vg_sample.get('objects', [])

    # 1. Extract object names
    all_object_names = []
    for obj in objects:
        names = obj.get('names', [])
        all_object_names.extend(names)

    # 2. Remove duplicates
    unique_names = list(set(all_object_names))

    # 3. Expand concepts using hierarchy
    concepts = []
    for name in unique_names:
        name_clean = name.lower().replace(' ', '_')

        if name_clean in hierarchy_data:
            # Use WordNet hierarchy expansion
            expanded = hierarchy_data[name_clean][:5]  # Top 5 hypernyms
            concepts.extend(expanded)
        elif name_clean in vocab_data['question_token_to_idx']:
            # Use vocabulary
            concepts.append(name_clean)
        else:
            # Keep original
            concepts.append(name)

    # 4. Remove duplicates from expanded concepts
    unique_concepts = list(set(concepts))

    return unique_concepts, concept_hierarchies, objects
```

### Key Insights

**Input Example**:
```python
VG objects: ["tree", "car", "person", "building"]
```

**Hierarchy Expansion** (from `hierarchy_data`):
```python
"tree" → ["tree", "woody_plant", "vascular_plant", "plant", "organism"]
"car" → ["car", "motor_vehicle", "vehicle", "conveyance", "artifact"]
```

**Output**:
```python
concepts = [
    "tree", "woody_plant", "vascular_plant", "plant", "organism",
    "car", "motor_vehicle", "vehicle", "conveyance", "artifact",
    "person", "adult", "human", "living_thing",
    "building", "structure", "artifact"
]
# ~5x expansion from 4 objects to ~20 concepts
```

---

## Step 2: Spatial Topology Construction

**Function**: `build_spatial_topology()` (lines 182-224)

**Purpose**: Build concept-to-concept connectivity based on spatial relationships

### Algorithm

```python
def build_spatial_topology(objects, concepts):
    """
    Build topology matrix based on spatial relationships.

    Two types of connections:
    1. Bounding box overlap (IoU > threshold)
    2. Spatial proximity (distance < threshold)

    Returns:
        topology_matrix: (n_concepts, n_concepts) adjacency matrix
    """
    n_concepts = len(concepts)
    topology_matrix = np.zeros((n_concepts, n_concepts))

    # Create object-to-concept mapping
    object_concept_map = {}
    for i, obj in enumerate(objects[:n_concepts]):
        object_concept_map[i] = i

    overlap_threshold = 0.1  # 10% IoU
    proximity_threshold = 200  # pixels

    for i in range(n_objects):
        for j in range(i + 1, n_objects):

            # 1. Calculate bounding box overlap (IoU)
            overlap = calculate_spatial_overlap(objects[i], objects[j])
            if overlap > overlap_threshold:
                ci, cj = object_concept_map[i], object_concept_map[j]
                topology_matrix[ci, cj] = overlap
                topology_matrix[cj, ci] = overlap  # Symmetric

            # 2. Calculate spatial proximity
            dist = np.sqrt((objects[i]['x'] - objects[j]['x'])**2 +
                          (objects[i]['y'] - objects[j]['y'])**2)
            if dist < proximity_threshold:
                ci, cj = object_concept_map[i], object_concept_map[j]
                proximity_weight = max(0.1, 1.0 - dist/200)
                topology_matrix[ci, cj] = max(topology_matrix[ci, cj],
                                             proximity_weight * 0.5)
                topology_matrix[cj, ci] = topology_matrix[ci, cj]

    return topology_matrix
```

### Spatial Overlap Calculation

```python
def calculate_spatial_overlap(box1, box2):
    """Calculate IoU (Intersection over Union) between two boxes."""
    x1, y1, w1, h1 = box1['x'], box1['y'], box1['w'], box1['h']
    x2, y2, w2, h2 = box2['x'], box2['y'], box2['w'], box2['h']

    # Intersection rectangle
    x_left = max(x1, x2)
    y_top = max(y1, y2)
    x_right = min(x1 + w1, x2 + w2)
    y_bottom = min(y1 + h1, y2 + h2)

    if x_right < x_left or y_bottom < y_top:
        return 0.0  # No intersection

    intersection = (x_right - x_left) * (y_bottom - y_top)
    area1 = w1 * h1
    area2 = w2 * h2
    union = area1 + area2 - intersection

    return intersection / union  # IoU
```

### Example Output

```python
# Input: 4 objects with bboxes
objects = [
    {'x': 100, 'y': 100, 'w': 50, 'h': 50},  # object 0
    {'x': 120, 'y': 120, 'w': 50, 'h': 50},  # object 1 (overlaps with 0)
    {'x': 500, 'y': 100, 'w': 50, 'h': 50},  # object 2 (far from 0,1)
    {'x': 510, 'y': 110, 'w': 50, 'h': 50},  # object 3 (near 2)
]

# Output topology matrix (4x4)
topology_matrix = [
    [0.00, 0.25, 0.00, 0.00],  # obj 0: overlaps with 1 (IoU=0.25)
    [0.25, 0.00, 0.00, 0.00],  # obj 1: overlaps with 0
    [0.00, 0.00, 0.00, 0.35],  # obj 2: proximity to 3
    [0.00, 0.00, 0.35, 0.00],  # obj 3: proximity to 2
]
```

**Topology Connections**:
- Edge weight = IoU if overlap > 0.1
- Edge weight = proximity_score if distance < 200px
- Matrix is symmetric: `topology[i,j] = topology[j,i]`

---

## Step 3: Property Generation

**Function**: `generate_object_properties()` (lines 226-295)

**Purpose**: Assign visual properties to concepts based on object characteristics

### Algorithm

```python
def generate_object_properties(objects, concepts, property_data):
    """
    Generate property vectors based on object names and characteristics.

    Property categories:
    - Colors: red, blue, green, yellow, black, white, brown, gray
    - Sizes: large, small, medium, tiny, huge
    - Shapes: round, square, rectangular, circular
    - Materials: metal, wood, glass, plastic, fabric, stone
    - Context: indoor, outdoor, natural, artificial

    Returns:
        property_vectors: (n_concepts, n_properties) binary matrix
        properties: list of property names
    """
    # Define property vocabulary
    properties = [
        'red', 'blue', 'green', 'yellow', 'black', 'white', 'brown', 'gray',
        'large', 'small', 'medium', 'tiny', 'huge',
        'round', 'square', 'rectangular', 'circular', 'linear',
        'metal', 'wood', 'glass', 'plastic', 'fabric', 'stone',
        'indoor', 'outdoor', 'natural', 'artificial', 'movable', 'fixed'
    ]

    n_concepts = len(concepts)
    n_properties = len(properties)
    property_vectors = np.zeros((n_concepts, n_properties))

    for i, concept in enumerate(concepts):
        concept_lower = concept.lower()

        # 1. Color properties (keyword matching)
        color_map = {
            'red': 0, 'blue': 1, 'green': 2, 'yellow': 3,
            'black': 4, 'white': 5, 'brown': 6, 'gray': 7
        }
        for color, idx in color_map.items():
            if color in concept_lower:
                property_vectors[i, idx] = 1.0

        # 2. Size properties
        if any(word in concept_lower for word in ['big', 'large', 'huge']):
            property_vectors[i, 8] = 1.0  # large
        if any(word in concept_lower for word in ['small', 'tiny', 'little']):
            property_vectors[i, 9] = 1.0  # small

        # 3. Shape properties
        if any(word in concept_lower for word in ['round', 'circle', 'ball']):
            property_vectors[i, 13] = 1.0  # round
        if any(word in concept_lower for word in ['square', 'box']):
            property_vectors[i, 14] = 1.0  # square

        # 4. Material properties (heuristic)
        material_keywords = {
            'metal': ['metal', 'steel', 'iron', 'car', 'bike'],
            'wood': ['wood', 'tree', 'wooden'],
            'glass': ['glass', 'window'],
            'fabric': ['shirt', 'pants', 'jacket', 'clothing']
        }
        for prop_idx, (material, keywords) in enumerate(material_keywords.items()):
            prop_pos = 19 + prop_idx
            if any(kw in concept_lower for kw in keywords):
                property_vectors[i, prop_pos] = 1.0

    return property_vectors, properties
```

### Example Output

```python
# Input concepts
concepts = ["red car", "tree", "person", "building"]

# Output property vectors (4 concepts × 30 properties)
property_vectors = [
    [1, 0, 0, 0, ..., 1, 0, ...],  # red car: red=1, metal=1
    [0, 0, 1, 0, ..., 0, 1, ...],  # tree: green=1, wood=1
    [0, 0, 0, 0, ..., 0, 0, ...],  # person: (no specific properties)
    [0, 0, 0, 0, ..., 0, 0, ...],  # building: (no specific properties)
]

properties = [
    'red', 'blue', 'green', 'yellow', 'black', 'white', 'brown', 'gray',
    'large', 'small', 'medium', 'tiny', 'huge',
    'round', 'square', 'rectangular', 'circular', 'linear',
    'metal', 'wood', 'glass', 'plastic', 'fabric', 'stone',
    'indoor', 'outdoor', 'natural', 'artificial', 'movable', 'fixed'
]
```

**Property Assignment Strategy**:
- **Keyword matching**: Simple string contains check
- **Heuristics**: Domain knowledge (e.g., "car" → "metal")
- **Binary vectors**: 1 if property applies, 0 otherwise

---

## Complete HCG Data Structure

After all 3 steps, we have the full HCG:

```python
HCG = {
    'concepts': ['tree', 'woody_plant', ..., 'car', 'vehicle', ...],
    'topology_matrix': np.array([[0.0, 0.3, ...], [0.3, 0.0, ...], ...]),
    'property_vectors': np.array([[0, 0, 1, ...], [1, 0, 0, ...], ...]),
    'properties': ['red', 'blue', 'green', ...],
    'objects': [{'x': 100, 'y': 100, 'w': 50, 'h': 50, 'names': ['tree']}, ...],
    'statistics': {
        'num_objects': 20,
        'num_concepts': 50,
        'spatial_connections': 35,
        'property_assignments': 60,
        'topology_density': 0.028
    }
}
```

This structure is **model-compatible** and can be used directly by HCNMN for training/inference.

---

## Model Integration

### How HCNMN Uses the Generated HCG

The generated HCG feeds into the HCNMN model's hierarchical modules:

```python
# From model/hierarchical_module.py

class FindModule(nn.Module):
    def forward(self, vision_feat, feat, feat_edge, c_i, relation_mask,
                att_stack, stack_ptr, mem_in, HCG):
        # HCG structure expected:
        # HCG['concept_vis']: (batch, CONCEPT_NUM, CV_DIM)
        # HCG['concept_lin']: (batch, CONCEPT_NUM, CL_DIM)
        # HCG['mono_mask']: (batch, CONCEPT_NUM, CONCEPT_NUM)  ← topology_matrix
        # HCG['cross_mask']: (batch, CONCEPT_NUM, CONCEPT_NUM)
        # HCG['concept_property']: (batch, CONCEPT_NUM, PROP_NUM) ← property_vectors

        # Our generated data maps to:
        # topology_matrix → HCG['mono_mask'] (same-level connections)
        # property_vectors → HCG['concept_property'] (concept properties)
```

### Data Conversion for Model

```python
# Convert our HCG to model format
def convert_to_model_format(hcg_data, batch_size=1):
    """Convert generated HCG to HCNMN model input format."""

    n_concepts = len(hcg_data['concepts'])

    # Topology → mono_mask
    mono_mask = torch.tensor(hcg_data['topology_matrix']).unsqueeze(0)
    mono_mask = mono_mask.expand(batch_size, n_concepts, n_concepts)

    # Property vectors → concept_property
    concept_property = torch.tensor(hcg_data['property_vectors']).unsqueeze(0)
    concept_property = concept_property.expand(batch_size, n_concepts, -1)

    # Create visual embeddings (from object features)
    concept_vis = create_concept_visual_embeddings(hcg_data['objects'])

    # Create linguistic embeddings (from GloVe)
    concept_lin = create_concept_linguistic_embeddings(hcg_data['concepts'])

    HCG = {
        'concept_vis': concept_vis,
        'concept_lin': concept_lin,
        'mono_mask': mono_mask,
        'cross_mask': create_cross_mask(mono_mask),  # Cross-granularity
        'concept_property': concept_property
    }

    return HCG
```

---

## Usage Example

### Generate HCG for a Single VG Image

```bash
cd /home/jiachen/scratch/graph_reasoning/HCNMN/inspect

# Run HCG generation
conda run -n hcnmn python test_vg_hcg_generation.py \
    --vg_dir ../data/vg \
    --data_dir ../data \
    --output_dir vg \
    --sample_id 498202
```

### Required Input Files

```python
# 1. VG Annotations
vg_objects_file = "data/vg/annotations/v1.4/objects.json"
# Format: [{'image_id': 498202, 'objects': [{'names': ['tree'], 'x': 100, ...}]}]

# 2. Vocabulary (from VQA preprocessing)
vocab_file = "data/features/vocab_augmented.json"
# Format: {'question_token_to_idx': {...}, 'terms': [...]}

# 3. Hierarchy (from vocab_augmentation.py)
hierarchy_file = "data/features/hierarchy.json"
# Format: {'tree': ['tree', 'woody_plant', 'vascular_plant', ...]}

# 4. Properties (optional)
property_file = "data/features/property.json"
# Format: {'properties': ['red', 'blue', ...], 'property_embeddings': [...]}
```

### Output Files

```bash
vg/sample_498202/
├── hcg_data.json                    # Complete HCG structure
├── hcg_visualization.png            # 4-panel visualization
├── topology_sample.json             # Model-compatible topology
├── concept_property_sample.json     # Model-compatible properties
├── relation_sample.json             # Relation types
└── property_sample.json             # Property vocabulary
```

---

## Key Code Snippets Reference

### 1. Load VG Sample
```python
# test_vg_hcg_generation.py:22-69
def load_vg_objects(objects_file, sample_image_id=None):
    with open(objects_file, 'r') as f:
        data = json.load(f)

    # Find sample with good object count (15-30 objects)
    for item in data:
        object_count = len(item.get('objects', []))
        if 15 <= object_count <= 30:
            return item

    return data[0]  # Fallback
```

### 2. Expand Concepts
```python
# test_vg_hcg_generation.py:127-142
for name in unique_names:
    name_clean = name.lower().replace(' ', '_')

    if name_clean in hierarchy_data:
        expanded = hierarchy_data[name_clean][:5]
        concepts.extend(expanded)
```

### 3. Build Topology
```python
# test_vg_hcg_generation.py:200-218
for i in range(n_objects):
    for j in range(i + 1, n_objects):
        overlap = calculate_spatial_overlap(objects[i], objects[j])
        if overlap > 0.1:
            topology_matrix[ci, cj] = overlap
            topology_matrix[cj, ci] = overlap

        dist = compute_distance(objects[i], objects[j])
        if dist < 200:
            proximity_weight = 1.0 - dist/200
            topology_matrix[ci, cj] = max(topology_matrix[ci, cj],
                                         proximity_weight * 0.5)
```

### 4. Assign Properties
```python
# test_vg_hcg_generation.py:248-289
for i, concept in enumerate(concepts):
    # Color matching
    for color, idx in color_map.items():
        if color in concept.lower():
            property_vectors[i, idx] = 1.0

    # Size matching
    if 'large' in concept or 'big' in concept:
        property_vectors[i, size_idx] = 1.0
```

---

## Summary

### Key Functions

| Function | Lines | Purpose |
|----------|-------|---------|
| `extract_concepts_from_objects()` | 100-159 | Extract & expand concepts from VG objects |
| `build_spatial_topology()` | 182-224 | Build concept connectivity from spatial relationships |
| `generate_object_properties()` | 226-295 | Assign visual properties to concepts |
| `create_vg_visualization()` | 307-448 | Generate 4-panel HCG visualization |
| `save_vg_hcg_data()` | 450-531 | Save HCG in model-compatible format |
| `main()` | 533-609 | Orchestrate complete pipeline |

### HCG Components Generated

1. **Concepts**: Expanded from VG objects using WordNet hierarchies
2. **Topology**: Spatial connectivity based on overlap + proximity
3. **Properties**: Visual attributes assigned via keyword matching
4. **Statistics**: Coverage, density, connections metrics

### Model Compatibility

The generated HCG matches the HCNMN model's expected format:
- `topology_matrix` → `HCG['mono_mask']`
- `property_vectors` → `HCG['concept_property']`
- Can be directly used for training/inference

---

**Script Location**: `/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/test_vg_hcg_generation.py`

**Documentation**: See also `MULTI_GRANULARITY_EXPLANATION.md` for multi-level hierarchy details
