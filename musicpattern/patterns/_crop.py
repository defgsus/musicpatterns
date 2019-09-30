from ._base import PatternBase
from ._next import Next


class MaxLength(PatternBase):
    """
    Force maximum length
    """

    def __init__(self, pattern, length):
        self.pattern = None
        self.length = None
        super().__init__(pattern=pattern, length=length)

    def iterate(self):
        try:
            pattern = Next(self.pattern)
            length = Next(self.length, repeat_scalar=True)

            count = 0
            while count < length.next():
                count += 1
                yield pattern.next()

        except StopIteration:
            return
