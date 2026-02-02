# Week 04 Assignments

## Assignment 04: Neural Network for Atomic-Level Pattern Recognition

### Overview
This assignment demonstrates the development of a convolutional neural network (CNN) for classifying atomic-level patterns in microscopy images. Students will:
- Generate synthetic atomic pattern datasets
- Build and train a CNN classifier
- Evaluate model performance
- Create comprehensive visualization summaries

### Files
- `assignment_04_combined.ipynb` - Main assignment notebook with complete workflow

### Key Deliverable: Four-Panel Summary Figure

The main deliverable is a comprehensive four-panel summary figure (`figures/assignment_04_summary_figure.png`) that includes:

1. **Panel 1: Sample Images from Each Class**
   - Shows representative examples of each atomic pattern type:
     - Square lattice
     - Hexagonal lattice
     - Random defects
     - Diamond lattice

2. **Panel 2: Training History**
   - Training and validation loss curves
   - Training and validation accuracy curves
   - Helps assess model convergence and potential overfitting

3. **Panel 3: Confusion Matrix**
   - Detailed breakdown of model predictions vs. true labels
   - Shows which classes are most easily confused
   - Helps identify specific areas for improvement

4. **Panel 4: Sample Predictions**
   - Random selection of test images with predictions
   - Shows true label, predicted label, and confidence score
   - Color-coded (green=correct, red=incorrect)
   - Provides qualitative assessment of model performance

### Running the Assignment

#### Using Google Colab
Click the "Open in Colab" badge at the top of the notebook and run all cells.

#### Running Locally
```bash
jupyter notebook assignment_04_combined.ipynb
```

Or execute with:
```bash
jupyter nbconvert --to notebook --execute assignment_04_combined.ipynb
```

### Dependencies
- TensorFlow/Keras
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy

### Output
The notebook will generate:
- A trained CNN model for atomic pattern recognition
- Performance metrics (accuracy, confusion matrix, classification report)
- A four-panel summary figure saved to `figures/assignment_04_summary_figure.png`

### Learning Objectives
1. Understand CNN architecture design for microscopy data
2. Learn data augmentation and synthetic data generation techniques
3. Apply proper train/validation/test splitting strategies
4. Create publication-quality visualization summaries
5. Interpret model performance through multiple evaluation metrics

### Notes
- The synthetic dataset is designed to be computationally lightweight for educational purposes
- The model architecture can be adapted for real microscopy data
- The four-panel summary format is a standard approach for reporting ML results in scientific publications
