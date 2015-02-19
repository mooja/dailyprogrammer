#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 5 Intermediate
#
# http://www.reddit.com/r/dailyprogrammer/comments/pnhtj/2132012_challenge_5_intermediate/
#
# Your challenge today is to write a program that can find the amount of
# anagrams within a .txt file. For example, "snap" would be an anagram of
# "pans", and "skate" would be an anagram of "stake".
#
#
# February.03.2015


import pytest

from challenge5interm import nanagrams


@pytest.mark.parametrize("input, expected", [
    ('one two three', 0),
    ('one eno eno three', 1),
    ('one eno two three eerht', 2),
])
def test_nanagrams(input, expected):
    input = input.strip().split()
    assert nanagrams(input) == expected
