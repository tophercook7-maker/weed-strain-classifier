# 🚀 Complete Setup Instructions

## Step 1: Create GitHub Repository

### Via GitHub CLI (Recommended)
```bash
cd /Users/christophercook/Projects/weed-strain-classifier
gh repo create weed-strain-classifier --public --source=. --remote=origin --push
```

### Via GitHub Web Interface
1. Go to https://github.com/new
2. Repository name: `weed-strain-classifier`
3. Description: "AI-powered cannabis strain image classifier"
4. Visibility: Public (or Private)
5. **Don't** initialize with README (we already have one)
6. Click "Create repository"

Then push:
```bash
cd /Users/christophercook/Projects/weed-strain-classifier
git remote add origin https://github.com/tophercook7-maker/weed-strain-classifier.git
git branch -M main
git push -u origin main
```

## Step 2: Add Collaborator

After creating the repo:
1. Go to repo settings: https://github.com/tophercook7-maker/weed-strain-classifier/settings/access
2. Click "Collaborators" → "Add people"
3. Search for: `tophercook7-maker`
4. Add as collaborator

## Step 3: Upload Dataset

### If Dataset is < 100MB:
- Create `data/` folder in repo
- Add to git (may take time)

### If Dataset is > 100MB:
Use GitHub Releases:

```bash
# Create a release and upload dataset.zip
gh release create v1.0-dataset dataset.zip --title "Training Dataset v1.0" --notes "Top 100 cannabis strain images"
```

Or use Git LFS:
```bash
git lfs install
git lfs track "*.zip"
git add .gitattributes
git add dataset.zip
git commit -m "Add dataset via Git LFS"
```

### Alternative: External Hosting
- Upload to Google Drive (share publicly)
- Upload to Dropbox (create public link)
- Use S3/Cloud Storage with public URL

## Step 4: Train Model in Colab

1. **Open Google Colab**: https://colab.research.google.com/
2. **Upload `train.ipynb`**:
   - File → Upload notebook
   - Select `train.ipynb` from this repo
3. **Enable GPU**:
   - Runtime → Change runtime type
   - Hardware accelerator: GPU (T4 recommended)
4. **Upload/Download Dataset**:
   - Follow instructions in notebook
   - Extract to `/content/data/`
5. **Run All Cells**:
   - Runtime → Run all
   - Training takes ~2-4 hours on GPU
6. **Download Results**:
   - After training, download:
     - `model.pt` (~200-500MB)
     - `class_names.txt` (~1KB)

## Step 5: Add Model Files to Repo

```bash
cd /Users/christophercook/Projects/weed-strain-classifier

# Copy downloaded files
cp ~/Downloads/model.pt .
cp ~/Downloads/class_names.txt .

# Commit and push
git add model.pt class_names.txt
git commit -m "Add trained model weights and class names"
git push
```

**Note**: If files are too large (>100MB), use Git LFS or GitHub Releases:

```bash
git lfs install
git lfs track "*.pt"
git add .gitattributes model.pt
git commit -m "Add model via Git LFS"
git push
```

## Step 6: Deploy to Replicate

1. **Go to Replicate**: https://replicate.com/
2. **Sign in** with your GitHub account
3. **Create Model**:
   - Click "Create Model" or "New Model"
   - Name: `cannabis-strain-classifier`
   - Visibility: Public or Private
4. **Connect GitHub Repo**:
   - Click "Connect GitHub"
   - Select: `tophercook7-maker/weed-strain-classifier`
   - Replicate will detect `replicate.yaml` automatically
5. **Wait for Build**:
   - Replicate builds Docker image (5-10 minutes)
   - Watch build logs for any errors
6. **Get Version ID**:
   - After build completes, copy the version ID
   - Format: `tophercook7-maker/cannabis-strain-classifier:abc123def456`
   - Or just: `abc123def456` (shorter version)

## Step 7: Update Your App

Add to `frontend/.env`:
```env
VITE_REPLICATE_MODEL_VERSION=tophercook7-maker/cannabis-strain-classifier:abc123def456
```

Or update `ScannerPage.jsx` directly:
```javascript
const modelVersion = import.meta.env.VITE_REPLICATE_MODEL_VERSION || 'tophercook7-maker/cannabis-strain-classifier:abc123def456';
```

## Step 8: Test the Integration

1. **Rebuild frontend**:
   ```bash
   cd frontend
   npm run build:mobile
   ```

2. **Test scanner**:
   - Open app
   - Scan a cannabis image
   - Should get strain prediction
   - Should match against Supabase database

## Troubleshooting

### Model not found error:
- Check version ID is correct
- Ensure model files (`model.pt`, `class_names.txt`) are in repo

### Prediction fails:
- Check Replicate logs: https://replicate.com/tophercook7-maker/cannabis-strain-classifier
- Verify image format (JPG/PNG)
- Check model output format matches `predict.py`

### Low accuracy:
- Train for more epochs
- Add more training data
- Adjust learning rate
- Use data augmentation

## Next Steps

- ✅ Model deployed to Replicate
- ✅ Integrated with ScannerPage
- ✅ Matching against Supabase strains
- 🎉 Full end-to-end scan flow working!

