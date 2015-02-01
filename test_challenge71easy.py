#!/usr/bin/env python
# encoding: utf-8


import pytest

from challenge71easy import pytriples


@pytest.mark.parametrize("input, expected", [
    (240, {(15, 112, 113), (40, 96, 104), (48, 90, 102), (60, 80, 100)}),
])
def test_pytriples(input, expected):
    assert pytriples(input) == expected
