#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge #25 Weekly
#
# https://www.reddit.com/r/dailyprogrammer/comments/4vrb8n/weekly_25_escape_the_trolls/
#
# 02 August 2016

from random import randrange
from collections import namedtuple


Pos = namedtuple('Pos', ['x', 'y'])


class Maze(object):
    offsets = {
        'up': Pos(0, -1),
        'right': Pos(1, 0),
        'down': Pos(0, 1),
        'left': Pos(-1, 0)
    }

    def __init__(self, map, pos=None):
        self.grid = [list(line) for line in map.split('\n')]
        if pos is not None:
            self.pos = pos
        else:
            self.pos = self.get_random_pos()
        self.direction = '>'

    def can_move(self, direction):
        new_x = self.pos.x + Maze.offsets[direction].x
        new_y = self.pos.y + Maze.offsets[direction].y

        try:
            target_cell = self.grid[new_y][new_x]
        except IndexError:
            return False
        if target_cell != ' ' and target_cell != 'X':
            return False
        return True

    def move(self, direction):
        if not self.can_move(direction):
            raise IndexError
        new_x = self.pos.x + Maze.offsets[direction].x
        new_y = self.pos.y + Maze.offsets[direction].y
        self.pos = Pos(new_x, new_y)

    def at_exit(self):
        return self.grid[self.pos.y][self.pos.x] == 'X'

    def get_random_pos(self):
        height = len(self.grid)
        width = len(self.grid[0])
        new_pos = Pos(randrange(width), randrange(height))
        while self.grid[new_pos.y][new_pos.x] != ' ':
            new_pos = Pos(randrange(width), randrange(height))
        return new_pos

    def display(self):
        for ridx, row in enumerate(self.grid):
            line_chars = []
            for colidx, ch in enumerate(row):
                if Pos(colidx, ridx) == self.pos:
                    line_chars.append(self.direction)
                else:
                    line_chars.append(ch)
            print(''.join(line_chars))


MAP = """#####################################
# #       #       #     #         # #
# # ##### # ### ##### ### ### ### # #
#       #   # #     #     # # #   # #
##### # ##### ##### ### # # # ##### #
#   # #       #     # # # # #     # #
# # ####### # # ##### ### # ##### # #
# #       # # #   #     #     #   # #
# ####### ### ### # ### ##### # ### #
#     #   # #   # #   #     # #     #
# ### ### # ### # ##### # # # #######
#   #   # # #   #   #   # # #   #   #
####### # # # ##### # ### # ### ### #
#     # #     #   # #   # #   #     #
# ### # ##### ### # ### ### ####### #
# #   #     #     #   # # #       # #
# # ##### # ### ##### # # ####### # #
# #     # # # # #     #       # #   #
# ##### # # # ### ##### ##### # #####
# #   # # #     #     # #   #       #
# # ### ### ### ##### ### # ##### # #
# #         #     #       #       # #
#X###################################"""


if __name__ == "__main__":
    maze = Maze(MAP, Pos(1, 15))
    possible_inputs = {
        'u': 'up',
        'up': 'up',
        'r': 'right',
        'right': 'right',
        'd': 'down',
        'down': 'down',
        'l': 'left',
        'left': 'left'
    }
    while not maze.at_exit():
        maze.display()
        direction = input('Enter your move: (u)p, (r)right, (d)own, (l)eft\n').strip()
        while direction not in possible_inputs:
            direction = input('Please enter a correct move: (u)p, (r)right, (d)own, (l)eft \n').strip()
        direction = possible_inputs[direction]
        if not maze.can_move(direction):
            print('You can\'t move {}.'.format(direction))
        else:
            maze.move(direction)
    print('You have found the exit!')
