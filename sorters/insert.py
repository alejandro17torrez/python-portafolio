def insert(list: list) -> list:
    """sorting method by insert"""

    for item in range(1, len(list) + 1):
        k = item - 1
        while (k > 0) and (list[k] < list[k - 1]):
            list[k], list[k - 1] = list[k - 1], list[k]
            k -= 1
    return list
