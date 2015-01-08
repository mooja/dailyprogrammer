#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#                          challenge 50 easy                          #
#######################################################################

import pytest

from challenge50easy import pick_two

@pytest.mark.parametrize('input,expected', [
    ((100, (5, 75, 25)),                   (2, 3)),
    ((200, (150,24,79,50,88,345,3)),       (1, 4)),
    ((8,   (2,1,9,4,4,56,90,3 )),          (4, 5))
])
def test_pick_two(input, expected):
    assert pick_two(*input) == expected
