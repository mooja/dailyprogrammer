#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 353 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/826coe/20180305_challenge_353_easy_closest_string/
#
# 09 April 2018


def hamming_distance(seq1, seq2):
    """
    >>> hamming_distance('aaa', 'bbb')
    3
    >>> hamming_distance('abc', 'aaa')
    2
    """
    if len(seq1) != len(seq2):
        raise ValueError("Strings should be the same length")
    total = 0
    for (c1, c2) in zip(seq1, seq2):
        if c1 != c2:
            total += 1
    return total


def hamming_center(seqs):
    """
    >>> seqs = ['CTCCATCACAC', 'AATATCTACAT', 'ACATTCTCCAT', 'CCTCCCCACTC']
    >>> hamming_center(seqs)
    'AATATCTACAT'
    """
    def by_distance(seq):
        return sum(hamming_distance(seq, seq2) for seq2 in seqs)
    return sorted(seqs, key=by_distance)[0]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
