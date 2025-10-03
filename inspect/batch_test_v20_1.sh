#!/bin/bash
# Batch test V20.1 (Enhanced Vision-Grounded VLM) on selected test images
# Note: V20.1 uses same pipeline as V20 but with enhanced prompting and JSON extraction
# These improvements are already in vlm_granularity_selector_v20.py

METHOD="V20.1"
OUTPUT_DIR="/nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v20_1"
TEST_IMAGES="/nas/jiachen/graph_reasoning/HCNMN/inspect/test_images.txt"
DEVICE="cuda:4"

echo "=== V20.1 Enhanced Vision-Grounded VLM Batch Test ==="
echo "Device: $DEVICE"
echo "Output: $OUTPUT_DIR"
echo "Note: Using current V20 implementation with enhanced prompting"
echo ""

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Read test images
image_ids=($(cat "$TEST_IMAGES"))

echo "Processing ${#image_ids[@]} images..."
echo ""

# Process each image
for image_id in "${image_ids[@]}"; do
    echo "[$(date '+%H:%M:%S')] Processing image $image_id..."

    output_path="$OUTPUT_DIR/sample_$image_id"

    timeout 300 conda run -n qwen3 python visualize_scene_graph_hierarchy_v20.py \
        --image_id "$image_id" \
        --output_dir "$output_path" \
        --device "$DEVICE" \
        2>&1 | tee "$OUTPUT_DIR/log_$image_id.txt"

    exit_code=${PIPESTATUS[0]}

    if [ $exit_code -eq 0 ]; then
        echo "✓ Image $image_id completed successfully"
    elif [ $exit_code -eq 124 ]; then
        echo "⚠ Image $image_id timed out (300s)"
    else
        echo "✗ Image $image_id failed (exit code: $exit_code)"
    fi

    echo ""
done

echo "=== V20.1 Batch Test Complete ==="
echo "Results saved to: $OUTPUT_DIR"
