from .base import PatternBase


class Range(PatternBase):

    def __init__(self, start_or_end, end=None, offset=None):
        self.start_or_end = None
        self.end = None
        self.offset = None
        super().__init__(start_or_end=start_or_end, end=end, offset=offset)

    def iterate(self):
        if not self.end:
            for x in range(self.start_or_end):
                yield x
        elif not self.offset:
            for x in range(self.start_or_end, self.end):
                yield x
        else:
            for x in range(self.start_or_end, self.end, self.offset):
                yield x
