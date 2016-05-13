#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 205 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2ygsxs/20150309_challenge_205_easy_friendly_date_ranges/
#
# 13 May 2016

import fileinput


from datetime import date, datetime
from collections import namedtuple


PrettyDate = namedtuple('PrettyDate', ['day', 'month', 'year'])


def humanize_day(day_num):
    """
    >>> humanize_day(1)
    '1st'
    >>> humanize_day(2)
    '2nd'
    >>> humanize_day(11)
    '11th'
    >>> humanize_day(31)
    '31st'
    """
    if 11 <= day_num <= 13:
        suffix = 'th'
    else:
        r = day_num % 10
        if r == 1:
            suffix = 'st'
        elif r == 2:
            suffix = 'nd'
        elif r == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    return str(day_num) + suffix

def pretty_date(date_):
    """
    >>> pretty_date(date(2000, 1, 1))
    PrettyDate(day='1st', month='January', year='2000')
    """
    day_str = humanize_day(date_.day)
    month_str = date_.strftime('%B')
    year_str = date_.strftime('%Y')
    return PrettyDate(day_str, month_str, year_str)

def pretty_date_range(d1, d2):
    """
    >>> pretty_date_range(date(2016, 1, 2), date(2016, 3, 1))
    'January 2nd - March 1st'
    >>> pretty_date_range(date(2000, 1, 1), date(2002, 3, 2))
    'January 1st, 2000 - March 2nd, 2002'
    >>> pretty_date_range(date(2015, 1, 2), date(2015, 3, 1))
    'January 2nd - March 1st, 2015'
    """
    d1_pretty = pretty_date(d1)
    d2_pretty = pretty_date(d2)

    # same date this year
    if d1 == d2 and d1.year == date.today().year:
        return '{d.month} {d.day}'.format(d=pd1)
    # same date
    if d1 == d2:
        return '{d.month} {d.day}, {d.year}'.format(d=d1_pretty)

    # same years this year
    if d1.year == d2.year and d1.year == date.today().year:
        pd1 = '{d.month} {d.day}'.format(d=d1_pretty)
        pd2 = '{d.month} {d.day}'.format(d=d2_pretty)
    # same year
    elif d1.year == d2.year:
        pd1 = '{d.month} {d.day}'.format(d=d1_pretty)
        pd2 = '{d.month} {d.day}, {d.year}'.format(d=d2_pretty)
    # different years
    else:
        pd1 = '{d.month} {d.day}, {d.year}'.format(d=d1_pretty)
        pd2 = '{d.month} {d.day}, {d.year}'.format(d=d2_pretty)

    pretty_range = '{pd1} - {pd2}'.format(pd1=pd1, pd2=pd2)
    return pretty_range


def main():
    for line in fileinput.input():
        line = line.strip()
        d1 = datetime.strptime(line.split()[0], '%Y-%m-%d')
        d2 = datetime.strptime(line.split()[1], '%Y-%m-%d')
        if (d2 - d1).seconds < 0:
            print('{} is a negative range'.format(line))
        print(pretty_date_range(d1, d2))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    main()
