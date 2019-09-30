from ._base import PatternBase


class List(PatternBase):

    def __init__(self, values):
        self.values = None
        super().__init__(values=values)

    def iterate(self):
        for x in self.values:
            yield x


class FlatList(PatternBase):
    """
    Flattens all nested lists
    """

    def __init__(self, values):
        assert hasattr(values, "__iter__"), "FlatList values must be iterable, got %s" % type(values).__name__
        self.values = None
        super().__init__(values=values)

    def iterate(self):
        def _iterate(values):
            for x in values:
                if hasattr(x, "__iter__"):
                    yield from _iterate(x)
                else:
                    yield x

        yield from _iterate(self.values)
