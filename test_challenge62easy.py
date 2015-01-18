#!/usr/bin/env python
# encoding: utf-8

from challenge62easy import ullmans_puzzle

import pytest


def test_ullmans_puzzle_true():
    assert ullmans_puzzle(2, 2, [0, 0, 1]) == True


def test_ullmans_puzzle_false():
    assert ullmans_puzzle(2, 3, [5, 5, 5]) == False


@pytest.mark.parametrize('input, expected', [
    ((98.2, 3, [18.1, 55.1, 91.2, 74.6, 73.0, 85.9, 73.9, 81.4, 87.1, 49.3, 88.8, 5.7, 26.3, 7.1, 58.2, 31.7, 5.8, 76.9, 16.5, 8.1, 48.3, 6.8, 92.4, 83.0, 19.6]), True),
])
def test_ullmans_puzzle(input, expected):
    assert ullmans_puzzle(*input) == expected
