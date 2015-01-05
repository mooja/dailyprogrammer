#!/usr/bin/env python
# encoding: utf-8

import pytest

from challenge48easy import partition_evens


@pytest.mark.parametrize('input,expected', [
    ([1, 1, 2, 2, 2, 2], [2, 2, 2, 2, 1, 1]),
    ([1, 2], [2, 1]),
    ([0, 0, 1], [0, 0, 1])
])
def test_partition_evens(input, expected):
    assert partition_evens(input) == expected
