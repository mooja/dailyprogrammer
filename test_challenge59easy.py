#!/usr/bin/env python
# encoding: utf-8

import pytest

from challenge59easy import find_substring


@pytest.mark.parametrize('input, expected', [
    (('hello', 'hello world'), 0),
    (('are', 'how are you today?'), 4),
    (('this', 'in this string'), 3),
    (('not', 'in this string'), -1),
])
def test_find_substring(input, expected):
    assert find_substring(*input) == expected
