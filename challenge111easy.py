#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 111 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/12qi5b/1162012_challenge_111_easy_star_delete/
#
# May.15.2015


import re


def star_delete(text):
    """
    >>> star_delete('adf*lp')
    'adp'
    >>> star_delete('*dech*')
    'ec'
    >>> star_delete('sa*n*ti')
    'si'
    """

    return re.sub(r'.?\*.?', '', text)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
