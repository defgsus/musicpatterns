import unittest

from musicpattern.patterns import *


class TestPatternBase(unittest.TestCase):

    def test_01_pattern_base(self):
        p = PatternBase()

    def test_02_list(self):
        self.assertEqual([5, 7, 9], list(List([1, 2, 3]) + List([4, 5, 6])))
        self.assertEqual([1, 2, 3], list(List((1, 2, 3))))

    def test_03_range_int(self):
        self.assertEqual([0, 1, 2], list(Range(3)))
        self.assertEqual([0, 2, 4, 6, 8], list(Range(9, 2)))
        self.assertEqual([0, -1, -2, -3], list(Range(-4, -1)))

    def test_04_range_pattern(self):
        count = Range(5) + 1
        self.assertEqual([1, 2, 3, 4, 5], list(count))

        count2 = Range(10, count)
        self.assertEqual([0, 1, 3, 6], list(count2))

    def test_05_repeat(self):
        l123 = List([1, 2, 3])
        self.assertEqual([1, 2, 3, 1, 2, 3], list(Repeat(l123, 2)))

        self.assertEqual([1, 2, 3], list(Repeat(l123, [3, 1])))

        # nested = List([l123, l123])


if __name__ == "__main__":
    unittest.main()
