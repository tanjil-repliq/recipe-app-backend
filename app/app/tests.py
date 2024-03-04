"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test calc module"""

    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)

    def test_multiply_numbers(self):
        """Test multiply numbers"""
        res = calc.multiply(5, 2)
        self.assertEqual(res, 10)

    def test_divide_numbers(self):
        res = calc.divide(6, 2)
        self.assertEqual(res, 3)
