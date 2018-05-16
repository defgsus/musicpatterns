

def _get_item(x, idx):
    try:
        return x[idx]
    except TypeError:
        return x


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

    def __init__(self):
        pass

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, self.info_str())

    def info_str(self):
        return ""

    def values(self, count):
        return [self[x] for x in range(count)]

    def __iter__(self):
        return PatternIterator(self)

    def __getitem__(self, idx):
        raise NotImplementedError

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
        super().__init__()
        self.left = left
        self.right = right
        self.op = op
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

    def info_str(self):
        return "%s %s %s" % (self.left, self.op, self.right)

    def __getitem__(self, idx):
        return self.func(_get_item(self.left, idx), _get_item(self.right, idx))


class PatternValues(PatternBase):

    def __init__(self, values, loop=True):
        super().__init__()
        self._values = list(values)
        self.loop = loop

    def info_str(self):
        s = "len=%s" % len(self._values)
        if self.loop:
            s += ", loop"
        return s

    def __getitem__(self, idx):
        if self.loop and self._values:
            idx = idx % len(self._values)
        return self._values[idx]


class PatternFormula(PatternBase):

    def __init__(self, func):
        super().__init__()
        self.func = func

    def __getitem__(self, idx):
        return self.func(idx)


class PatternResize(PatternBase):
    def __init__(self, pattern, length, default=0, loop=True):
        super().__init__()
        self.pattern = pattern
        self.length = length
        self.default = default
        self.loop = loop

    def info_str(self):
        s = "pat=%s, len=%s, def=%s" % (self.pattern, self.length, self.default)
        if self.loop:
            s += ", loop"
        return s

    def __getitem__(self, idx):
        length = _get_item(self.length, idx)
        if idx >= length:
            if not self.loop:
                raise IndexError("index %s exceeds length %s" % (idx, length))
            idx = idx % length if length > 0 else 0
        try:
            return _get_item(self.pattern, idx)
        except IndexError:
            return _get_item(self.default, idx)


class PatternRepeat(PatternBase):
    """Repeat every item in pattern `count` times"""
    def __init__(self, pattern, count):
        super().__init__()
        self.pattern = pattern
        self.count = count

    def info_str(self):
        s = "pat=%s, len=%s" % (self.pattern, self.count)
        return s

    def __getitem__(self, idx):
        count = _get_item(self.count, idx)
        if count > 1:
            idx //= count
        return _get_item(self.pattern, idx)
