import unittest

from musicpattern.patterns import Next


class TestNext(unittest.TestCase):

    def test_01_next_iterator(self):
        n = Next([1, 2, 3])
        self.assertEqual([1, 2, 3], [n.next(), n.next(), n.next()])

        with self.assertRaises(StopIteration):
            n.next()

    def test_01_scalar(self):
        n = Next(23)
        self.assertEqual(23, n.next())

        with self.assertRaises(StopIteration):
            n.next()

    def test_02_scalar_repeat(self):
        n = Next(23, repeat_scalar=True)
        for i in range(10):
            self.assertEqual(23, n.next())


if __name__ == "__main__":
    unittest.main()
