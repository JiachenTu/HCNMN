# Batch Sampling Code Explanation

## Overview

The `batch_sample_vg.py` script automates the process of sampling diverse Visual Genome images and generating multi-granularity HCG visualizations for each. This document explains how the code works step-by-step.

---

## Architecture

```
batch_sample_vg.py (396 lines)
│
├── Data Loading & Filtering
│   ├── load_vg_scene_graphs()         # Load all 108K VG images
│   └── filter_good_samples()          # Filter by quality criteria
│
├── Sampling Strategy
│   └── stratified_sample()            # Balanced sampling across object counts
│
├── Processing Pipeline
│   ├── run_visualization()            # Execute visualization script
│   └── process_sample()               # Process single image (2 pipelines)
│
├── Reporting
│   └── generate_summary_report()      # Create markdown + JSON report
│
└── main()                             # Orchestrate everything
```

---

## Step-by-Step Breakdown

### **Step 1: Load VG Scene Graphs**

**Function**: `load_vg_scene_graphs()` (lines 16-25)

```python
def load_vg_scene_graphs(vg_dir):
    """Load all VG scene graphs."""
    scene_graphs_path = os.path.join(vg_dir, 'annotations', 'v1.2', 'scene_graphs.json')
    print(f"Loading scene graphs from: {scene_graphs_path}")

    with open(scene_graphs_path, 'r') as f:
        scene_graphs = json.load(f)

    print(f"✓ Loaded {len(scene_graphs)} scene graphs")
    return scene_graphs
```

**What it does**:
- Loads the massive VG scene_graphs.json file (~108K images)
- Each entry contains: `image_id`, `objects[]`, `relationships[]`
- Returns list of all scene graph annotations

**Example data structure**:
```python
scene_graphs = [
    {
        'image_id': 498202,
        'objects': [
            {'object_id': 1, 'x': 100, 'y': 100, 'w': 50, 'h': 50, 'names': ['tree']},
            {'object_id': 2, 'x': 200, 'y': 150, 'w': 60, 'h': 80, 'names': ['car']},
            ...
        ],
        'relationships': [
            {'subject': {'object_id': 1}, 'predicate': 'near', 'object': {'object_id': 2}},
            ...
        ]
    },
    ...
]
```

---

### **Step 2: Filter Good Samples**

**Function**: `filter_good_samples()` (lines 27-81)

```python
def filter_good_samples(scene_graphs, vg_dir, min_objects=10, max_objects=30):
    """
    Filter scene graphs for good visualization candidates.

    Criteria:
    - Object count in reasonable range (10-30)
    - Has some relationships
    - Image file exists
    """
    good_samples = []
    object_count_bins = defaultdict(list)  # For stratified sampling

    for sg in scene_graphs:
        image_id = sg['image_id']
        objects = sg.get('objects', [])
        relationships = sg.get('relationships', [])

        num_objects = len(objects)
        num_relationships = len(relationships)

        # Criterion 1: Object count in range
        if not (min_objects <= num_objects <= max_objects):
            continue

        # Criterion 2: Has relationships
        if num_relationships == 0:
            continue

        # Criterion 3: Image file exists
        image_path = os.path.join(vg_dir, 'images', 'VG_100K', 'VG_100K', f'{image_id}.jpg')
        if not os.path.exists(image_path):
            continue

        # Bin by object count (for stratified sampling)
        bin_idx = (num_objects - min_objects) // 5  # 5-object bins
        object_count_bins[bin_idx].append({
            'image_id': image_id,
            'num_objects': num_objects,
            'num_relationships': num_relationships,
            'image_path': image_path
        })

        good_samples.append({...})  # Same info

    return good_samples, object_count_bins
```

**Quality Criteria**:

1. **Object Count Range** (default: 10-30)
   - Too few objects (< 10): Not interesting enough
   - Too many objects (> 30): Too cluttered, hard to visualize
   - Sweet spot: 10-30 objects for rich but manageable scenes

2. **Has Relationships**
   - Images with 0 relationships are boring
   - Relationships enable scene graph visualization

3. **Image File Exists**
   - Verifies the actual JPG file exists in VG_100K directory
   - Some annotations may not have corresponding images

**Binning Strategy**:
```python
bin_idx = (num_objects - min_objects) // 5
```

- Creates bins of 5-object ranges
- Example with min=10, max=30:
  - Bin 0: 10-14 objects
  - Bin 1: 15-19 objects
  - Bin 2: 20-24 objects
  - Bin 3: 25-30 objects

