#!/usr/bin/env python
# encoding: utf-8

from challenge31easy import alphadigit2decimaldigit
from challenge31easy import alphanum2decimalnum
from challenge31easy import decimalnum2alphanum


def test_alphadigit2decimaldigit():
    assert alphadigit2decimaldigit('A') == 0
    assert alphadigit2decimaldigit('B') == 1
    assert alphadigit2decimaldigit('Z') == 25


def test_alphanum2decimalnum():
    assert alphanum2decimalnum('A') == 0
    assert alphanum2decimalnum('AA') == 0
    assert alphanum2decimalnum('B') == 1
    assert alphanum2decimalnum('BA') == 26
    assert alphanum2decimalnum('CA') == 26 * 2


def test_decimalnum2alphanum():
    assert decimalnum2alphanum(2, '0123456789') == '2'
    assert decimalnum2alphanum(200, '0123456789') == '200'
    assert decimalnum2alphanum(2000, '0123456789') == '2000'
