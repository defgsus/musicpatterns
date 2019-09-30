
class Next:

    def __init__(self, value, repeat_scalar=False):
        self.value = value
        self.repeat_scalar = repeat_scalar
        self.offset = 0
        self.iterator = None
        if hasattr(self.value, "__iter__"):
            self.iterator = getattr(self.value, "__iter__")()

    def __str__(self):
        return "Next(value=%s, repeat_scalar=%s)" % (
            self.value, self.repeat_scalar
        )

    def next(self):
        if self.iterator:
            return self.iterator.__next__()

        if self.repeat_scalar:
            return self.value

        if self.offset == 0:
            self.offset += 1
            return self.value
        else:
            raise StopIteration
