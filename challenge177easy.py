#!/usr/bin/env python
# encoding: utf-8



# Daily Programmer Challenge 177 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2ejl4x/8252014_challenge_177_easy_quicksort/
#
# 14.April.2016

import random
 

def qsort(seq):
    """
    >>> qsort([5, 3, 2, 1, 4])
    [1, 2, 3, 4, 5]
    >>> qsort([5, 3, 4, 1, 2])
    [1, 2, 3, 4, 5]
    """

    if len(seq) <= 1:
        return seq

    pivot_val = random.choice(seq)
    seq1 = list(filter(lambda x: x <= pivot_val, seq))
    seq2 = list(filter(lambda x: x > pivot_val, seq))
    seq1 = qsort(seq1)
    seq2 = qsort(seq2)

    return seq1 + seq2



if __name__ == '__main__':
    import doctest
    doctest.testmod()
