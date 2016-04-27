#!/usr/bin/env python3
# encoding: utf-8



# Daily Programmer Challenge 188 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2lvgz6/20141110_challenge_188_easy_yyyymmdd/
#
# 27.April.2016

import re
import fileinput


MONTH_MAP = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12,
}

FMT_REGEXPS = [
    re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'),
    re.compile(r'(?P<month>\d{2})/(?P<year>\d{2})/(?P<day>\d{2})'),
    re.compile(r'(?P<month>\d{2})#(?P<day>\d{2})#(?P<year>\d{2})'),
    re.compile(r'(?P<day>\d{2})\*(?P<month>\d{2})\*(?P<year>\d{4})'),
    re.compile(r'(?P<month>\w{3}) (?P<day>\d{2}), (?P<year>\d{2})'),
    re.compile(r'(?P<month>\w{3}) (?P<day>\d{2}), (?P<year>\d{4})'),
]

class UnknownFormatException(Exception): 
    pass

def parse_date(date_str):
    year, month, day = None, None, None
    for regexp in FMT_REGEXPS:
        m = regexp.match(date_str)
        if m is None:
            continue

        year = m.groupdict()['year']
        month = m.groupdict()['month']
        day = m.groupdict()['day']

        if len(year) == 2 and int(year) < 50:
            year = 2000 + int(year)
        if len(year) == 2 and int(year) >= 50:
            year = 1900 + int(year)
        year = int(year)

        if not month.isdigit():
            month = MONTH_MAP[month]
        month = int(month)

        day = int(day)

        return year, month, day

    raise UnknownFormatException('Couldn\'t parse the date format! {}'.fomrat(date_str))


if __name__ == '__main__':
    for line in fileinput.input(): 
        try:
            y, m, d = parse_date(line.strip())
            print('{:04}-{:02}-{:02}'.format(y, m, d))
        except UnknownFormatException:
            print('!!error: couldn\'t parse {}'.format(line.strip()))
