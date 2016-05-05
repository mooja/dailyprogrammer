#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 197 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2s7ezp/20150112_challenge_197_easy_isbn_validator/
#
# 05.May.2016

import re


def isbn_is_valid(isbn_str):
    """ 
    >>> isbn_is_valid('0-7475-3269-9')
    True
    >>> isbn_is_valid('1-7475-3269-9')
    False
    """
    digits = [int(d) for d in isbn_str.replace('-', '')]
    for i, n in enumerate(digits):
        digits[i] = n*(10-i)
    return sum(digits) % 11 == 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
