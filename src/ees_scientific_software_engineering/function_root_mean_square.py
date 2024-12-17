"""
This is a docstring
"""

import numpy as np

class DimensionError(Exception):
    """
    Custom exception for dimensionality error
    """
    pass

def rms(input_array: np.ndarray) -> float:  # input_array should be an instance of np.ndarray.
    """
    This function calculates the rms based on np
    Parameters:
    np.ndarray: input_array

    Returns:
    float: rms value
    """
    if not isinstance(input_array,np.ndarray):
        raise TypeError("Type is not np.ndarray!")

    if input_array.ndim != 1:
        raise DimensionError("Dimension of inputarray is not one")

    if input_array.dtype != np.float64:
        raise TypeError("Datatype is not np.float64")

    return np.sqrt(np.mean(input_array**2))
