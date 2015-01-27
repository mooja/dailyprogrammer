#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 4 Intermediate
#
# http://www.reddit.com/r/dailyprogrammer/comments/pm6sq/2122012_challenge_4_intermediate/
#
# create a calculator program that will take an input, following normal
# calculator input (5*5+4) and give an answer (29). This calculator should
# use all four operators.
#
# January.27.2015

import pytest

from challenge4interm import tokenize
from challenge4interm import calculate


@pytest.mark.parametrize("input, expected", [
    ('2+2+3', [2, '+', 2, '+', 3]),
    ('22 + 23 * 3/2', [22, '+', 23, '*', 3, '/', 2]),
])
def test_tokenize(input, expected):
    assert tokenize(input) == expected


@pytest.mark.parametrize("input, expected", [
    ('5*5+4', 29),
])
def test_calculate(input, expected):
    assert calculate(input) == expected
