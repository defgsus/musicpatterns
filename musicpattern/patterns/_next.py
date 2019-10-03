from ._inspect import is_iterable


class Next:
    """
    Little helper that manually iterates over sequences or scalars
    """

    def __init__(self, value, repeat_scalar=False):
        self.value = value
        self.repeat_scalar = repeat_scalar
        self.offset = 0
        self.iterator = None
        self.current = None
        if is_iterable(self.value):
            self.iterator = getattr(self.value, "__iter__")()

    def __str__(self):
        return "Next(value=%s, repeat_scalar=%s)" % (
            self.value, self.repeat_scalar
        )

    def next(self):
        if self.iterator:
            self.current = self.iterator.__next__()
            return self.current

        if self.repeat_scalar:
            self.current = self.value
            return self.current

        if self.offset == 0:
            self.offset += 1
            self.current = self.value
            return self.current
        else:
            raise StopIteration
