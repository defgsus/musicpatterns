import unittest

from musicpattern.patterns import *


class TestEuclidean(unittest.TestCase):

    def test_01_toussaints_examples(self):
        self.assertEqual([1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0], list(EuclideanRhythm(5, 13)))


if __name__ == "__main__":
    unittest.main()
