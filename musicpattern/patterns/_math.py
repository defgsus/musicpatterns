import math

from ._base import PatternBase
from ._next import Next
from ._list import List
from ._lambda import Lambda


class IsPrime(PatternBase):

    def __init__(self, value):
        self.value = None
        super().__init__(value=value)

    def iterate(self):
        try:
            values = Next(self.value)

            while True:
                num = int(values.next())

                is_prime = not (num < 2 or any(num % x == 0 for x in range(2, int(num ** 0.5) + 1)))

                yield 1 if is_prime else 0

        except StopIteration:
            return


class Sin(Lambda):
    def __init__(self, value):
        super().__init__(value, math.sin)
