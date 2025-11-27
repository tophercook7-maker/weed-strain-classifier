# 📍 Where Everything Is - Complete Guide

## 🎯 Quick Reference

### Training Notebook
```
/Users/christophercook/Projects/weed-strain-classifier/train.ipynb
```
✅ **Ready to upload to Google Colab**

### Datasets
```
/Users/christophercook/Projects/strainspotter-web/datasets/
├── Weed-non-weed-dataset/
│   ├── gplant1.zip
│   ├── gplant2.zip
│   ├── plant1.zip
│   └── ... (10 ZIP files total)
└── DeepWeeds/
    ├── labels/
    └── ... (Research dataset)
```

### Repository
```
/Users/christophercook/Projects/weed-strain-classifier/
├── train.ipynb              ← Upload this to Colab
├── model.py                 ← Model architecture
├── predict.py               ← Replicate handler
├── replicate.yaml           ← Deployment config
├── prepare_dataset.py       ← Dataset preparation tool
├── GET_STARTED.md           ← Complete guide (READ THIS!)
└── data/                    ← Will contain prepared dataset
```

---

## 🚀 What To Do Right Now

### 1. Check Everything is Ready
```bash
cd /Users/christophercook/Projects/weed-strain-classifier
./QUICK_START.sh
```

### 2. Prepare Dataset (If Needed)
```bash
# Extract from ZIP files
./prepare_from_strainspotter.sh

# Then organize images by strain name and split
python prepare_dataset.py --source ./data/raw --output ./data/prepared
```

### 3. Train in Google Colab

**Open:** https://colab.research.google.com/

**Upload:** `/Users/christophercook/Projects/weed-strain-classifier/train.ipynb`

**Enable GPU:**
- Runtime → Change runtime type → GPU

**Upload Dataset:**
- Option A: Upload ZIP to Colab Files
- Option B: Upload to Google Drive and mount

**Run Training:**
- Runtime → Run all
- Wait 2-4 hours
- Download `model.pt` and `class_names.txt`

### 4. Deploy to Replicate

1. Go to: https://replicate.com/
2. Create Model → Connect GitHub repo
3. Wait for build
4. Copy Model Version ID

### 5. Update Your App

Add to `frontend/.env`:
```
VITE_REPLICATE_MODEL_VERSION=your-version-id-here
```

---

## 📖 Complete Guides

1. **GET_STARTED.md** - Step-by-step from start to finish
2. **LOCAL_WORKFLOW.md** - What you can do locally
3. **SETUP_INSTRUCTIONS.md** - Deployment instructions

---

## ⚡ Quick Commands

```bash
# Check status
cd /Users/christophercook/Projects/weed-strain-classifier
./QUICK_START.sh

# Extract datasets
./prepare_from_strainspotter.sh

# Prepare dataset
python prepare_dataset.py --source ./data/raw --output ./data/prepared

# Push updates
ALLOW_PUSH=1 git push
```

---

## 🔗 Important Links

- **GitHub Repo:** https://github.com/tophercook7-maker/weed-strain-classifier
- **Google Colab:** https://colab.research.google.com/
- **Replicate:** https://replicate.com/
- **Your App:** Frontend at `/Users/christophercook/Projects/strainspotter/frontend/`

---

## ✅ Checklist

- [x] train.ipynb created
- [x] Repository setup
- [x] Datasets located
- [ ] Dataset extracted and organized
- [ ] Model trained in Colab
- [ ] Deployed to Replicate
- [ ] Model version ID added to app

---

**Next Step:** Open `GET_STARTED.md` for the complete walkthrough!

