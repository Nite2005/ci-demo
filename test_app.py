import unittest
from app import add, sub, mul

class TestMathFunctions(unittest.TestCase):


    def test_add(self):
        self.assertEqual(add(4,5), 9)
        self.assertEqual(add(3,4), 7)


    def test_sub(self):
        self.assertEqual(sub(5,4), 1)
        self.assertEqual(sub(9,5), 4)


    def test_mul(self):
        self.assertEqual(mul(1, 2), 2)
        self.assertEqual(mul(2, 2), 4)


if __name__ == '__main__':
    unittest.main()

