def selection(list: list) -> list:
    """Sorting method by selection"""
    for item in range(0, len(list) - 1):
        minimun = item
        for adyacent_item in range(item + 1, len(list)):
            if list[adyacent_item] < list[minimun]:
                minimun = adyacent_item
            list[item], list[minimun] = list[minimun], list[item]
    return list
