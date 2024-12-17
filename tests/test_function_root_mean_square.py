import numpy as np
import pytest

from ees_scientific_software_engineering.function_root_mean_square import NanError, DimensionError, SizeError, rms


def test_rms():
    a = np.ones(10)
    assert rms(a) == 1


def testInputType():
    a = [1, 2, 3, 4, 5]
    with pytest.raises(TypeError, match="Type is not np.ndarray!"):
        rms(a)


def testDimensionality():
    a = np.ones((10, 10))
    with pytest.raises(DimensionError, match="Dimension of inputarray is not one"):
        rms(a)


def testDType():
    a = np.ones(10, dtype="int")
    with pytest.raises(TypeError, match="Datatype is not np.float64"):
        rms(a)
      
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
