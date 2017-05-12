#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 314 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/6aefs1/20170510_challenge_314_intermediate_comparing/
#
# 12 May 2017


from operator import itemgetter


def rotate_string(s, n):
    return s[n:] + s[:n]


def find_minimal_rot(s):
    """
    >>> find_minimal_rot('onion')
    (2, 'ionon')
    >>> find_minimal_rot('bbaaccaadd')
    (2, 'aaccaaddbb')
    >>> find_minimal_rot('alfalfa')
    (6, 'aalfalf')
    >>> find_minimal_rot('weugweougewoiheew')
    (14, 'eewweugweougewoih')
    """
    candidates = []
    for idx in range(0, len(s)):
        candidates.append((idx, rotate_string(s, idx)))
    return min(candidates, key=itemgetter(1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
