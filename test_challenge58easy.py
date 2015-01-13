#!/usr/bin/env python
# encoding: utf-8


import pytest


from challenge58easy import to_base


@pytest.mark.parametrize('input,expected', [
    ((2, 1), '1'),
    ((2, 2), '10'),
    ((2, 4), '100'),
    ((2, 9), '1001'),
    ((8, 1), '1'),
    ((8, 8), '10'),
    ((8, 9), '11'),
    ((36, 1), '1'),
    ((36, 36), '10'),
    ((36, 35), 'z'),
    ((36, 36 + 35), '1z'),
])
def test_to_base(input, expected):
    assert to_base(*input) == expected
