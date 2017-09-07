
from src.tools.converter import Converter
import unittest

class ConverterTest(unittest.TestCase):

    def test_is_number_with_commas(self):
        num = "1,234.23"
        self.assertTrue(Converter.is_number_with_commas(num))

    def test_string_with_commas_to_float(self):
        num = "1,234.23"
        number = Converter.string_with_commas_to_float(num)
        self.assertTrue(float(number))