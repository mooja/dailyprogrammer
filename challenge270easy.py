#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 270 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4msu2x/challenge_270_easy_transpose_the_input_text/
#
# 19 July 2016

import fileinput


def transpose(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    new_matrix = []
    for _ in range(ncols):
        row = []
        for _ in range(nrows):
            row.append(None)
        new_matrix.append(row)
    for r_idx, row in enumerate(matrix):
        for c_idx, col in enumerate(row):
            new_matrix[c_idx][r_idx] = col
    return new_matrix


def squarify(lines):
    """ If lines are of varying length, add spaces to make all lines of the
        same length.
    """
    longest = max([len(l) for l in lines])
    line_template = '{:<' + str(longest) + '}'
    lines = [line_template.format(l) for l in lines]
    return lines


def main():
    lines = [l[:-1] for l in fileinput.input()]
    lines = squarify(lines)
    for l in transpose(lines):
        print(''.join(l))


if __name__ == "__main__":
    main()
