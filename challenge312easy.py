#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 312 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/67dxts/20170424_challenge_312_easy_l33tspeak_translator/
#
# 25 April 2017


m = {
    'A': '4',
    'B': '6',
    'E': '3',
    'L': '1',
    'M': '(V)',
    'N': '(\)',
    'O': '0',
    'S': '5',
    'T': '7',
    'V': '\/',
    'W': '`//'
}


def encode(text):
    """
    >>> encode('storm')
    '570R(V)'
    """
    rv = ''
    for char in text.upper():
        if char in m:
            rv += m[char]
        else:
            rv += char
    return rv


def decode(text):
    """
    >>> decode('31337')
    'eleet'
    """
    for k, v in m.items():
        text = text.replace(v, k).lower()
    return text


if __name__ == "__main__":
    import doctest
    doctest.testmod()
