# 🚀 Quick GitHub Setup Guide

## Option 1: Create Repo via GitHub CLI (Fastest)

If you have GitHub CLI installed:

```bash
cd /Users/christophercook/Projects/weed-strain-classifier
gh repo create tophercook7-maker/weed-strain-classifier --public --source=. --remote=origin --push
```

This will:
- ✅ Create the repo on GitHub
- ✅ Set the remote
- ✅ Push all code
- ✅ Make it public

## Option 2: Manual GitHub Creation

### Step 1: Create Repository on GitHub

1. Go to: **https://github.com/new**
2. Repository name: `weed-strain-classifier`
3. Description: `AI-powered cannabis strain image classifier`
4. Visibility: **Public** (or Private)
5. **Important:** Do NOT check "Initialize with README" (we already have one)
6. Click **"Create repository"**

### Step 2: Push Your Code

Run the push script:

```bash
cd /Users/christophercook/Projects/weed-strain-classifier
./PUSH_TO_GITHUB.sh
```

Or manually:

```bash
cd /Users/christophercook/Projects/weed-strain-classifier
git remote add origin https://github.com/tophercook7-maker/weed-strain-classifier.git
git branch -M main
git push -u origin main
```

### Step 3: Add Collaborator

1. Go to: **https://github.com/tophercook7-maker/weed-strain-classifier/settings/access**
2. Click **"Collaborators"** → **"Add people"**
3. Search for: `tophercook7-maker`
4. Add as collaborator with **Write** access

## ✅ After Setup

Your repo will be live at:
**https://github.com/tophercook7-maker/weed-strain-classifier**

## 📋 Files in Repo

- ✅ `model.py` - Model architecture
- ✅ `predict.py` - Replicate prediction handler
- ✅ `replicate.yaml` - Deployment config
- ✅ `train.ipynb` - Colab training notebook
- ✅ `README.md` - Documentation
- ✅ `SETUP_INSTRUCTIONS.md` - Full setup guide
- ✅ `DATASET_SETUP.md` - Dataset instructions

## 🎯 Next Steps

1. ✅ Push to GitHub (you're here)
2. 📦 Upload dataset (see `DATASET_SETUP.md`)
3. 🧪 Train model in Colab (see `SETUP_INSTRUCTIONS.md`)
4. 🚀 Deploy to Replicate
5. 🔗 Get model version ID
6. ✅ Update `ScannerPage.jsx` with version ID

## 🔗 Useful Links

- **Repository:** https://github.com/tophercook7-maker/weed-strain-classifier
- **Settings:** https://github.com/tophercook7-maker/weed-strain-classifier/settings
- **Releases:** https://github.com/tophercook7-maker/weed-strain-classifier/releases (for dataset upload)

