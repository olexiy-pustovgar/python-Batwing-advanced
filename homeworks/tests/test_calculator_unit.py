import unittest
from functions_to_test import Calculator


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(10, -10), 0)
        self.assertEqual(Calculator.add(-10, -10), -20)
        self.assertEqual(Calculator.add(20, -10), 10)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, -10), 20)
        self.assertEqual(Calculator.subtract(-10, -10), 0)
        self.assertEqual(Calculator.subtract(20, -10), 30)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(100, 0), 0)
        self.assertEqual(Calculator.multiply(12, 12), 144)

    def test_divide(self):
        self.assertRaises(ValueError, Calculator.divide, 23, 0)
        self.assertEqual(Calculator.divide(20, -4), -5)
