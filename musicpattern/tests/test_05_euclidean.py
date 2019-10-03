import unittest

from musicpattern.patterns import *


class TestEuclideanRhythm(unittest.TestCase):

    def assertPattern(self, expected_pattern, ones, length):
        pattern = EuclideanRhythm(ones, length).to_string()
        if expected_pattern != pattern:
            error = ""
            if len(expected_pattern) != len(pattern):
                error = "wrong length"
            else:
                shift_pattern = pattern
                for i in range(len(shift_pattern)):
                    shift_pattern = shift_pattern[-1:] + shift_pattern[:-1]
                    if shift_pattern == expected_pattern:
                        error = "but same 'necklace'"
                        # TODO: currently we allow the shifts
                        return

            if error:
                error = f", {error}"
            raise AssertionError(
                f"expected '{expected_pattern}', got '{pattern}', for E({ones}, {length}){error}"
            )

    def test_02_toussaints_examples(self):
        self.assertPattern("x.x", 2, 3)
        self.assertPattern("x.x..", 2, 5)

    def test_03_toussaints_examples(self):
        self.assertPattern("x.xx", 3, 4)
        self.assertPattern("x.x.x", 3, 5)
        self.assertPattern("x.x.x..", 3, 7)
        self.assertPattern("x..x..x.", 3, 8)

    def test_04_toussaints_examples(self):
        self.assertPattern("x.x.x.x", 4, 7)
        self.assertPattern("x.x.x.x..", 4, 9)
        self.assertPattern("x..x..x..x.", 4, 11)

    def test_05_toussaints_examples(self):
        self.assertPattern("x.xxxx", 5, 6)
        self.assertPattern("x.xx.xx", 5, 7)
        self.assertPattern("x.xx.xx.", 5, 8)
        self.assertPattern("x.x.x.x.x", 5, 9)
        self.assertPattern("x.x.x.x.x..", 5, 11)
        self.assertPattern("x..x.x..x.x.", 5, 12)
        self.assertPattern("x..x.x..x.x..", 5, 13)
        # Note: Toussaint has a dot too much in his paper
        self.assertPattern("x..x..x..x..x...", 5, 16)

    def test_07_toussaints_examples(self):
        self.assertPattern("x.xxxxxx", 7, 8)
        self.assertPattern("x.xx.x.xx.x.", 7, 12)
        self.assertPattern("x..x.x.x..x.x.x.", 7, 16)

    def test_09_toussaints_examples(self):
        self.assertPattern("x.xx.x.x.xx.x.x.", 9, 16)

    def test_11_toussaints_examples(self):
        self.assertPattern("x..x.x.x.x.x..x.x.x.x.x.", 11, 24)

    def test_13_toussaints_examples(self):
        self.assertPattern("x.xx.x.x.x.x.xx.x.x.x.x.", 13, 24)

    def test_100_repeat(self):
        self.assertPattern("x...", 1, 4)
        self.assertPattern("x...x...", [1, 1], 4)
        self.assertPattern("x...x...", 1, [4, 4])
        self.assertPattern("x...x...", [1, 1], [4, 4])
        self.assertPattern("x...x.x.", [1, 2], 4)
        self.assertPattern("xx.x..x...", 1, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
