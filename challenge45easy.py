#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#    challenge 45 - draw a checkered board to specified dimensions    #
#######################################################################


def checkered_board(height, width):
    TOTAL_WIDTH = 78
    TOTAL_HEIGHT = height * (TOTAL_WIDTH / width)
    row_size = TOTAL_HEIGHT / height
    col_size = TOTAL_WIDTH / width

    lines = []
    for lineno in range(TOTAL_HEIGHT):
        line = []
        row = lineno / row_size
        for col in range(width):
            if (col+row) % 2 == 0:
                line.append(' '*col_size)
            else:
                line.append('#'*col_size)
        line = ['*'] + line + ['*']
        lines.append(''.join(line))

    lines.insert(0, '*'*80)
    lines.append('*'*80)

    return '\n'.join(lines)

if __name__ == '__main__':
    board = checkered_board(6, 6)
