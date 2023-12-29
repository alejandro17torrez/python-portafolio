import logging

import numpy as np

logging.basicConfig(level=logging.DEBUG)

random_number = np.random.randint(low=0, high=10)


def try_to_guess_random_number(random_number: int) -> int:
    guessed_number: int = int(input("try to guess a random int number: "))
    if guessed_number != random_number:
        logging.debug(f"Try again | pista: {random_number - 2} dos unidades menos")
        try_to_guess_random_number(random_number=random_number)
    return random_number


result = try_to_guess_random_number(random_number)
logging.debug(result)
