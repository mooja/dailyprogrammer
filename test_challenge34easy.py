#!/usr/bin/env python
# encoding: utf-8

from challenge34easy import *


def test_two_largest_squared():
    assert two_largest_squared(1, 1, 1) == 2
    assert two_largest_squared(1, 2, 2) == 8
    assert two_largest_squared(2, 3, 5) == 34
