# Week 2: Python Tools for EM Data Analysis
**January 12-16, 2026**

## Learning Objectives
By the end of this week, students will be able to:
- Use py4DSTEM for 4D-STEM data loading, processing, and virtual imaging
- Apply HyperSpy framework for multi-dimensional EM data analysis
- Integrate ASE (Atomic Simulation Environment) for atomic structure manipulation
- Understand data format standards and interoperability between EM tools
- Implement virtual detector methods and basic strain mapping techniques

## Topics Covered

### Tuesday: Core Python Libraries - py4DSTEM and HyperSpy
- py4DSTEM architecture and capabilities (Version 0.14+)
- 4D-STEM data structures and virtual imaging
- HyperSpy framework and multi-dimensional analysis
- Integration with ASE for atomic structure manipulation

### Thursday: Advanced EM Analysis Tools
- LiberTEM for high-throughput distributed processing
- pyXEM for diffraction microscopy
- AtomAI framework for physics-guided analysis
- Data format standards and interoperability

## Materials

### Lectures
- `lecture_01_py4dstem_fundamentals.ipynb` - py4DSTEM architecture and basic operations
- `lecture_02_hyperspy_integration.ipynb` - HyperSpy and advanced EM tools

### Assignment
- `assignment_02_4dstem_virtual_imaging.ipynb` - 4D STEM virtual imaging with py4DSTEM

### Exercises
- `py4dstem_basics.ipynb` - Basic py4DSTEM operations and data structures
- `hyperspy_tutorial.ipynb` - HyperSpy framework exploration  
- `ase_structures.ipynb` - Atomic structure manipulation with ASE

### Code Examples
- `virtual_detectors.py` - Virtual detector implementations
- `data_format_conversion.py` - Converting between EM data formats
- `strain_mapping_basics.py` - Basic strain mapping techniques

## Key Software Focus

### py4DSTEM (≥0.14)
```python
import py4DSTEM

# Core functionality covered:
# - DataCube loading and creation
# - Virtual imaging and detector methods
# - Bragg disk detection and strain mapping
# - Phase reconstruction and ptychography basics
```

### HyperSpy (≥1.7)
```python
import hyperspy.api as hs

# Core functionality covered:
# - Multi-dimensional data handling
# - Interactive data exploration
# - Signal processing and analysis
# - Integration with other EM tools
```

### ASE (≥3.22)
```python
from ase import Atoms
from ase.io import read, write
from ase.visualize import view

# Core functionality covered:
# - Atomic structure creation and manipulation
# - File I/O for various structure formats
# - Crystal structure analysis
# - Integration with simulation codes
```

## Assignment 2: 4D STEM Virtual Imaging with py4DSTEM
**Due: Friday, January 16, 2026 at 11:59 PM**

### Objectives
1. Load and analyze real 4D-STEM datasets using py4DSTEM
2. Implement various virtual detector geometries
3. Perform basic strain mapping and orientation analysis
4. Compare different analysis approaches and their trade-offs

### Deliverables
1. **Data Loading and Exploration**: Load provided 4D-STEM datasets and explore their properties
2. **Virtual Imaging**: Implement bright field, dark field, and custom virtual detectors
3. **Strain Analysis**: Perform basic strain mapping using Bragg disk detection
4. **Method Comparison**: Compare results from different virtual detector configurations

### Evaluation Criteria
- **Technical Implementation (30%)**: Correct use of py4DSTEM functions and methods
- **Analysis Quality (30%)**: Meaningful interpretation of virtual imaging results
- **Code Documentation (20%)**: Clear explanations and well-commented code
- **Scientific Insight (20%)**: Understanding of physical principles behind the analysis

## Key Concepts and Methods

### 4D-STEM Data Structure
- **Scan Dimensions**: Real-space scanning positions (Rx, Ry)
- **Detector Dimensions**: Reciprocal-space diffraction patterns (Qx, Qy)
- **Data Organization**: 4D array indexing and memory considerations
- **Metadata Management**: Experimental parameters and calibration

### Virtual Imaging Techniques
- **Bright Field (BF)**: Central beam intensity mapping
- **Dark Field (DF)**: Scattered beam intensity mapping
- **Annular Dark Field (ADF)**: Ring-shaped detector geometries
- **Custom Detectors**: Application-specific detector shapes

