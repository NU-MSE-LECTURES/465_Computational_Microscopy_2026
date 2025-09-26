# Materials Science 465: Computational Electron Microscopy
## Week-by-Week Code Organization Structure

### Course Overview
This repository contains all code implementations, assignments, and project materials for MS 465: Computational Electron Microscopy (Winter Quarter 2026). The structure is organized by weekly topics to facilitate progressive learning and easy navigation.

## Directory Structure

```
465_Computational_Microscopy_2026/
├── README.md                          # Course overview and setup instructions
├── COURSE_STRUCTURE.md                # This file - detailed weekly breakdown
├── environment.yml                    # Conda environment specification
├── requirements.txt                   # Python package requirements
├── .gitignore                        # Git ignore patterns
├── common_utilities/                  # Shared utility functions and classes
├── datasets/                         # Sample datasets and data loading utilities
├── docs/                             # Documentation, references, and guides
└── week_XX_topic/                    # Weekly directories (detailed below)
```

## Weekly Structure

Each week follows a consistent structure:
```
week_XX_topic/
├── README.md                         # Week overview and learning objectives
├── lectures/                         # Lecture notebooks and materials
│   ├── lecture_01_topic.ipynb
│   └── lecture_02_topic.ipynb
├── assignments/                      # Weekly assignments
│   ├── assignment_XX.ipynb
│   ├── solution_XX.ipynb           # Available after due date
│   └── data/                       # Assignment-specific data
├── exercises/                        # In-class exercises and practice problems
├── code_examples/                    # Standalone code examples
└── resources/                        # Additional materials, papers, links
```

---

## Week 1: Foundations and Environment Setup
**Focus**: Course overview, Python environment, GitHub workflows, data management

### Key Components:
- **Environment Setup**: Conda environments, package management
- **GitHub Workflows**: Version control, GitHub Classroom integration
- **Data Management**: HDF5 formats, compression, metadata handling
- **Jupyter Best Practices**: Reproducible research, documentation

### Assignment 1: Environment Setup and First GitHub Commit
- Environment configuration verification
- GitHub repository initialization
- First Jupyter notebook with basic EM data loading

---

## Week 2: Python Tools for EM Data Analysis
**Focus**: py4DSTEM, HyperSpy, ASE integration

### Key Components:
- **py4DSTEM Framework**: Data structures, virtual imaging, basic analysis
- **HyperSpy Integration**: Multi-dimensional data handling
- **ASE Structures**: Atomic structure manipulation and visualization
- **Data Interoperability**: Format conversions, metadata preservation

### Assignment 2: 4D STEM Virtual Imaging
- py4DSTEM data loading and visualization
- Virtual detector implementation
- Basic strain mapping and orientation analysis

---

## Week 3: Machine Learning Fundamentals for EM
**Focus**: Deep learning architectures, image segmentation, pattern recognition

### Key Components:
- **CNN Architectures**: Implementation from scratch and with PyTorch/TensorFlow
- **U-Net Segmentation**: Semantic segmentation for EM images
- **Physics-Aware ML**: Incorporating domain knowledge into models
- **Data Augmentation**: EM-specific augmentation strategies

### Assignment 3: CNN-Based Image Segmentation
- Implement U-Net for defect detection
- Training pipeline with validation
- Performance evaluation and visualization

---

## Week 4: Advanced ML Applications
**Focus**: Real-time processing, generative models, autonomous experiments

### Key Components:
- **Real-Time Processing**: Stream processing, optimization strategies
- **Active Learning**: Autonomous experiment design
- **Generative Models**: VAEs and GANs for EM data
- **Transfer Learning**: Leveraging pre-trained models

### Assignment 4: Real-Time Analysis Pipeline
- Live data processing simulation
- Performance optimization and profiling
- Integration with microscope control systems (simulated)

---

## Week 5: Multislice Simulations and Theory
**Focus**: Computational electron scattering, GPU acceleration, modern implementations

### Key Components:
- **Multislice Theory**: Mathematical formulation and implementation
- **GPU Acceleration**: CUDA/OpenCL implementations
- **Software Comparison**: Prismatic, MULTEM, abTEM benchmarking
- **Validation Methods**: Convergence testing, experimental comparison

### Assignment 5: Multislice Simulation Project
- Implement basic multislice algorithm
- GPU acceleration (if available)
- Comparison with commercial software

---

## Week 6: Dynamical Diffraction and Two-Dimensional Channeling
**Focus**: Bloch wave theory, dynamical diffraction, theoretical foundations

### Key Components:
- **Bloch Wave Theory**: Eigenvalue solutions, zone axis calculations
- **Two-Dimensional Channeling**: Computational implementation
- **Convergence Analysis**: Beam parameters, thickness effects
- **ML Integration**: Neural networks for diffraction pattern analysis

### Assignment 6: Dynamical Diffraction Simulation
- Bloch wave implementation
- Comparison with multislice methods
- ML-enhanced pattern recognition

---

## Week 7: Data Processing and Analysis Pipelines
**Focus**: 4D-STEM workflows, automated analysis, field mapping

### Key Components:
- **Virtual Detectors**: Advanced detector geometries
- **Phase Retrieval**: Ptychography implementations
- **Field Mapping**: Electric and magnetic field quantification
- **Pipeline Automation**: Batch processing, parallelization

### Assignment 7: Complete 4D STEM Analysis Workflow
- End-to-end processing pipeline
- Multiple analysis techniques integration
- Performance optimization and scaling

---

## Week 8: Electron Crystallography and Automated Structure Analysis
**Focus**: Structure solution, charge density analysis, automated crystallography

