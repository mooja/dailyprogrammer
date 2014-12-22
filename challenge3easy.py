#!/usr/bin/env python

import string


def rotchar(c, n):
    if c not in string.ascii_letters:
        return c
    offset = ord('a') if c in string.ascii_lowercase else ord('A')
    r = (ord(c) + n - offset) % 26
    return chr(r + offset)


def rotn(n, data):
    def rot(c):
        return rotchar(c, n)
    return "".join(map(rot, data))
