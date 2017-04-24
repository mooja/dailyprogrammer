#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 307 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/60ibay/20170320_challenge_307_easy_base_255_part1/
#
# 24 April 2017

import re


def encode1(arr):
    """
    >>> encode1(['abc+def', 'ghij', 'klmno++p+'])
    'abc++def+,ghij+,klmno++++p++'
    """
    rv = ''
    for item in arr:
        if rv != '':
            rv += '+,'
        for char in item:
            if char == '+':
                rv += '++'
            else:
                rv += char
    return rv


def decode1(s):
    """
    >>> decode1('abc++def+,ghij+,klmno++++p++')
    ['abc+def', 'ghij', 'klmno++p+']
    """
    rv = []
    idx = 0
    item = ''
    while True:
        try:
            if s[idx:idx+2] == '+,':
                rv.append(item)
                item = ''
                idx += 2
            elif s[idx:idx+2] == '++':
                item += '+'
                idx += 2
            else:
                item += s[idx]
                idx += 1
        except IndexError:
            rv.append(item)
            break
    return rv


if __name__ == "__main__":
    import doctest
    doctest.testmod()
