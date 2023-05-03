def mergesort(list: list) -> list:
    """sorting method by merge"""
    if len(list) <= 1:
        return list
    else:
        middle = len(list) // 2
        left = make_side(list, 0, middle)
        right = make_side(list, middle, len(list))
        left = mergesort(left)
        right = mergesort(right)

        if left[middle - 1] <= right[0]:
            left += right
            return left
        result = merge(left, right)
        return result


def merge(left: list, right: list) -> list:
    mixed_list = []
    while (len(left) > 0) and (len(right) > 0):
        if left[0] < right[0]:
            mixed_list.append(left.pop(0))
        else:
            mixed_list.append(right.pop(0))
    if len(left) > 0:
        mixed_list += left
    if len(right) > 0:
        mixed_list += right
    return mixed_list


def make_side(list: list, beginning: int, ending: int) -> list:
    new_list = []
    for item in range(beginning, ending):
        new_list.append(list[item])
    return new_list