### Key Components:
- **Structure Solution**: Automated algorithms, space group determination
- **Charge Density**: Refinement methods, visualization
- **High-Throughput**: Batch crystallographic analysis
- **ML Integration**: Structure prediction and classification

### Assignment 8: Automated Crystallographic Analysis
- Structure solution pipeline
- Charge density refinement
- Machine learning classification system

---

## Week 9: Integration of Theory and Computation
**Focus**: Case studies, industrial applications, performance optimization

### Key Components:
- **Case Studies**: Real-world materials problems
- **Performance Optimization**: HPC strategies, memory management
- **Theory-Experiment Integration**: Validation workflows
- **Industrial Applications**: Semiconductor, catalyst, energy materials

### Assignment 9: Integration Project
- Combined theoretical and computational approach
- Real materials problem solving
- Performance benchmarking

---

## Week 10: Project Presentations and Future Directions
**Focus**: Final projects, peer review, career development

### Key Components:
- **Project Presentations**: Conference-style presentations
- **Peer Review**: Scientific discussion and feedback
- **Future Trends**: Emerging technologies and methods
- **Career Development**: Industry and academic pathways

### Final Projects Due
- Complete computational implementation
- Technical report and documentation
- Professional presentation

---

## Common Utilities Structure

### `common_utilities/`
```
common_utilities/
├── __init__.py
├── data_io/                          # Data loading and saving utilities
│   ├── __init__.py
│   ├── em_formats.py                # EM-specific format handlers
│   ├── hdf5_utils.py               # HDF5 optimization utilities
│   └── metadata_tools.py           # Metadata management
├── visualization/                    # Plotting and visualization tools
│   ├── __init__.py
│   ├── em_plotting.py              # EM-specific plotting functions
│   ├── interactive_plots.py        # Interactive visualization tools
│   └── animation_tools.py          # Animation utilities
├── ml_tools/                        # Machine learning utilities
│   ├── __init__.py
│   ├── model_architectures.py      # Common ML architectures
│   ├── training_utils.py           # Training loop utilities
│   ├── evaluation_metrics.py       # EM-specific metrics
│   └── data_augmentation.py        # Augmentation strategies
├── simulation/                      # Simulation utilities
│   ├── __init__.py
│   ├── multislice_utils.py         # Multislice common functions
│   ├── structure_tools.py          # Atomic structure utilities
│   └── scattering_factors.py       # Scattering factor calculations
└── performance/                     # Performance optimization tools
    ├── __init__.py
    ├── gpu_utils.py                # GPU acceleration utilities
    ├── parallel_processing.py      # Parallelization tools
    └── memory_management.py        # Memory optimization
```

## Dataset Organization

### `datasets/`
```
datasets/
├── README.md                        # Dataset descriptions and usage
├── sample_data/                     # Small sample datasets for testing
├── simulated_data/                  # Simulated datasets for validation
├── experimental_data/               # Real experimental datasets
├── benchmarks/                      # Benchmark datasets for comparisons
└── data_loaders/                    # Dataset-specific loading utilities
    ├── __init__.py
    ├── py4dstem_loaders.py
    ├── hyperspy_loaders.py
    └── custom_formats.py
```

## Assessment Integration

### Programming Assignments (35%)
Each assignment is designed to build upon previous weeks:
1. **Progressive Complexity**: From basic environment setup to advanced integration
2. **Code Quality**: Emphasis on documentation, testing, and reproducibility
3. **Version Control**: All assignments tracked through GitHub
4. **Peer Review**: Code review processes integrated into workflow

### Major Project (40%)
- **Repository Structure**: Professional-level code organization
- **Documentation**: Comprehensive README, API documentation
- **Testing**: Unit tests and validation procedures
- **Reproducibility**: Environment specifications and data management

## Best Practices

### Code Quality Standards
- **PEP 8 Compliance**: Python style guide adherence
- **Documentation**: Docstrings, inline comments, README files
- **Testing**: Unit tests, integration tests, validation procedures
- **Version Control**: Meaningful commit messages, branching strategies

### Reproducible Research
- **Environment Management**: Pinned package versions, environment files
- **Data Provenance**: Clear data lineage and metadata
- **Computational Reproducibility**: Seed management, deterministic algorithms
- **Documentation**: Clear instructions for reproduction

### Collaborative Development
- **GitHub Workflows**: Issues, pull requests, project boards
- **Code Review**: Structured feedback and improvement processes
- **Knowledge Sharing**: Wiki pages, discussion forums
- **Open Science**: Public repositories, open data practices

## Getting Started

1. **Clone Repository**: `git clone https://github.com/NU-MSE-LECTURES/465-WINTER2026.git`
2. **Setup Environment**: `conda env create -f environment.yml`
3. **Activate Environment**: `conda activate ms465-2026`
4. **Verify Installation**: Run `week_01_foundations/exercises/environment_check.ipynb`
5. **Start Learning**: Begin with Week 1 materials

## Support and Resources

- **Office Hours**: Wednesday 1:00-3:00 PM, Friday 10:00-11:30 AM
- **Discussion Forum**: GitHub Discussions for course-related questions
- **Documentation**: Comprehensive guides in `docs/` directory
- **Help Sessions**: Weekly help sessions for technical difficulties

## Course Philosophy Integration

This structure embodies McCormick's "whole-brain engineering" approach by:
- **Analytical Thinking**: Rigorous theoretical implementations
- **Creative Problem-Solving**: Open-ended project work
- **Collaborative Learning**: Peer review and group discussions
- **Innovation**: Cutting-edge ML and computational methods
- **Real-World Application**: Industry-relevant case studies and projects