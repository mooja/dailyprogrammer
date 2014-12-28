#!/usr/bin/env python
# encoding: utf-8

from collections import Counter
from math import factorial


def listPosition(word):
    index = 1

    for i, letter in enumerate(word):
        size = len(word[i:])
        alphabet = sorted(word[i:])

        num_perms = factorial(size)
        num_perms /= reduce(lambda x,y: x*y,
            [factorial(j) for j in Counter(word[i:]).values()])

        index += alphabet.index(letter)*(num_perms/size)

    return index
