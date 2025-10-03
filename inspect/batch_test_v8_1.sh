#!/bin/bash
# Batch test V8.1 (Context-Aware LLM) on selected test images

METHOD="V8.1"
OUTPUT_DIR="/nas/jiachen/graph_reasoning/HCNMN/inspect/batch_results/v8_1"
TEST_IMAGES="/nas/jiachen/graph_reasoning/HCNMN/inspect/test_images.txt"
DEVICE="cuda:2"

echo "=== V8.1 Context-Aware LLM Batch Test ==="
echo "Device: $DEVICE"
echo "Output: $OUTPUT_DIR"
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

    timeout 300 conda run -n qwen3 python visualize_scene_graph_hierarchy_v8_1.py \
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

echo "=== V8.1 Batch Test Complete ==="
echo "Results saved to: $OUTPUT_DIR"
