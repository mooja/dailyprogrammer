#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 221 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/3bi5na/20150629_challenge_221_easy_word_snake/
#
# 28 May 2016

import sys


def get_positions(words):
    row, col = 0, 0
    direction = 'e'
    positions = {} 

    for word in words:
        # create a position for every letter in the direction we're facing
        for ch in word:
            positions[(row, col)] = ch
            if direction == 'e':
                col += 1
            if direction == 's':
                row += 1
        # once the word is finished backtrack one unit and change direction
        if direction == 'e':
            col -= 1
            direction = 's'
        else:
            row -= 1
            direction = 'e'

    return positions

def display_positions(positions):
    max_row = max(p[0] for p in positions.keys())
    max_col = max(p[1] for p in positions.keys())

    for row in range(max_row):
        line = []
        for col in range(max_col):
            if (row, col) in positions:
                line.append(positions[(row, col)])
            else:
                line.append(' ')
        yield(''.join(line)+'\n')

if __name__ == "__main__":
    words = 'SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE'.split()
    positions = get_positions(words)
    sys.stdout.writelines(display_positions(positions))
