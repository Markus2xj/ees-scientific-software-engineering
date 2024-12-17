import numpy as np


def rms(input_array: np.ndarray) -> float:
    """
    This function calculates the rms based on np functions.
    """
    return np.sqrt(np.mean(input_array**2))
