"""
pycpf - Generate random CPF
Usage:
    pycpf
    pycpf -v | --validate <cpf>
    pycpf -u | --unformatted
Options:
    -h,--help          Show this help message
    -v,--validate      Validate a given CPF
    -u,--unformatted   Generate a non formatted cpf
"""

from docopt import docopt
from random import randint
from functools import reduce
from re import match

def _first_digit(sequence):
    mapped_values = map(lambda x,y: x*y, list(range(10, 1, -1)), sequence)
    digit = abs((reduce(lambda x,y: x + y, mapped_values) % 11) - 11)
    return 0 if digit > 9 else digit

def _second_digit(sequence):
    values = map(lambda x,y: x*y, list(range(11, 2, -1)), sequence)
    digit = reduce(lambda x,y: x + y, values) + (_first_digit(sequence) * 2)
    digit = abs((digit % 11) - 11)
    return 0 if digit > 9 else digit

def cpf():
    random_sequence = [randint(0,9) for i in range(9)]
    random_sequence.append(_first_digit(random_sequence))
    random_sequence.append(_second_digit(random_sequence))
    return ''.join(str(num) for num in random_sequence)

def formattedCpf():
    _cpf = cpf()
    return '{}.{}.{}-{}'.format(_cpf[0:3], _cpf[3:6], _cpf[6:9], _cpf[9:])

def is_a_valid_cpf_format(given_cpf):
    cpf_re = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return match(cpf_re, given_cpf) or match(r'^\d{11}$', given_cpf)

def is_a_valid_cpf(given_cpf):
    if is_a_valid_cpf_format(given_cpf):
        given_cpf = given_cpf.replace('.','').replace('-','')
        given_cpf = [int(d) for d in given_cpf]
        first_digit = _first_digit(given_cpf[0:-2])
        second_digit = _second_digit(given_cpf[0:-2])
        return given_cpf[-2:] == [first_digit, second_digit]
    return False

def validate_cpf(given_cpf):
    if is_a_valid_cpf(given_cpf):
        return '{} is a valid cpf.'.format(given_cpf)
    else:
        return '{} is not a valid cpf.'.format(given_cpf)

def main():
    args = docopt(__doc__)

    if args['--unformatted']:
        return print(cpf())

    if args['--validate']:
        return print(validate_cpf(args.get('<cpf>')))

    print(formattedCpf())

if __name__ == "__main__":
    main()
