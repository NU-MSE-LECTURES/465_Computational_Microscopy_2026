# Week 8: Electron Crystallography and AI-assisted Structure Analysis
February 23-27, 2026

## Overview
This week connects diffraction-based structure analysis with lightweight machine learning workflows. The emphasis is on extracting physically meaningful features from diffraction data, organizing those features into interpretable groups, and using simple classifiers to support phase or defect identification.

## Monday: Fundamentals of Electron Crystallography
- Bulk structure solution and refinement
- Charge density analysis
- Limitations of dynamical vs. kinematic approaches

## Wednesday: AI for Automated Structure Analysis
- Machine learning for diffraction pattern classification
- Feature extraction and clustering with pyXEM and AtomAI
- Automated phase and defect identification

## Assignment 8
AI-based crystallographic classification

## Code Examples
- **example_01_diffraction_feature_clustering.py**: build radial-profile features from synthetic diffraction patterns, reduce dimensionality with PCA, and cluster the patterns with k-means
- **example_02_diffraction_nearest_template.py**: compare diffraction patterns against reference templates using normalized feature distances

## Exercises
- Inspect how ring radius, spot anisotropy, and noise level affect the extracted feature vectors
- Compare unsupervised grouping with simple template matching on the same synthetic dataset

## Resources
- Short notes on recommended workflows for diffraction feature engineering and interpretable ML baselines are included in `resources/resources.md`

## Directory Structure
```
Week_08/
├── README.md
├── lectures/
│   └── README.md
├── code_examples/
│   ├── example_01_diffraction_feature_clustering.py
│   └── example_02_diffraction_nearest_template.py
├── exercises/
│   └── README.md
├── assignments/
│   └── assignment_08_crystal_classification.md
└── resources/
	└── resources.md
```
