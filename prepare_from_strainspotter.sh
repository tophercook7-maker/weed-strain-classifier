#!/bin/bash
# 🚀 Quick script to prepare dataset from existing StrainSpotter datasets

STRAINSPOTTER_DATASETS="/Users/christophercook/Projects/strainspotter-web/datasets"
OUTPUT_DIR="./data"

echo "🌿 Preparing cannabis strain dataset..."
echo ""
echo "📁 Source: $STRAINSPOTTER_DATASETS"
echo "📁 Output: $OUTPUT_DIR"
echo ""

# Check if source exists
if [ ! -d "$STRAINSPOTTER_DATASETS" ]; then
    echo "❌ Source directory not found: $STRAINSPOTTER_DATASETS"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR/raw"

echo "📦 Extracting ZIP files..."
cd "$STRAINSPOTTER_DATASETS/Weed-non-weed-dataset"

# Extract all ZIP files
for zip in *.zip; do
    if [ -f "$zip" ]; then
        echo "   Extracting $zip..."
        unzip -q -o "$zip" -d "$OUTPUT_DIR/raw" 2>/dev/null || echo "   ⚠️  Failed to extract $zip"
    fi
done

echo ""
echo "✅ Extraction complete!"
echo ""
echo "📊 Next steps:"
echo "   1. Organize images by strain name into folders"
echo "   2. Run: python prepare_dataset.py --source ./data/raw --output ./data/prepared"
echo "   3. Or manually organize and split into train/val/test"
echo ""
echo "💡 Tip: Use the DeepWeeds dataset for labeled examples:"
echo "   $STRAINSPOTTER_DATASETS/DeepWeeds/"

