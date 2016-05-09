#!/usr/bin/env python3
# encoding: utf-8


# Daily Programmer Challenge 201 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2vc5xq/20150209_challenge_201_easy_counting_the_days/
#
# 09.May.2016

import fileinput
import datetime


def main():
    now = datetime.date.today()
    for l in fileinput.input():
        y, m, d = l.strip().split()
        date = datetime.date(int(y), int(m), int(d))
        delta = date - now
        print('{ndays} day(s) from {ty} {tm} {td} to {fy} {fm} {fd}'.format(
            ndays=delta.days,
            ty=now.year, tm=now.month, td=now.day,
            fy=date.year, fm=date.month, fd=date.day,
        ))

if __name__ == '__main__':
    main()
