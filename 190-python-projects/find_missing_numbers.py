"""
coding analyzing:
    -> convert list to set for getting unique values
    -> declare an instance of empty list
    -> iterate from one to last value of parameter list
    -> validate if each number is on set of unique value numbers
        ->> True: set element on empty list
    -> return the list that maybe is not empty already

"""


def find_missing_numbers(numbers: list) -> list:
    if not numbers:
        return []

    set_of_numbers = set(numbers)
    missing_number_list = []
    for iterator in range(1, numbers[-1]):
        if iterator not in set_of_numbers:
            missing_number_list.append(iterator)
    return missing_number_list
