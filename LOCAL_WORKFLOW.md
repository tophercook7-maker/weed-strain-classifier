# 🏠 Local Workflow Guide

## What We Can Do Here

✅ **Prepare dataset** - Organize and split images  
✅ **Create scripts** - Automation tools  
✅ **Test integration** - Verify code works  
✅ **Update ScannerPage** - Ready for model deployment  

❌ **Cannot do here:**
- Train model (needs GPU/Colab)
- Deploy to Replicate (needs Replicate.com)
- Run full training (needs time/GPU)

## Quick Start: Prepare Dataset Locally

### Option 1: Use Existing StrainSpotter Datasets

```bash
cd /Users/christophercook/Projects/weed-strain-classifier

# Extract and organize existing datasets
./prepare_from_strainspotter.sh

# Then organize by strain name and split
python prepare_dataset.py --source ./data/raw --output ./data/prepared
```

### Option 2: Use Your Own Images

```bash
# Organize your images like this:
source_images/
├── blue-dream/
│   ├── img1.jpg
│   ├── img2.jpg
│   └── ...
├── og-kush/
└── ...

# Then split into train/val/test
python prepare_dataset.py --source ./source_images --output ./data/prepared
```

### Option 3: Extract from ZIPs

```bash
# Extract all ZIPs first
python prepare_dataset.py --source ./zip_files --output ./data/prepared --extract-zips
```

## Dataset Structure After Preparation

```
data/prepared/
├── train/          # 80% of images
│   ├── blue-dream/
│   ├── og-kush/
│   └── ... (100 strain folders)
├── val/            # 10% of images
│   ├── blue-dream/
│   └── ...
└── test/           # 10% of images
    ├── blue-dream/
    └── ...
```

## Upload to Colab

### Method 1: Google Drive

```bash
# Zip the prepared dataset
cd data
zip -r dataset.zip prepared/

# Upload to Google Drive
# Then in Colab: from google.colab import drive; drive.mount('/content/drive')
# Copy from Drive to /content/data/
```

### Method 2: Direct Upload to Colab

```bash
# Create ZIP
cd data
zip -r ../dataset.zip prepared/

# Upload dataset.zip to Colab Files
# Then in Colab: !unzip dataset.zip
```

### Method 3: GitHub Releases (for large datasets)

```bash
cd data
zip -r ../dataset.zip prepared/

# Push to GitHub release
gh release create v1.0-dataset dataset.zip --title "Training Dataset" --notes "Top 100 strains"
```

## Local Testing (Without Training)

You can test the integration code locally:

```python
# Test predict.py locally (without model.pt)
from predict import Predictor

# This will fail until you have model.pt, but you can test the structure
predictor = Predictor()
```

## Update ScannerPage Locally

The ScannerPage is already set up to use Replicate. Once you have the model version ID:

1. Add to `frontend/.env`:
   ```
   VITE_REPLICATE_MODEL_VERSION=your-version-id-here
   ```

2. Rebuild:
   ```bash
   cd frontend
   npm run build:mobile
   ```

## Complete Workflow

1. ✅ **Here (local):** Prepare dataset
2. 🌐 **Colab:** Train model
3. 🌐 **Replicate:** Deploy model
4. ✅ **Here (local):** Update ScannerPage with version ID
5. ✅ **Here (local):** Test integration

## Next Steps

1. Run `./prepare_from_strainspotter.sh` to extract datasets
2. Organize images by strain name
3. Run `python prepare_dataset.py` to split
4. Upload to Colab and train
5. Deploy to Replicate
6. Get version ID and update ScannerPage

## Tips

- **Dataset size:** Aim for 100-200 images per strain minimum
- **Image quality:** Use clear, high-res images of buds/flowers
- **Variety:** Include different lighting, angles, stages
- **Labels:** Ensure folder names match strain names exactly

