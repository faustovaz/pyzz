import unittest
from pyzz import pycnpj


class TestPycpf(unittest.TestCase):
    def test_valid_cpf_format(self):
        self.assertTrue(pycnpj.is_a_valid_cnpj_format('63.374.914/0001-32'))
        self.assertTrue(pycnpj.is_a_valid_cnpj_format('98.596.537/0001-60'))
        self.assertTrue(pycnpj.is_a_valid_cnpj_format('75397291000100'))
        self.assertTrue(pycnpj.is_a_valid_cnpj_format('52770315000111'))

    def test_valid_cpf(self):
        self.assertTrue(pycnpj.is_a_valid_cnpj('48.926.331/0001-83'))
        self.assertTrue(pycnpj.is_a_valid_cnpj('88.903.683/0001-38'))
        self.assertTrue(pycnpj.is_a_valid_cnpj('62.675.344/0001-58'))
        self.assertTrue(pycnpj.is_a_valid_cnpj('21550986000143'))
        self.assertTrue(pycnpj.is_a_valid_cnpj('77318979000175'))

    def test_validate_cnpj(self):
        self.assertEquals(pycnpj.validate_cnpj('71.322.454/0001-27'),
                          '71.322.454/0001-27 is a valid cnpj.')
        self.assertEquals(pycnpj.validate_cnpj('16.187.148/0001-17'),
                          '16.187.148/0001-17 is a valid cnpj.')
        self.assertEquals(pycnpj.validate_cnpj('86362378000150'),
                          '86362378000150 is a valid cnpj.')
        self.assertEquals(pycnpj.validate_cnpj('43.401.364/0001-95'),
                          '43.401.364/0001-95 is not a valid cnpj.')
        self.assertEquals(pycnpj.validate_cnpj('35527827000187'),
                          '35527827000187 is not a valid cnpj.')
        self.assertEquals(pycnpj.validate_cnpj('73.520.655/0001.64'),
                          '73.520.655/0001.64 is not a valid cnpj.')


    def test_generated_cpf(self):
        self.assertTrue(pycnpj.is_a_valid_cnpj(pycnpj.cnpj()))
        self.assertTrue(pycnpj.is_a_valid_cnpj(pycnpj.cnpj()))
        self.assertTrue(pycnpj.is_a_valid_cnpj(pycnpj.cnpj()))

    def test_formatted_generated_cpf(self):
        self.assertTrue(pycnpj.is_a_valid_cnpj(pycnpj.formatted_cnpj()))
        self.assertTrue(pycnpj.is_a_valid_cnpj(pycnpj.formatted_cnpj()))
        self.assertTrue(pycnpj.is_a_valid_cnpj(pycnpj.formatted_cnpj()))

    def test_invalid_cpf(self):
        self.assertFalse(pycnpj.is_a_valid_cnpj('47.566.523/0001-62'))
        self.assertFalse(pycnpj.is_a_valid_cnpj('26.631.463/0001-34'))
        self.assertFalse(pycnpj.is_a_valid_cnpj('74.152.556/0001-66'))
        self.assertFalse(pycnpj.is_a_valid_cnpj(''))
        self.assertFalse(pycnpj.is_a_valid_cnpj('17734126000166'))
