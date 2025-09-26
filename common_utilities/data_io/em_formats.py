"""
Data I/O utilities for electron microscopy formats
"""

import numpy as np
import h5py
import os
from typing import Dict, Any, Optional, Tuple
import warnings

def load_4dstem_data(filepath: str, lazy: bool = False) -> Dict[str, Any]:
    """
    Load 4D-STEM data from various formats
    
    Parameters:
    -----------
    filepath : str
        Path to the data file
    lazy : bool
        Whether to load data lazily (for large datasets)
        
    Returns:
    --------
    Dict containing:
        - 'data': 4D numpy array or dask array if lazy=True
        - 'metadata': Dictionary of experimental parameters
        - 'calibration': Calibration parameters
    """
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    file_ext = os.path.splitext(filepath)[1].lower()
    
    if file_ext in ['.h5', '.hdf5']:
        return _load_hdf5_4dstem(filepath, lazy)
    elif file_ext in ['.dm3', '.dm4']:
        return _load_dm_4dstem(filepath, lazy)
    elif file_ext == '.mib':
        return _load_mib_4dstem(filepath, lazy)
    else:
        raise ValueError(f"Unsupported file format: {file_ext}")

def save_4dstem_data(data: np.ndarray, filepath: str, 
                     metadata: Optional[Dict] = None,
                     compression: str = 'gzip') -> None:
    """
    Save 4D-STEM data to HDF5 format with metadata
    
    Parameters:
    -----------
    data : np.ndarray
        4D data array (scan_x, scan_y, detector_x, detector_y)
    filepath : str
        Output file path
    metadata : dict, optional
        Experimental metadata to save
    compression : str
        Compression algorithm ('gzip', 'lzf', 'szip')
    """
    
    if data.ndim != 4:
        raise ValueError(f"Expected 4D data, got {data.ndim}D")
    
    with h5py.File(filepath, 'w') as f:
        # Create data group
        data_group = f.create_group('4dstem_data')
        
        # Save main dataset with compression
        dataset = data_group.create_dataset(
            'datacube',
            data=data,
            compression=compression,
            chunks=True,
            shuffle=True
        )
        
        # Add basic attributes
        dataset.attrs['shape'] = data.shape
        dataset.attrs['dtype'] = str(data.dtype)
        
        # Save metadata if provided
        if metadata:
            meta_group = f.create_group('metadata')
            for key, value in metadata.items():
                if isinstance(value, (str, int, float, bool)):
                    meta_group.attrs[key] = value
                elif isinstance(value, np.ndarray):
                    meta_group.create_dataset(key, data=value)

def _load_hdf5_4dstem(filepath: str, lazy: bool) -> Dict[str, Any]:
    """Load 4D-STEM data from HDF5 format"""
    
    result = {
        'data': None,
        'metadata': {},
        'calibration': {}
    }
    
    with h5py.File(filepath, 'r') as f:
        # Find the main data array
        if '4dstem_data/datacube' in f:
            dataset = f['4dstem_data/datacube']
        elif 'datacube' in f:
            dataset = f['datacube']
        else:
            # Try to find any 4D dataset
            for key in f.keys():
                if isinstance(f[key], h5py.Dataset) and len(f[key].shape) == 4:
                    dataset = f[key]
                    break
            else:
                raise ValueError("No 4D dataset found in HDF5 file")
        
        if lazy:
            import dask.array as da
            result['data'] = da.from_array(dataset, chunks='auto')
        else:
            result['data'] = dataset[:]
        
        # Load metadata
        if 'metadata' in f:
            meta_group = f['metadata']
            for key in meta_group.attrs:
                result['metadata'][key] = meta_group.attrs[key]
    
    return result

def _load_dm_4dstem(filepath: str, lazy: bool) -> Dict[str, Any]:
    """Load 4D-STEM data from DigitalMicrograph format"""
    
    try:
        import ncempy.io as nio
    except ImportError:
        raise ImportError("ncempy required for DM file support. Install with: pip install ncempy")
    
    # Load DM file
    dm_data = nio.dm.dmReader(filepath)
    
    result = {
        'data': dm_data['data'],
        'metadata': dm_data.get('tags', {}),
        'calibration': {}
    }
    
    # Extract calibration from DM tags if available
    if 'tags' in dm_data:
        tags = dm_data['tags']
        # Add calibration extraction logic here
        pass
    
    return result

def _load_mib_4dstem(filepath: str, lazy: bool) -> Dict[str, Any]:
    """Load 4D-STEM data from MIB format (Medipix detector)"""
    
    try:
        import py4DSTEM
    except ImportError:
        raise ImportError("py4DSTEM required for MIB file support")
    
    # Use py4DSTEM's built-in MIB loader
    datacube = py4DSTEM.io.read(filepath)
    
    result = {
        'data': datacube.data,
        'metadata': {},
        'calibration': {
            'R_pixel_size': getattr(datacube, 'R_pixel_size', None),
            'Q_pixel_size': getattr(datacube, 'Q_pixel_size', None)
        }
    }
    
    return result

def validate_4dstem_data(data: np.ndarray) -> bool:
    """
    Validate 4D-STEM data array
    
    Parameters:
    -----------
    data : np.ndarray
        Data array to validate
        
    Returns:
    --------
    bool : True if valid, raises exception if not
    """
    
    if not isinstance(data, np.ndarray):
        raise TypeError("Data must be numpy array")
    
    if data.ndim != 4:
        raise ValueError(f"Expected 4D data, got {data.ndim}D")
    
    if data.size == 0:
        raise ValueError("Data array is empty")
    
    if not np.isfinite(data).all():
        warnings.warn("Data contains non-finite values")
    
    return True

def get_data_info(data: np.ndarray) -> Dict[str, Any]:
    """
    Get comprehensive information about 4D-STEM dataset
    
    Parameters:
    -----------
    data : np.ndarray
        4D data array
        
    Returns:
    --------
    Dict with data statistics and properties
    """
    
    validate_4dstem_data(data)
    
    info = {
        'shape': data.shape,
        'dtype': data.dtype,
        'size_mb': data.nbytes / (1024**2),
        'scan_shape': data.shape[:2],
        'detector_shape': data.shape[2:],
        'total_counts': int(np.sum(data)),
        'mean_counts': float(np.mean(data)),
        'std_counts': float(np.std(data)),
        'max_counts': int(np.max(data)),
        'min_counts': int(np.min(data))
    }
    
    return info