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


class Length(PatternBase):
    """
    Force length.
    If `pattern` ends before `length`, `default` is used instead.
    However, if `length` or `default` are patterns, their StopIteration will
    end this sequence.
    """

    def __init__(self, pattern, length, default=0):
        self.pattern = None
        self.length = None
        self.default = None
        super().__init__(pattern=pattern, length=length, default=default)

    def iterate(self):
        try:
            pattern = Next(self.pattern)
            length = Next(self.length, repeat_scalar=True)
            default = Next(self.default, repeat_scalar=True)

            count = 0
            while count < length.next():
                count += 1
                try:
                    yield pattern.next()
                except StopIteration:
                    yield default.next()

        except StopIteration:
            return
