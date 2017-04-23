#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Daily Programmer Challenge 311 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/65vgkh/20170417_challenge_311_easy_jolly_jumper/
#
# 23 April 2017


def is_jolly(seq):
    """
    >>> is_jolly([1, 4, 2, 3])
    True
    >>> is_jolly([4, 1, 2, 3])
    False
    """
    if len(seq) == 1:
        return True

    differences = []
    for idx in range(0, len(seq)-1):
        differences.append(abs(seq[idx] - seq[idx+1]))

    target_sequence = list(range(1, len(seq)))
    return set(differences) == set(target_sequence)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import fileinput
    for line in fileinput.input():
        sequence = [int(x) for x in line.strip().split()][1:]
        if is_jolly(sequence):
            print(sequence, 'JOLLY')
        else:
            print(sequence, 'NOT JOLLY')
