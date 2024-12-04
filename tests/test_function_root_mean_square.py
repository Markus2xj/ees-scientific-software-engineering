import numpy as np

from ees_scientific_software_engineering.function_root_mean_square import rms


def test_rms():
    a = np.ones(10)
    assert rms(a) == 1
