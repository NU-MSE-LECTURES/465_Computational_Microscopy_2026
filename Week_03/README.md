# Week 3: Image Processing and Classical Analysis Methods
January 19-23, 2026

## Overview
This week covers fundamental image processing techniques for microscopy data analysis, including spatial and frequency-domain filtering, contrast enhancement, and classical segmentation methods. Students will learn to apply these techniques to real microscopy datasets and understand when to use each approach.

Students will implement classical computer vision pipelines including noise reduction, contrast enhancement, morphological segmentation, and particle quantification. These skills form the foundation for comparing classical approaches with modern machine learning and deep learning methods in Week 4.

## Monday: Image Processing Foundations
- Image filtering and noise reduction techniques
- Real-space and FFT-based contrast enhancement
- Histogram equalization and normalization

## Wednesday: Classical Image and Diffraction Analysis
- Morphological operations and segmentation methods
- Template matching and particle identification
- Diffraction pattern analysis using pyXEM

## Code Examples
Week 3 includes five progressively advanced image processing examples:

- **example_01_image_filtering.ipynb**: Real-data filtering comparison
  - Loading STEM-HAADF datasets (Au FCC, GaAs IDB-1)
  - Gaussian vs Median filtering with parameter exploration
  - Quantitative comparison and visualization
  - Robust EMD file loading with fallback strategies

- **example_02_cameraman_filtering.ipynb**: Controlled noise experiments
  - Synthetic noise generation (Gaussian, salt-and-pepper)
  - Filter performance benchmarking with MSE metrics
  - ROI-based analysis and filter selection guidance
  - Clean vs noisy image comparisons

- **example_03_fft_filtering.ipynb**: Frequency-domain filtering
  - FFT computation and visualization (magnitude, phase)
  - Radial profile analysis
  - Low-pass, high-pass, and band-pass filtering
  - Frequency interpretation and practical applications

- **example_04_histogram_equalization.ipynb**: Contrast enhancement
  - Global histogram equalization
  - Adaptive equalization (CLAHE)
  - Parameter sweep for clip_limit optimization
  - ROI-based comparisons and best practices

- **example_05_segmentation.ipynb**: Segmentation techniques
  - Global thresholding (Otsu, Yen)
  - Local adaptive thresholding (Sauvola)
  - Watershed segmentation with distance transform
  - Template matching via normalized cross-correlation
  - Morphological clean-up and object counting

## Assignment 3
Classical image segmentation pipeline

## Directory Structure
```
Week_03/
├── README.md                              # This file
├── lectures/                              # Lecture materials and notebooks
├── code_examples/                         # Example code and scripts
│   ├── example_01_image_filtering.ipynb
│   ├── example_02_cameraman_filtering.ipynb
│   ├── example_03_fft_filtering.ipynb
│   ├── example_04_histogram_equalization.ipynb
│   └── example_05_segmentation.ipynb
├── exercises/                             # Practice problems
├── assignments/                           # Assignment descriptions and templates
└── resources/                             # Additional reading and references
```

## Key Concepts
- **Spatial Filtering**: Gaussian (noise reduction), Median (salt-and-pepper noise)
- **Frequency-Domain Filtering**: FFT-based low/high/band-pass for structured noise removal
- **Contrast Enhancement**: Histogram equalization (global and adaptive/CLAHE)
- **Thresholding**: Global (Otsu, Yen) and local adaptive (Sauvola) methods
- **Watershed Segmentation**: Distance transform-based object separation
- **Template Matching**: Normalized cross-correlation for pattern localization
- **Morphological Operations**: Small object removal, hole filling, labeling

## Learning Objectives
By the end of this week, students should be able to:
1. Apply appropriate spatial filters (Gaussian, Median) to reduce noise in microscopy images
2. Perform FFT-based filtering to remove periodic artifacts or enhance specific frequencies
3. Use histogram equalization techniques to improve image contrast
4. Implement global and local thresholding methods for binary segmentation
5. Separate touching objects using watershed segmentation
6. Locate known patterns in images using template matching
7. Evaluate filter performance using quantitative metrics (MSE, SNR)
8. Choose appropriate preprocessing methods based on image characteristics and noise types
