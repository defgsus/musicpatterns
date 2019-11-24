from ._base import PatternBase


class Lambda(PatternBase):
    """
    Apply function to each value of input
    """

    def __init__(self, pattern, function):
        self.pattern = None
        self.function = None
        super().__init__(pattern=pattern, function=function)

    def iterate(self):
        for x in self.pattern:
            yield self.function(x)
