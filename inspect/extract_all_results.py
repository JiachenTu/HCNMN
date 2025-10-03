#!/usr/bin/env python3
"""
Extract and aggregate results from all method batch tests.
Creates CSV files with metrics for each method.
"""

import os
import json
import csv
from pathlib import Path

# Configuration
BATCH_RESULTS_DIR = Path("/nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results")
OUTPUT_DIR = Path("/nas/jiachen/graph_reasoning/HCNMN/inspect/batch_analysis")
OUTPUT_DIR.mkdir(exist_ok=True)

METHODS = ["v7", "v8", "v8_1", "v20", "v20_1"]
METHOD_NAMES = {
    "v7": "V7 (Adaptive Rules)",
    "v8": "V8 (Basic LLM)",
    "v8_1": "V8.1 (Context-Aware LLM)",
    "v20": "V20 (Vision VLM)",
    "v20_1": "V20.1 (Enhanced VLM)"
}

def extract_method_results(method):
    """Extract results for a specific method."""
    method_dir = BATCH_RESULTS_DIR / method

    if not method_dir.exists():
        print(f"⚠ Method directory not found: {method_dir}")
        return []

    results = []

    # Find all sample directories
    sample_dirs = sorted([d for d in method_dir.iterdir() if d.is_dir() and d.name.startswith("sample_")])

    for sample_dir in sample_dirs:
        image_id = sample_dir.name.replace("sample_", "")

        # Try V7/V8/V8.1 format: ontology_data.json
        json_file = sample_dir / f"sample_{image_id}" / "ontology_data.json"
        if not json_file.exists():
            json_file = sample_dir / "ontology_data.json"

        if json_file.exists():
            # Parse JSON data (V7/V8/V8.1)
            stats = parse_json_file(json_file)
        else:
            # Try V20/V20.1 format: text reports
            concept_report = sample_dir / f"sample_{image_id}" / "concept_mapping_report.txt"
            vlm_report = sample_dir / f"sample_{image_id}" / "v20_vision_grounded_method_report.txt"

            if not concept_report.exists():
                print(f"  ⚠ Data file not found for {method}/{image_id}")
                continue

            # Parse text reports (V20/V20.1)
            stats = parse_text_reports(concept_report, vlm_report if vlm_report.exists() else None)

        if stats:
            stats['method'] = method
            stats['image_id'] = image_id
            results.append(stats)
            print(f"  ✓ Extracted {method}/{image_id}")

    return results

def parse_json_file(json_file):
    """Parse statistics from ontology_data.json file."""
    with open(json_file, 'r') as f:
        data = json.load(f)

    stats = {}

    # Extract statistics from JSON
    if 'statistics' in data:
        json_stats = data['statistics']
        stats['fine_concepts'] = json_stats.get('fine_concepts')
        stats['mid_concepts'] = json_stats.get('mid_concepts')
        stats['coarse_concepts'] = json_stats.get('coarse_concepts')
        stats['compression_fine_to_mid'] = json_stats.get('compression_fine_to_mid')
        stats['compression_fine_to_coarse'] = json_stats.get('compression_fine_to_coarse')

        # Calculate mid to coarse compression if available
        if stats.get('mid_concepts') and stats.get('coarse_concepts') and stats['coarse_concepts'] > 0:
            stats['compression_mid_to_coarse'] = round(stats['mid_concepts'] / stats['coarse_concepts'], 2)

    # For VLM methods, check if there's a success rate in the data
    # This would be added by V20/V20.1 pipelines if they track it
    if 'vlm_stats' in data:
        vlm_stats = data['vlm_stats']
        stats['vlm_success_count'] = vlm_stats.get('success_count')
        stats['vlm_total_count'] = vlm_stats.get('total_count')
        if stats.get('vlm_total_count') and stats['vlm_total_count'] > 0:
            stats['vlm_success_rate'] = round(100 * stats['vlm_success_count'] / stats['vlm_total_count'], 1)

    # For LLM methods
    if 'llm_stats' in data:
        llm_stats = data['llm_stats']
        stats['llm_success_count'] = llm_stats.get('success_count')
        stats['llm_total_count'] = llm_stats.get('total_count')
        if stats.get('llm_total_count') and stats['llm_total_count'] > 0:
            stats['llm_success_rate'] = round(100 * stats['llm_success_count'] / stats['llm_total_count'], 1)

    return stats

