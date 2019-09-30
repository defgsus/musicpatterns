import math

from ._base import PatternBase
from ._next import Next
from ._list import List


class Divisors(PatternBase):

    """
    Outputs the set of divisors for each input
    """

    def __init__(self, pattern):
        self.pattern = None
        super().__init__(pattern=pattern)

    def iterate(self):
        try:
            pattern = Next(self.pattern)

            while True:
                sign = 1
                number = int(pattern.next())

                if number == 0:
                    yield []
                    continue

                elif number == 1:
                    yield List([1])
                    continue

                elif number == -1:
                    yield List([-1])
                    continue

                elif number < 0:
                    sign = -1
                    number = abs(number)

                divisors = [sign]
                for i in range(2, number // 2 + 1):
                    if number / i == number // i:
                        divisors.append(i * sign)
                if divisors[-1] != number * sign:
                    divisors.append(number * sign)

                yield List(divisors)

        except StopIteration:
            return
