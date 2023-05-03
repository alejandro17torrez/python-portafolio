from typing import Any

import numpy as np


def recursion_binary_search(
    arr: np.ndarray | list, left: int, right: int, key: Any
) -> Any:
    if right >= left:
        middle = left + (right - left) // 2
        if arr[middle] == key:
            return {"index": middle, "value": arr[middle]}
        elif arr[middle] > key:
            return recursion_binary_search(arr, left, middle - 1, key)
        else:
            return recursion_binary_search(arr, middle + 1, right, key)
    else:
        return -1
