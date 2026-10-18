"""Unit tests for the Python Calculator module."""

import unittest
from calculator import add, subtract, multiply, divide, calculate


class TestCalculator(unittest.TestCase):
    """Test suite covering arithmetic operations and edge cases."""

    def test_add(self):
        """Test addition with positive, negative, and decimal numbers."""
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-4, -6), -10)
        self.assertEqual(add(-5, 12), 7)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self):
        """Test subtraction with positive, negative, and decimal numbers."""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(-3, -7), 4)
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3, places=7)

    def test_multiply(self):
        """Test multiplication including zero and negative numbers."""
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-3, 6), -18)
        self.assertEqual(multiply(-2, -5), 10)
        self.assertEqual(multiply(100, 0), 0)
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    def test_divide(self):
        """Test division with whole and fractional results."""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 2), 4.5)
        self.assertEqual(divide(-12, 3), -4)
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        """Ensure dividing by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError) as context:
            divide(10, 0)
        self.assertIn("Division by zero", str(context.exception))

    def test_calculate_function(self):
        """Test calculate() dispatcher with symbols, numbers, and aliases."""
        self.assertEqual(calculate("+", 10, 20), 30)
        self.assertEqual(calculate("1", 10, 20), 30)
        self.assertEqual(calculate("add", 10, 20), 30)

        self.assertEqual(calculate("-", 20, 5), 15)
        self.assertEqual(calculate("*", 6, 7), 42)
        self.assertEqual(calculate("/", 20, 4), 5)

    def test_calculate_invalid_operation(self):
        """Test that invalid operation input raises ValueError."""
        with self.assertRaises(ValueError):
            calculate("%", 10, 3)
        with self.assertRaises(ValueError):
            calculate("power", 2, 3)

    def test_calculate_zero_division(self):
        """Test that calculate() raises ZeroDivisionError when dividing by zero."""
        with self.assertRaises(ZeroDivisionError):
            calculate("/", 5, 0)


if __name__ == "__main__":
    unittest.main()
