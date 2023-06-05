import numpy as np

rn = [number for number in range(1, np.random.randint(2, 50))]


def median(numbers: list) -> float | int:
    return np.sum(numbers) / len(rn)


def mean(numbers: list) -> float | int:
    numbers_sorted = np.sort(numbers)
    if len(numbers_sorted) % 2 == 0:
        min = numbers_sorted[len(numbers_sorted) // 2]
        max = numbers_sorted[len(numbers_sorted) // 2 - 1]
        return (min + max) / 2
    return numbers_sorted[len(numbers_sorted) // 2]


def mode(numbers: list) -> float | int:
    count_of_values = {}
    set_of_numbers = set(numbers)

    for number in set_of_numbers:
        count_of_values[number] = numbers.count(number)
    return max(count_of_values, key=count_of_values.get)


MTC = {
    "median": median(rn),
    "mean": mean(rn),
    "mode": mode([1, 2, 4, 4, 5, 7, 8, 3, 2, 2, 1]),
}

print(MTC)
