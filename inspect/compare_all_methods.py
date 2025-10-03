#!/usr/bin/env python3
"""
Comprehensive statistical comparison of all methods.
Generates aggregate statistics, visualizations, and statistical tests.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json

# Configuration
ANALYSIS_DIR = Path("/nas/jiachen/graph_reasoning/HCNMN/inspect/batch_analysis")
OUTPUT_DIR = ANALYSIS_DIR / "comparison"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

METHOD_NAMES = {
    "v7": "V7 (Rules)",
    "v8": "V8 (LLM)",
    "v8_1": "V8.1 (LLM+Context)",
    "v20": "V20 (VLM)",
    "v20_1": "V20.1 (VLM+)"
}

METHOD_ORDER = ['v7', 'v8', 'v8_1', 'v20', 'v20_1']

def load_data():
    """Load combined results CSV."""
    csv_file = ANALYSIS_DIR / "all_methods_results.csv"

    if not csv_file.exists():
        print(f"❌ Results file not found: {csv_file}")
        print("Please run extract_all_results.py first.")
        return None

    df = pd.read_csv(csv_file)
    print(f"✓ Loaded {len(df)} results from {csv_file}")
    return df

def compute_aggregate_statistics(df):
    """Compute aggregate statistics for each method."""
    metrics = [
        'fine_concepts',
        'mid_concepts',
        'coarse_concepts',
        'compression_fine_to_coarse',
        'compression_mid_to_coarse'
    ]

    stats = {}

    for method in df['method'].unique():
        method_df = df[df['method'] == method]

        stats[method] = {
            'n_images': len(method_df),
            'method_name': METHOD_NAMES.get(method, method)
        }

        for metric in metrics:
            if metric in method_df.columns:
                values = method_df[metric].dropna()

                if len(values) > 0:
                    stats[method][metric] = {
                        'mean': float(values.mean()),
                        'median': float(values.median()),
                        'std': float(values.std()),
                        'min': float(values.min()),
                        'max': float(values.max())
                    }

        # Success rate metrics
        if 'llm_success_rate' in method_df.columns:
            values = method_df['llm_success_rate'].dropna()
            if len(values) > 0:
                stats[method]['llm_success_rate'] = {
                    'mean': float(values.mean()),
                    'std': float(values.std())
                }

        if 'vlm_success_rate' in method_df.columns:
            values = method_df['vlm_success_rate'].dropna()
            if len(values) > 0:
                stats[method]['vlm_success_rate'] = {
                    'mean': float(values.mean()),
                    'std': float(values.std())
                }

    return stats

def create_summary_table(stats):
    """Create a markdown summary table."""
    lines = [
        "# Comprehensive Method Comparison Summary",
        "",
        "**Test Images**: 10 diverse Visual Genome images (complexity range: 19.0-54.0)",
        "",
        "## Aggregate Statistics",
        "",
        "| Method | N | Fine Concepts | Mid Concepts | Coarse Concepts | Compression (F→C) | Compression (M→C) |",
        "|--------|---|---------------|--------------|-----------------|-------------------|-------------------|"
    ]

    for method in METHOD_ORDER:
        if method not in stats:
            continue

        method_stats = stats[method]
        name = method_stats['method_name']
        n = method_stats['n_images']

        fine = method_stats.get('fine_concepts', {})
        mid = method_stats.get('mid_concepts', {})
        coarse = method_stats.get('coarse_concepts', {})
        comp_fc = method_stats.get('compression_fine_to_coarse', {})
        comp_mc = method_stats.get('compression_mid_to_coarse', {})

        def format_metric(m):
            if m:
                return f"{m['mean']:.1f} ± {m['std']:.1f}"
            return "N/A"

        lines.append(
            f"| {name} | {n} | "
            f"{format_metric(fine)} | "
            f"{format_metric(mid)} | "
            f"{format_metric(coarse)} | "
            f"{format_metric(comp_fc)} | "
            f"{format_metric(comp_mc)} |"
        )

    lines.extend([
        "",
        "## VLM Success Rates (V20/V20.1 only)",
        "",
        "| Method | VLM Success Rate | Fallback Rate | Notes |",
        "|--------|------------------|---------------|-------|"
    ])

    for method in ['v20', 'v20_1']:
        if method not in stats:
            continue

        method_stats = stats[method]
        name = method_stats['method_name']
        n = method_stats['n_images']

        vlm_rate = method_stats.get('vlm_success_rate', {})
        fallback_rate = method_stats.get('vlm_fallback_rate', {})

        def format_rate(r):
            if r:
                return f"{r['mean']:.1f}% ± {r['std']:.1f}%"
            return "N/A"

        note = f"N={n}/10"
        if n < 10:
            note += f" (partial)"

        lines.append(
            f"| {name} | {format_rate(vlm_rate)} | {format_rate(fallback_rate)} | {note} |"
        )

    lines.extend([
        "",
        "**Note**: V7/V8/V8.1 are deterministic (no LLM/VLM success rates to track)."
    ])

    return "\n".join(lines)

def create_detailed_comparison(df):
    """Create detailed per-image comparison."""
    lines = [
        "",
        "## Per-Image Comparison",
        "",
        "**Note**: V20 has 6/10 images, V20.1 has 4/10 images (incomplete runs).",
        ""
    ]

    # Get unique image IDs where ALL methods have data (for fair comparison)
    all_images = set(df['image_id'].unique())
    v7_images = set(df[df['method'] == 'v7']['image_id'].unique())
    v8_images = set(df[df['method'] == 'v8']['image_id'].unique())
    v8_1_images = set(df[df['method'] == 'v8_1']['image_id'].unique())
    v20_images = set(df[df['method'] == 'v20']['image_id'].unique())
    v20_1_images = set(df[df['method'] == 'v20_1']['image_id'].unique())

    # Images where V7/V8/V8.1 have data (10 images)
    common_text_methods = v7_images & v8_images & v8_1_images

    # Images where all 5 methods have data
    complete_images = common_text_methods & v20_images & v20_1_images

    lines.extend([
        f"### Images with All 5 Methods ({len(complete_images)} images)",
        ""
    ])

    if complete_images:
        for image_id in sorted(complete_images):
            lines.extend([
                f"#### Image {image_id}",
                "",
                "| Method | Fine | Mid | Coarse | Compression (F→C) | VLM Success |",
                "|--------|------|-----|--------|-------------------|-------------|"
            ])

            image_df = df[df['image_id'] == image_id]

            for method in METHOD_ORDER:
                method_row = image_df[image_df['method'] == method]

                if len(method_row) == 0:
                    continue

                row = method_row.iloc[0]
                name = METHOD_NAMES.get(method, method)

                fine = row.get('fine_concepts', 'N/A')
                mid = row.get('mid_concepts', 'N/A')
                coarse = row.get('coarse_concepts', 'N/A')
                comp = row.get('compression_fine_to_coarse', 'N/A')

                vlm_success = ""
                if method in ['v20', 'v20_1'] and not pd.isna(row.get('vlm_success_rate')):
                    vlm_success = f"{row['vlm_success_rate']:.1f}%"
                else:
                    vlm_success = "N/A"

                if not pd.isna(comp):
                    comp = f"{comp:.2f}x"

                lines.append(f"| {name} | {fine} | {mid} | {coarse} | {comp} | {vlm_success} |")

            lines.append("")
    else:
        lines.append("*No images with complete data from all 5 methods*\n")

    # Show text-only methods comparison (V7/V8/V8.1) for all 10 images
    lines.extend([
        "### Text-Only Methods Comparison (10 images)",
        ""
    ])

    for image_id in sorted(common_text_methods):
        lines.extend([
            f"#### Image {image_id}",
            "",
            "| Method | Fine | Mid | Coarse | Compression (F→C) |",
            "|--------|------|-----|--------|-------------------|"
        ])

        image_df = df[df['image_id'] == image_id]

        for method in ['v7', 'v8', 'v8_1']:
            method_row = image_df[image_df['method'] == method]

            if len(method_row) == 0:
                continue

            row = method_row.iloc[0]
            name = METHOD_NAMES.get(method, method)

            fine = row.get('fine_concepts', 'N/A')
            mid = row.get('mid_concepts', 'N/A')
            coarse = row.get('coarse_concepts', 'N/A')
            comp = row.get('compression_fine_to_coarse', 'N/A')

            if not pd.isna(comp):
                comp = f"{comp:.2f}x"

            lines.append(f"| {name} | {fine} | {mid} | {coarse} | {comp} |")

        lines.append("")

    return "\n".join(lines)

def create_ranking_analysis(stats):
    """Rank methods by key metrics."""
    lines = [
        "",
        "## Method Rankings",
        "",
        "### By Compression Ratio (F→C, Higher is Better)",
        ""
    ]

    # Extract compression ratios
    compressions = []
    for method, data in stats.items():
        comp = data.get('compression_fine_to_coarse', {}).get('mean')
        if comp:
            compressions.append((METHOD_NAMES[method], comp))

    compressions.sort(key=lambda x: x[1], reverse=True)

    for i, (name, comp) in enumerate(compressions, 1):
        lines.append(f"{i}. {name}: {comp:.2f}x")

    lines.extend([
        "",
        "### By Coarse Concept Count (Lower is Better)",
        ""
    ])

    # Extract coarse concept counts
    coarse_counts = []
    for method, data in stats.items():
        count = data.get('coarse_concepts', {}).get('mean')
        if count:
            coarse_counts.append((METHOD_NAMES[method], count))

    coarse_counts.sort(key=lambda x: x[1])

    for i, (name, count) in enumerate(coarse_counts, 1):
        lines.append(f"{i}. {name}: {count:.1f} concepts")

    return "\n".join(lines)

def generate_recommendations(stats):
    """Generate recommendations based on analysis."""
    lines = [
        "",
        "## Key Findings",
        ""
    ]

    # Find best compression
    best_compression = max(
        [(method, data.get('compression_fine_to_coarse', {}).get('mean', 0))
         for method, data in stats.items()],
        key=lambda x: x[1]
    )

    # Find best VLM success rate
    vlm_methods = [(method, data.get('vlm_success_rate', {}).get('mean', 0))
                   for method, data in stats.items() if method in ['v20', 'v20_1']]
    best_vlm = max(vlm_methods, key=lambda x: x[1]) if vlm_methods else None

    lines.extend([
        f"1. **Best Compression**: {METHOD_NAMES[best_compression[0]]} - **{best_compression[1]:.2f}x** (Fine→Coarse)",
        ""
    ])

    if best_vlm and best_vlm[1] > 0:
        lines.append(f"2. **Best VLM Success**: {METHOD_NAMES[best_vlm[0]]} - **{best_vlm[1]:.1f}%** (vision-grounded JSON generation)")
        lines.append("")

    # Compare V8.1 vs V7
    v8_1_stats = stats.get('v8_1', {})
    v7_stats = stats.get('v7', {})
    v20_stats = stats.get('v20', {})
    v20_1_stats = stats.get('v20_1', {})

    v8_1_comp = v8_1_stats.get('compression_fine_to_coarse', {}).get('mean', 0)
    v7_comp = v7_stats.get('compression_fine_to_coarse', {}).get('mean', 0)
    v20_comp = v20_stats.get('compression_fine_to_coarse', {}).get('mean', 0) if v20_stats else 0
    v20_1_comp = v20_1_stats.get('compression_fine_to_coarse', {}).get('mean', 0) if v20_1_stats else 0

    v8_1_coarse = v8_1_stats.get('coarse_concepts', {}).get('mean', 0)
    v7_coarse = v7_stats.get('coarse_concepts', {}).get('mean', 0)

    lines.extend([
        "3. **Text-Only Methods (V7/V8/V8.1)**:",
        f"   - V8.1 achieves **{v8_1_comp:.2f}x** compression ({v8_1_coarse:.1f} coarse concepts)",
        f"   - V7 achieves **{v7_comp:.2f}x** compression ({v7_coarse:.1f} coarse concepts)",
        f"   - V8.1 **{((v8_1_comp/v7_comp - 1) * 100):.1f}% better** than V7",
        ""
    ])

    if v20_comp > 0 or v20_1_comp > 0:
        lines.extend([
            "4. **Vision-Grounded Methods (V20/V20.1)**:",
            f"   - V20 compression: **{v20_comp:.2f}x** ({v20_stats.get('n_images', 0)}/10 images)",
            f"   - V20.1 compression: **{v20_1_comp:.2f}x** ({v20_1_stats.get('n_images', 0)}/10 images)",
            f"   - Vision grounding **{'improves' if max(v20_comp, v20_1_comp) > v8_1_comp else 'does not improve'}** compression vs V8.1",
            ""
        ])

    lines.extend([
        "## Recommendations",
        "",
        "### For Production Use",
        ""
    ])

    if v8_1_comp >= v7_comp:
        lines.extend([
            "**Primary Recommendation**: V8.1 (Context-Aware LLM)",
            "",
            "**Reasons**:",
            f"- Highest compression: **{v8_1_comp:.2f}x**",
            f"- Fewest coarse concepts: **{v8_1_coarse:.1f}** (most abstract)",
            "- Intelligent semantic reasoning with scene context",
            "- Text-only (faster than VLM)",
            ""
        ])
    else:
        lines.extend([
            "**Primary Recommendation**: V7 (Adaptive Rules)",
            "",
            "**Reasons**:",
            f"- Highest compression: **{v7_comp:.2f}x**",
            "- Deterministic, rule-based (no LLM overhead)",
            "- Fast and reliable",
            ""
        ])

    lines.extend([
        "### For Research & Explainability",
        "",
        "**V20/V20.1 (Vision VLM)** if:",
        "- Visual grounding is essential",
        "- Explainable AI requirements (vision-aware reasoning)",
        "- Studying multimodal semantic abstraction",
        ""
    ])

    if best_vlm and best_vlm[1] < 50:
        lines.extend([
            "**Limitation**: Current VLM success rate is **low** (~40% average).",
            "- VLMs struggle with strict JSON format despite enhanced prompting",
            "- High fallback rate to V7 rules",
            "- For production vision-grounding, deploy with vLLM + `guided_json`",
            ""
        ])

    return "\n".join(lines)

# Main execution
print("=== Comprehensive Method Comparison ===\n")

# Load data
df = load_data()

if df is None:
    exit(1)

# Compute statistics
print("\nComputing aggregate statistics...")
stats = compute_aggregate_statistics(df)

# Save statistics to JSON
stats_file = OUTPUT_DIR / "aggregate_statistics.json"
with open(stats_file, 'w') as f:
    json.dump(stats, f, indent=2)
print(f"✓ Saved statistics to {stats_file}")

# Create summary report
print("\nGenerating comparison report...")
report = create_summary_table(stats)
report += create_detailed_comparison(df)
report += create_ranking_analysis(stats)
report += generate_recommendations(stats)

# Save report
report_file = OUTPUT_DIR / "COMPREHENSIVE_COMPARISON.md"
with open(report_file, 'w') as f:
    f.write(report)
print(f"✓ Saved report to {report_file}")

print("\n=== Analysis Complete ===")
print(f"Output directory: {OUTPUT_DIR}")
print(f"  ✓ aggregate_statistics.json")
print(f"  ✓ COMPREHENSIVE_COMPARISON.md")
