#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 294 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/
#
# 27 December 2016


def scrabble(tiles, word):
    """
    >>> scrabble("ladilmy", "daily")
    True
    >>> scrabble("eerriin", "eerie")
    False
    >>> scrabble("orrpgma", "program")
    True
    >>> scrabble("orppgma", "program")
    False
    >>> scrabble("pizza??", "pizzazz")
    True
    >>> scrabble("piizza?", "pizzazz")
    False
    >>> scrabble("a??????", "program")
    True
    >>> scrabble("b??????", "program")
    False
    """
    tiles = list(tiles)
    for ch in word:
        if ch not in tiles and '?' not in tiles:
            return False
        if ch not in tiles:
            tiles.remove('?')
        else:
            tiles.remove(ch)
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    inputs = [
        "dcthoyueorza",
        "uruqrnytrois",
        "rryqeiaegicgeo??",
        "udosjanyuiuebr??",
        "vaakojeaietg????????"
    ]

    with open('enable1.txt') as f:
        dictionary = [l.strip() for l in f]

    def longest(tiles):
        longest_found = None
        for word in dictionary:
            if scrabble(tiles, word):
                try:
                    if len(longest_found) < len(word):
                        longest_found = word
                except TypeError:
                    longest_found = word
        return longest_found

    for inp in inputs:
        print('longest("{}") -> "{}"'.format(inp, longest(inp)))
