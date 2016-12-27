#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 294 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/
#
# 27 December 2016


def scrabble(letters, word):
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
    letters = list(letters)
    for ch in word:
        if ch not in letters and '?' not in letters:
            return False
        if ch not in letters:
            letters.remove('?')
        else:
            letters.remove(ch)
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