### Strain Mapping Fundamentals
- **Bragg Disk Detection**: Automated peak finding in diffraction patterns
- **Lattice Parameter Measurement**: Quantitative strain analysis
- **Orientation Mapping**: Crystal orientation determination
- **Geometric Phase Analysis**: Phase-based strain measurement

## Advanced Topics Introduced

### Data Preprocessing
- **Bad Pixel Correction**: Identifying and correcting detector artifacts
- **Background Subtraction**: Removing systematic backgrounds
- **Calibration**: Converting pixels to reciprocal space units
- **Drift Correction**: Compensating for sample or beam drift

### Performance Optimization
- **Memory Management**: Handling large 4D datasets efficiently
- **Parallel Processing**: Utilizing multiple CPU cores
- **Lazy Loading**: Processing data without loading entire datasets
- **GPU Acceleration**: Using CUDA for intensive computations

### Data Export and Integration
- **HDF5 Export**: Saving processed results in standardized formats
- **Visualization**: Creating publication-quality figures
- **Integration with Other Tools**: Connecting py4DSTEM with external software
- **Reproducible Workflows**: Version control and parameter tracking

## Common Issues and Solutions

### Memory Management
**Issue**: 4D datasets too large for available RAM
**Solution**: Use lazy loading and chunked processing
```python
import py4DSTEM
datacube = py4DSTEM.DataCube.from_file('large_dataset.h5', lazy=True)
result = datacube.get_virtual_image_lazy(detector, chunk_size=64)
```

### Calibration Problems
**Issue**: Incorrect reciprocal space calibration
**Solution**: Use known diffraction spots for calibration
```python
# Calibrate using known diffraction spot positions
datacube.calibrate_pixel_size_from_diffraction_spots(known_spots)
```

### Performance Issues
**Issue**: Slow processing of large datasets
**Solution**: Optimize chunking and use parallel processing
```python
# Enable parallel processing
import multiprocessing
py4DSTEM.set_ncpu(multiprocessing.cpu_count())
```

## Best Practices Established

### Code Organization
- Use py4DSTEM's object-oriented approach consistently
- Separate data loading, processing, and visualization steps
- Implement parameter validation and error checking
- Document analysis parameters and assumptions

### Data Management
- Preserve original data and track all processing steps
- Use meaningful variable names reflecting physical quantities
- Implement consistent units and calibration throughout
- Save intermediate results for complex workflows

### Visualization Standards
- Use appropriate colormaps for different data types
- Include proper axis labels and units
- Add scalebars and calibration information
- Create both overview and detailed views

### Scientific Rigor
- Validate results against known standards when possible
- Quantify uncertainties and error propagation
- Compare multiple analysis methods
- Document limitations and assumptions

## Resources

### Required Reading
- py4DSTEM documentation: "Getting Started Guide"
- HyperSpy User Guide: Chapters 1-3
- Course notes: "4D-STEM Analysis Fundamentals"

### Supplementary Materials
- py4DSTEM tutorials and example notebooks
- HyperSpy example datasets and tutorials
- Recent papers on 4D-STEM analysis techniques
- Video tutorials from software development teams

### Useful Links
- [py4DSTEM Documentation](https://py4dstem.readthedocs.io/)
- [HyperSpy Documentation](https://hyperspy.org/)
- [ASE Documentation](https://wiki.fysik.dtu.dk/ase/)
- [4D-STEM Community Forum](https://groups.google.com/g/py4dstem)

## Preparation for Week 3
To prepare for next week's focus on machine learning:
1. Review basic machine learning concepts (supervised vs unsupervised learning)
2. Ensure scikit-learn and deep learning frameworks are installed
3. Practice image preprocessing techniques
4. Review linear algebra and statistics fundamentals

## Advanced Extensions (Optional)
For students who complete the core assignment early:
- Implement custom virtual detector shapes for specific applications
- Explore ptychographic reconstruction methods in py4DSTEM
- Compare py4DSTEM results with commercial EM software
- Develop automated workflows for batch processing

The skills developed this week form the foundation for all subsequent computational EM analysis in the course. Take time to thoroughly understand the data structures and analysis principles.