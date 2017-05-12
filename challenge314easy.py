#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 314 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/69y21t/20170508_challenge_314_easy_concatenated_integers/
#
# 11 May 2017

from functools import cmp_to_key


def concatSorted(ints, reverse=False):
    """
    >>> concatSorted([79, 82, 34, 83, 69])
    '3469798283'
    >>> concatSorted([79, 82, 34, 83, 69], reverse=True)
    '8382796934'
    """
    def conc_compare(a, b):
        if len(str(a)) != len(str(b)):
            return len(str(a)) - len(str(b))
        return a - b

    ints = sorted(ints, key=cmp_to_key(conc_compare), reverse=reverse)
    return ''.join(str(n) for n in ints)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
