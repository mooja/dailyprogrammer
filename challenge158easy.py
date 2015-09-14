#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 158 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/230m05/4142014_challenge_158_easy_the_torn_number/
#
# September.14.2015


def is_torn_number(n):
    """
    >>> is_torn_number(3025)
    True
    >>> is_torn_number(1000)
    False
    """
    n_str = '{:04}'.format(n)
    a = int(n_str[:2])
    b = int(n_str[2:])

    if (a + b)**2 == n:
        return True
    return False


if __name__ == '__main__':
    # print is_torn_number(3025)
    import doctest
    doctest.testmod()

    for i in xrange(1, 9999):
        if is_torn_number(i):
            print(i)
