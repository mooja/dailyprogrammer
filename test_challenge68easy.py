#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 68 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/vmblw/6262012_challenge_69_easy/
#
# An emirp ("prime" spelled backwards) is a prime whose (base 10) reversal
# is also prime, but which is not a palindromic prime. The first few are 13,
# 17, 31, 37, 71, 73, 79, 97, 107, 113, 149, 157, ... (OEIS A006567). A
# binary plot of the emirps is illustrated above.
#
# Emirp is an interesting concept. The explanation about it is provided in
# the link i just gave.

# Your task is to implement a function which prints out the emirps below a
# number(input) given by the user.
#
# 15.January.25

import pytest

from challenge68easy import is_emirp
from challenge68easy import gen_emirps
from challenge68easy import is_prime
from challenge68easy import is_palindrome


@pytest.mark.parametrize("input, expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
])
def test_is_prime(input, expected):
    assert is_prime(input) == expected


@pytest.mark.parametrize("input, expected", [
    (1, True),
    (2, True),
    (10, False),
    (11, True),
    (21, False),
    (22, True),
])
def test_is_palindrome(input, expected):
    assert is_palindrome(input) == expected


@pytest.mark.parametrize("input, expected", [
    (13, True),
    (17, True),
    (31, True),
    (3, False),
    (4, False),
    (14, False),
    (19, False),
])
def test_is_emirp(input, expected):
    assert is_emirp(input) == expected


@pytest.mark.parametrize("input, expected", [
    (100, [13, 17, 31, 37, 71, 73, 79, 97]),
])
def test_gen_emirps(input, expected):
    assert gen_emirps(input) == expected
