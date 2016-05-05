#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 197 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2s7ezp/20150112_challenge_197_easy_isbn_validator/
#
# 05.May.2016

import re
import random


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


def generate_isbn():
    """
    >>> all(isbn_is_valid(generate_isbn()) for _ in range(10))
    True
    """
    remainder = None
    while remainder != 0:
        random_digits = [random.randint(0, 9) for _ in range(10)]
        digits_isbn_sum = sum(n*(10-i) for i, n in enumerate(random_digits))
        remainder = digits_isbn_sum % 11
    isbn_str = '{}-{}{}{}{}-{}{}{}{}-{}'.format(*random_digits)
    return isbn_str


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    for i in range(10):
        print(generate_isbn())
