#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 147 Easy
#
# url
#
# June.23.2015


def is_valid_score(score):
    """
    >>> is_valid_score(2)
    False
    >>> is_valid_score(3)
    True
    >>> is_valid_score(4)
    True
    >>> is_valid_score(5)
    False
    >>> is_valid_score(6)
    True
    """

    q, r = divmod(score, 3)

    if not q:
        return False
    if r == 2 and q < 2:
        return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    score = input()
    print is_valid_score(score)
