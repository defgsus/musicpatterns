from ._base import PatternBase


class List(PatternBase):

    def __init__(self, values):
        self.values = None
        super().__init__(values=values)

    def iterate(self):
        for x in self.values:
            yield x
