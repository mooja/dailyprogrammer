#!/usr/bin/env python3
# encoding: utf-8



# Daily Programmer Challenge 180 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2ggy30/9152014_challenge180_easy_looknsay/
#
# 17.April.2016


from itertools import groupby
from functools import lru_cache


@lru_cache(None)
def looknsay(n):
    """
    >>> looknsay(1)
    1
    >>> looknsay(2)
    11
    >>> looknsay(3)
    21
    >>> looknsay(4)
    1211
    >>> looknsay(5)
    111221
    """
    if n == 1: return 1

    prev_str = str(looknsay(n-1))
    result = []
    for (k, group) in groupby(prev_str):
        result.append(str(len(list(group))))
        result.append(k)

    return int(''.join(result))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
