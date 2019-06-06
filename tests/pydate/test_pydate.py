import unittest
from pyzz import pydate
from datetime import datetime

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

    def test_parse_iso_date(self):
        self.assertEqual(pydate.parse_date('1983-11-27'), 
                        datetime(1983, 11, 27))
        self.assertEqual(pydate.parse_date('2018-02-24 14:57:00'),
                        datetime(2018, 2, 24, 14, 57, 0))
        self.assertEqual(pydate.parse_date('2018-02-32'), None)