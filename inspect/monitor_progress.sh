#!/bin/bash
# Monitor progress of all batch tests

WORK_DIR="/nas/jiachen/graph_reasoning/HCNMN/inspect"
RESULTS_DIR="$WORK_DIR/batch_results"

echo "╔══════════════════════════════════════════════════════════════════════╗"
echo "║          Hierarchical Scene Graph Batch Test Progress               ║"
echo "╚══════════════════════════════════════════════════════════════════════╝"
echo ""

# Function to count completed images for a method
count_results() {
    local method=$1
    local method_dir="$RESULTS_DIR/$method"

    if [ ! -d "$method_dir" ]; then
        echo "0"
        return
    fi

    # Count directories starting with "sample_"
    local count=$(find "$method_dir" -maxdepth 1 -type d -name "sample_*" 2>/dev/null | wc -l)
    echo "$count"
}

# Function to check if tmux session is running
check_session() {
    local session=$1
    tmux has-session -t "$session" 2>/dev/null
    return $?
}

# Total images to process
TOTAL_IMAGES=10

echo "Method Status (Completed/Total):"
echo "─────────────────────────────────────────────────────────────────────"

# V7
v7_count=$(count_results "v7")
v7_status="●"
check_session "batch_v7" && v7_status="🔄" || v7_status="✓"
[ "$v7_count" -eq 0 ] && check_session "batch_v7" || v7_status="🔄"
[ "$v7_count" -eq "$TOTAL_IMAGES" ] && v7_status="✓"
printf "%-25s %2d/%d %s\n" "V7 (Adaptive Rules)" "$v7_count" "$TOTAL_IMAGES" "$v7_status"

# V8
v8_count=$(count_results "v8")
v8_status="●"
check_session "batch_v8" && v8_status="🔄" || v8_status="✓"
[ "$v8_count" -eq 0 ] && check_session "batch_v8" || v8_status="🔄"
[ "$v8_count" -eq "$TOTAL_IMAGES" ] && v8_status="✓"
printf "%-25s %2d/%d %s\n" "V8 (Basic LLM)" "$v8_count" "$TOTAL_IMAGES" "$v8_status"

# V8.1
v8_1_count=$(count_results "v8_1")
v8_1_status="●"
check_session "batch_v8_1" && v8_1_status="🔄" || v8_1_status="✓"
[ "$v8_1_count" -eq 0 ] && check_session "batch_v8_1" || v8_1_status="🔄"
[ "$v8_1_count" -eq "$TOTAL_IMAGES" ] && v8_1_status="✓"
printf "%-25s %2d/%d %s\n" "V8.1 (Context-Aware LLM)" "$v8_1_count" "$TOTAL_IMAGES" "$v8_1_status"

# V20
v20_count=$(count_results "v20")
v20_status="●"
check_session "batch_v20" && v20_status="🔄" || v20_status="✓"
[ "$v20_count" -eq 0 ] && check_session "batch_v20" || v20_status="🔄"
[ "$v20_count" -eq "$TOTAL_IMAGES" ] && v20_status="✓"
printf "%-25s %2d/%d %s\n" "V20 (Vision VLM)" "$v20_count" "$TOTAL_IMAGES" "$v20_status"

# V20.1
v20_1_count=$(count_results "v20_1")
v20_1_status="●"
check_session "batch_v20_1" && v20_1_status="🔄" || v20_1_status="✓"
[ "$v20_1_count" -eq 0 ] && check_session "batch_v20_1" || v20_1_status="🔄"
[ "$v20_1_count" -eq "$TOTAL_IMAGES" ] && v20_1_status="✓"
printf "%-25s %2d/%d %s\n" "V20.1 (Enhanced VLM)" "$v20_1_count" "$TOTAL_IMAGES" "$v20_1_status"

echo "─────────────────────────────────────────────────────────────────────"
total_completed=$((v7_count + v8_count + v8_1_count + v20_count + v20_1_count))
total_expected=$((TOTAL_IMAGES * 5))
printf "%-25s %2d/%d (%.1f%%)\n" "Overall Progress" "$total_completed" "$total_expected" "$(echo "scale=1; $total_completed * 100 / $total_expected" | bc)"

echo ""
echo "Active tmux sessions:"
tmux ls 2>/dev/null | grep "batch_" || echo "  None"

echo ""
echo "Legend: ● Not started | 🔄 Running | ✓ Completed"
echo ""
echo "Commands:"
echo "  ./monitor_progress.sh              # Refresh this view"
echo "  tmux attach -t batch_v7            # Attach to a session"
echo "  ./stop_all_methods.sh              # Stop all sessions"
echo "  tail -f batch_results/v7/log_*.txt # View logs"
