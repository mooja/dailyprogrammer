#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 121 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/19mn2d/030413_challenge_121_easy_bytelandian_exchange_1/
#
# May.26.2015


#  very brute memoization function (to avoid stack overflow)
def memoize(func):
    cache = {}

    def new_func(arg):
        if arg in cache:
            return cache[arg]

        result = func(arg)
        cache[arg] = result
        return result

    return new_func


@memoize
def zero_count(n):
    """ zero_count: return a maximum number of 0-coints you can get from n-valued coin
        >>> zero_count(0)
        1
        >>> zero_count(1)
        3
        >>> zero_count(2)
        5
    """
    if n == 0:
        return 1
    return sum((zero_count(n / 2), zero_count(n / 3), zero_count(n / 4)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print "A 1000-valued coin will produce {} 0-coins.".format(zero_count(1000))
