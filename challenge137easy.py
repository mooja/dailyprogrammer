#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 137 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1m1jam/081313_challenge_137_easy_string_transposition/
#
# June.12.2015

import sys

from collections import namedtuple


CharPos = namedtuple('CharPos', 'row, col, char')


def draw_to_column(colnum, s):
    char_positions = []
    for i, char in enumerate(s):
        char_position = CharPos(i, colnum, char)
        char_positions.append(char_position)
    return char_positions


def draw_vertical_strings(string_list):
    char_positions = set()
    for i, s in enumerate(string_list):
        char_positions.update(draw_to_column(i, s))
    return list(char_positions)


def draw_char_positions(char_positions):
    max_row = max(charpos.row for charpos in char_positions)
    max_col = max(charpos.col for charpos in char_positions)

    for row_idx in xrange(max_row + 1):
        line = []
        for col_idx in xrange(max_col + 1):
            chars_at_this_pos = filter(
                lambda x: x.row == row_idx and x.col == col_idx,
                char_positions
            )

            if chars_at_this_pos:
                line.append(chars_at_this_pos[0].char)
            else:
                line.append(' ')

        yield ''.join(line) + '\n'


def main():
    nlines = input()
    signs = [raw_input().strip() for _ in range(nlines)]
    signs_positions = draw_vertical_strings(signs)
    output = draw_char_positions(signs_positions)
    sys.stdout.writelines(output)


if __name__ == '__main__':
    main()
