import unittest

from musicpattern.patterns import *


class TestPatternBase(unittest.TestCase):

    def test_01_pattern_base(self):
        p = PatternBase()

    def test_02_list(self):
        self.assertEqual([5, 7, 9], list(List([1, 2, 3]) + List([4, 5, 6])))
        self.assertEqual([1, 2, 3], list(List((1, 2, 3))))

    def test_03_nested_list(self):
        self.assertEqual([5, 7, 9], list(List([1, 2, 3]) + List([4, 5, 6])))
        self.assertEqual([1, 2, 3], list(List((1, 2, 3))))

        self.assertEqual([[1, 2], [3, 4]], List([List([1, 2]), List([3, 4])]).to_list())

    def test_04_limit(self):
        def run_forever():
            while True:
                yield 23

        self.assertEqual([23, 23], list(Limit(run_forever(), 2)))

    def test_05_range_int(self):
        self.assertEqual([0, 1, 2], list(Range(3)))
        self.assertEqual([0, 2, 4, 6, 8], list(Range(9, 2)))
        self.assertEqual([0, -1, -2, -3], list(Range(-4, -1)))

    def test_06_range_pattern(self):
        count = Range(5) + 1
        self.assertEqual([1, 2, 3, 4, 5], list(count))

        count2 = Range(10, count)
        self.assertEqual([0, 1, 3, 6], list(count2))

    def test_10_repeat(self):
        l123 = List([1, 2, 3])
        self.assertEqual([1, 2, 3, 1, 2, 3], list(Repeat(l123, 2)))

        self.assertEqual([1, 2, 3], list(Repeat(l123, [3, 1])))

        self.assertEqual([1, 2, 3, 1, 2], list(Limit(Repeat(l123, 2), 5)))

        nested = List([l123, l123])
        self.assertEqual([[1, 2, 3], [1, 2, 3]], nested.to_list())


if __name__ == "__main__":
    unittest.main()
