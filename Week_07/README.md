# Week 7: 4D-STEM and Quantitative Analysis
February 16-20, 2026

## Overview
This week focuses on advanced 4D-STEM analysis techniques for quantitative measurements. Students will learn to implement center-of-mass (COM) calculations, differential phase contrast (DPC) imaging, strain/electric field mapping, and ptychographic phase reconstruction. The week covers both fundamental theory and practical implementation using py4DSTEM.

## Monday: Processing and Analysis of 4D-STEM
- py4DSTEM workflow and data structure
- Center-of-mass (COM) and differential phase contrast (DPC)
- Quantitative strain and electric field mapping

### Lectures
- **lecture_7.1_py4dstem_workflow.ipynb**: Complete py4DSTEM pipeline and data handling
- **lecture_7.2_com_dpc_analysis.ipynb**: COM calculations and DPC imaging theory
- **lecture_7.3_strain_field_mapping.ipynb**: Quantitative strain and electric field measurements

## Wednesday: Advanced 4D-STEM Applications
- Ptychography and phase reconstruction
- Integration of 4D-STEM and spectroscopy data
- Machine learning-assisted pattern analysis

### Lectures
- **lecture_7.4_ptycho.ipynb**: Ptychographic phase reconstruction principles
- **lecture_7.4a_ptycho_ePIE.ipynb**: Extended Ptychographic Iterative Engine (ePIE) implementation

## Assignment 7: DPC and Ptychography
- **assignment_07_dpc_ptychography.ipynb**: Full 4D-STEM analysis workflow
- Topics: COM computation, DPC potential reconstruction, ptychographic phase retrieval
- Dataset: MoS2 4D-STEM data

## Code Examples
Week 7 includes three practical examples for 4D-STEM analysis:

- **example_01_com_calculation.ipynb**: Center-of-mass (COM) computation
  - Implementing COM algorithms
  - Beam shift measurements
  - Vector field visualization

- **example_02_dpc_potential_mapping.ipynb**: Differential phase contrast imaging
  - DPC phase reconstruction
  - Electric potential mapping
  - Integration techniques and boundary conditions

- **example_03_dpc_transfer_function.ipynb**: DPC transfer function analysis
  - Transfer function theory and implementation
  - Frequency domain analysis
  - Contrast optimization

## Data
- **MoS2_4D_data_step2x_crop_3x3uc.mat**: 4D-STEM dataset of MoS2 monolayer
- **helper/**: Utility functions for data processing

## Directory Structure
```
Week_07/
├── README.md                              # This file
├── lectures/                              # Lecture materials and notebooks
│   ├── lecture_7.1_py4dstem_workflow.ipynb
│   ├── lecture_7.2_com_dpc_analysis.ipynb
│   ├── lecture_7.3_strain_field_mapping.ipynb
│   ├── lecture_7.4_ptycho.ipynb
│   ├── lecture_7.4a_ptycho_ePIE.ipynb
│   ├── MoS2_4D_data_step2x_crop_3x3uc.mat
│   └── helper/                            # Helper functions
├── code_examples/                         # Example code and scripts
│   ├── example_01_com_calculation.ipynb
│   ├── example_02_dpc_potential_mapping.ipynb
│   └── example_03_dpc_transfer_function.ipynb
└── assignments/                           # Assignment descriptions and templates
    └── assignment_07_dpc_ptychography.ipynb
```
