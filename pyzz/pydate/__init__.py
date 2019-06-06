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
from datetime import datetime


BR_STANDARD =  r'^(\d{2})/(\d{2})/(\d{4})(\s(\d{2}):(\d{2}):(\d{2}))?$'
ISO_STANDARD = r'^(\d{4})-(\d{2})-(\d{2})(\s(\d{2}):(\d{2}):(\d{2}))?$'

def is_iso_format(str_date):
    matched = match(ISO_STANDARD, str_date)
    if matched:
        return {
            'year':     int(matched.group(1)),
            'month':    int(matched.group(2)),
            'day':      int(matched.group(3)),
            'hour':     int(matched.group(5)) if matched.group(5) else 0,
            'minute':   int(matched.group(6)) if matched.group(6) else 0,
            'second':   int(matched.group(7)) if matched.group(7) else 0,
        }
    return None

def is_brazilian_format(str_date):
    return match(BR_STANDARD, str_date)

def is_valid_format(str_date):
     return is_iso_format(str_date) or is_brazilian_format(str_date)

def parse_date(formatted_date):
    try:
        matched = is_iso_format(formatted_date)
        if matched:
            return datetime(matched['year'], 
                            matched['month'], 
                            matched['day'], 
                            matched['hour'], 
                            matched['minute'], 
                            matched['second'])
        if is_brazilian_format(formatted_date):
            pass
        return None
    except ValueError:
        return None
    

def main():
    #args = docopt(__doc__)
    pass

if __name__ == '__main__':
    main()
