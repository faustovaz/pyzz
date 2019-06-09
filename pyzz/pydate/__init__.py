"""
pydate - A date calculator
Usage:
    pydate
    pydate <arg1> <op> <arg2>
    pydate <arg1> <op> <arg2> --formatted
    pydate -h | --help
Options:
    arg1                today | date
    op                  + (Only for nubers) | -
    arg2                number[d|w|m|y]
    -h,--help           Show this help message
"""
from __future__ import print_function
from docopt import docopt
from re import match
from datetime import datetime, date, timedelta
from calendar import monthrange

def is_iso_format(str_date):
    matched = match(r'^(\d{4})-(\d{2})-(\d{2})(\s(\d{2}):(\d{2}):(\d{2}))?$', 
                    str_date)
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
    matched = match(r'^(\d{2})/(\d{2})/(\d{4})(\s(\d{2}):(\d{2}):(\d{2}))?$', 
                    str_date)
    if matched:
        return {
            'day':      int(matched.group(1)),
            'month':    int(matched.group(2)),
            'year':     int(matched.group(3)),
            'hour':     int(matched.group(5)) if matched.group(5) else 0,
            'minute':   int(matched.group(6)) if matched.group(6) else 0,
            'second':   int(matched.group(7)) if matched.group(7) else 0,
        }
    return None

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
        matched = is_brazilian_format(formatted_date)
        if matched:
            return datetime(matched['year'], 
                            matched['month'], 
                            matched['day'], 
                            matched['hour'], 
                            matched['minute'], 
                            matched['second'])
        if formatted_date == 'today':
            today = datetime.today()
            return datetime(today.year, today.month, today.day)
        return None
    except ValueError:
        return None

def calculate_days(arg1, op, arg2):
    date = parse_date(arg1)
    matched = match(r'^(\d+)(d?)$', arg2)
    if date and matched:
        ammount = int(matched.group(1))
        arg2 = timedelta(days=ammount)
        return date + arg2 if op == '+' else date - arg2
    return None

def calculate_weeks(arg1, op, arg2):
    date = parse_date(arg1)
    matched = match(r'^(\d+)(w)$', arg2)
    if date and matched:
        ammount = int(matched.group(1))
        arg2 = timedelta(weeks=ammount)
        return date + arg2 if op == '+' else date - arg2
    return None

def calculate_months(arg1, op, arg2):
    date = parse_date(arg1)
    matched = match(r'^(\d+)(m)$', arg2)
    if date and matched:
        ammount = int(matched.group(1))
        month = date.month
        year = date.year

        if op == '+':
            total_months = month + ammount
            year = year + int(total_months / 12)
            month = int(total_months % 12)
        else:
            total = month - ammount
            month = (12 - int(abs(total) % 12)) if total <= 0 else total
            year = year - (int(abs(total) / 12) + 1) if total <= 0 else year
        last_month_day = monthrange(year, month)[1]

        day = last_month_day if date.day > last_month_day else date.day
        return datetime(year, month, day)
    return None

def calculate_years(arg1, op, arg2):
    date = parse_date(arg1)
    matched = match(r'^(\d+)(y)$', arg2)
    if date and matched:
        year = date.year
        ammount = int(matched.group(1))
        year = year + ammount if op == '+' else year - ammount 
        last_month_day = monthrange(year, date.month)[1]
        day = last_month_day if date.day > last_month_day else date.day
        return datetime(year, date.month, day)
    return None

def calculate_using_number(arg1, op, arg2):
    matched = match(r'^(\d+)([dwmy]?)$', arg2)
    if matched:
        range_time = matched.group(2)
        if not range_time or range_time == 'd':
            return calculate_days(arg1, op, arg2)
        if range_time == 'w':
            return calculate_weeks(arg1, op, arg2)
        if range_time == 'm':
            return calculate_months(arg1, op, arg2)
        if range_time == 'y':
            return calculate_years(arg1, op, arg2)
    return None

def calculate_using_date(arg1, op, arg2):
    arg1, arg2 = parse_date(arg1), parse_date(arg2)
    if arg1 and arg2:
        delta = arg1 -  arg2 if op == '-' else None
        return delta
    return None

def calculate(arg1, op, arg2):
    if match(r'^(\d+)([dwmy]?)$', arg2):
        return calculate_using_number(arg1, op, arg2)
    if parse_date(arg2):
        return calculate_using_date(arg1, op, arg2)
    return None

def main():
    args = docopt(__doc__)

    if args['<arg1>']:
        d = calculate(args['<arg1>'], args['<op>'], args['<arg2>'])
        if isinstance(d, datetime):
            if args['--formatted']:
                return print(d.strftime('%Y-%m-%d %H:%M:%S'))
            return print(d.strftime('%d/%m/%Y %H:%M:%S'))
        if isinstance(d, timedelta):
            days = d.days
            return print('{} {}'.format(days, 'day'if days == 1 else 'days'))
        return print('pydate bad arguments. To see options: pydate -h')

    return print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
