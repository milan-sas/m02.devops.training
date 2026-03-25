import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(calculator.square_root(16), 4)

    # --- modulo ---
    def test_modulo(self):
        self.assertEqual(calculator.modulo(10, 3), 1)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.modulo(10, 0)

    # --- is_even ---
    def test_is_even_true(self):
        self.assertTrue(calculator.is_even(4))

    def test_is_even_false(self):
        self.assertFalse(calculator.is_even(7))

    def test_is_even_zero(self):
        self.assertTrue(calculator.is_even(0))

    # --- is_positive ---
    def test_is_positive_true(self):
        self.assertTrue(calculator.is_positive(5))

    def test_is_positive_false(self):
        self.assertFalse(calculator.is_positive(-1))

    def test_is_positive_zero(self):
        self.assertFalse(calculator.is_positive(0))

    # --- factorial ---
    def test_factorial_zero(self):
        self.assertEqual(calculator.factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(calculator.factorial(5), 120)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            calculator.factorial(-1)

    # --- edge cases for existing functions ---
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            calculator.square_root(-4)

    def test_multiply_negative(self):
        self.assertEqual(calculator.multiply(-3, 4), -12)

    def test_power_zero_exponent(self):
        self.assertEqual(calculator.power(5, 0), 1)


if __name__ == "__main__":
    unittest.main()
