#!/usr/bin/env python3
# encoding: utf-8

# daily programmer challenge 174 easy
#
# url: https://www.reddit.com/r/dailyprogrammer/comments/2cld8m/8042014_challenge_174_easy_thuemorse_sequences/

import sys
import string


table = str.maketrans('01', '10')
def boolean_complement(s):
    return s.translate(table)

cache = {}
def thue_morse(n):
    """
    >>> thue_morse(0)
    '0'
    >>> thue_morse(1)
    '01'
    >>> thue_morse(2)
    '0110'
    """
    if n == 0:
        return '0'
    if n not in cache:
        cache[n] = ''.join([thue_morse(n - 1),  boolean_complement(thue_morse(n - 1))])
    return cache[n]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    order = 6
    if len(sys.argv) > 1:
        order = int(sys.argv[1])

    print('nth     sequence')
    print('===========================================================================')

    for i in range(order):
        print('{:>4}      {}'.format(i, thue_morse(i)))
