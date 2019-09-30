from ._base import PatternBase


class Lambda(PatternBase):

    def __init__(self, pattern, function):
        self.pattern = None
        self.function = None
        super().__init__(pattern=pattern, function=function)

    def iterate(self):
        for x in self.pattern:
            yield self.function(x)
