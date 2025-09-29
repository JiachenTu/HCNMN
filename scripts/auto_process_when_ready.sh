#!/bin/bash

# Automatically process GloVe when download is complete
# This script waits for GloVe extraction to complete, then starts processing

echo "=== Auto-Processor for HCNMN ==="
echo "Waiting for GloVe extraction to complete..."

while true; do
    if [ -f "data/glove/glove.840B.300d.txt" ]; then
        echo "✅ GloVe text file found! Starting processing..."

        # Create tmux session for GloVe processing
        tmux new-session -d -s hcnmn-process-glove
        tmux send-keys -t hcnmn-process-glove "cd /home/jiachen/scratch/graph_reasoning/HCNMN" C-m
        tmux send-keys -t hcnmn-process-glove "python scripts/process_glove.py --input data/glove/glove.840B.300d.txt --output data/glove/glove.pt" C-m

        echo "🚀 GloVe processing started in tmux session: hcnmn-process-glove"
        echo "Monitor with: tmux attach-session -t hcnmn-process-glove"
        break
    else
        echo "⏳ Waiting for GloVe extraction... $(date +%H:%M:%S)"
        sleep 30
    fi
done

echo "✨ Auto-processor completed!"