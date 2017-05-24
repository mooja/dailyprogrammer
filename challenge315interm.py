#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 315 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/6bumxo/20170518_challenge_315_intermediate_game_of_life/
#
# 20 May 2017

from time import sleep
from array import array
from itertools import product


class ConwayGrid(object):
    def __init__(self, gridstr):
        m = {'.': 0, '#': 1}
        self.grid = []
        for line in gridstr.split('\n'):
            row = array('i', (m[ch] for ch in line))
            self.grid.append(row)
        self._update_neighbors()

    def _update_neighbors(self):
        self.neighbours_grid = [
            array('b', (0 for c in row))
            for row in self.grid
        ]

        for row_idx in range(len(self.grid)):
            for col_idx in range(len(self.grid[0])):
                if not self.grid[row_idx][col_idx]:
                    continue
                for r in range(row_idx-1, row_idx+2):
                    for c in range(col_idx-1, col_idx+2):
                        if r < 0 or r >= len(self.grid):
                            continue
                        if c < 0 or c >= len(self.grid[0]):
                            continue
                        if r == row_idx and c == col_idx:
                            continue
                        self.neighbours_grid[r][c] += self.grid[row_idx][col_idx]

    def _get_num_neighbors(self, row, col):
        return self.neighbours_grid[row][col]

    def next(self):
        nrows = len(self.grid)
        ncols = len(self.grid[0])
        for row_idx, col_idx in product(range(nrows), range(ncols)):
            is_alive = bool(self.grid[row_idx][col_idx])
            num_neighbors = self._get_num_neighbors(row_idx, col_idx)
            if is_alive:
                if num_neighbors < 2 or num_neighbors > 3:
                    self.grid[row_idx][col_idx] = 0
            else:
                if num_neighbors == 3:
                    self.grid[row_idx][col_idx] = 1
        self._update_neighbors()

    def show_enoughbours(self):
        rv = ''
        for row in self.neighbours_grid:
            rv += ''.join(str(col) for col in row) + '\n'
        return rv

    def __str__(self):
        m = {0: " ", 1: "#"}
        rv = ''
        for row in self.grid:
            rv += ''.join(m[col] for col in row) + '\n'
        return rv


if __name__ == "__main__":
    beacon = """\
.......
.......
...#...
...#...
...#...
.......\
"""
    g = ConwayGrid(beacon)
    for i in range(10):
        print(g)
        g.next()
        sleep(1)
