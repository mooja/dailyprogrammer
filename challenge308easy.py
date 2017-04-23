#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 308 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/61ub0j/20170327_challenge_308_easy_let_it_burn/
#
# 23 April 2017

from collections import deque


class FloorPlan(object):
    def __init__(self, map_):
        self.rows = [list(row) for row in map_.split('\n')]

    def add_smoke(self, x, y):
        is_pos_within_grid = (0 <= y < len(self.rows)) and (0 <= x < len(self.rows[0]))
        if not is_pos_within_grid:
            return

        target_cell = self.rows[y][x]
        add_smoke_rules = { 'S': 'F', ' ': 'S'}
        if target_cell in add_smoke_rules:
            self.rows[y][x] = add_smoke_rules[target_cell]

        self.spread_fire()

    def spread_fire(self):
        pass

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.rows)


if __name__ == "__main__":
    map_ = """\
#############/#
#     |       #
#     #       #
#     #       #
#######       #
#     _       #
###############\
"""
    inputs = """\
1 1
1 2
1 3
5 6
4 2
1 1
1 2
5 5
5 5
9 1
5 7
2 2"""

    plan = FloorPlan(map_)
    # plan.add_smoke(1, 1)
    # plan.add_smoke(9, 1)

    import fileinput
    for line in inputs.split('\n'):
        line = line.strip()
        x, y = line.split()
        x, y = int(x), int(y)
        plan.add_smoke(x, y)
        print(plan)
        _ = input()

    print(plan)