**Output Example**:
```python
good_samples = [...]  # ~30K-40K samples that pass filters

object_count_bins = {
    0: [{image_id: 123, num_objects: 12, ...}, ...],  # 10-14 objects
    1: [{image_id: 456, num_objects: 17, ...}, ...],  # 15-19 objects
    2: [{image_id: 789, num_objects: 22, ...}, ...],  # 20-24 objects
    3: [{image_id: 999, num_objects: 28, ...}, ...]   # 25-30 objects
}
```

---

### **Step 3: Stratified Sampling**

**Function**: `stratified_sample()` (lines 83-110)

```python
def stratified_sample(object_count_bins, num_samples, seed=42):
    """Sample images stratified by object count."""
    random.seed(seed)  # For reproducibility

    bins = sorted(object_count_bins.keys())  # [0, 1, 2, 3]
    samples_per_bin = max(1, num_samples // len(bins))  # 25 // 4 = 6

    sampled = []
    for bin_idx in bins:
        candidates = object_count_bins[bin_idx]
        n_sample = min(samples_per_bin, len(candidates))
        sampled.extend(random.sample(candidates, n_sample))

    # If we haven't reached num_samples, sample more randomly
    if len(sampled) < num_samples:
        all_candidates = [item for items in object_count_bins.values() for item in items]
        remaining = [c for c in all_candidates if c not in sampled]
        additional = random.sample(remaining, min(num_samples - len(sampled), len(remaining)))
        sampled.extend(additional)

    # Shuffle and limit
    random.shuffle(sampled)
    sampled = sampled[:num_samples]

    # Sort by image_id for consistent ordering
    sampled = sorted(sampled, key=lambda x: x['image_id'])

    return sampled
```

**Why Stratified Sampling?**

Instead of random sampling from all 108K images, we ensure **balanced representation** across object count ranges:

```
Without stratification (random):
  [||||||||||||||||||||] 10-14 objects (80% of samples)
  [|||]                  15-19 objects (15%)
  [|]                    20-24 objects (4%)
  [|]                    25-30 objects (1%)

With stratification (balanced):
  [||||||] 10-14 objects (25% of samples)
  [||||||] 15-19 objects (25%)
  [||||||] 20-24 objects (25%)
  [||||||] 25-30 objects (25%)
```

**Algorithm**:
1. Calculate `samples_per_bin = 25 / 4 = 6` (approximately)
2. Sample 6 images from each bin
3. If total < 25, randomly sample remaining from all candidates
4. Shuffle to avoid ordering bias
5. Sort by image_id for deterministic output

**Reproducibility**:
- `random.seed(seed)` ensures same samples with same seed
- `seed=42` always produces the same 25 images

---

### **Step 4: Run Visualization Scripts**

**Function**: `run_visualization()` (lines 112-133)

```python
def run_visualization(script_path, vg_dir, output_dir, image_id, conda_env='hcnmn'):
    """Run a visualization script for a specific image."""
    cmd = [
        'conda', 'run', '-n', conda_env, 'python',
        script_path,
        '--vg_dir', vg_dir,
        '--output_dir', output_dir,
        '--image_id', str(image_id)
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        if result.returncode == 0:
            return {'success': True, 'stdout': result.stdout, 'stderr': result.stderr}
        else:
            return {'success': False, 'stdout': result.stdout, 'stderr': result.stderr}

    except subprocess.TimeoutExpired:
        return {'success': False, 'error': 'Timeout (120s)'}
    except Exception as e:
        return {'success': False, 'error': str(e)}
```

**What it does**:
- Executes a Python visualization script as a subprocess
- Uses conda environment activation: `conda run -n hcnmn`
- Sets 120-second timeout per script
- Captures stdout/stderr for logging
- Returns success/failure status

**Equivalent Command**:
```bash
conda run -n hcnmn python visualize_merged_granularity.py \
    --vg_dir /path/to/vg \
    --output_dir vg/v4_batch_sample \
    --image_id 498202
```

**Error Handling**:
- Returns `success: False` if script exits with non-zero code
- Returns `error: 'Timeout'` if script takes > 120 seconds
- Captures exceptions and returns error message

---

### **Step 5: Process Single Sample**

**Function**: `process_sample()` (lines 135-172)

