import unittest
from pyzz import pydate

class TestParsingDate(unittest.TestCase):
    def test_brazilian_date_formatt(self):
        self.assertTrue(pydate.is_valid_format('27/11/1983'))
        self.assertTrue(pydate.is_valid_format('26/05/2019 01:12:13'))
        self.assertFalse(pydate.is_valid_format('27/11/83'))
        self.assertFalse(pydate.is_valid_format('27/11/1983 01:12'))

    def test_iso_date_format(self):
        self.assertTrue(pydate.is_valid_format('1983-11-27'))
        self.assertTrue(pydate.is_valid_format('2011-10-11 15:12:30'))
        self.assertFalse(pydate.is_valid_format('83-11-27 15:15:15'))
        self.assertFalse(pydate.is_valid_format('1983-11-27 15:15'))
