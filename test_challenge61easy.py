#!/usr/bin/env python
# encoding: utf-8

import pytest

from challenge61easy import bin_rotate
from challenge61easy import bin_rotate_seq


@pytest.mark.parametrize('input, expected', [
    ((19, 1), 25),
    ((19, 2), 28),
    ((19, 3), 14),
])
def test_bin_rotate(input, expected):
    assert bin_rotate(*input) == expected


@pytest.mark.parametrize('input, expected', [
    (69, (69, 98, 49, 56, 28, 14, 7)),
    (205, (205, 230, 115, 121, 124, 62, 31)),
    (357, (357, 434, 217, 236, 118, 59, 61, 62, 31)),
])
def test_bin_rotate_seq(input, expected):
    assert bin_rotate_seq(input) == expected
