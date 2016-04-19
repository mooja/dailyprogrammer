#!/usr/bin/env python3
# encoding: utf-8


# Daily Programmer Challenge 181 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2h5b2k/09222014_challenge_181_easy_basic_equations/
#
# 18.April.2016

import re


def intercept_point(a, c, b, d):
    """
    solves intercept point for equations y = ax + c and y = bx + d
    >>> intercept_point(-5, 0, -4, 1)
    (-1.0, 5.0)
    >>> intercept_point(2, 2, 5, -4)
    (2.0, 6.0)
    """
    x = (d - c) / (a - b)
    y = (a*d - b*c) / (a - b)
    return (x, y)


def parse_equation(eq):
    """
    >>> parse_equation('y = 2x + 1')
    (2.0, 1.0)
    """
    m = re.match(r'y\s*=\s*(-?\d+)x\s*\+\s*(-?\d+)', eq)
    if not m:
        raise Exception("couldn't parse!")

    return (float(m.group(1)), float(m.group(2)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    eq1 = 'y = 2x + 2'
    eq2 = 'y = 5x + -4'

    (a, c) = parse_equation(eq1)
    (b, d) = parse_equation(eq2)
    print(intercept_point(a, c, b, d))

