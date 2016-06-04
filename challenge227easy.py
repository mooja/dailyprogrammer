#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 227 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/3ggli3/20150810_challenge_227_easy_square_spirals/
#
# 04 June 2016

from itertools import islice

cclockwise = {
    'e': 'n',
    'n': 'w',
    'w': 's',
    's': 'e'
}

def move(pos, direction, units=1):
    x, y = pos
    if direction == 'e':
        x += units
    if direction == 'n':
        y -= units
    if direction == 'w':
        x -= units
    if direction == 's':
        y += units
    return (x, y)

def spiral_generator(initial_pos):
    x, y = initial_pos
    steps = 1 
    direction = 'e'
    yield (x, y)

    while True:
        for step in range(steps):
            x, y = move((x, y), direction)
            yield (x, y)
        direction = cclockwise[direction]

        for step in range(steps):
            x, y = move((x, y), direction)
            yield (x, y)
        direction = cclockwise[direction]

        steps += 1

def get_nth_item(generator, n):
    for idx, pos in enumerate(generator):
        if idx == n:
            return pos

def get_item_index(generator, target):
    for idx, item  in enumerate(generator):
        if item == target:
            return idx

def main():
    spiral_size = int(input())
    init_x, init_y = (spiral_size // 2) + 1, (spiral_size // 2) + 1
    spiral_positions = spiral_generator((init_x, init_y))

    second_line = input()
    if (len(second_line.split()) == 1):
        item_index = int(second_line)
        nth_pos = get_nth_item(spiral_positions, item_index - 1)
        print("({}, {})".format(nth_pos[0], nth_pos[1]))
    else:
        target_x, target_y = [int(x) for x in second_line.split()]
        target_pos = (target_x, target_y)
        target_index = get_item_index(spiral_positions, target_pos)
        print(target_index + 1)

if __name__ == "__main__":
    main()
