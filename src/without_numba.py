import random
from datetime import datetime


def calculate_number(*, goal: int):
    k = 0
    while k != goal:
        k += 1
    return k


now = datetime.now()
print(calculate_number(goal=999999999))
print(datetime.now() - now)
