#!/usr/bin/env python
# encoding: utf-8


import pytest


from challenge80easy import anagrams


@pytest.mark.parametrize("input, expected", [
    ('LEPROUS', ["PELORUS", "SPORULE"]),
    ("AMBLERS", ["BLAMERS", "LAMBERS", "MARBLES", "RAMBLES"]),

])
def test_anagrams(input, expected):
    assert anagrams(input) == expected
