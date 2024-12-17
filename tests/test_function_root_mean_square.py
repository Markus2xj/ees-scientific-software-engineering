import numpy as np
import pytest

from ees_scientific_software_engineering.function_root_mean_square import DimensionError, rms


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
