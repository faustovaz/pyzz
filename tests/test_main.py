import unittest
import pyzz

class TestPyzz(unittest.TestCase):
    def test_pyzz(self):
        self.assertEqual(pyzz.pyzz(), "pyzz - A tool belt for the shell.")