```python
def process_sample(image_id, vg_dir, output_dir, inspect_dir):
    """Process a single VG sample with all visualization pipelines."""
    print(f"\n{'='*70}")
    print(f"Processing Image {image_id}")
    print(f"{'='*70}")

    results = {
        'image_id': image_id,
        'timestamp': datetime.now().isoformat(),
        'visualizations': {}
    }

    # 1. Run merged granularity visualization
    print("\n[1/2] Running merged granularity visualization...")
    merged_script = os.path.join(inspect_dir, 'visualize_merged_granularity.py')
    merged_result = run_visualization(merged_script, vg_dir, output_dir, image_id)
    results['visualizations']['merged_granularity'] = merged_result

    if merged_result['success']:
        print("  ✓ Merged granularity visualization complete")
    else:
        print(f"  ✗ Failed: {merged_result.get('error', 'Unknown error')}")

    # 2. Run scene graph hierarchy visualization
    print("\n[2/2] Running scene graph hierarchy visualization...")
    hierarchy_script = os.path.join(inspect_dir, 'visualize_scene_graph_hierarchy.py')
    hierarchy_result = run_visualization(hierarchy_script, vg_dir, output_dir, image_id)
    results['visualizations']['scene_graph_hierarchy'] = hierarchy_result

    if hierarchy_result['success']:
        print("  ✓ Scene graph hierarchy visualization complete")
    else:
        print(f"  ✗ Failed: {hierarchy_result.get('error', 'Unknown error')}")

    # Check overall success (at least one pipeline succeeded)
    results['success'] = merged_result['success'] or hierarchy_result['success']

    return results
```

**Pipeline Sequence**:

```
For each image ID:
  ┌────────────────────────────────────────────────┐
  │ Pipeline 1: Merged Granularity                 │
  │ Script: visualize_merged_granularity.py        │
  │ Output:                                        │
  │   - merged_fine.png                            │
  │   - merged_mid.png                             │
  │   - merged_coarse.png                          │
  │   - merged_comparison.png                      │
  │   - merged_scene_graph_data.json               │
  │   - MERGED_SCENE_GRAPH_REPORT.md               │
  └────────────────────────────────────────────────┘
                    ↓
  ┌────────────────────────────────────────────────┐
  │ Pipeline 2: Scene Graph Hierarchy              │
  │ Script: visualize_scene_graph_hierarchy.py     │
  │ Output:                                        │
  │   - original_scene_graph.png                   │
  │   - hierarchical_ontology_tree.png             │
  │   - combined_visualization.png                 │
  │   - ontology_data.json                         │
  └────────────────────────────────────────────────┘
```

**Success Criteria**:
- Sample considered successful if **at least one pipeline** succeeds
- This allows partial success (e.g., one script fails but other works)
- Each pipeline is independent

**Processing Time**:
- ~60-120 seconds per sample (both pipelines combined)
- For 25 samples: ~25-50 minutes total

---

### **Step 6: Generate Summary Report**

**Function**: `generate_summary_report()` (lines 174-279)

```python
def generate_summary_report(output_dir, sampled_images, processing_results, elapsed_time):
    """Generate comprehensive summary report."""
    report_path = os.path.join(output_dir, 'BATCH_SAMPLING_REPORT.md')

    successful = [r for r in processing_results if r['success']]
    failed = [r for r in processing_results if not r['success']]

    # Calculate statistics
    object_counts = [s['num_objects'] for s in sampled_images]
    relationship_counts = [s['num_relationships'] for s in sampled_images]

    with open(report_path, 'w') as f:
        # Write markdown report
        f.write("# Visual Genome Batch Sampling Report\n\n")
        f.write(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Processing Time**: {elapsed_time:.2f} seconds ({elapsed_time/60:.2f} minutes)\n\n")

        # Summary statistics
        f.write(f"- **Total Samples**: {len(sampled_images)}\n")
        f.write(f"- **Successful**: {len(successful)} ({len(successful)/len(sampled_images)*100:.1f}%)\n")
        f.write(f"- **Failed**: {len(failed)}\n\n")

        # Object statistics
        f.write(f"- **Min Objects**: {min(object_counts)}\n")
        f.write(f"- **Max Objects**: {max(object_counts)}\n")
        f.write(f"- **Mean Objects**: {sum(object_counts)/len(object_counts):.1f}\n\n")

        # Relationship statistics
        f.write(f"- **Min Relationships**: {min(relationship_counts)}\n")
        f.write(f"- **Max Relationships**: {max(relationship_counts)}\n")
        f.write(f"- **Mean Relationships**: {sum(relationship_counts)/len(relationship_counts):.1f}\n\n")

        # Table of successful samples
        f.write("| Image ID | Objects | Relationships | Output Directory |\n")
        f.write("|----------|---------|---------------|------------------|\n")
        for result in successful:
            img_info = next((s for s in sampled_images if s['image_id'] == result['image_id']), None)
            if img_info:
                f.write(f"| {result['image_id']} | {img_info['num_objects']} | "
                       f"{img_info['num_relationships']} | `sample_{result['image_id']}/` |\n")

    # Also save JSON data
    json_data = {
        'timestamp': datetime.now().isoformat(),
        'elapsed_time_seconds': elapsed_time,
        'total_samples': len(sampled_images),
        'successful': len(successful),
        'failed': len(failed),
        'sampled_images': sampled_images,
        'processing_results': processing_results
    }

    json_path = os.path.join(output_dir, 'batch_sampling_data.json')
    with open(json_path, 'w') as f:
        json.dump(json_data, f, indent=2)
```

