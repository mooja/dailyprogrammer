#!/usr/bin/env python
# encoding: utf-8

import pytest

from challenge82easy import subs


@pytest.mark.parametrize("input, expected", [
    (3, sorted(['a', 'ab', 'abc', 'bc', 'b', 'c'])),
])
def test_subs(input, expected):
    assert subs(input) == expected
