#!/usr/bin/env python3
"""
Batch sampling and visualization of Visual Genome images for HCG generation.
Samples diverse images and runs both visualization pipelines.
"""
import os
import sys
import json
import argparse
import random
import subprocess
from datetime import datetime
from collections import defaultdict
from pathlib import Path

def load_vg_scene_graphs(vg_dir):
    """Load all VG scene graphs."""
    scene_graphs_path = os.path.join(vg_dir, 'annotations', 'v1.2', 'scene_graphs.json')
    print(f"Loading scene graphs from: {scene_graphs_path}")

    with open(scene_graphs_path, 'r') as f:
        scene_graphs = json.load(f)

    print(f"✓ Loaded {len(scene_graphs)} scene graphs")
    return scene_graphs

def filter_good_samples(scene_graphs, vg_dir, min_objects=10, max_objects=30):
    """
    Filter scene graphs for good visualization candidates.

    Criteria:
    - Object count in reasonable range (10-30)
    - Has some relationships
    - Image file exists
    """
    print(f"\nFiltering samples (object range: {min_objects}-{max_objects})...")

    good_samples = []
    object_count_bins = defaultdict(list)

    for sg in scene_graphs:
        image_id = sg['image_id']
        objects = sg.get('objects', [])
        relationships = sg.get('relationships', [])

        num_objects = len(objects)
        num_relationships = len(relationships)

        # Check object count
        if not (min_objects <= num_objects <= max_objects):
            continue

        # Prefer images with relationships
        if num_relationships == 0:
            continue

        # Check if image exists in VG_100K
        image_path = os.path.join(vg_dir, 'images', 'VG_100K', 'VG_100K', f'{image_id}.jpg')
        if not os.path.exists(image_path):
            continue

        # Bin by object count for stratified sampling
        bin_idx = (num_objects - min_objects) // 5  # 5-object bins
        object_count_bins[bin_idx].append({
            'image_id': image_id,
            'num_objects': num_objects,
            'num_relationships': num_relationships,
            'image_path': image_path
        })

        good_samples.append({
            'image_id': image_id,
            'num_objects': num_objects,
            'num_relationships': num_relationships,
            'image_path': image_path
        })

    print(f"✓ Found {len(good_samples)} good samples")
    print(f"  Object count bins: {dict((k, len(v)) for k, v in object_count_bins.items())}")

    return good_samples, object_count_bins

