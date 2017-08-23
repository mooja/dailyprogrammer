#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 328 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/6vi9ro/170823_challenge_328_intermediate_pyramid_sliding/
#
# 23 August 2017


def sum_shortest(pyramid):
    num_levels = len(pyramid)
    for row_idx in reversed(range(num_levels)):
        for col_idx, element in enumerate(pyramid[row_idx]):
            if row_idx == num_levels-1:
                continue
            child1 = pyramid[row_idx+1][col_idx]
            child2 = pyramid[row_idx+1][col_idx+1]
            pyramid[row_idx][col_idx] = element + min([child1, child2])
    return pyramid[0][0]

if __name__ == '__main__':
    with open("pyramid3.txt") as f:
        f.readline()  # discard num levels
        pyramid = [line.strip().split() for line in f.readlines()]
        pyramid = [list(map(int, row)) for row in pyramid]
        print(sum_shortest(pyramid))