**Outputs Two Files**:

1. **BATCH_SAMPLING_REPORT.md** (Human-readable)
   - Summary statistics (success rate, timing)
   - Object/relationship statistics
   - Table of successful samples
   - Failed samples with error messages

2. **batch_sampling_data.json** (Machine-readable)
   - Complete metadata for all samples
   - Processing results with timestamps
   - Full sample information for analysis

---

### **Step 7: Main Orchestration**

**Function**: `main()` (lines 281-396)

```python
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Batch sample and visualize VG images')
    parser.add_argument('--num_samples', type=int, default=25)
    parser.add_argument('--min_objects', type=int, default=10)
    parser.add_argument('--max_objects', type=int, default=30)
    parser.add_argument('--seed', type=int, default=42)
    # ... more arguments

    args = parser.parse_args()
    start_time = datetime.now()

    # 1. Create output directory
    output_dir = os.path.join(args.output_base, args.output_version)
    os.makedirs(output_dir, exist_ok=True)

    # 2. Load and filter VG scene graphs
    scene_graphs = load_vg_scene_graphs(args.vg_dir)
    good_samples, object_count_bins = filter_good_samples(
        scene_graphs, args.vg_dir, args.min_objects, args.max_objects
    )

    # 3. Stratified sampling
    sampled_images = stratified_sample(object_count_bins, args.num_samples, args.seed)

    print(f"\n✓ Sampled {len(sampled_images)} images:")
    for i, sample in enumerate(sampled_images, 1):
        print(f"  {i:2d}. Image {sample['image_id']:7d}: "
              f"{sample['num_objects']:2d} objects, "
              f"{sample['num_relationships']:3d} relationships")

    # 4. Process each sample
    processing_results = []
    for i, sample in enumerate(sampled_images, 1):
        print(f"\n\nProgress: [{i}/{len(sampled_images)}]")
        result = process_sample(
            sample['image_id'],
            args.vg_dir,
            output_dir,
            inspect_dir
        )
        processing_results.append(result)

    # 5. Calculate elapsed time
    elapsed_time = (datetime.now() - start_time).total_seconds()

    # 6. Generate summary report
    generate_summary_report(output_dir, sampled_images, processing_results, elapsed_time)

    # 7. Print final summary
    successful = sum(1 for r in processing_results if r['success'])
    print(f"\n{'='*70}")
    print("Batch Processing Complete!")
    print(f"  Total Samples: {len(sampled_images)}")
    print(f"  Successful: {successful} ({successful/len(sampled_images)*100:.1f}%)")
    print(f"  Failed: {len(sampled_images) - successful}")
    print(f"  Processing Time: {elapsed_time:.2f}s ({elapsed_time/60:.2f} minutes)")
    print(f"  Output Directory: {output_dir}")
```

**Execution Flow**:

```
main()
  ↓
[1] Parse arguments (num_samples=25, seed=42, ...)
  ↓
[2] Load scene_graphs.json (108K images)
  ↓
[3] Filter good samples (10-30 objects, has relationships, image exists)
    → Returns ~30K-40K good samples
  ↓
[4] Stratified sampling
    → Selects 25 images balanced across object count bins
  ↓
[5] Process each sample (loop 25 times)
    For each image:
      → Run visualize_merged_granularity.py (6 files)
      → Run visualize_scene_graph_hierarchy.py (4 files)
      → Collect results
  ↓
[6] Generate summary report
    → BATCH_SAMPLING_REPORT.md
    → batch_sampling_data.json
  ↓
[7] Print final statistics
```

---

## Complete Example Run

