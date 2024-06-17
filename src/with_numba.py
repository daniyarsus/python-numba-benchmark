import random
from datetime import datetime
from numba import jit, int64


@jit(int64(int64), nopython=True)
def calculate_number(*, goal: int64):
    k = 0
    while k != goal:
        k += 1
    return k


now = datetime.now()
print(calculate_number(goal=999999999))
print(datetime.now() - now)
