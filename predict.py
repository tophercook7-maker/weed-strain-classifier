"""
Replicate prediction handler for cannabis strain classifier
"""
import os
import torch
from PIL import Image
import io
import base64
from model import CannabisStrainClassifier, get_transforms

class Predictor:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = None
        self.class_names = None
        self.transform = get_transforms()
        
    def setup(self):
        """Load model and class names"""
        model_path = os.path.join(os.path.dirname(__file__), 'model.pt')
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        
        # Load class names from file (created during training)
        class_names_path = os.path.join(os.path.dirname(__file__), 'class_names.txt')
        if os.path.exists(class_names_path):
            with open(class_names_path, 'r') as f:
                self.class_names = [line.strip() for line in f.readlines()]
        else:
            # Fallback: generate placeholder class names
            self.class_names = [f"Strain_{i}" for i in range(100)]
        
        # Initialize model
        num_classes = len(self.class_names)
        self.model = CannabisStrainClassifier(num_classes=num_classes)
        
        # Load trained weights
        checkpoint = torch.load(model_path, map_location=self.device)
        if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
            self.model.load_state_dict(checkpoint['model_state_dict'])
        else:
            self.model.load_state_dict(checkpoint)
        
        self.model.to(self.device)
        self.model.eval()
        
    def predict(self, image):
        """
        Predict strain from image
        
        Args:
            image: Can be:
                - URL string
                - Base64 encoded image string (data:image/...;base64,...)
                - PIL Image object
                - File path string
        
        Returns:
            dict with:
                - predicted_label: str (strain name)
                - confidence: float (0-1)
                - top_5: list of {label, confidence} dicts
        """
        if self.model is None:
            self.setup()
        
        # Handle different input types
        if isinstance(image, str):
            if image.startswith('http://') or image.startswith('https://'):
                # URL
                import requests
                img = Image.open(requests.get(image, stream=True).raw).convert('RGB')
            elif image.startswith('data:image'):
                # Base64
                header, encoded = image.split(',', 1)
                img_data = base64.b64decode(encoded)
                img = Image.open(io.BytesIO(img_data)).convert('RGB')
            else:
                # File path
                img = Image.open(image).convert('RGB')
        elif hasattr(image, 'save'):  # PIL Image
            img = image.convert('RGB')
        else:
            raise ValueError("Unsupported image format")
        
        # Preprocess
        img_tensor = self.transform(img).unsqueeze(0).to(self.device)
        
        # Predict
        with torch.no_grad():
            outputs = self.model(img_tensor)
            probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
            confidence, predicted_idx = torch.max(probabilities, 0)
            
            # Get top 5 predictions
            top5_probs, top5_indices = torch.topk(probabilities, min(5, len(self.class_names)))
            top5 = [
                {
                    "label": self.class_names[idx.item()],
                    "confidence": prob.item()
                }
                for prob, idx in zip(top5_probs, top5_indices)
            ]
        
        predicted_label = self.class_names[predicted_idx.item()]
        confidence_score = confidence.item()
        
        return {
            "predicted_label": predicted_label,
            "confidence": confidence_score,
            "top_5": top5
        }

