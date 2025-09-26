"""
Common Utilities Package for MS 465: Computational Electron Microscopy

This package provides shared utilities and functions used throughout the course.
All modules are designed to be imported and used across different weekly assignments
and projects.

Modules:
- data_io: Data loading and saving utilities for various EM formats
- visualization: Plotting and visualization tools for EM data
- ml_tools: Machine learning utilities and model architectures
- simulation: Simulation utilities and helper functions
- performance: Performance optimization and GPU acceleration tools
"""

__version__ = "1.0.0"
__author__ = "MS 465 Course Team"

# Import key functions for easy access
from .data_io.em_formats import load_4dstem_data, save_4dstem_data
from .visualization.em_plotting import plot_4dstem_overview, plot_virtual_images
from .ml_tools.model_architectures import get_unet_model, get_cnn_classifier
from .simulation.multislice_utils import setup_simulation_params
from .performance.gpu_utils import check_gpu_availability

__all__ = [
    'load_4dstem_data',
    'save_4dstem_data', 
    'plot_4dstem_overview',
    'plot_virtual_images',
    'get_unet_model',
    'get_cnn_classifier',
    'setup_simulation_params',
    'check_gpu_availability'
]