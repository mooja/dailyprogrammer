#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 129 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1g0tw1/easy_longest_twocharacter_substring/
#
# June.05.2015

from itertools import combinations


def longest2charsubstr(s):
    """ longest2charsubstr: return longest substring that has at most two
                            different characters 
        >>> longest2charsubstr('a')
        'a'
        >>> longest2charsubstr('abc')
        'ab'
        >>> longest2charsubstr('abb')
        'abb'
        >>> longest2charsubstr('abbccc')
        'bbccc'
        >>> longest2charsubstr('qwertyytrewq')
        'tyyt'
    """
    if len(s) <= 2:
        return s
    return sorted([s[i1:i2] for i1, i2 in combinations(range(len(s)+1), r=2)
                            if len(set(s[i1:i2])) < 3],
                  key=len,
                  reverse=True)[0]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
