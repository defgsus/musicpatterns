from ._base import PatternBase


def bjorklund(steps, pulses):
    """
    (c) 2011 Brian House
    https://github.com/brianhouse/bjorklund

    TODO: this algorithm does not yield the same offsets as in Toussaint's paper
    """
    steps = int(steps)
    pulses = int(pulses)
    if pulses > steps:
        raise ValueError
    pattern = []
    counts = []
    remainders = []
    divisor = steps - pulses
    remainders.append(pulses)
    level = 0
    while True:
        counts.append(divisor // remainders[level])
        remainders.append(divisor % remainders[level])
        divisor = remainders[level]
        level = level + 1
        if remainders[level] <= 1:
            break
    counts.append(divisor)

    def build(level):
        if level == -1:
            pattern.append(0)
        elif level == -2:
            pattern.append(1)
        else:
            for i in range(0, counts[level]):
                build(level - 1)
            if remainders[level] != 0:
                build(level - 2)

    build(level)
    i = pattern.index(1)
    pattern = pattern[i:] + pattern[0:i]
    return pattern


class EuclideanRhythm(PatternBase):

    """
    Euclidean rythm generator after Godfried Toussaint
    "The Euclidean Algorithm Generates Traditional Musical Rhythms"
    http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf
    """

    def __init__(self, ones, length):
        assert isinstance(ones, int)
        assert isinstance(length, int)
        self.ones = None
        self.length = None
        super().__init__(ones=ones, length=length)

    def iterate(self):
        rhythm = bjorklund(self.length, self.ones)
        yield from rhythm

    def to_string(self):
        return "".join("x" if x else "." for x in self)


