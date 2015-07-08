#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 149 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/1ystvb/022414_challenge_149_easy_disemvoweler/
#
# July.08.2015

import re


def disemvowel(word):
    """
    >>> disemvowel('two drums and a cymbal fall off a cliff')
    ('twdrmsndcymblfllffclff', 'ouaaaaoai')
    """
    vowels = re.sub(r'[^aeiou]', '', word)
    disemvoweled = re.sub(r'[aeiou\s]', '', word)
    return (disemvoweled, vowels)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
