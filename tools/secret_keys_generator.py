import string
from pprint import pprint

import numpy as np

MIN = 25

LENGTH = np.random.randint(MIN, MIN + 1)
RANDOM_CHARS = np.array(
    list(string.ascii_letters + string.digits),
    dtype=np.str_,
)

secret_key = "".join(np.random.choice(RANDOM_CHARS, LENGTH))
pprint(secret_key)
