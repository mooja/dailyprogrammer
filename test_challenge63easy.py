#!/usr/bin/env python
# encoding: utf-8

import pytest

from challenge63easy import reverse_subseq


@pytest.mark.parametrize('input, expected', [
    ((3, range(5)), [2, 1, 0, 3, 4]),
    ((2, range(2)), [1, 0]),
])
def test_reverse_subseq(input, expected):
    assert reverse_subseq(*input) == expected
