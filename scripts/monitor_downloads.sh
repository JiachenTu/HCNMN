#!/bin/bash

# Monitor HCNMN data downloads progress
# This script shows the status of all running downloads

echo "=== HCNMN Download Monitor ==="
echo "Last checked: $(date)"
echo ""

# Check tmux sessions
echo "🖥️  Active HCNMN TMux Sessions:"
tmux list-sessions 2>/dev/null | grep hcnmn || echo "No HCNMN tmux sessions found"
echo ""

# Check VQA data
echo "📊 VQA v2 Data:"
if [ -f "data/vqa/v2_OpenEnded_mscoco_train2014_questions.json" ]; then
    size=$(du -sh data/vqa/ | cut -f1)
    echo "✅ VQA data complete ($size)"
else
    echo "❌ VQA data missing"
fi
echo ""

# Check Knowledge sources
echo "🧠 Knowledge Sources:"
if [ -f "data/knowledge/conceptnet.db" ]; then
    size=$(du -sh data/knowledge/ | cut -f1)
    echo "✅ Knowledge sources complete ($size)"
elif [ -d "data/knowledge" ] && [ "$(ls -A data/knowledge)" ]; then
    size=$(du -sh data/knowledge/ | cut -f1)
    echo "🔄 Knowledge download in progress ($size)"
else
    echo "⏳ Knowledge download not started"
fi
echo ""

# Check GloVe embeddings
echo "📝 GloVe Embeddings:"
if [ -f "data/glove/glove.840B.300d.txt" ]; then
    txt_size=$(du -sh data/glove/glove.840B.300d.txt | cut -f1)
    echo "✅ GloVe text file extracted ($txt_size)"
    if [ -f "data/glove/glove.pt" ]; then
        pt_size=$(du -sh data/glove/glove.pt | cut -f1)
        echo "✅ GloVe pickle processed ($pt_size)"
    else
        echo "⏳ GloVe pickle processing pending"
    fi
elif [ -f "data/glove/glove.840B.300d.zip" ]; then
    zip_size=$(du -sh data/glove/glove.840B.300d.zip | cut -f1)
    expected_size="2.0G"
    echo "🔄 GloVe download complete, extracting... ($zip_size)"
elif [ -d "data/glove" ] && [ "$(ls -A data/glove)" ]; then
    size=$(du -sh data/glove/ | cut -f1)
    echo "🔄 GloVe download in progress ($size / ~2.0G)"
else
    echo "⏳ GloVe download not started"
fi
echo ""

# Check LXMERT features
echo "👁️  LXMERT Features:"
if [ -d "data/features/trainval_36" ]; then
    size=$(du -sh data/features/trainval_36/ | cut -f1 2>/dev/null || echo "0")
    echo "✅ LXMERT features extracted ($size)"
elif [ -f "data/features/trainval_obj36.zip" ]; then
    zip_size=$(du -sh data/features/trainval_obj36.zip | cut -f1)
    echo "🔄 LXMERT download complete, extracting... ($zip_size)"
elif [ -d "data/features" ] && [ "$(ls -A data/features)" ]; then
    size=$(du -sh data/features/ | cut -f1)
    echo "🔄 LXMERT download in progress ($size / ~8.0G)"
else
    echo "⏳ LXMERT download not started"
fi
echo ""

# Check NLTK
echo "📚 NLTK Data:"
if python -c "import nltk; from nltk.corpus import wordnet; print('✅ NLTK WordNet available')" 2>/dev/null; then
    echo "✅ NLTK setup complete"
else
    echo "❌ NLTK setup incomplete"
fi
echo ""

# Overall progress
echo "📈 Overall Progress:"
total_steps=5
completed=0

[ -f "data/vqa/v2_OpenEnded_mscoco_train2014_questions.json" ] && ((completed++))
[ -f "data/knowledge/conceptnet.db" ] && ((completed++))
[ -f "data/glove/glove.840B.300d.txt" ] && ((completed++))
[ -d "data/features/trainval_36" ] && ((completed++))
python -c "import nltk; from nltk.corpus import wordnet" 2>/dev/null && ((completed++))

progress=$((completed * 100 / total_steps))
echo "Progress: $completed/$total_steps steps complete ($progress%)"

echo ""
echo "🔧 Commands to monitor:"
echo "  tmux attach-session -t hcnmn-knowledge"
echo "  tmux attach-session -t hcnmn-glove"
echo "  tmux attach-session -t hcnmn-lxmert"
echo "  python scripts/verify_data.py"