def parse_text_reports(concept_report, vlm_report=None):
    """Parse statistics from V20/V20.1 text reports."""
    stats = {}

    # Parse concept_mapping_report.txt
    with open(concept_report, 'r') as f:
        content = f.read()

    # Extract concept counts
    import re

    # Fine concepts
    match = re.search(r'\*\*Unique Fine Concepts\*\*:\s*(\d+)', content)
    if match:
        stats['fine_concepts'] = int(match.group(1))

    # Mid concepts
    match = re.search(r'\*\*Unique Mid Concepts\*\*:\s*(\d+)', content)
    if match:
        stats['mid_concepts'] = int(match.group(1))

    # Coarse concepts
    match = re.search(r'\*\*Unique Coarse Concepts\*\*:\s*(\d+)', content)
    if match:
        stats['coarse_concepts'] = int(match.group(1))

    # Compression ratios
    match = re.search(r'Fine → Mid:\s*\*\*([0-9.]+)x\*\*', content)
    if match:
        stats['compression_fine_to_mid'] = float(match.group(1))

    match = re.search(r'Fine → Coarse:\s*\*\*([0-9.]+)x\*\*', content)
    if match:
        stats['compression_fine_to_coarse'] = float(match.group(1))

    match = re.search(r'Mid → Coarse:\s*\*\*([0-9.]+)x\*\*', content)
    if match:
        stats['compression_mid_to_coarse'] = float(match.group(1))

    # Parse VLM report if available
    if vlm_report and vlm_report.exists():
        with open(vlm_report, 'r') as f:
            vlm_content = f.read()

        # Extract VLM success rate
        # Format: "VLM success: 1/9 (11.1%)"
        match = re.search(r'VLM success:\s*(\d+)/(\d+)\s*\(([0-9.]+)%\)', vlm_content)
        if match:
            stats['vlm_success_count'] = int(match.group(1))
            stats['vlm_total_count'] = int(match.group(2))
            stats['vlm_success_rate'] = float(match.group(3))

        # Extract fallback rate
        match = re.search(r'Fallback to V7 rules:\s*(\d+)/(\d+)\s*\(([0-9.]+)%\)', vlm_content)
        if match:
            stats['vlm_fallback_count'] = int(match.group(1))
            stats['vlm_fallback_rate'] = float(match.group(3))

    return stats

def save_results_to_csv(results, method):
    """Save results to CSV file."""
    if not results:
        print(f"No results to save for {method}")
        return

    csv_file = OUTPUT_DIR / f"{method}_results.csv"

    # Get all fieldnames from all results
    fieldnames = set()
    for result in results:
        fieldnames.update(result.keys())

    fieldnames = sorted(list(fieldnames))

    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"✓ Saved {len(results)} results to {csv_file}")

def create_combined_csv(all_results):
    """Create a combined CSV with all methods."""
    combined_file = OUTPUT_DIR / "all_methods_results.csv"

    if not all_results:
        print("No results to combine")
        return

    # Get all fieldnames
    fieldnames = set()
    for result in all_results:
        fieldnames.update(result.keys())

    fieldnames = sorted(list(fieldnames))

    with open(combined_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_results)

    print(f"✓ Saved {len(all_results)} combined results to {combined_file}")

# Main execution
print("=== Extracting Results from All Methods ===\n")

all_results = []

for method in METHODS:
    print(f"\nExtracting {METHOD_NAMES[method]}...")
    results = extract_method_results(method)

    if results:
        save_results_to_csv(results, method)
        all_results.extend(results)
    else:
        print(f"  No results found for {method}")

print(f"\n=== Creating Combined Dataset ===")
create_combined_csv(all_results)

print(f"\n=== Summary ===")
print(f"Total results extracted: {len(all_results)}")
print(f"Output directory: {OUTPUT_DIR}")
print(f"\nCSV files created:")
for method in METHODS:
    csv_file = OUTPUT_DIR / f"{method}_results.csv"
    if csv_file.exists():
        print(f"  ✓ {csv_file}")

print(f"  ✓ {OUTPUT_DIR / 'all_methods_results.csv'}")
