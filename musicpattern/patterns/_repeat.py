from ._base import PatternBase
from ._next import Next


class Repeat(PatternBase):
    """
    Repeat the input n times.
    if `times` is None, repeats forever.
    """

    def __init__(self, pattern, times=None):
        self.pattern = None
        self.times = None
        super().__init__(pattern=pattern, times=times)

    def iterate(self):
        try:
            if self.times is None:
                while True:
                    yield from self.pattern

            else:
                times = Next(self.times, repeat_scalar=True)

                count = 0
                while count < times.next():
                    count += 1
                    yield from self.pattern

        except StopIteration:
            return


class RepeatEach(PatternBase):
    """
    Repeat each element n times.
    """

    def __init__(self, pattern, times):
        self.pattern = None
        self.times = None
        super().__init__(pattern=pattern, times=times)

    def iterate(self):
        try:
            times = Next(self.times, repeat_scalar=True)

            for x in self.pattern:
                for i in range(times.next()):
                    yield x

        except StopIteration:
            return
