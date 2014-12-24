#!/usr/bin/env python
# encoding: utf-8

from kata_linearfunction import *


def test_get_function():
    assert get_function([0, 1, 2, 3, 4]) == "f(x) = x"
    assert get_function([0, 3, 6, 9, 12]) == "f(x) = 3x"
    assert get_function([1, 4, 7, 10, 13]) == "f(x) = 3x + 1"
