#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 157 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/22fgs1/472014_challenge_157_easy_the_winning_move_xgames/
#
# September.12.2015


class TicTagGrid(object):
    def __init__(self, gridstr):
        self.grid = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(gridstr[i*3+j])
            self.grid.append(row)

    def victory_by(self, c):
        row_strings = self._get_row_strings()
        col_strings = self._get_col_strings()
        diag_strings = self._get_diag_strings()

        if c*3 in row_strings+col_strings+diag_strings:
            return True
        return False

    def _get_row_strings(self):
        results = []
        for r in range(3):
            results.append(''.join(self.grid[r]))
        return results

    def _get_col_strings(self):
        results = []
        for col in range(3):
            column = []
            for row in range(3):
                column.append(self.grid[row][col])
            results.append(''.join(column))
        return results

    def _get_diag_strings(self):
        results = []
        results.append(''.join([self.grid[i][i] for i in range(3)]))
        results.append(''.join([self.grid[i][2-i] for i in range(3)]))
        return results

    def __str__(self):
        lines = []
        for row in self.grid:
            lines.append(''.join(row))
        return '\n'.join(lines)


if __name__ == '__main__':
    g = TicTagGrid('--x-x-x--')
    print(g)
    print g.victory_by('x')
