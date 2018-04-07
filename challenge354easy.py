#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 354 easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/83uvey/20180312_challenge_354_easy_integer_complexity_1/
#
# 07 April 2018


from math import sqrt, ceil


def min_fact_sum2(n):
    """
    >>> min_fact_sum2(12)
    7
    >>> min_fact_sum2(12345)
    838
    >>> min_fact_sum2(4567)
    4568
    """
    for i in range(ceil(sqrt(n))+1, 0, -1):
        if n % i == 0:
            return i + n // i


if __name__ == '__main__':
    import doctest
    doctest.testmod()
