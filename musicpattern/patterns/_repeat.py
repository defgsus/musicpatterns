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
