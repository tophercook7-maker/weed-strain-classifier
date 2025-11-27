# 🚀 Get Started - Complete Guide

## 📍 Where Everything Is

### 1. Training Notebook
**Location:** `/Users/christophercook/Projects/weed-strain-classifier/train.ipynb`

✅ **Ready to use in Google Colab**

### 2. Datasets Available

**Location:** `/Users/christophercook/Projects/strainspotter-web/datasets/`

You have:
- ✅ **Weed-non-weed-dataset/** - Contains multiple ZIP files with plant images
- ✅ **DeepWeeds/** - Research dataset with labels

### 3. Repository
**Location:** `/Users/christophercook/Projects/weed-strain-classifier/`
**GitHub:** https://github.com/tophercook7-maker/weed-strain-classifier

---

## 🎯 Step-by-Step: Get Started

### STEP 1: Prepare Dataset (Local - 10 minutes)

```bash
cd /Users/christophercook/Projects/weed-strain-classifier

# Extract from existing datasets
./prepare_from_strainspotter.sh
```

This will:
- Extract images from ZIP files
- Create `./data/raw/` folder
- Prepare for organization

**Note:** The extracted images may not be organized by strain yet. You'll need to:
- Organize images into folders by strain name
- Example: `data/raw/blue-dream/`, `data/raw/og-kush/`, etc.

### STEP 2: Organize Images by Strain

You have two options:

#### Option A: Manual Organization
1. Create folders for each strain in `data/raw/`
2. Move/copy images to appropriate strain folders
3. Name folders after strains: `blue-dream`, `og-kush`, etc.

#### Option B: Use Existing Dataset Structure
If your ZIP files are already organized, just extract and rename folders to match strain names.

### STEP 3: Split into Train/Val/Test

```bash
cd /Users/christophercook/Projects/weed-strain-classifier

# Split organized images
python prepare_dataset.py --source ./data/raw --output ./data/prepared
```

This creates:
```
data/prepared/
├── train/     # 80% of images
├── val/       # 10% of images
└── test/      # 10% of images
```

### STEP 4: Upload to Google Colab

#### Option A: Google Drive (Recommended)
```bash
# Zip the prepared dataset
cd data
zip -r ../dataset.zip prepared/

# Upload dataset.zip to Google Drive
# Then in Colab, mount Drive and extract
```

#### Option B: Direct Upload to Colab
```bash
# Create ZIP
cd data
zip -r ../dataset.zip prepared/

# Upload dataset.zip to Colab Files (Files tab in Colab)
```

### STEP 5: Train in Colab

1. **Open Google Colab**: https://colab.research.google.com/

2. **Upload train.ipynb**:
   - File → Upload notebook
   - Select: `/Users/christophercook/Projects/weed-strain-classifier/train.ipynb`

3. **Enable GPU**:
   - Runtime → Change runtime type
   - Hardware accelerator: **GPU (T4 recommended)**

4. **Upload Dataset**:
   - If using Drive: Mount Drive and extract
   - If uploaded directly: Extract in Colab

5. **Run All Cells**:
   - Runtime → Run all
   - Training takes 2-4 hours on GPU

6. **Download Results**:
   - After training completes, download:
     - `model.pt` (~200-500MB)
     - `class_names.txt` (~1KB)

### STEP 6: Add Model to Repository

```bash
cd /Users/christophercook/Projects/weed-strain-classifier

# Copy downloaded files
cp ~/Downloads/model.pt .
cp ~/Downloads/class_names.txt .

# Commit and push
git add model.pt class_names.txt
git commit -m "Add trained model"
ALLOW_PUSH=1 git push
```

**Note:** If files are >100MB, use Git LFS:
```bash
git lfs install
git lfs track "*.pt"
git add .gitattributes model.pt
git commit -m "Add model via Git LFS"
git push
```

### STEP 7: Deploy to Replicate

1. Go to: https://replicate.com/
2. Sign in with GitHub
3. Click **"Create Model"**
4. Name: `cannabis-strain-classifier`
5. Connect GitHub repo: `tophercook7-maker/weed-strain-classifier`
6. Replicate auto-detects `replicate.yaml`
7. Wait for build (5-10 minutes)
8. Copy **Model Version ID** (e.g., `abc123def456`)

### STEP 8: Update Your App

```bash
cd /Users/christophercook/Projects/strainspotter/frontend

# Add to .env file
echo "VITE_REPLICATE_MODEL_VERSION=tophercook7-maker/cannabis-strain-classifier:VERSION_ID" >> .env

# Rebuild
npm run build:mobile
```

---

## 🆘 Quick Help

### "I don't have images organized by strain"

You can:
1. Use the DeepWeeds dataset which has labels
2. Start with a smaller subset (10-20 strains)
3. Scrape images from cannabis websites
4. Use stock images (check licensing)

### "Dataset is too large"

Use Git LFS or GitHub Releases:
```bash
git lfs install
git lfs track "*.pt"
gh release create v1.0-dataset dataset.zip
```

### "Training fails in Colab"

- Check GPU is enabled
- Verify dataset structure matches expected format
- Check notebook output for errors
- Reduce batch size if out of memory

---

## 📋 Checklist

- [ ] Dataset extracted (`./prepare_from_strainspotter.sh`)
- [ ] Images organized by strain name
- [ ] Split into train/val/test (`prepare_dataset.py`)
- [ ] Uploaded to Colab/Drive
- [ ] Trained model in Colab
- [ ] Downloaded `model.pt` and `class_names.txt`
- [ ] Added to GitHub repo
- [ ] Deployed to Replicate
- [ ] Got model version ID
- [ ] Updated `ScannerPage.jsx` with version ID

---

## 🔗 Useful Links

- **Repository:** https://github.com/tophercook7-maker/weed-strain-classifier
- **Colab:** https://colab.research.google.com/
- **Replicate:** https://replicate.com/
- **Local Workflow:** See `LOCAL_WORKFLOW.md`

---

## 💡 Tips

1. **Start Small**: Test with 10-20 strains first
2. **Use GPU**: Training without GPU takes days
3. **Save Often**: Colab sessions can timeout
4. **Check Dataset**: Verify images are correctly labeled
5. **Monitor Training**: Watch for overfitting (val accuracy plateauing)

