
from collections.abc import Iterable

def col():
    n = 0
    while n < 19:
        yield n
        n += 2

n = col()
print(n)
print(isinstance(n, Iterable))