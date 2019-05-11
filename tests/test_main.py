import unittest
import pyzz

class TestPyzz(unittest.TestCase):
    def test_pyzz(self):
        self.assertEqual(pyzz.main(), "Just starting...")
