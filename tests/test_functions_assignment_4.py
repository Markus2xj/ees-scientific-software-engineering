import numpy as np

from ees_scientific_software_engineering.functions_assignment_4 import LUSolver


def test_input_matrix():
    input_matrix = np.ones((10, 10))
    a = LUSolver(input_matrix)
    assert isinstance(a, LUSolver), "Object 'a' is not an instance of LUSolver"
