#!/usr/bin/env python
# encoding: utf-8



# Daily Programmer Challenge 183 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/3o4tpz/weekly_24_mini_challenges/
#
# 22.April.2016


def grab(fname, s):
    with open(fname, 'rU') as f:
        for line in (l for l in f if s in l):
            yield line


def to_base_n(base, n):
    """
    >>> to_base_n(4, 987)
    '33123'
    """
    result = ''
    while n:
        result = str(n % base) + result
        n = n // base
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
