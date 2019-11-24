from ._base import PatternBase
from ._next import Next
from ._inspect import is_iterable


class Chord(PatternBase):
    """
    Simply put the input into a list
    """

    def __init__(self, values):
        assert is_iterable(values)
        self.values = None
        super().__init__(values=values)

    def iterate(self):
        yield list(self.values)

