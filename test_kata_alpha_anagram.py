#!/usr/bin/env python
# encoding: utf-8

import pytest

from kata_alpha_anagram import *


TEST_DATA = {'A': 1,
             'ABAB': 2,
             'AAAB': 1,
             'BAAA': 4,
             'QUESTION': 24572,
             'BOOKKEEPER': 10743}

@pytest.mark.parametrize("input,expected", TEST_DATA.iteritems())
def test_listPosition(input, expected):
    assert listPosition(input) == expected
