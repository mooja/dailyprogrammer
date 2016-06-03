#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 226 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/3fmke1/20150803_challenge_226_easy_adding_fractions/
#
# 03 June 2016

import fileinput

from functools import reduce
from collections import namedtuple


Fraction = namedtuple('Fraction', ['n', 'd'])

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def add_fractions(a, b):
    common_d = a.d * b.d

    # convert to same denominator before adding
    a_multiplier = common_d // a.d 
    b_multiplier = common_d // b.d

    a = Fraction(a.n * a_multiplier, a.d * a_multiplier)
    b = Fraction(b.n * b_multiplier, b.d * b_multiplier)
    c = Fraction(a.n + b.n, a.d)

    # reduce the result
    common_divisor = gcd(c.n, c.d)
    c = Fraction(c.n // common_divisor, c.d // common_divisor)

    return c

def main():
    fractions = []
    for line in fileinput.input():
        numerator = int(line.strip().split('/')[0])
        denominator = int(line.strip().split('/')[1])
        fractions.append(Fraction(numerator, denominator))

    sum_fraction = reduce(add_fractions, fractions)
    print('{fract.n}/{fract.d}'.format(fract=sum_fraction))

if __name__ == "__main__":
    main()