def stratified_sample(object_count_bins, num_samples, seed=42):
    """Sample images stratified by object count."""
    random.seed(seed)

    bins = sorted(object_count_bins.keys())
    samples_per_bin = max(1, num_samples // len(bins))

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

    # Check overall success
    results['success'] = merged_result['success'] or hierarchy_result['success']

    return results

def generate_summary_report(output_dir, sampled_images, processing_results, elapsed_time):
    """Generate comprehensive summary report."""
    report_path = os.path.join(output_dir, 'BATCH_SAMPLING_REPORT.md')

    successful = [r for r in processing_results if r['success']]
    failed = [r for r in processing_results if not r['success']]

    # Calculate statistics
    object_counts = [s['num_objects'] for s in sampled_images]
    relationship_counts = [s['num_relationships'] for s in sampled_images]

    with open(report_path, 'w') as f:
        f.write("# Visual Genome Batch Sampling Report\n\n")
        f.write(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Processing Time**: {elapsed_time:.2f} seconds ({elapsed_time/60:.2f} minutes)\n\n")
        f.write("---\n\n")

        # Summary statistics
        f.write("## Summary Statistics\n\n")
        f.write(f"- **Total Samples**: {len(sampled_images)}\n")
        f.write(f"- **Successful**: {len(successful)} ({len(successful)/len(sampled_images)*100:.1f}%)\n")
        f.write(f"- **Failed**: {len(failed)} ({len(failed)/len(sampled_images)*100:.1f}%)\n\n")

        f.write("### Object Statistics\n")
        f.write(f"- **Min Objects**: {min(object_counts)}\n")
        f.write(f"- **Max Objects**: {max(object_counts)}\n")
        f.write(f"- **Mean Objects**: {sum(object_counts)/len(object_counts):.1f}\n\n")

        f.write("### Relationship Statistics\n")
        f.write(f"- **Min Relationships**: {min(relationship_counts)}\n")
        f.write(f"- **Max Relationships**: {max(relationship_counts)}\n")
        f.write(f"- **Mean Relationships**: {sum(relationship_counts)/len(relationship_counts):.1f}\n\n")

        f.write("---\n\n")

        # Successful samples
        f.write("## Successful Samples\n\n")
        f.write("| Image ID | Objects | Relationships | Output Directory |\n")
        f.write("|----------|---------|---------------|------------------|\n")

        for result in successful:
            img_info = next((s for s in sampled_images if s['image_id'] == result['image_id']), None)
            if img_info:
                sample_dir = f"sample_{result['image_id']}"
                f.write(f"| {result['image_id']} | {img_info['num_objects']} | "
                       f"{img_info['num_relationships']} | `{sample_dir}/` |\n")

        f.write("\n---\n\n")

        # Failed samples (if any)
        if failed:
            f.write("## Failed Samples\n\n")
            f.write("| Image ID | Reason |\n")
            f.write("|----------|--------|\n")

            for result in failed:
                error_msg = "Unknown error"
                for viz_name, viz_result in result['visualizations'].items():
                    if not viz_result['success']:
                        error_msg = viz_result.get('error', viz_result.get('stderr', 'Unknown'))[:100]
                        break
                f.write(f"| {result['image_id']} | {error_msg} |\n")

            f.write("\n---\n\n")

        # Output structure
        f.write("## Output Structure\n\n")
        f.write("Each sample directory contains:\n\n")
        f.write("```\n")
        f.write("sample_{image_id}/\n")
        f.write("├── merged_fine.png              # Merged fine-grained scene graph\n")
        f.write("├── merged_mid.png               # Merged mid-level scene graph\n")
        f.write("├── merged_coarse.png            # Merged coarse-grained scene graph\n")
        f.write("├── merged_comparison.png        # 3-panel comparison\n")
        f.write("├── merged_scene_graph_data.json # Merged graph data\n")
        f.write("├── MERGED_SCENE_GRAPH_REPORT.md # Detailed report\n")
        f.write("├── original_scene_graph.png     # Original VG scene graph\n")
        f.write("├── hierarchical_ontology_tree.png # Hierarchy tree\n")
        f.write("├── combined_visualization.png   # Combined view\n")
        f.write("└── ontology_data.json           # Ontology structure\n")
        f.write("```\n\n")

        f.write("---\n\n")
        f.write("**Pipeline**: HCNMN Hierarchical Concept Graph Generation\n")
        f.write("**Scripts Used**:\n")
        f.write("- `visualize_merged_granularity.py`\n")
        f.write("- `visualize_scene_graph_hierarchy.py`\n")

    print(f"\n✓ Generated summary report: {report_path}")

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

    print(f"✓ Saved JSON data: {json_path}")

def main():
    parser = argparse.ArgumentParser(description='Batch sample and visualize VG images')
    parser.add_argument('--vg_dir', type=str,
                       default='/home/jiachen/scratch/graph_reasoning/HCNMN/data/vg',
                       help='Visual Genome data directory')
    parser.add_argument('--output_base', type=str,
                       default='/home/jiachen/scratch/graph_reasoning/HCNMN/inspect/vg',
                       help='Output base directory')
    parser.add_argument('--output_version', type=str,
                       default=f'v4_batch_sample_{datetime.now().strftime("%Y%m%d")}',
                       help='Output version/directory name')
    parser.add_argument('--num_samples', type=int, default=25,
                       help='Number of images to sample')
    parser.add_argument('--min_objects', type=int, default=10,
                       help='Minimum object count')
    parser.add_argument('--max_objects', type=int, default=30,
                       help='Maximum object count')
    parser.add_argument('--seed', type=int, default=42,
                       help='Random seed for reproducibility')
    parser.add_argument('--conda_env', type=str, default='hcnmn',
                       help='Conda environment name')

    args = parser.parse_args()

    print("="*70)
    print("VG Batch Sampling and Visualization Pipeline")
    print("="*70)
    print(f"\nConfiguration:")
    print(f"  VG Directory: {args.vg_dir}")
    print(f"  Output Version: {args.output_version}")
    print(f"  Samples: {args.num_samples}")
    print(f"  Object Range: {args.min_objects}-{args.max_objects}")
    print(f"  Random Seed: {args.seed}")
    print(f"  Conda Env: {args.conda_env}")

    start_time = datetime.now()

    # Create output directory
    output_dir = os.path.join(args.output_base, args.output_version)
    os.makedirs(output_dir, exist_ok=True)
    print(f"\n✓ Output directory: {output_dir}")

    # Get inspect directory (where scripts are)
    inspect_dir = os.path.dirname(os.path.abspath(__file__))

    # Load and filter VG scene graphs
    scene_graphs = load_vg_scene_graphs(args.vg_dir)
    good_samples, object_count_bins = filter_good_samples(
        scene_graphs, args.vg_dir, args.min_objects, args.max_objects
    )

    if len(good_samples) < args.num_samples:
        print(f"\n⚠ Warning: Only {len(good_samples)} good samples available, "
              f"requested {args.num_samples}")
        args.num_samples = len(good_samples)

    # Stratified sampling
    print(f"\nPerforming stratified sampling...")
    sampled_images = stratified_sample(object_count_bins, args.num_samples, args.seed)

    print(f"\n✓ Sampled {len(sampled_images)} images:")
    for i, sample in enumerate(sampled_images, 1):
        print(f"  {i:2d}. Image {sample['image_id']:7d}: "
              f"{sample['num_objects']:2d} objects, "
              f"{sample['num_relationships']:3d} relationships")

    # Process each sample
    print(f"\n{'='*70}")
    print("Starting Batch Processing")
    print(f"{'='*70}")

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

    # Calculate elapsed time
    elapsed_time = (datetime.now() - start_time).total_seconds()

    # Generate summary report
    print(f"\n{'='*70}")
    print("Generating Summary Report")
    print(f"{'='*70}")

    generate_summary_report(output_dir, sampled_images, processing_results, elapsed_time)

    # Final summary
    successful = sum(1 for r in processing_results if r['success'])
    print(f"\n{'='*70}")
    print("Batch Processing Complete!")
    print(f"{'='*70}")
    print(f"  Total Samples: {len(sampled_images)}")
    print(f"  Successful: {successful} ({successful/len(sampled_images)*100:.1f}%)")
    print(f"  Failed: {len(sampled_images) - successful}")
    print(f"  Processing Time: {elapsed_time:.2f}s ({elapsed_time/60:.2f} minutes)")
    print(f"  Output Directory: {output_dir}")
    print(f"\n✓ See BATCH_SAMPLING_REPORT.md for detailed results")

if __name__ == '__main__':
    main()
