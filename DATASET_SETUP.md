# 📦 Dataset Setup Guide

## Dataset Requirements

The model is trained on **top 100 cannabis strains**. Each strain should have:
- Minimum: 50-100 images per strain
- Recommended: 200+ images per strain for better accuracy
- Total dataset: ~10,000-20,000 images

## Expected Structure

```
data/
├── train/           # 80% of data
│   ├── blue-dream/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │   └── ...
│   ├── og-kush/
│   ├── white-widow/
│   └── ... (100 strain folders)
│
├── val/             # 10% of data
│   ├── blue-dream/
│   ├── og-kush/
│   └── ...
│
└── test/            # 10% of data
    ├── blue-dream/
    ├── og-kush/
    └── ...
```

## Dataset Sources

### Option 1: Scrape from Cannabis Websites
- Leafly (with permission)
- Wikileaf
- AllBud
- Weedmaps

### Option 2: Use Existing Datasets
- Search Kaggle for "cannabis strain" datasets
- Check GitHub for cannabis image datasets
- Use the dataset from `strainspotter-web/datasets/Weed-non-weed-dataset`

### Option 3: Manual Collection
- Take photos of different strains
- Use stock images (ensure licensing)
- User-contributed photos (with consent)

## Upload Options

### For Google Colab Training:

**Option A: Google Drive**
1. Upload dataset ZIP to Google Drive
2. Mount Drive in Colab: `drive.mount('/content/drive')`
3. Extract to `/content/data/`

**Option B: Direct Upload**
1. Zip your dataset: `zip -r dataset.zip data/`
2. Upload to Colab files
3. Extract: `!unzip dataset.zip`

**Option C: GitHub Releases** (for large datasets)
1. Create a release on GitHub
2. Upload dataset.zip as release asset
3. Download in Colab: `!wget https://github.com/username/repo/releases/download/v1.0/dataset.zip`

## Dataset Preparation Script

If you have images organized differently, use this to restructure:

```python
import os
import shutil
from pathlib import Path
import random

def prepare_dataset(source_dir, output_dir, train_ratio=0.8, val_ratio=0.1):
    """Split dataset into train/val/test"""
    strains = os.listdir(source_dir)
    
    for strain in strains:
        strain_dir = Path(source_dir) / strain
        images = list(strain_dir.glob('*.jpg')) + list(strain_dir.glob('*.png'))
        
        random.shuffle(images)
        
        n_train = int(len(images) * train_ratio)
        n_val = int(len(images) * val_ratio)
        
        train_images = images[:n_train]
        val_images = images[n_train:n_train+n_val]
        test_images = images[n_train+n_val:]
        
        # Create directories
        (Path(output_dir) / 'train' / strain).mkdir(parents=True, exist_ok=True)
        (Path(output_dir) / 'val' / strain).mkdir(parents=True, exist_ok=True)
        (Path(output_dir) / 'test' / strain).mkdir(parents=True, exist_ok=True)
        
        # Copy images
        for img in train_images:
            shutil.copy(img, Path(output_dir) / 'train' / strain / img.name)
        for img in val_images:
            shutil.copy(img, Path(output_dir) / 'val' / strain / img.name)
        for img in test_images:
            shutil.copy(img, Path(output_dir) / 'test' / strain / img.name)
        
        print(f"{strain}: {len(train_images)} train, {len(val_images)} val, {len(test_images)} test")
```

## Top 100 Strains List

Here's a suggested list of top 100 strains to train on:

1. Blue Dream
2. OG Kush
3. White Widow
4. Granddaddy Purple
5. Sour Diesel
6. Northern Lights
7. Girl Scout Cookies
8. Pineapple Express
9. Jack Herer
10. AK-47
... (add 90 more)

See `top_100_strains.txt` for the complete list.

