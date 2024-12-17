import numpy as np
import pytest

from ees_scientific_software_engineering.function_root_mean_square import NanError, SizeError, rms


def test_rms():
    a = np.ones(10)
    assert rms(a) == 1


def test_size_error():
    a = np.ones(0)
    with pytest.raises(SizeError, match="The size of the input array should be at least one!"):
        rms(a)


def test_inf_error():
    a = np.ones(10)
    a[0] = np.inf
    with pytest.raises(ValueError, match="There should be no inf in the input array!"):
        rms(a)


def test_nan_error():
    a = np.ones(10)
    a[0] = np.nan
    with pytest.raises(NanError, match="There should be no nan in the input array!"):
        rms(a)
