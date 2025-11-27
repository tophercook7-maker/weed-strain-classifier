#!/bin/bash
# 🚀 Quick Start Script - One command to prepare everything

echo "🌿 Cannabis Strain Classifier - Quick Start"
echo "============================================"
echo ""

REPO_DIR="/Users/christophercook/Projects/weed-strain-classifier"
DATASETS_DIR="/Users/christophercook/Projects/strainspotter-web/datasets"

cd "$REPO_DIR"

echo "📍 Current location: $(pwd)"
echo ""

# Step 1: Check if train.ipynb exists
echo "1️⃣  Checking training notebook..."
if [ -f "train.ipynb" ]; then
    echo "   ✅ train.ipynb found ($(ls -lh train.ipynb | awk '{print $5}'))"
    echo "   📍 Location: $(pwd)/train.ipynb"
else
    echo "   ❌ train.ipynb not found!"
    exit 1
fi
echo ""

# Step 2: Check datasets
echo "2️⃣  Checking datasets..."
if [ -d "$DATASETS_DIR" ]; then
    DATASET_COUNT=$(ls -d "$DATASETS_DIR"/*/ 2>/dev/null | wc -l)
    echo "   ✅ Found $DATASET_COUNT dataset folders:"
    ls -d "$DATASETS_DIR"/*/ 2>/dev/null | sed 's|.*/|      - |' | sed 's|/$||'
else
    echo "   ⚠️  Datasets directory not found: $DATASETS_DIR"
fi
echo ""

# Step 3: Check if data directory exists
echo "3️⃣  Checking data directory..."
if [ ! -d "data" ]; then
    echo "   📁 Creating data directory..."
    mkdir -p data/{raw,prepared}
    echo "   ✅ Created data/ directory"
else
    echo "   ✅ data/ directory exists"
    if [ -d "data/raw" ]; then
        RAW_COUNT=$(find data/raw -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" \) 2>/dev/null | wc -l)
        echo "      Found $RAW_COUNT images in data/raw/"
    fi
    if [ -d "data/prepared" ]; then
        PREPARED_COUNT=$(find data/prepared -type d -mindepth 2 2>/dev/null | wc -l)
        if [ "$PREPARED_COUNT" -gt 0 ]; then
            echo "      Found $PREPARED_COUNT strain folders in data/prepared/"
        fi
    fi
fi
echo ""

# Step 4: Summary
echo "📋 NEXT STEPS:"
echo "=============="
echo ""
echo "To prepare dataset:"
echo "  ./prepare_from_strainspotter.sh"
echo ""
echo "To organize and split:"
echo "  python prepare_dataset.py --source ./data/raw --output ./data/prepared"
echo ""
echo "To train in Colab:"
echo "  1. Go to: https://colab.research.google.com/"
echo "  2. Upload: $(pwd)/train.ipynb"
echo "  3. Enable GPU runtime"
echo "  4. Upload dataset"
echo "  5. Run all cells"
echo ""
echo "📖 Full guide: GET_STARTED.md"
echo ""
echo "✅ Everything is ready to go!"

