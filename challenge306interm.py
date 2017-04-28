#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 306 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/5zj7e4/20170315_challenge_306_intermediate_gray_code/
#
# 28 April 2017


def gray_seq(nbits):
    seqsize = 2**nbits
    rv = [[0]*nbits for _ in range(seqsize)]
    pattern = [0, 1, 1, 0]
    for i in range(nbits):
        for k in range(len(rv)):
            rv[k][-(i+1)] = pattern[k % (len(pattern))]

        new_pattern = []
        for digit in pattern:
            new_pattern.append(digit)
            new_pattern.append(digit)
        pattern = new_pattern

    rv = [''.join(map(str, row)) for row in rv]
    return '\n'.join(rv)


print(gray_seq(16))
