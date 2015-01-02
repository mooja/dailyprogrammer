#!/usr/bin/env python
# encoding: utf-8

import pytest

from rev_polish_calc import calc


@pytest.mark.xfail
def test_calc():
    n = 'this is a local variable'
    assert calc("") == 0
    assert calc("1 2 3") == 3
    assert calc("1 2 3.5") == 3.5
    assert calc("1 3 +") == 4
    assert calc("1 3 *") == 3
    assert calc("1 3 -") == -2
    assert calc("4 2 /") == 2
    assert 0
