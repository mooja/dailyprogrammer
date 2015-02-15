#!/usr/bin/env python
# encoding: utf-8


import pytest


from challenge78easy import key2char
@pytest.mark.parametrize("input, expected", [
    ({'key': 'a', 'caps': False, 'shift': False}, 'a'),
    ({'key': 'a', 'caps': False, 'shift': True},  'A'),
    ({'key': 'a', 'caps': True,  'shift': False}, 'A'),
    ({'key': 'a', 'caps': True,  'shift': True},  'a'),
    ({'key': '7', 'caps': False, 'shift': True},  '&'),
])
def test_key2char(input, expected):
    assert key2char(**input) == expected
