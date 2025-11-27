#!/usr/bin/env python3
"""
Dataset Preparation Script
Organizes cannabis strain images into train/val/test splits for training.

Usage:
    python prepare_dataset.py --source /path/to/raw/images --output /path/to/prepared/data
"""

import os
import shutil
import random
from pathlib import Path
import argparse
from collections import defaultdict

def prepare_dataset(source_dir, output_dir, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1):
    """
    Split dataset into train/val/test directories
    
    Expected source structure:
        source_dir/
            strain-name-1/
                img1.jpg
                img2.jpg
            strain-name-2/
                ...
    
    Creates:
        output_dir/
            train/
                strain-name-1/
                ...
            val/
                ...
            test/
                ...
    """
    source = Path(source_dir)
    output = Path(output_dir)
    
    if not source.exists():
        print(f"❌ Source directory not found: {source_dir}")
        return False
    
    # Get all strain folders
    strain_dirs = [d for d in source.iterdir() if d.is_dir()]
    
    if not strain_dirs:
        print(f"❌ No strain directories found in {source_dir}")
        print(f"   Expected structure: {source_dir}/strain-name/images...")
        return False
    
    print(f"📊 Found {len(strain_dirs)} strain classes")
    print(f"   Splitting: {train_ratio*100:.0f}% train, {val_ratio*100:.0f}% val, {test_ratio*100:.0f}% test")
    print()
    
    total_images = 0
    for strain_dir in sorted(strain_dirs):
        strain_name = strain_dir.name
        
        # Get all images
        image_extensions = {'.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG'}
        images = [f for f in strain_dir.iterdir() 
                 if f.is_file() and f.suffix in image_extensions]
        
        if not images:
            print(f"⚠️  Skipping {strain_name}: No images found")
            continue
        
        # Shuffle and split
        random.shuffle(images)
        n = len(images)
        n_train = int(n * train_ratio)
        n_val = int(n * val_ratio)
        n_test = n - n_train - n_val
        
        train_images = images[:n_train]
        val_images = images[n_train:n_train+n_val]
        test_images = images[n_train+n_val:]
        
        # Create directories
        for split in ['train', 'val', 'test']:
            (output / split / strain_name).mkdir(parents=True, exist_ok=True)
        
        # Copy images
        for img in train_images:
            shutil.copy2(img, output / 'train' / strain_name / img.name)
        for img in val_images:
            shutil.copy2(img, output / 'val' / strain_name / img.name)
        for img in test_images:
            shutil.copy2(img, output / 'test' / strain_name / img.name)
        
        total_images += n
        print(f"  ✅ {strain_name}: {n_train} train, {n_val} val, {n_test} test ({n} total)")
    
    print()
    print(f"✅ Dataset preparation complete!")
    print(f"   Total images: {total_images}")
    print(f"   Output directory: {output_dir}")
    print()
    print(f"📦 Next steps:")
    print(f"   1. Zip the dataset: cd {output_dir} && zip -r dataset.zip train val test")
    print(f"   2. Upload to Google Drive or Colab")
    print(f"   3. Use in train.ipynb")
    
    return True

def extract_from_zips(zip_dir, output_dir):
    """Extract images from ZIP files organized by strain"""
    zip_path = Path(zip_dir)
    output = Path(output_dir)
    
    zip_files = list(zip_path.glob('*.zip'))
    if not zip_files:
        print(f"❌ No ZIP files found in {zip_dir}")
        return False
    
    print(f"📦 Found {len(zip_files)} ZIP files")
    
    import zipfile
    for zip_file in zip_files:
        print(f"   Extracting {zip_file.name}...")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(output / zip_file.stem)
    
    print(f"✅ Extraction complete!")
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prepare cannabis strain dataset for training')
    parser.add_argument('--source', required=True, help='Source directory with strain folders')
    parser.add_argument('--output', required=True, help='Output directory for train/val/test')
    parser.add_argument('--train-ratio', type=float, default=0.8, help='Training set ratio (default: 0.8)')
    parser.add_argument('--val-ratio', type=float, default=0.1, help='Validation set ratio (default: 0.1)')
    parser.add_argument('--test-ratio', type=float, default=0.1, help='Test set ratio (default: 0.1)')
    parser.add_argument('--extract-zips', action='store_true', help='Extract from ZIP files first')
    parser.add_argument('--seed', type=int, default=42, help='Random seed for reproducibility')
    
    args = parser.parse_args()
    
    # Validate ratios
    if abs(args.train_ratio + args.val_ratio + args.test_ratio - 1.0) > 0.01:
        print("❌ Ratios must sum to 1.0")
        exit(1)
    
    # Set random seed
    random.seed(args.seed)
    
    # Extract ZIPs if needed
    if args.extract_zips:
        temp_dir = Path(args.source) / '_extracted'
        extract_from_zips(args.source, temp_dir)
        args.source = str(temp_dir)
    
    # Prepare dataset
    success = prepare_dataset(
        args.source,
        args.output,
        args.train_ratio,
        args.val_ratio,
        args.test_ratio
    )
    
    if not success:
        exit(1)

