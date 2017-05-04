#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 313 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/68oda5/20170501_challenge_313_easy_subset_sum/
#
# 04 May 2017

from itertools import combinations


def subset_sum(seq):
    """
    >>> subset_sum([-83314, -82838, -80120, -63468, -62478, -59378, -56958,\
        -50061, -34791, -32264, -21928, -14988, 23767, 24417, 26403, 26511,\
        36399, 78055])
    False
    >>> subset_sum([-97162, -95761, -94672, -87254, -57207, -22163, -20207,\
        -1753, 11646, 13652, 14572, 30580, 52502, 64282, 74896, 83730, 89889,\
        92200])
    True
    """
    for r in range(1, len(seq)+1):
        for combination in combinations(seq, r=r):
            if sum(combination) == 0:
                return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
