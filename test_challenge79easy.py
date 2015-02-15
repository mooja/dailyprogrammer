#!/usr/bin/env python
# encoding: utf-8


import pytest

from challenge79easy import step_count


@pytest.mark.parametrize("input, expected", [
    ((18.75, -22.0, 5), [18.75, 8.5625, -1.625, -11.8125, -22.0]),
    ((-5.75, 12.00, 5), [-5.75, -1.3125, 3.125, 7.5625, 12.0]),
    ((13.50, -20.75, 3), [13.5, -3.625, -20.75]),
])
def test_step_count(input, expected):
    assert step_count(*input) == expected
