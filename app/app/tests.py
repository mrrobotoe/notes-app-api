"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Testing adding the numbers together."""
        res = calc.add(4, 7)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""

        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
