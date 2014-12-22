#!/usr/bin/env python
# encoding: utf-8

import string

def alphadigit2decimaldigit(alphadigit, alphabet=string.ascii_uppercase):
    n = alphabet.index(alphadigit)
    return n

def alphanum2decimalnum(alphanum, alphabet=string.ascii_uppercase):
    base = len(alphabet)
    result = 0
    for i, digit in enumerate(alphanum[::-1]):
        result += alphadigit2decimaldigit(digit, alphabet=alphabet) * (base**i)
    return result

def decimalnum2alphanum(decimalnum, alphabet=string.ascii_uppercase):
    base = len(alphabet)
    result = []

    while decimalnum >= base:
        result.insert(0, alphabet[decimalnum % base])
        decimalnum = decimalnum / base
    result.insert(0, alphabet[decimalnum])

    return ''.join(result)

def convert(input, source, target):
    decimal = alphanum2decimalnum(input, alphabet=source)
    translated = decimalnum2alphanum(decimal, alphabet=target)
    return translated
