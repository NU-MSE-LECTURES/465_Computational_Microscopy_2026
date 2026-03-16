# Week 9: Integration and High-Performance Computing
March 2-6, 2026

## Overview
This week focuses on turning individual analysis steps into reproducible pipelines. The examples emphasize two practical ideas: chaining multiple microscopy operations into a single workflow, and measuring how simple parallelism or parameter sweeps can speed up exploratory analysis.

## Monday: Integrating Simulation, Experiment, and ML
- Designing end-to-end analysis workflows
- Combining multislice output, 4D-STEM data, and ML analysis
- Case studies in energy, semiconductor, and catalyst materials

## Wednesday: High-Performance Computing for Microscopy
- Cluster computing for large-scale datasets
- GPU parallelization and optimization
- Reproducibility and scalability in research workflows

## Assignment 9
Mini-integration project with simulation and ML components

## Code Examples
- **example_01_integrated_analysis_pipeline.py**: generate a synthetic microscopy image, denoise it, segment candidate particles, and summarize measurements in one script
- **example_02_parallel_parameter_sweep.py**: benchmark a simple parameter sweep with serial and parallel execution

## Exercises
- Modify the parameter sweep to test different denoising settings or threshold values
- Compare runtime and output quality when the image size is scaled up by $2\times$ and $4\times$

## Resources
- Pipeline design notes and scaling questions are collected in `resources/resources.md`

## Directory Structure
```
Week_09/
├── README.md
├── lectures/
│   └── README.md
├── code_examples/
│   ├── example_01_integrated_analysis_pipeline.py
│   └── example_02_parallel_parameter_sweep.py
├── exercises/
│   └── README.md
├── assignments/
│   └── assignment_09_integration_pipeline.md
└── resources/
	└── resources.md
```
