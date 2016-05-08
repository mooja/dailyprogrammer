#!/usr/bin/env python3
# encoding: utf-8


# Daily Programmer Challenge 200 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2ug3hx/20150202_challenge_200_easy_floodfill/
#
# 08.May.2016

from collections import deque, namedtuple


class OutOfImgBoundsException(Exception):
    pass

Pos = namedtuple('Pos', ['x', 'y'])


class Grid(object):
    """represents and ascii image grid"""
    def __init__(self, lines):
        self.rows = [list(l) for l in lines]

    def charat(self, x, y):
        within_width = 0 <= x < len(self.rows[0])
        within_height = 0 <= y < len(self.rows)
        if not within_width or not within_height:
            return None
        return self.rows[y][x]

    def color_neighbors_of(self, x, y):
        ch = self.charat(x, y)
        if ch is None:
            return None

        neighbors = []
        possible_neighbor_positions = (
            Pos(x+1, y),
            Pos(x-1, y), 
            Pos(x, y+1), 
            Pos(x, y-1)
        )
        for pos in possible_neighbor_positions:
            if self.charat(pos.x, pos.y) == ch:
                neighbors.append(pos)
        return neighbors

    def fill(self, x, y, ch):
        change_from_ch = self.charat(x, y)
        if not change_from_ch:
           raise OutOfImgBoundsException('no char at {}, ch={}'.format(
               Pos(x, y),
               change_from_ch)
           )

        visited = []
        pos_queue = deque(self.color_neighbors_of(x, y))
        while pos_queue:
            pos = pos_queue.popleft()
            unvisited_neighbors = (
                pos 
                for pos in self.color_neighbors_of(pos.x, pos.y)
                if pos not in visited
            )
            pos_queue.extend(unvisited_neighbors)
            self.rows[pos[1]][pos[0]] = ch
            visited.append(pos)

    def display(self):
        for r in self.rows:
            print(''.join(r))

    def __str__(self):
        return '<Grid: {}x{}>'.format(len(self.rows), len(self.rows[0]))

def main():
    first_line = input().strip()
    w = int(first_line.split()[0])
    h = int(first_line.split()[1])

    img_lines = (input() for _ in range(h))
    grid = Grid(img_lines)

    fill_line = input()
    fill_x = int(fill_line.split()[0])
    fill_y = int(fill_line.split()[1])
    fill_char = fill_line.split()[2]

    grid.fill(fill_x, fill_y, fill_char)
    grid.display()


if __name__ == '__main__':
    main()
