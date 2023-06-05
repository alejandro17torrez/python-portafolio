"""
code analyzing:
    -> make a numpy array of list of lists
    -> make a expected list
    -> use a property T to group elements of same index
"""

import numpy as np


def group_elements_of_same_index(array_2d: list) -> np.ndarray:
    np_array_2d = np.array(array_2d)
    return np_array_2d.T
