#!/usr/bin/env python
# encoding: utf-8

import pytest

from challenge52easy import merge_lists


@pytest.mark.parametrize('input,expected', [
    (([], []), []),
    (([1,5,7,8], [2,3,4,7,9]), [1,2,3,4,5,7,7,8,9]),
])
def test_merge_lists(input, expected):
    assert merge_lists(*input) == expected
