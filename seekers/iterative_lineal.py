from typing import Any

import numpy as np


def lineal_search(arr: np.ndarray | list, element_wasted: Any) -> Any:
    for item in range(len(arr)):
        if arr[item] == element_wasted:
            return arr[item]
    return -1
