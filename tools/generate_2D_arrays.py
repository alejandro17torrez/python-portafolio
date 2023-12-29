import logging

logging.basicConfig(level=logging.DEBUG)


def generate_2d_empty_array() -> list[int]:
    """This is a method to generate a empty 2D list

    args:
        rows: int -> numbers of rows on matrix
        cols: int -> numbers of cols on matrix

    results:
        arr: list[int] -> list of 2D

    """

    rows: int = int(input("add the row's numbers: "))
    cols: int = int(input("add the col's numbers: "))

    arr = [[0 for i in range(cols)] for j in range(rows)]
    logging.debug(arr)
    return arr
