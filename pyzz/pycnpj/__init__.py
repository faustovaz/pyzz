"""
pycnpj - Generate random CNPJ numbers
Usage:
    pycnpj
    pycnpj -v | --validate <cnpj>
    pycnpj -u | --unformatted
Options:
    -h,--help          Show this help message
    -v,--validate      Validate a given CNPJ
    -u,--unformatted   Generate a non formatted CPNJ
"""
from __future__ import print_function
from docopt import docopt
from re import match
from functools import reduce
from random import randint

def _first_digit(sequence):
    multipliers = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    # list(map(...)) Python 2 and 3 compatible
    values = list(map(lambda x,y: x * y, sequence, multipliers))
    digit = reduce(lambda x,y: x + y, values) % 11
    return 0 if digit < 2 else 11 - digit

def _second_digit(sequence):
    multipliers = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    # list(map(...)) Python 2 and 3 compatible
    values = list(map(lambda x, y: x * y, sequence, multipliers))
    digit = reduce(lambda x, y: x + y, values) % 11
    return 0 if digit < 2 else 11 - digit

def is_a_valid_cnpj_format(cnpj):
    cpnj_re = r'^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$'
    return match(cpnj_re, cnpj) or match(r'^\d{14}$', cnpj)

def is_a_valid_cnpj(cnpj):
    if is_a_valid_cnpj_format(cnpj):
        cnpj = cnpj.replace('.','').replace('/','').replace('-', '')
        cnpj = [int(n) for n in cnpj]
        first_digit = _first_digit(cnpj[:-2])
        second_digit = _second_digit(cnpj[:-2] + [first_digit])
        return cnpj[-2:] == [first_digit, second_digit]
    return False

def validate_cnpj(cnpj):
    if is_a_valid_cnpj(cnpj):
        return '{} is a valid cnpj.'.format(cnpj)
    return '{} is not a valid cnpj.'.format(cnpj)

def cnpj():
    base = [randint(0,9) for i in range(8)] + [0, 0, 0, 1]
    first_digit = _first_digit(base)
    second_digit = _second_digit(base + [first_digit])
    base = base + [first_digit, second_digit]
    return ''.join(str(n) for n in base)

def formatted_cnpj():
    _cnpj = cnpj()
    return '{}.{}.{}/{}-{}'.format(_cnpj[0:2], 
                                    _cnpj[2:5], 
                                    _cnpj[5:8],
                                    _cnpj[8:12], 
                                    _cnpj[12:])

def main():
    args = docopt(__doc__)

    if args['--unformatted']:
        return print(cnpj())

    if args['--validate']:
        return print(validate_cnpj(args.get('<cnpj>')))

    print(formatted_cnpj())
