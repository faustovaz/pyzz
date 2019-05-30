"""
pydate - A date calculator
Usage:
    <Usage here>
Options:
    <Describe options here>
"""
from __future__ import print_function
from docopt import docopt
from re import match

def is_valid_format(str_date):
    br_standard = r'^\d{2}/\d{2}/\d{4}(\s\d{2}:\d{2}:\d{2})?$'
    iso_standard = r'^\d{4}-\d{2}-\d{2}(\s\d{2}:\d{2}:\d{2})?$'
    return match(br_standard, str_date) or match(iso_standard, str_date)

def parse_date(formatted_date):
    pass
    

def main():
    #args = docopt(__doc__)
    pass

if __name__ == '__main__':
    main()