```bash
$ conda run -n hcnmn python batch_sample_vg.py --num_samples 25 --seed 42

======================================================================
VG Batch Sampling and Visualization Pipeline
======================================================================

Configuration:
  VG Directory: /home/jiachen/scratch/graph_reasoning/HCNMN/data/vg
  Output Version: v4_batch_sample_20251001
  Samples: 25
  Object Range: 10-30
  Random Seed: 42
  Conda Env: hcnmn

✓ Output directory: inspect/vg/v4_batch_sample_20251001

Loading scene graphs from: data/vg/annotations/v1.2/scene_graphs.json
✓ Loaded 108077 scene graphs

Filtering samples (object range: 10-30)...
✓ Found 38245 good samples
  Object count bins: {0: 12340, 1: 10234, 2: 8976, 3: 6695}

Performing stratified sampling...

✓ Sampled 25 images:
   1. Image  498202: 30 objects,  25 relationships
   2. Image  498348: 13 objects,   4 relationships
   3. Image 1159629: 21 objects,  10 relationships
  ...

======================================================================
Starting Batch Processing
======================================================================

Progress: [1/25]
======================================================================
Processing Image 498202
======================================================================

[1/2] Running merged granularity visualization...
  ✓ Merged granularity visualization complete

[2/2] Running scene graph hierarchy visualization...
  ✓ Scene graph hierarchy visualization complete

Progress: [2/25]
...

======================================================================
Generating Summary Report
======================================================================
✓ Generated summary report: vg/v4_batch_sample_20251001/BATCH_SAMPLING_REPORT.md
✓ Saved JSON data: vg/v4_batch_sample_20251001/batch_sampling_data.json

======================================================================
Batch Processing Complete!
======================================================================
  Total Samples: 25
  Successful: 25 (100.0%)
  Failed: 0
  Processing Time: 2110.15s (35.17 minutes)
  Output Directory: inspect/vg/v4_batch_sample_20251001

✓ See BATCH_SAMPLING_REPORT.md for detailed results
```

---

## Key Design Decisions

### 1. **Why Stratified Sampling?**
- Ensures diverse representation across object complexity levels
- Avoids bias toward simple or complex scenes
- Better for demonstrating multi-granularity reasoning

### 2. **Why Two Separate Scripts?**
- Modular design: each visualization type is independent
- Easier to debug individual pipelines
- Can run scripts separately if needed

### 3. **Why Subprocess Instead of Import?**
- Isolation: each script runs in its own process
- Error handling: one script failure doesn't crash entire batch
- Memory management: process cleanup after each sample

### 4. **Why 120-Second Timeout?**
- Most samples process in 60-90 seconds
- 120s allows buffer for complex images
- Prevents infinite hangs on problematic samples

### 5. **Why Object Range 10-30?**
- < 10 objects: Too simple, not interesting
- > 30 objects: Too cluttered, visualization becomes messy
- 10-30: Sweet spot for clear, informative visualizations

---

## Usage Patterns

### **Standard Usage**
```bash
conda run -n hcnmn python batch_sample_vg.py --num_samples 25
```

### **Custom Parameters**
```bash
# More samples
conda run -n hcnmn python batch_sample_vg.py --num_samples 50

# Different object range
conda run -n hcnmn python batch_sample_vg.py --min_objects 15 --max_objects 25

# Different random seed (different samples)
conda run -n hcnmn python batch_sample_vg.py --seed 123

# Custom output directory
conda run -n hcnmn python batch_sample_vg.py --output_version my_batch
```

### **Debugging Single Sample**
```bash
# If batch fails on image 498202, debug individually:
conda run -n hcnmn python visualize_merged_granularity.py --image_id 498202
conda run -n hcnmn python visualize_scene_graph_hierarchy.py --image_id 498202
```

---

## Output Structure

```
vg/v4_batch_sample_20251001/
├── BATCH_SAMPLING_REPORT.md          # Human-readable summary
├── batch_sampling_data.json          # Machine-readable metadata
│
├── sample_498202/                    # Sample directory (×25)
│   ├── merged_fine.png
│   ├── merged_mid.png
│   ├── merged_coarse.png
│   ├── merged_comparison.png
│   ├── merged_scene_graph_data.json
│   ├── MERGED_SCENE_GRAPH_REPORT.md
│   ├── original_scene_graph.png
│   ├── hierarchical_ontology_tree.png
│   ├── combined_visualization.png
│   └── ontology_data.json
│
├── sample_498348/
│   └── ... (same 10 files)
│
└── ... (23 more sample directories)
```

---

## Summary

**What the code does**:
1. Loads 108K VG images
2. Filters for quality (10-30 objects, has relationships, image exists)
3. Samples 25 images using stratified sampling (balanced across complexity)
4. For each sample, runs 2 visualization pipelines
5. Generates comprehensive report with statistics

**Key features**:
- **Stratified sampling** for diverse representation
- **Modular design** with independent visualization scripts
- **Robust error handling** with timeouts and logging
- **Comprehensive reporting** (markdown + JSON)
- **Reproducible** with fixed random seed

**Time complexity**:
- ~60-90 seconds per sample × 25 samples = 25-40 minutes total

