#!/usr/bin/env python
# encoding: utf-8

from kata_alphabet_converter import *


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


def test_convert():
    Alphabet = {
        "BINARY":        '01',
        "OCTAL":         '01234567',
        "DECIMAL":       '0123456789',
        "HEXA_DECIMAL":  '0123456789abcdef',
        "ALPHA_LOWER":   'abcdefghijklmnopqrstuvwxyz',
        "ALPHA_UPPER":   'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        "ALPHA":         'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
        "ALPHA_NUMERIC": '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    }

    bin = Alphabet["BINARY"]
    oct = Alphabet["OCTAL"]
    dec = Alphabet["DECIMAL"]
    hex = Alphabet["HEXA_DECIMAL"]
    allow = Alphabet["ALPHA_LOWER"]
    alup = Alphabet["ALPHA_UPPER"]
    alpha = Alphabet["ALPHA"]
    alnum = Alphabet["ALPHA_NUMERIC"]

    assert convert("15", dec, bin) == '1111'
    assert convert("15", dec, oct) == '17'
    assert convert("1010", bin, dec) == '10'
    assert convert("1010", bin, hex) == 'a'
    assert convert("0", dec, alpha) == 'a'
    assert convert("27", dec, allow) == 'bb'
    assert convert("hello", allow, hex) == '320048'
    assert convert("SAME", alup, alup) == 'SAME'
