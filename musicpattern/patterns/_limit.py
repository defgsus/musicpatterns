from ._base import PatternBase
from ._next import Next


class Limit(PatternBase):

    def __init__(self, pattern, end):
        self.pattern = None
        self.end = None
        super().__init__(pattern=pattern, end=end)

    def iterate(self):
        try:
            pattern = Next(self.pattern)
            end = Next(self.end)

            count = 0
            while count < end.next():
                count += 1
                yield pattern.next()

        except StopIteration:
            return
