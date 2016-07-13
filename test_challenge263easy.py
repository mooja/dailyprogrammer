#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from challenge263easy import shannon_entropy

@pytest.mark.parametrize(['inp', 'expected'],[
    ('122333444455555666666777777788888888', 2.79),
    ('563881467447538846567288767728553786', 2.79),
    ('https://www.reddit.com/r/dailyprogrammer', 4.06),
    ('int main(int argc, char *argv[])', 3.87)
])
def test_shannon_entropy(inp, expected):
    assert shannon_entropy(inp) == expected
