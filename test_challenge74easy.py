#!/usr/bin/env python
# encoding: utf-8

import pytest

from challenge74easy import fib
from challenge74easy import zeck_repr


@pytest.mark.parametrize("input, expected", [
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
])
def test_fib(input, expected):
    assert fib(input) == expected


@pytest.mark.parametrize("input, expected", [  # noqa
    (100, '89+8+3'),
])
def test_zeck_repr(input, expected):
    assert zeck_repr(input) == expected
