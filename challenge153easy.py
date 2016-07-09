#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 153 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/20l2it/17042014_challenge_153_easy_pascals_pyramid/
#
# September.10.2015


from functools import wraps
from math import factorial


def memoize(f):
    memo = {}

    @wraps(f)
    def f_(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return f_


factorial = memoize(factorial)


@memoize
def tri_coeff(n, i, j, k):
    return factorial(n) / (factorial(i) * factorial(j) * factorial(k))
