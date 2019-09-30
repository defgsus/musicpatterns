from .next import Next


class PatternIterator:

    def __init__(self, pattern):
        self.pattern = pattern
        self.idx = 0

    def __next__(self):
        try:
            v = self.pattern[self.idx]
        except IndexError:
            raise StopIteration
        self.idx += 1
        return v


class PatternBase:

    def __init__(self, **parameters):
        self._parameter_names = list(parameters.keys())
        for key, value in parameters.items():
            setattr(self, key, value)

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, self.info_str())

    def __repr__(self):
        return str(self)

    def info_str(self):
        return ", ".join(
            "%s=%s" % (key, value)
            for key, value in self.parameters().items()
        )

    def parameters(self):
        return {key: getattr(self, key) for key in self._parameter_names}

    def iterate(self):
        raise NotImplementedError

    #def values(self, count):
    #    return [self[x] for x in range(count)]

    def __iter__(self):
        return self.iterate()
        #return PatternIterator(self)

    #def __getitem__(self, idx):
    #    if isinstance(idx, slice):
    #        return [self.get_item(i) for i in range(idx.start or 0, idx.stop, idx.step or 1)]
    #    return self.get_item(idx)

    # def get_item(self, idx):
    #    raise NotImplementedError

    def __add__(self, other):
        return PatternBinaryOperator(self, other, "+")

    def __sub__(self, other):
        return PatternBinaryOperator(self, other, "-")

    def __mul__(self, other):
        return PatternBinaryOperator(self, other, "*")

    def __div__(self, other):
        return PatternBinaryOperator(self, other, "/")

    def __idiv__(self, other):
        return PatternBinaryOperator(self, other, "//")

    def __mod__(self, other):
        return PatternBinaryOperator(self, other, "%")

    def __radd__(self, other):
        return PatternBinaryOperator(other, self, "+")

    def __rsub__(self, other):
        return PatternBinaryOperator(other, self, "-")

    def __rmul__(self, other):
        return PatternBinaryOperator(other, self, "*")

    def __rdiv__(self, other):
        return PatternBinaryOperator(other, self, "/")

    def __rmod__(self, other):
        return PatternBinaryOperator(other, self, "%")


class PatternBinaryOperator(PatternBase):
    def __init__(self, left, right, op):
        self.left = None
        self.right = None
        self.op = None
        super().__init__(left=left, right=right, op=op)

        self.func = None
        if self.op == "+":
            self.func = lambda l, r: l + r
        elif self.op == "-":
            self.func = lambda l, r: l - r
        elif self.op == "*":
            self.func = lambda l, r: l * r
        elif self.op == "/":
            self.func = lambda l, r: l / r
        elif self.op == "//":
            self.func = lambda l, r: l // r
        elif self.op == "%":
            self.func = lambda l, r: l % r
        if self.func is None:
            raise ValueError("Unsupported operator '%s'" % self.op)

    def iterate(self):
        try:
            left = Next(self.left)
            right = Next(self.right)
            while True:
                yield self.func(left.next(), right.next())

        except StopIteration:
            pass
