from ._base import PatternBase
from ._next import Next


class Repeat(PatternBase):

    def __init__(self, pattern, times):
        self.pattern = None
        self.times = None
        super().__init__(pattern=pattern, times=times)

    def iterate(self):
        try:
            times = Next(self.times)

            count = 0
            while count < times.next():
                count += 1
                try:
                    yield from self.pattern
                except StopIteration:
                    return

        except StopIteration:
            return
