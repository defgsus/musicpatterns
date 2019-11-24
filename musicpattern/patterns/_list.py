from ._base import PatternBase
from ._inspect import is_iterable


class List(PatternBase):
    """
    Just convert the input iterable to a pattern type.
    """

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
        assert is_iterable(values), "FlatList values must be iterable, got %s" % type(values).__name__
        self.values = None
        super().__init__(values=values)

    def iterate(self):
        def _iterate(values):
            for x in values:
                if is_iterable(x):
                    yield from _iterate(x)
                else:
                    yield x

        yield from _iterate(self.values)
