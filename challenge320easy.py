#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 320 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/6i60lr/20170619_challenge_320_easy_spiral_ascension/

from itertools import cycle
from pprint import pprint


def move(x, y, x_vec, y_vec):
    return x+x_vec, y+y_vec

def draw_square(n=5):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    counter = 1
    directions = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])
    direction = next(directions)
    while counter <= n*n:
        grid[y][x] = counter
        counter += 1
        x, y = move(x, y, *direction)

        try:
            position_empty = grid[y][x] == 0
            if not position_empty: raise IndexError
        except IndexError:
            x -= direction[0]
            y -= direction[1]
            direction = next(directions)
            x, y = move(x, y, *direction)

    rv = ''
    ndigits = len(str(n*n))
    for row in grid:
        line = ''
        for col in row:
            line += "{0:>{1}} ".format(col, ndigits)
        rv += line+"\n"
    return rv

print(draw_square(16))
