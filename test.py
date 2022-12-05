import unittest
import main


class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(10, 5), 15)
        self.assertEqual(main.add(3, 5), 8)
        self.assertEqual(main.add(2, 2), 4)

    def test_multiply(self):
        self.assertEqual(main.multiply(5, 3), 15)
        self.assertEqual(main.multiply(2, 3), 6)

    def test_subtraction(self):
        self.assertEqual(main.subtraction(10, 1), 7)
        self.assertEqual(main.subtraction(7, 2), 5)



