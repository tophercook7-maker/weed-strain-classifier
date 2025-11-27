# 🌿 Cannabis Strain Classifier

AI-powered image classifier for identifying top 100 cannabis strains.

## 🚀 Quick Start

### Training the Model

1. **Open `train.ipynb` in Google Colab**
   - Upload the notebook to Colab
   - Ensure GPU runtime is enabled (Runtime → Change runtime type → GPU)
   - Run all cells to train the model

2. **Download trained model**
   - After training completes, download `model.pt` and `class_names.txt`
   - Place them in the root of this repo

### Deploying to Replicate

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Cannabis strain classifier"
   git remote add origin https://github.com/tophercook7-maker/weed-strain-classifier.git
   git push -u origin main
   ```

2. **Deploy on Replicate**
   - Go to https://replicate.com
   - Click "Create Model"
   - Connect your GitHub repo: `tophercook7-maker/weed-strain-classifier`
   - Replicate will automatically detect `replicate.yaml` and deploy

3. **Get Model Version ID**
   - After deployment, copy the version ID (e.g., `username/model-name:abc123`)
   - Add to your app's `.env`: `VITE_REPLICATE_MODEL_VERSION=your-version-id`

## 📁 Project Structure

```
weed-strain-classifier/
├── model.py              # Model architecture (ResNet50)
├── predict.py            # Replicate prediction handler
├── replicate.yaml        # Replicate deployment config
├── train.ipynb          # Colab training notebook
├── model.pt             # Trained model weights (not in repo)
├── class_names.txt      # Strain class names (not in repo)
└── README.md
```

## 🔧 Requirements

- Python 3.10+
- PyTorch 2.0+
- torchvision 0.15+
- PIL/Pillow 10.0+

## 📊 Dataset

Training dataset should be organized as:
```
data/
├── train/
│   ├── blue-dream/
│   ├── og-kush/
│   └── ...
├── val/
└── test/
```

## 🎯 Model Output

The model returns:
```json
{
  "predicted_label": "Blue Dream",
  "confidence": 0.85,
  "top_5": [
    {"label": "Blue Dream", "confidence": 0.85},
    {"label": "White Widow", "confidence": 0.10},
    ...
  ]
}
```

## 📝 Notes

- Model is trained on top 100 cannabis strains
- Images are resized to 224x224 and normalized
- Uses transfer learning from ImageNet-pretrained ResNet50

