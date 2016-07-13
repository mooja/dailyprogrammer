#!/usr/bin/env python
# encoding: utf-8

import pytest

from challenge77easy import morse


@pytest.mark.parametrize("input, expected", [
    (5, set(['.....', '...-', '..-.', '.-..', '-...', '.--', '-.-', '--.'])),
])
def test_morse(input, expected):
    assert morse(input) == expected
