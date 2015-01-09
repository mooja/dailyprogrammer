#!/usr/bin/env python
# encoding: utf-8

import pytest

from challenge51easy import word_value


@pytest.mark.parametrize('input,expected', [
    ('hat', 29),
    ('shoe', 47),
])
def test_wordvalue(input, expected):
    assert word_value(input) == expected
