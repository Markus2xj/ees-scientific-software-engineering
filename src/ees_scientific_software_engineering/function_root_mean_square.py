"""
This is a docstring
"""

import numpy as np


def rms(input_array: np.ndarray) -> float:
    """
    This function calculates the rms based on np
    Parameters:
    np.ndarray: input_array

    Returns:
    float: rms value
    """
    return np.sqrt(np.mean(input_array**2))
