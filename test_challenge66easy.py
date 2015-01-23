#!/usr/bin/env python
# encoding: utf-8

import pytest


from challenge66easy import cmp_roman
@pytest.mark.parametrize("input, expected", [
    (('I', 'II'), True),
    (('II', 'II'), False),
    (('X', 'X'), False),
    (('XX', 'XX'), False),
    (('XX', 'XXVI'), True),
    (('X', 'XI'), True),
])
def test_cmp_roman(input, expected):
    assert cmp_roman(*input) == expected
