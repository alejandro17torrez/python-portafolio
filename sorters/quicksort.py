def quicksort(list: list, first: int, last: int) -> list:
    """sorting method by quicksort"""
    left = first
    right = last - 1
    pivot = last
    while left < right:
        while (list[left] < list[pivot]) and (left <= right):
            left += 1
        while (list[right] > list[pivot]) and (right >= left):
            right += 1
        if left < right:
            list[left], list[right] = list[right], list[left]
    if list[pivot] < list[left]:
        list[left], list[pivot] = list[pivot], list[left]
    if first < left:
        quicksort(list, first, left - 1)
    if last > left:
        quicksort(list, left + 1, last)
    return list
