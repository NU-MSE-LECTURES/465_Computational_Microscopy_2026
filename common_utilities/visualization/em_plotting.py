"""
Visualization utilities for electron microscopy data
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LogNorm
from typing import Tuple, Optional, Dict, Any, List
import warnings

def plot_4dstem_overview(data: np.ndarray, 
                        figsize: Tuple[int, int] = (16, 12),
                        positions: Optional[List[Tuple[int, int]]] = None,
                        save_path: Optional[str] = None) -> plt.Figure:
    """
    Create comprehensive overview plot of 4D-STEM dataset
    
    Parameters:
    -----------
    data : np.ndarray
        4D-STEM data array (scan_x, scan_y, detector_x, detector_y)
    figsize : tuple
        Figure size in inches
    positions : list of tuples, optional
        Specific scan positions to highlight
    save_path : str, optional
        Path to save the figure
        
    Returns:
    --------
    matplotlib.Figure
    """
    
    if data.ndim != 4:
        raise ValueError(f"Expected 4D data, got {data.ndim}D")
    
    scan_x, scan_y, det_x, det_y = data.shape
    
    # Create figure with subplots
    fig = plt.figure(figsize=figsize)
    
    # Virtual bright field (central detector)
    ax1 = plt.subplot(2, 4, 1)
    center_x, center_y = det_x // 2, det_y // 2
    radius = min(det_x, det_y) // 8
    
    y, x = np.ogrid[:det_x, :det_y]
    bf_mask = (x - center_x)**2 + (y - center_y)**2 <= radius**2
    vbf = np.sum(data * bf_mask, axis=(2, 3))
    
    im1 = ax1.imshow(vbf, cmap='gray', origin='lower')
    ax1.set_title('Virtual Bright Field')
    ax1.set_xlabel('Scan X')
    ax1.set_ylabel('Scan Y')
    plt.colorbar(im1, ax=ax1, fraction=0.046)
    
    # Virtual dark field (annular detector)
    ax2 = plt.subplot(2, 4, 2)
    inner_r = radius * 1.5
    outer_r = radius * 3
    
    df_mask = ((x - center_x)**2 + (y - center_y)**2 >= inner_r**2) & \
              ((x - center_x)**2 + (y - center_y)**2 <= outer_r**2)
    vdf = np.sum(data * df_mask, axis=(2, 3))
    
    im2 = ax2.imshow(vdf, cmap='hot', origin='lower')
    ax2.set_title('Virtual Dark Field')
    ax2.set_xlabel('Scan X')
    ax2.set_ylabel('Scan Y')
    plt.colorbar(im2, ax=ax2, fraction=0.046)
    
    # Average diffraction pattern
    ax3 = plt.subplot(2, 4, 3)
    avg_dp = np.mean(data, axis=(0, 1))
    
    im3 = ax3.imshow(avg_dp, cmap='viridis', origin='lower',
                     norm=LogNorm(vmin=max(1, np.percentile(avg_dp, 1)),
                                  vmax=np.percentile(avg_dp, 99)))
    ax3.set_title('Average Diffraction Pattern')
    ax3.set_xlabel('Detector X')
    ax3.set_ylabel('Detector Y')
    
    # Add detector regions
    bf_circle = plt.Circle((center_x, center_y), radius, fill=False, color='red', linewidth=2)
    df_inner = plt.Circle((center_x, center_y), inner_r, fill=False, color='yellow', linewidth=2)
    df_outer = plt.Circle((center_x, center_y), outer_r, fill=False, color='yellow', linewidth=2)
    ax3.add_patch(bf_circle)
    ax3.add_patch(df_inner)
    ax3.add_patch(df_outer)
    
    plt.colorbar(im3, ax=ax3, fraction=0.046)
    
    # Virtual detector diagram
    ax4 = plt.subplot(2, 4, 4)
    detector_map = np.zeros((det_x, det_y))
    detector_map[bf_mask] = 1
    detector_map[df_mask] = 2
    
    im4 = ax4.imshow(detector_map, cmap='Set1', origin='lower')
    ax4.set_title('Virtual Detector Map')
    ax4.set_xlabel('Detector X')
    ax4.set_ylabel('Detector Y')
    
    # Selected diffraction patterns
    if positions is None:
        positions = [(scan_x//4, scan_y//4), 
                    (scan_x//2, scan_y//2), 
                    (3*scan_x//4, 3*scan_y//4)]
    
    for i, (px, py) in enumerate(positions[:4]):
        if px < scan_x and py < scan_y:
            ax = plt.subplot(2, 4, 5 + i)
            dp = data[px, py]
            
            im = ax.imshow(dp, cmap='plasma', origin='lower',
                          norm=LogNorm(vmin=max(1, np.percentile(dp, 1)),
                                       vmax=np.percentile(dp, 99.5)))
            ax.set_title(f'DP at ({px}, {py})')
            ax.set_xlabel('Detector X')
            ax.set_ylabel('Detector Y')
            
            if i == 0:
                plt.colorbar(im, ax=ax, fraction=0.046)
            
            # Mark position on VBF
            ax1.plot(py, px, 'ro', markersize=8, markerfacecolor='none', markeredgewidth=2)
            ax1.text(py+1, px+1, f'{i+1}', color='red', fontweight='bold')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig

def plot_virtual_images(vbf: np.ndarray, vdf: np.ndarray,
                       titles: Optional[Tuple[str, str]] = None,
                       cmaps: Tuple[str, str] = ('gray', 'hot'),
                       figsize: Tuple[int, int] = (12, 5),
                       save_path: Optional[str] = None) -> plt.Figure:
    """
    Plot virtual bright field and dark field images side by side
    
    Parameters:
    -----------
    vbf : np.ndarray
        Virtual bright field image
    vdf : np.ndarray
        Virtual dark field image
    titles : tuple, optional
        Custom titles for the images
    cmaps : tuple
        Colormaps for BF and DF images
    figsize : tuple
        Figure size
    save_path : str, optional
        Path to save figure
        
    Returns:
    --------
    matplotlib.Figure
    """
    
    if titles is None:
        titles = ('Virtual Bright Field', 'Virtual Dark Field')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    
    # Virtual bright field
    im1 = ax1.imshow(vbf, cmap=cmaps[0], origin='lower')
    ax1.set_title(titles[0])
    ax1.set_xlabel('Scan X')
    ax1.set_ylabel('Scan Y')
    plt.colorbar(im1, ax=ax1, fraction=0.046)
    
    # Virtual dark field
    im2 = ax2.imshow(vdf, cmap=cmaps[1], origin='lower')
    ax2.set_title(titles[1])
    ax2.set_xlabel('Scan X')
    ax2.set_ylabel('Scan Y')
    plt.colorbar(im2, ax=ax2, fraction=0.046)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig

def plot_diffraction_pattern(dp: np.ndarray,
                           title: str = 'Diffraction Pattern',
                           cmap: str = 'viridis',
                           log_scale: bool = True,
                           percentile_range: Tuple[float, float] = (1, 99),
                           circle_params: Optional[Dict] = None,
                           figsize: Tuple[int, int] = (8, 6),
                           save_path: Optional[str] = None) -> plt.Figure:
    """
    Plot a single diffraction pattern with optional overlay features
    
    Parameters:
    -----------
    dp : np.ndarray
        2D diffraction pattern
    title : str
        Plot title
    cmap : str
        Colormap name
    log_scale : bool
        Use logarithmic intensity scaling
    percentile_range : tuple
        Intensity percentile range for display
    circle_params : dict, optional
        Parameters for overlay circles {'center': (x, y), 'radii': [r1, r2, ...]}
    figsize : tuple
        Figure size
    save_path : str, optional
        Path to save figure
        
    Returns:
    --------
    matplotlib.Figure
    """
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Set up normalization
    vmin = np.percentile(dp, percentile_range[0])
    vmax = np.percentile(dp, percentile_range[1])
    
    if log_scale:
        vmin = max(1, vmin)  # Avoid log(0)
        norm = LogNorm(vmin=vmin, vmax=vmax)
    else:
        norm = plt.Normalize(vmin=vmin, vmax=vmax)
    
    im = ax.imshow(dp, cmap=cmap, origin='lower', norm=norm)
    ax.set_title(title)
    ax.set_xlabel('Detector X (pixels)')
    ax.set_ylabel('Detector Y (pixels)')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, fraction=0.046)
    cbar.set_label('Intensity' + (' (log scale)' if log_scale else ''))
    
    # Add overlay circles if specified
    if circle_params:
        center = circle_params.get('center', (dp.shape[1]//2, dp.shape[0]//2))
        radii = circle_params.get('radii', [])
        colors = circle_params.get('colors', ['red'] * len(radii))
        
        for radius, color in zip(radii, colors):
            circle = plt.Circle(center, radius, fill=False, color=color, linewidth=2)
            ax.add_patch(circle)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig

def plot_strain_map(strain_xx: np.ndarray, strain_yy: np.ndarray, strain_xy: np.ndarray,
                   scale_bar: Optional[float] = None,
                   figsize: Tuple[int, int] = (15, 5),
                   save_path: Optional[str] = None) -> plt.Figure:
    """
    Plot strain tensor components
    
    Parameters:
    -----------
    strain_xx, strain_yy, strain_xy : np.ndarray
        Strain tensor components
    scale_bar : float, optional
        Scale bar size in same units as strain
    figsize : tuple
        Figure size
    save_path : str, optional
        Path to save figure
        
    Returns:
    --------
    matplotlib.Figure
    """
    
    fig, axes = plt.subplots(1, 3, figsize=figsize)
    
    strain_data = [strain_xx, strain_yy, strain_xy]
    titles = ['Strain εₓₓ', 'Strain εᵧᵧ', 'Shear εₓᵧ']
    
    # Find common scale for all strain components
    vmin = min(np.percentile(s, 5) for s in strain_data)
    vmax = max(np.percentile(s, 95) for s in strain_data)
    vext = max(abs(vmin), abs(vmax))
    
    for i, (strain, title, ax) in enumerate(zip(strain_data, titles, axes)):
        im = ax.imshow(strain, cmap='RdBu_r', origin='lower',
                      vmin=-vext, vmax=vext)
        ax.set_title(title)
        ax.set_xlabel('X (pixels)')
        ax.set_ylabel('Y (pixels)')
        
        cbar = plt.colorbar(im, ax=ax, fraction=0.046)
        cbar.set_label('Strain')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig

def setup_em_plotting_style():
    """
    Set up matplotlib style for electron microscopy plots
    """
    
    plt.style.use('default')
    
    # Set high DPI for crisp images
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['savefig.dpi'] = 300
    
    # Font settings
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10
    
    # Layout settings
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['axes.grid'] = False
    
    # Color settings
    plt.rcParams['image.cmap'] = 'viridis'
    plt.rcParams['axes.prop_cycle'] = plt.cycler('color', 
        ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
         '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])

# Initialize EM plotting style when module is imported
setup_em_plotting_style()