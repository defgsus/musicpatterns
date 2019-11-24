from ._next import Next
from ._convert import convert_to_list


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
    """
    base class for iterable patterns.
    Constructor takes all key/value pairs as arguments to the generator.
    A pattern can be iterated, indexed and combined via binary operators
    """

    def __init__(self, **parameters):
        self._parameter_names = list(parameters.keys())
        for key, value in parameters.items():
            setattr(self, key, value)

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, self.parameter_string())

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return self.iterate()

    def __getitem__(self, x):
        assert isinstance(x, int), "expected int, got '%s' (%s)" % (type(x).__name__, x)
        for i, value in enumerate(self):
            if i == x:
                return value
        raise KeyError

    def parameter_string(self):
        return ", ".join(
            "%s=%s" % (key, repr(value))
            for key, value in self.parameters().items()
        )

    def parameters(self):
        return {key: getattr(self, key) for key in self._parameter_names}

    def iterate(self):
        raise NotImplementedError

    # --- conversion ---

    def to_list(self):
        return convert_to_list(self)

    def to_flat_list(self):
        from ._list import FlatList
        return convert_to_list(FlatList(self))

    # --- math operators ---

    def __neg__(self):
        from ._lambda import Lambda
        return Lambda(self, lambda x: -x)

    def __add__(self, other):
        return BinaryOperator(self, other, "+")

    def __sub__(self, other):
        return BinaryOperator(self, other, "-")

    def __mul__(self, other):
        return BinaryOperator(self, other, "*")

    def __truediv__(self, other):
        return BinaryOperator(self, other, "/")

    def __idiv__(self, other):
        return BinaryOperator(self, other, "//")

    def __mod__(self, other):
        return BinaryOperator(self, other, "%")

    def __pow__(self, power, modulo=None):
        assert not modulo, "power modulo not supported"
        return BinaryOperator(self, power, "**")

    def __radd__(self, other):
        return BinaryOperator(other, self, "+")

    def __rsub__(self, other):
        return BinaryOperator(other, self, "-")

    def __rmul__(self, other):
        return BinaryOperator(other, self, "*")

    def __rtruediv__(self, other):
        return BinaryOperator(other, self, "/")

    def __rmod__(self, other):
        return BinaryOperator(other, self, "%")

    def __rpow__(self, other):
        return BinaryOperator(other, self, "**")

    def __eq__(self, other):
        return BinaryOperator(self, other, "==")

    def __ne__(self, other):
        return BinaryOperator(self, other, "!=")

    def __gt__(self, other):
        return BinaryOperator(self, other, ">")

    def __ge__(self, other):
        return BinaryOperator(self, other, ">=")

    def __lt__(self, other):
        return BinaryOperator(self, other, "<")

    def __le__(self, other):
        return BinaryOperator(self, other, "<=")


class BinaryOperator(PatternBase):
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
        elif self.op == "**":
            self.func = lambda l, r: l ** r
        elif self.op == "==":
            self.func = lambda l, r: 1 if l == r else 0
        elif self.op == "!=":
            self.func = lambda l, r: 1 if l != r else 0
        elif self.op == ">":
            self.func = lambda l, r: 1 if l > r else 0
        elif self.op == ">=":
            self.func = lambda l, r: 1 if l >= r else 0
        elif self.op == "<":
            self.func = lambda l, r: 1 if l < r else 0
        elif self.op == "<=":
            self.func = lambda l, r: 1 if l <= r else 0
        if self.func is None:
            raise ValueError("Unsupported operator '%s'" % self.op)

    def iterate(self):
        try:
            left = Next(self.left, repeat_scalar=True)
            right = Next(self.right, repeat_scalar=True)
            while True:
                yield self.func(left.next(), right.next())

        except StopIteration:
            pass
