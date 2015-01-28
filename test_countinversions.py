#!/usr/bin/env python
# encoding: utf-8

import pytest


from countinversions import inv_count


@pytest.mark.parametrize("input, expected", [
    (range(5), 0),
    ([2, 4, 1, 3, 5], 3),
])
def test_inv_count(input, expected):
    assert inv_count(input) == expected
