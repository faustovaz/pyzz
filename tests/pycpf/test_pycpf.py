import unittest
from pyzz import pycpf

class TestPycpf(unittest.TestCase):
    def test_valid_cpf_format(self):
        self.assertTrue(pycpf.is_a_valid_cpf_format('900.405.870-29'))
        self.assertTrue(pycpf.is_a_valid_cpf_format('90040587029'))

    def test_valid_cpf(self):
        self.assertTrue(pycpf.is_a_valid_cpf('374.085.480-41'))
        self.assertTrue(pycpf.is_a_valid_cpf('37408548041'))

    def test_validate_cpf(self):
        self.assertEqual(pycpf.validate_cpf('997.324.590-34'), \
                        '997.324.590-34 is a valid cpf.')
        self.assertEqual(pycpf.validate_cpf('67405489001'), \
                        '67405489001 is a valid cpf.')

    def test_generated_cpf(self):
        self.assertTrue(pycpf.is_a_valid_cpf(pycpf.cpf()))
        self.assertTrue(pycpf.is_a_valid_cpf(pycpf.cpf()))
        self.assertTrue(pycpf.is_a_valid_cpf(pycpf.cpf()))

    def test_formatted_generated_cpf(self):
        self.assertTrue(pycpf.is_a_valid_cpf(pycpf.formattedCpf()))
        self.assertTrue(pycpf.is_a_valid_cpf(pycpf.formattedCpf()))
        self.assertTrue(pycpf.is_a_valid_cpf(pycpf.formattedCpf()))

    def test_invalid_cpf(self):
        self.assertFalse(pycpf.is_a_valid_cpf('997.324.590-35'))
        self.assertFalse(pycpf.is_a_valid_cpf('997.324.590.34'))
        self.assertFalse(pycpf.is_a_valid_cpf('997324590-34'))
        self.assertFalse(pycpf.is_a_valid_cpf(''))
        self.assertFalse(pycpf.is_a_valid_cpf('997324590345'))



