#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#                       challenge60easy tests                         #
#######################################################################

import pytest

from challenge60easy import is_polite


@pytest.mark.parametrize('input,expected', [
    (2, False),
    (3, True),
    (4, False),
    (5, True),
    (16, False),
    (30, True),
    (50, True),
])
def test_is_polite(input, expected):
    assert is_polite(input) == expected


@pytest.mark.parametrize('input,expected', [
    (2, False),
    (3, True),
    (4, False),
    (5, True),
    (16, False),
    (30, True),
    (50, True),
])
def test_is_polite_alt(input, expected):
    assert is_polite(input) == expected
