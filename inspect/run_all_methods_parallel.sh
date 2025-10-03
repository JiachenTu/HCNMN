#!/bin/bash
# Master script to run all 5 methods in parallel using tmux sessions
# Each method runs on a separate GPU device

WORK_DIR="/nas/jiachen/graph_reasoning/HCNMN/inspect"
cd "$WORK_DIR"

echo "=== Starting Parallel Batch Tests ==="
echo "Workspace: $WORK_DIR"
echo ""

# Check if tmux is available
if ! command -v tmux &> /dev/null; then
    echo "Error: tmux not found. Please install tmux first."
    exit 1
fi

# Create batch_results directory
mkdir -p batch_results

# Kill existing sessions if they exist
echo "Cleaning up existing sessions..."
tmux kill-session -t batch_v7 2>/dev/null
tmux kill-session -t batch_v8 2>/dev/null
tmux kill-session -t batch_v8_1 2>/dev/null
tmux kill-session -t batch_v20 2>/dev/null
tmux kill-session -t batch_v20_1 2>/dev/null

echo ""
echo "Creating tmux sessions..."
echo ""

# V7 - Adaptive Rules (GPU 0)
echo "1. Starting V7 (Adaptive Rules) on cuda:0..."
tmux new-session -d -s batch_v7 -c "$WORK_DIR"
tmux send-keys -t batch_v7 "cd $WORK_DIR && ./batch_test_v7.sh" C-m
echo "   ✓ Session 'batch_v7' created"

# V8 - Basic LLM (GPU 1)
echo "2. Starting V8 (Basic LLM) on cuda:1..."
tmux new-session -d -s batch_v8 -c "$WORK_DIR"
tmux send-keys -t batch_v8 "cd $WORK_DIR && ./batch_test_v8.sh" C-m
echo "   ✓ Session 'batch_v8' created"

# V8.1 - Context-Aware LLM (GPU 2)
echo "3. Starting V8.1 (Context-Aware LLM) on cuda:2..."
tmux new-session -d -s batch_v8_1 -c "$WORK_DIR"
tmux send-keys -t batch_v8_1 "cd $WORK_DIR && ./batch_test_v8_1.sh" C-m
echo "   ✓ Session 'batch_v8_1' created"

# V20 - Vision-Grounded VLM (GPU 3)
echo "4. Starting V20 (Vision-Grounded VLM) on cuda:3..."
tmux new-session -d -s batch_v20 -c "$WORK_DIR"
tmux send-keys -t batch_v20 "cd $WORK_DIR && ./batch_test_v20.sh" C-m
echo "   ✓ Session 'batch_v20' created"

# V20.1 - Enhanced VLM (GPU 4)
echo "5. Starting V20.1 (Enhanced VLM) on cuda:4..."
tmux new-session -d -s batch_v20_1 -c "$WORK_DIR"
tmux send-keys -t batch_v20_1 "cd $WORK_DIR && ./batch_test_v20_1.sh" C-m
echo "   ✓ Session 'batch_v20_1' created"

echo ""
echo "=== All Sessions Started ==="
echo ""
echo "Monitor sessions with:"
echo "  tmux ls                     # List all sessions"
echo "  tmux attach -t batch_v7     # Attach to V7 session"
echo "  tmux attach -t batch_v8     # Attach to V8 session"
echo "  tmux attach -t batch_v8_1   # Attach to V8.1 session"
echo "  tmux attach -t batch_v20    # Attach to V20 session"
echo "  tmux attach -t batch_v20_1  # Attach to V20.1 session"
echo ""
echo "Or use the monitoring dashboard:"
echo "  ./monitor_progress.sh"
echo ""
echo "To stop all sessions:"
echo "  ./stop_all_methods.sh"
