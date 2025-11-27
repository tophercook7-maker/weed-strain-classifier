"""
Cannabis Strain Classifier Model
Fine-tuned ResNet50 for top 100 cannabis strain classification
"""
import torch
import torch.nn as nn
import torchvision.models as models
from torchvision import transforms

class CannabisStrainClassifier(nn.Module):
    def __init__(self, num_classes=100):
        super(CannabisStrainClassifier, self).__init__()
        # Use pretrained ResNet50 as backbone
        self.backbone = models.resnet50(pretrained=True)
        
        # Replace the final fully connected layer
        num_features = self.backbone.fc.in_features
        self.backbone.fc = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(num_features, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, num_classes)
        )
    
    def forward(self, x):
        return self.backbone(x)

# Image preprocessing transforms (match training)
def get_transforms():
    return transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                           std=[0.229, 0.224, 0.225])
    ])

