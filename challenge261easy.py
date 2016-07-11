#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 261 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/
#
# 11 July 2016

from itertools import chain, permutations

def is_magic_square(grid):
    """
    >>> is_magic_square([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
    True
    >>> is_magic_square([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
    True
    >>> is_magic_square([[3, 5, 7], [8, 1, 6], [4, 9, 2]])
    False
    >>> is_magic_square([[8, 1, 6], [7, 5, 3], [4, 9, 2]])
    False
    """
    rows = [row for row in grid]
    cols = [[row[c] for row in rows] for c in range(len(grid))]
    diagonal1 = [grid[i][i] for i in range(len(grid))]
    diagonal2 = [grid[len(grid)-i-1][i] for i in range(len(grid))]
    lines = chain(rows, cols, [diagonal1, diagonal2])
    for line in lines:
        if sum(line) != 15:
            return False
    return True

def can_be_magic_square(incomplete_grid):
    """
    >>> can_be_magic_square([[8, 1, 6], [3, 5, 7]])
    True
    >>> can_be_magic_square([[3, 5, 7], [8, 1, 6]])
    False
    """
    grid_numbers = chain(*incomplete_grid)
    missing_numbers = list(set(range(1, 10)) - set(grid_numbers))
    for perm in permutations(missing_numbers, 3):
        grid_candidate = [row for row in incomplete_grid]
        grid_candidate.append(perm)
        if is_magic_square(grid_candidate):
            return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
