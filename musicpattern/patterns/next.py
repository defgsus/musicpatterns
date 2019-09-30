
class Next:

    def __init__(self, value):
        self.value = value
        self.offset = 0
        self.iterator = None
        if hasattr(self.value, "__iter__"):
            self.iterator = getattr(self.value, "__iter__")()

    def next(self):
        if self.iterator:
            return self.iterator.__next__()
        return self.value
