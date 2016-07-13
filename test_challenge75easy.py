#!/usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import

import pytest


from challenge75easy import math2c


@pytest.mark.parametrize("input, expected", [  # noqa
    ('L0(x,y)=abs(x)+abs(y)', 'float L0(float x,float y)\n{\n    return'
                              ' fabsf(x)+fabsf(y)\n}'),
])
def test_math2c(input, expected):
    assert math2c(input) == expected
