#!/bin/bash
# Stop all batch test tmux sessions

echo "Stopping all batch test sessions..."
echo ""

sessions=("batch_v7" "batch_v8" "batch_v8_1" "batch_v20" "batch_v20_1")

for session in "${sessions[@]}"; do
    if tmux has-session -t "$session" 2>/dev/null; then
        echo "✓ Killing session: $session"
        tmux kill-session -t "$session"
    else
        echo "  Session $session not running"
    fi
done

echo ""
echo "All sessions stopped."
