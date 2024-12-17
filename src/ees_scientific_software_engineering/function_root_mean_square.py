import numpy as np


def rms(input_array: np.ndarray) -> float:
    return np.sqrt(np.mean(input_array**2))
