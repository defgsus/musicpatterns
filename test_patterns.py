from tools.patterns import *
from tools.plot import dump_values


def dump(pat):
    print()
    print(pat)
    print(pat.values(30))
    dump_values(pat.values(150))


if 1:
    p1 = PatternValues([1,2,3])
    dump(p1)

    p2 = PatternValues([10,20,30,40])
    dump(p1+p2)

    dump(100+p1)

    dump(10*p2 + p2%(p1+3))

    pat = PatternFormula(lambda x: x*x)
    #dump(pat)

    p3 = PatternResize([1,2,3], PatternValues([1,2,3]))
    dump(p3)

    p4 = PatternRepeat(PatternValues([1,2,3]), PatternValues([1,2,3,4,5]))
    dump(p4)