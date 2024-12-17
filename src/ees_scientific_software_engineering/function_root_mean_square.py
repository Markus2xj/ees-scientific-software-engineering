"""
This is a docstring
"""

import numpy as np


class DimensionError(Exception):
    """
    Custom exception for dimensionality error
    """


class SizeError(Exception):
    """
    Custom expection size for less than one
    """


class NanError(Exception):
    """
    Custom expection contains nan
    """


def rms(input_array: np.ndarray) -> float:
    """
    This function calculates the rms based on np
    Parameters:
    np.ndarray: input_array

    Returns:
    float: rms value
    """

    if not isinstance(input_array, np.ndarray):
        raise TypeError("Type is not np.ndarray!")

    if input_array.ndim != 1:
        raise DimensionError("Dimension of inputarray is not one")

    if input_array.dtype != np.float64:
        raise TypeError("Datatype is not np.float64")

    if np.size(input_array) < 1:
        raise SizeError("The size of the input array should be at least one!")

    if np.any(np.isinf(input_array)) and not np.any(np.isnan(input_array)):
        raise ValueError("There should be no inf in the input array!")

    if np.any(np.isnan(input_array)) and not np.any(np.isinf(input_array)):
        raise NanError("There should be no nan in the input array!")

    return np.sqrt(np.mean(input_array**2))
