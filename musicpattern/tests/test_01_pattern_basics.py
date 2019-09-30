import unittest

from musicpattern.patterns import PatternBase, List, Range


class TestPatternBase(unittest.TestCase):

    def test_01_pattern_base(self):
        p = PatternBase()
        print(p)

    def test_02_list(self):
        l = List([1, 2, 3]) + List([4, 5, 6])
        print(l)
        print(list(l))

    def test_02_range(self):
        self.assertEqual([0, 1, 2], list(Range(3)))
        self.assertEqual([1, 2], list(Range(1, 3)))
        self.assertEqual([2, 4, 6, 8], list(Range(2, 9, 2)))
        self.assertEqual([0, -1, -2, -3], list(Range(0, -4, -1)))


if __name__ == "__main__":
    unittest.main()
