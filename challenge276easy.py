#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 276 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/
#
# 28 July 2016

from itertools import product


def wordtangle(word, width, height):
    m_width = len(word)*width - (width - 1)
    m_height = len(word)*height - (height - 1)
    matrix = [[' ' for _ in range(m_width)] for i in range(m_height)]

    forward = False
    for row, col in product(range(height), range(width)):
        top = row*len(word) - row
        left = col*len(word) - col
        draw_square(matrix, word, top, left, forward)
        forward = not forward

    for row in matrix:
        yield ''.join(row)


def draw_square(matrix, word, top, left, forward):
    r, c = top, left
    rword = word[::-1]

    for i, ch in enumerate(word):
        if forward:
            matrix[r][c] = word[i]
        else:
            matrix[r][c] = rword[i]
        c += 1

    c -= 1
    forward = not forward

    for i, ch in enumerate(word):
        if forward:
            matrix[r][c] = word[i]
        else:
            matrix[r][c] = rword[i]
        r += 1

    r -= 1
    forward = not forward

    for i, ch in enumerate(word):
        if forward:
            matrix[r][c] = word[i]
        else:
            matrix[r][c] = rword[i]
        c -= 1

    c += 1
    forward = not forward

    for i, ch in enumerate(word):
        if forward:
            matrix[r][c] = word[i]
        else:
            matrix[r][c] = rword[i]
        r -= 1


if __name__ == "__main__":
    for line in wordtangle('rekt', 2, 2):
        print(line)
