# Materials Science 465: Computational Electron Microscopy
**Northwestern University - Winter Quarter 2026**

## Course Repository Structure

This repository contains all materials for MS 465: Computational Electron Microscopy, organized by weekly topics with progressive complexity from foundational Python skills to advanced machine learning applications in electron microscopy.

## Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NU-MSE-LECTURES/465-WINTER2026.git
   cd 465-WINTER2026
   ```

2. **Set up the environment**:
   ```bash
   conda env create -f environment.yml
   conda activate ms465-2026
   ```

3. **Verify installation**:
   ```bash
   jupyter lab week_01_foundations/exercises/environment_check.ipynb
   ```

## Directory Structure

```
465_Computational_Microscopy_2026/
├── README.md                          # This file
├── COURSE_STRUCTURE.md                # Detailed weekly breakdown
├── environment.yml                    # Conda environment specification
├── requirements.txt                   # Python package requirements
├── .gitignore                        # Git ignore patterns
├── common_utilities/                  # Shared utility functions
├── datasets/                         # Sample datasets and loaders
├── docs/                             # Documentation and guides
├── week_01_foundations/              # Environment setup and GitHub
├── week_02_python_tools/             # py4DSTEM, HyperSpy, ASE
├── week_03_ml_fundamentals/          # ML for EM image analysis
├── week_04_advanced_ml/              # Real-time processing, GANs
├── week_05_multislice_simulations/   # Computational electron scattering
├── week_06_dynamical_diffraction/   # Bloch waves, channeling theory
├── week_07_4dstem_analysis/          # Advanced 4D-STEM workflows
├── week_08_electron_crystallography/ # Automated structure analysis
├── week_09_integration/              # Theory-computation integration
└── week_10_projects/                 # Final project presentations
```

## Weekly Learning Progression

### Weeks 1-2: Foundation and Core Tools
- **Week 1**: Python environment, Git workflows, data management
- **Week 2**: py4DSTEM, HyperSpy, virtual imaging techniques

### Weeks 3-4: Machine Learning Integration
- **Week 3**: CNNs, U-Net, physics-aware ML for EM
- **Week 4**: Real-time processing, generative models, autonomous experiments

### Weeks 5-6: Computational Theory
- **Week 5**: Multislice simulations, GPU acceleration, PRISM algorithm
- **Week 6**: Dynamical diffraction, Bloch waves, two-dimensional channeling

### Weeks 7-8: Advanced Analysis
- **Week 7**: Complete 4D-STEM workflows, ptychography, field mapping
- **Week 8**: Automated crystallography, structure solution, ML integration

### Weeks 9-10: Integration and Projects
- **Week 9**: Case studies, HPC, theory-experiment integration
- **Week 10**: Final project presentations, future directions

## Key Technologies and Libraries

### Core Scientific Computing
- **NumPy/SciPy**: Numerical computing and scientific algorithms
- **Matplotlib**: Data visualization and publication-quality figures
- **Pandas**: Data manipulation and analysis
- **HDF5**: Efficient storage of large EM datasets

### Electron Microscopy Specific
- **py4DSTEM** (≥0.14): 4D-STEM data analysis and virtual imaging
- **HyperSpy** (≥1.7): Multi-dimensional data analysis framework
- **ASE** (≥3.22): Atomic structure manipulation and visualization
- **ncempy**: Reading various EM data formats

### Machine Learning and AI
- **PyTorch/TensorFlow**: Deep learning frameworks
- **scikit-learn**: Traditional machine learning algorithms
- **AtomAI**: Physics-guided ML for atomic-resolution data

### Simulation Software
- **abTEM**: Pure Python multislice simulations
- **Prismatic**: GPU-accelerated STEM simulations
- **MULTEM**: Advanced electron scattering simulations

## Assessment Overview

- **Weekly Programming Assignments (35%)**: 8 assignments building practical skills
- **Major Computational Project (40%)**: Independent research project
- **Project Presentation (15%)**: Conference-style presentation
- **Participation and Peer Review (10%)**: Active engagement and collaboration

## Getting Help

### Office Hours
- **Wednesday 1:00-3:00 PM**: General questions and troubleshooting
- **Friday 10:00-11:30 AM**: Technical support and project guidance

### Online Resources
- **GitHub Discussions**: Course forum for questions and collaboration
- **Documentation**: Comprehensive guides in `docs/` directory
- **Video Tutorials**: Links to software-specific tutorials

### Contact Information
- **Instructor**: Prof. Dr. Roberto dos Reis
- **Email**: roberto.reis@northwestern.edu
- **Office**: Tech AB Wing AG90

## Prerequisites

- Graduate standing in Materials Science, Physics, Chemistry, or related field
- Programming experience in Python
- Undergraduate courses in electron microscopy or materials characterization
- Familiarity with linear algebra and statistical methods

## Course Philosophy

This course embodies McCormick's "whole-brain engineering" approach by integrating:
- **Analytical Thinking**: Rigorous theoretical foundations and mathematical formulations
- **Creative Problem-Solving**: Open-ended projects and innovative applications
- **Collaborative Learning**: Peer review, code sharing, and group discussions
- **Innovation**: Cutting-edge ML and computational methods
- **Real-World Impact**: Industry-relevant skills and career preparation

## Important Dates

- **January 5**: First day of classes
- **January 19**: No classes (Martin Luther King Jr. Day)
- **February 13**: Last day to drop a class
- **March 21**: End of Winter Classes, Final projects due

## Academic Integrity

All work must represent original effort with proper citation. Students may use Large Language Models (LLMs) for assistance but must cite usage and demonstrate full understanding. Collaboration is encouraged with proper attribution.

## Accessibility

Northwestern University is committed to providing equitable access. Students with documented learning differences should contact [AccessibleNU](https://www.northwestern.edu/accessiblenu/) for accommodations.

---

*This course prepares students for the rapidly evolving field of AI/ML-enhanced electron microscopy, providing both theoretical foundations and practical skills essential for modern materials research and industrial applications.*

**Course Website**: [GitHub Repository](https://github.com/NU-MSE-LECTURES/465-WINTER2026)  
**Northwestern University Syllabus Standards**: [Link](https://www.registrar.northwestern.edu/registration-graduation/northwestern-university-syllabus-standards.html)
