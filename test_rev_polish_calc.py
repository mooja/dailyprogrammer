#!/usr/bin/env python
# encoding: utf-8

from rev_polish_calc import calc


def test_calc():
    assert calc("") == 0
    assert calc("1 2 3") == 3
    assert calc("1 2 3.5") == 3.5
    assert calc("1 3 +") == 4
    assert calc("1 3 *") == 3
    assert calc("1 3 -") == -2
    assert calc("4 2 /") == 2
