"""
Sample tests
"""

from django.test import SimpleTestCase # type: ignore
from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(5, 11)
        self.assertEqual(res, 6)