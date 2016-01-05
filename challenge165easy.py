#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 165 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/271xyp/622014_challenge_165_easy_ascii_game_of_life/
#
# January.05.2016

from itertools import product


def gen_positions(cells):
    positions = []
    for r, row in enumerate(cells):
        for c, cell in enumerate(row):
            if cells[r][c] == 1:
                positions.append((r, c))
    return positions


class Grid(object):
    def __init__(self, cells):
        self.positions = gen_positions(cells)
        self.topleft = self.get_topleft_pos()
        self.botright = self.get_botright_pos()

    def get_topleft_pos(self):
        top = min([y for x, y in self.positions])
        left = min([x for x, y in self.positions])
        return (left, top)

    def get_botright_pos(self):
        bot = max([y for x, y in self.positions])
        right = max([x for x, y in self.positions])
        return (right, bot)

    def nextgen(self):
        nextgen_positions = []
        for x, y in product(range(self.topleft[0] - 2, self.botright[0] + 2),
                            range(self.topleft[1] - 2, self.botright[1] + 2)):
            neighbors = self.get_neighbors(x, y)
            if (x, y) in self.positions and (2 <= len(neighbors) <= 3):
                nextgen_positions.append((x, y))
            if not (x, y) in self.positions and (len(neighbors) == 3):
                nextgen_positions.append((x, y))

        self.positions = nextgen_positions
        self.topleft = self.get_topleft_pos()
        self.botright = self.get_botright_pos()

    def get_neighbors(self, x, y):
        neighbors = []
        for x1, y1 in product(range(x-1, x+2), range(y-1, y+2)):
            if (x1, y1) != (x, y) and (x1, y1) in self.positions:
                neighbors.append((x1, y1))
        return neighbors

    def get_cells(self):
        cells = []
        for row in range(self.topleft[0], self.botright[0]+1):
            row_cells = []
            for col in range(self.topleft[1], self.botright[1]+1):
                if (row, col) in self.positions:
                    row_cells.append(1)
                else:
                    row_cells.append(0)
            cells.append(row_cells)
        return cells


def get_generation(cells, generation):
    grid = Grid(cells)
    for i in range(generation):
        grid.nextgen()
    return grid.get_cells()
