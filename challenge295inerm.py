#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 295 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/5ijb4z/20161215_challenge_295_intermediate_seperated/
#
# 02 January 2017

from itertools import permutations
from string import ascii_lowercase, ascii_uppercase


def properly_seperated(s):
    """
    >>> properly_seperated('abcABC')
    True
    >>> properly_seperated('acbBCA')
    False
    """
    for idx, ch in enumerate(s):
        prev_ch = s[idx-1]
        next_ch = s[(idx+1) % len(s)]
        if ch.lower() in (prev_ch.lower(), next_ch.lower()):
            return False
    return True


def is_rotation_of(s1, s2):
    """
    >>> is_rotation_of('abc', 'bca')
    True
    >>> is_rotation_of('abc', 'acb')
    False
    """
    rotations = []
    for i in range(len(s1)):
        rot = [s1[j % len(s1)] for j in range(i, i+len(s1))]
        rotations.append(''.join(rot))
    return s2 in rotations


def n_arrangements(ncouples):
    s = ascii_lowercase[:ncouples] + ascii_uppercase[:ncouples]
    found = []
    for perm in filter(properly_seperated, permutations(s)):
        perm = ''.join(perm)
        if any(is_rotation_of(perm, s1) for s1 in found):
            continue
        found.append(perm)
    return len(found)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    for n in range(1, 4):
        print('{} couples = {} arrangements'.format(n, n_arrangements(n)))
