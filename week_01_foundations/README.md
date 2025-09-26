# Week 1: Foundations and Environment Setup
**January 5-9, 2026**

## Learning Objectives
By the end of this week, students will be able to:
- Set up a complete Python environment for electron microscopy data analysis
- Use Git and GitHub for version control and collaborative development
- Understand modern data management practices for large EM datasets
- Create reproducible Jupyter notebooks with proper documentation
- Navigate the Python ecosystem for scientific computing and EM analysis

## Topics Covered

### Monday: Course Overview and Modern EM Data Analysis Landscape
- Evolution of electron microscopy data analysis 2023-2025
- Introduction to 4D STEM and pixelated detectors
- Overview of Python ecosystem for EM data analysis
- Course project preview and GitHub repository setup

### Wednesday: Computational Environment and Data Management
- Python environment setup (conda, virtual environments)
- GitHub Classroom and version control workflows
- Data management for large EM datasets (HDF5, compression, metadata)
- Introduction to Jupyter notebooks and reproducible research

## Materials

### Lectures
- `lecture_01_course_overview.ipynb` - Course introduction and modern EM landscape
- `lecture_02_environment_setup.ipynb` - Computational environment and data management

### Assignment
- `assignment_01_environment_setup.ipynb` - Environment setup and first GitHub commit

### Exercises
- `environment_check.ipynb` - Verify installation and environment
- `git_basics.ipynb` - Git and GitHub workflow practice
- `data_management_demo.ipynb` - HDF5 and metadata handling

### Code Examples
- `python_em_ecosystem.py` - Overview of Python packages for EM
- `git_workflow_example.py` - Example Git workflow for collaborative coding
- `hdf5_examples.py` - HDF5 data management examples

## Key Software and Tools

### Required Installations
1. **Anaconda/Miniconda**: Package and environment management
2. **Git**: Version control system
3. **GitHub Account**: Code repository and collaboration
4. **VS Code or PyCharm**: Integrated development environment
5. **JupyterLab**: Interactive development and analysis

### Python Packages (Week 1 Focus)
```python
# Environment management
conda>=23.0
mamba>=1.4  # Optional but recommended for faster installs

# Core scientific computing
numpy>=1.24
scipy>=1.10
matplotlib>=3.6
pandas>=2.0
h5py>=3.8
zarr>=2.14

# Jupyter ecosystem
jupyterlab>=4.0
jupyter-lsp
jupyterlab-git
ipywidgets
```

## Assignment 1: Environment Setup and First GitHub Commit
**Due: Friday, January 9, 2026 at 11:59 PM**

### Objectives
1. Set up complete Python environment for the course
2. Create and configure GitHub repository
3. Demonstrate basic data loading and visualization
4. Practice version control workflow

### Deliverables
1. **Environment Verification**: Complete `environment_check.ipynb` showing all packages installed correctly
2. **GitHub Repository**: Personal course repository with proper structure
3. **Data Loading Notebook**: Load and visualize sample EM data
4. **Version Control**: At least 5 meaningful commits documenting your setup process

### Evaluation Criteria
- **Environment Setup (25%)**: All required packages installed and functional
- **GitHub Integration (25%)**: Repository properly configured with meaningful commits
- **Code Quality (25%)**: Clean, documented code following Python best practices
- **Data Handling (25%)**: Successful loading and visualization of EM data

## Resources

### Required Reading
- Course notes: "Modern Python Environment for Scientific Computing"
- GitHub documentation: "Getting Started with GitHub"
- HDF5 documentation: "Introduction to HDF5 for Scientific Data"

### Supplementary Materials
- Python Data Science Handbook: Chapters 1-2
- Effective Python: Items 1-10 (Environment and best practices)
- Git Pro: Chapters 1-3 (Git fundamentals)

### Useful Links
- [Anaconda Installation Guide](https://docs.anaconda.com/anaconda/install/)
- [GitHub Desktop](https://desktop.github.com/) (Optional GUI for Git)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Conda Forge](https://conda-forge.org/)

## Common Issues and Solutions

### Environment Problems
**Issue**: Package installation failures
**Solution**: Use mamba instead of conda for faster and more reliable installs
```bash
conda install mamba -c conda-forge
mamba install package_name
```

**Issue**: Jupyter kernel not found
**Solution**: Install nb_conda_kernels and register environment
```bash
conda install nb_conda_kernels
python -m ipykernel install --user --name ms465-2026 --display-name "MS465-2026"
```

### Git/GitHub Issues
**Issue**: Authentication problems with GitHub
**Solution**: Use personal access tokens or SSH keys
```bash
git config --global credential.helper store
# Or set up SSH keys following GitHub documentation
```

**Issue**: Large files causing push failures
**Solution**: Use Git LFS for large data files
```bash
git lfs install
git lfs track "*.h5"
git add .gitattributes
```

## Best Practices Established This Week

### Code Organization
- Use meaningful directory and file names
- Include docstrings for all functions
- Follow PEP 8 style guidelines
- Separate data, code, and documentation

### Version Control
- Make frequent, small commits
- Write descriptive commit messages
- Use branches for experimental features
- Keep repositories clean with .gitignore

### Data Management
- Use HDF5 for large numerical datasets
- Include metadata with all data files
- Implement data validation and error checking
- Document data provenance and processing steps

### Documentation
- Include README files in all directories
- Use markdown for documentation
- Add inline comments for complex code
- Maintain change logs for major updates

## Preparation for Week 2
To prepare for next week's focus on py4DSTEM and EM-specific tools:
1. Ensure your environment is fully functional
2. Review linear algebra and Fourier transforms
3. Read py4DSTEM introduction documentation (provided in resources)
4. Practice basic image processing with scikit-image

## Office Hours and Support
- **Wednesday 1:00-3:00 PM**: General office hours
- **Friday 10:00-11:30 AM**: Technical support and troubleshooting
- **GitHub Discussions**: Online forum for course-related questions
- **Email**: roberto.reis@northwestern.edu for urgent issues

Remember: The goal this week is to establish a solid foundation for the rest of the course. Take time to ensure everything is working correctly before moving forward.