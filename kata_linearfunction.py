#!/usr/bin/env python
# encoding: utf-8


def sign(n):
    if n < 0:
        return '-'
    else:
        return '+'


def get_function(seq):
    offset = seq[0]
    factor = seq[1] - seq[0]

    for i, n in enumerate(seq):
        if n != (i*factor + offset):
            return 'None-linear sequence'

    output = 'f(x) = '
    if factor != 0:
        if factor < 0:
            output = output + '-'
        if abs(factor) != 1:
            output = output + str(abs(factor))
        output = output + 'x'
    if offset:
        output = output + ' {} {}'.format(sign(offset), abs(offset))

    return output
