import unittest

from musicpattern.patterns import *


class TestNotes(unittest.TestCase):

    def test_01(self):
        data = {
            "note": Range(5) + 60,
            "vel": Repeat([1, 2], 4),
            "time": 50
        }
        seq = KeyValue(data)


if __name__ == "__main__":
    unittest.main()
