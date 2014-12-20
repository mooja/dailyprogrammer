#!/usr/bin/env python
# encoding: utf-8


import pytest


def get_century(year):
    def is_leap(year):
        if not year % 4 == 0:
            return False
        if not year % 100 == 0:
            return True
        if not year % 400 == 0:
            return False
        return True

    def century(y):
        return ((y-1) / 100) + 1

    return century(year), is_leap(year)


@pytest.mark.parametrize("input,expected", [
    (1996, (20, True)),
    (1900, (19, False)),
])
def test_get_century(input, expected):
    assert get_century(input) == expected


if __name__ == '__main__':
    pytest.main(str(__file__))
