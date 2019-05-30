import unittest
from pyzz import pydate

class TestParsingDate(unittest.TestCase):
    def test_parse_date_brazilian_standard(self):
        self.assertEqual(pydate.parse_date('2018-07-07'), 1)