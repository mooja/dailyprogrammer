#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 69 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/vmblw/6262012_challenge_69_easy/
# 
#
# Write a program that takes a title and a list as input and outputs the
# list in a nice column. Try to make it so the title is centered. For
# example:
#
# title: 'Necessities'
# input: ['fairy', 'cakes', 'happy', 'fish', 'disgustipated', 'melon-balls']
#
# output:
#
#     +---------------+
#     |  Necessities  |
#     +---------------+
#     | fairy         |
#     | cakes         |
#     | happy         |
#     | fish          |
#     | disgustipated |
#     | melon-balls   |
#     +---------------+
# 
# 15.January.26

import pytest


from challenge69easy import columnize
@pytest.mark.parametrize("input, expected", [
    (('Necessities', ['fairy', 'cakes', 'happy', 'fish', 'disgustipated',
        'melon-balls']), (
            "+---------------+\n"
            "|  Necessities  |\n"
            "+---------------+\n"
            "| fairy         |\n"
            "| cakes         |\n"
            "| happy         |\n"
            "| fish          |\n"
            "| disgustipated |\n"
            "| melon-balls   |\n"
            "+---------------+\n"
    )),
])
def test_columnize(input, expected):
    assert columnize(*input) == expected
