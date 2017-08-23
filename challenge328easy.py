#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 328 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/6v29zk/170821_challenge_328_easy_latin_squares/
#
# 22 August 2017

import math
from itertools import chain


def is_latin_square(width, numbers):
    def rows():
        for row_idx in range(width):
            start = row_idx*width
            end = start + width
            yield numbers[start:end]

    def cols():
        for col_idx in range(width):
            yield [numbers[i*width + col_idx] for i in range(width)]

    target = list(range(1, width+1))
    for vector in chain(cols(), rows()):
        if sorted(vector) != target:
            return False
    return True


if __name__ == '__main__':
    data = input().strip()
    data = data.split()
    data = list(map(int, data))
    width = int(math.sqrt(len(data)))
    print(is_latin_square(width, data))
