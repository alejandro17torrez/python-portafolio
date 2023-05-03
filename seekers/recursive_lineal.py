from typing import Any

import numpy as np


def recursive_search(arr: np.ndarray | list, key: Any, current_index: int = 0) -> Any:
    current_value = arr[current_index]
    if current_index == -1:
        return -1
    if current_value == key:
        return current_value
    return recursive_search(arr, current_index + 1, key)
