import unittest
from pyzz import pydate
from datetime import datetime, timedelta

class TestParsingDate(unittest.TestCase):

    def test_parse_iso_date(self):
        self.assertEqual(pydate.parse_date('1983-11-27'), datetime(1983,11,27))
        self.assertEqual(pydate.parse_date('2018-02-24 14:57:00'),
                        datetime(2018, 2, 24, 14, 57, 0))
        self.assertEqual(pydate.parse_date('2018-02-32'), None)

    def test_parse_brazilian_date(self):
        self.assertEqual(pydate.parse_date('18/06/2018'), datetime(2018,6,18))
        self.assertEqual(pydate.parse_date('01/05/2019 14:12:12'), 
                        datetime(2019, 5, 1, 14, 12, 12))
        self.assertEqual(pydate.parse_date('28/13/2019'), None)

class TestCalculateDate(unittest.TestCase):

    def test_calculate_days(self):
        self.assertEqual(pydate.calculate('27/11/1983', '+', '3d'),
                        datetime(1983, 11, 30))
        self.assertEqual(pydate.calculate('1983-11-27', '+', '4'),
                        datetime(1983, 12, 1))
        self.assertEqual(pydate.calculate('2019-05-01', '-', '1'),
                        datetime(2019, 4, 30))
        self.assertEqual(pydate.calculate('02/02/2018', '-', '2d'),
                        datetime(2018, 1, 31))

    def test_calculate_months(self):
        self.assertEqual(pydate.calculate('01/06/2019', '+', '2m'),
                        datetime(2019, 8, 1))
        self.assertEqual(pydate.calculate('31/12/2018', '+', '2m'),
                        datetime(2019, 2, 28))
        self.assertEqual(pydate.calculate('2015-10-31', '+', '4m'),
                        datetime(2016, 2, 29))
        self.assertEqual(pydate.calculate('01/04/2018', '-', '20m'),
                        datetime(2016, 8, 1))
        self.assertEqual(pydate.calculate('01/02/2019', '-', '4m'),
                        datetime(2018, 10, 1))
        self.assertEqual(pydate.calculate('01/04/2019', '-', '2m'),
                        datetime(2019, 2, 1))
        self.assertEqual(pydate.calculate('01/01/2015', '-', '1m'),
                        datetime(2014, 12, 1))
        self.assertEqual(pydate.calculate('2019-12-01', '-', '12m'),
                        datetime(2018, 12, 1))
        self.assertEqual(pydate.calculate('27/11/1983', '-', '77m'),
                        datetime(1977, 6, 27))
    
    def test_calculate_years(self):
        self.assertEqual(pydate.calculate('01/06/2019', '+', '2y'),
                        datetime(2021, 6, 1))
        self.assertEqual(pydate.calculate('31/12/2018', '+', '2y'),
                        datetime(2020, 12, 31))
        self.assertEqual(pydate.calculate('2016-02-29', '+', '3y'),
                        datetime(2019, 2, 28))
        self.assertEqual(pydate.calculate('2016-02-29', '-', '6y'),
                         datetime(2010, 2, 28))

    def test_calculate_dates(self):
        self.assertEqual(pydate.calculate('1984-11-27', '-', '1983-11-27'),
                        timedelta(days=366))
        self.assertEqual(pydate.calculate('20/10/2018', '-', '19/10/2018'),
                        timedelta(days=1))
