#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 315 Intermediate



def xor_mult(a, b):
    rv = 0
    b_str = '{:b}'.format(b)
    for bin_digit in reversed(b_str):
        if bin_digit == '1':
            rv = rv ^ a
        a = a << 1
    return rv
