#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 223 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/3d4fwj/20150713_challenge_223_easy_garland_words/
#
# 31 May 2016


def garland(word):
    """
    >>> garland("programmer")
    0
    >>> garland("ceramic")
    1
    >>> garland("onion")
    2
    >>> garland("alfalfa")
    4
    """
    n = 0
    for i in range(1, len(word)):
        if word[:i] == word[-i:]:
            n = i
    return n

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    max_garland_deg = 0
    max_garland_word = ''
    with open("enable1.txt", 'r') as f:
        for line in f:
            word = line.strip()
            if garland(word) > max_garland_deg:
                max_garland_deg = garland(word)
                max_garland_word = word

    print('biggiest garland ({}): {}'.format(max_garland_deg, max_garland_word))
