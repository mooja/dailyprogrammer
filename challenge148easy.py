#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 148 Easy
#
# url
#
# June.23.2015


def spin_distance(N, a, b, c):
    """
    >>> spin_distance(5, 1, 2, 3)
    21
    """
    return 3 * N + a + (a - b) % N + (c - b) % N


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    N, a, b, c = map(int, raw_input.strip().split())
    print spin_distance(N, a, b, c)
