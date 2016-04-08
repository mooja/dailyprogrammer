#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 102 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/10pf0j/9302012_challenge_102_easy_dice_roller/
#
# May.07.2015


# In tabletop role-playing games like Dungeons & Dragons, people use a system
# called dice notation to represent a combination of dice to be rolled to
# generate a random number. Dice rolls are of the form AdB (+/-) C, and are
# calculated like this:

# * Generate A random numbers from 1 to B and add them together.  * Add or
# subtract the modifier, C.

# * If A is omitted, its value is 1; if (+/-)C is omitted, step 2 is skipped.
# That is, "d8" is equivalent to "1d8+0".

# * Write a function that takes a string like "10d6-2" or "d20+7" and generates
# a random number using this syntax.

import re
import random

from random import choice


def unpackDiceNotation(dndstr):
    """ unpackDiceNotation: takes a string in form of DND notations and unpacks
                            values A, B, and C

    :dndcode: a string in the form of dnd notation
    :returns: a tuple of integers (A, B, C)

    >>> unpackDiceNotation('2d5-3')
    (2, 5, -3)
    >>> unpackDiceNotation('d10+5')
    (1, 10, 5)
    """

    m = re.match(r'(\d*)d(\d+)([+-]\d+)?', dndstr)
    if not m:
        raise ValueError("Bad DND Dice Notation Expression")
    A, B, C = m.groups()

    if A == '':  # if A is missing, set it to '1'
        A = '1'
    if C is None:
        C = '0'
    if C.startswith('+'):  # remove possible '+' before converting C to integer
        C = C[1:]

    return (int(A), int(B), int(C))


def generateRoll(A, B, C):
    """generateRoll: Generate Number from 1 to B and add C to the result, A
                     times

    :returns: integer result
    """

    i = 0
    total = 0
    while i < A:
        i += 1
        total += random.randrange(1, B+1) + C
    return total


def test_generateRoll():
    for i in range(10):
        n = generateRoll(1, 5, 5)
        assert 5 < n
        assert n <= 10


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print generateRoll(50000000, 100000000, -5)
