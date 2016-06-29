#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 251 Easy
#
# 
#
# 29 June 2016

data = \
"""
    *
   **
  * *
 *  *
*****
"""[1:-1]

data2 = \
"""
    ** *  
   *****  
  ******  
 ******** 
**********
 *      * 
 * ** * * 
 * ** * * 
 * **   * 
 ******** 
"""[1:-1]

data3 = \
"""
     ***       
  **** **      
 ****** ****** 
 * **** **    *
 ****** ***  **
 ****** *******
****** ********
 *   **********
 *   **********
 *   **********
 * * ****  ****
 *** ****  ****
     ****  ****
     ****  ****
     ****  ****
"""[1:-1]


def rotate90(s):
    grid = [list(line) for line in s.split('\n')]
    width = len(grid[0])
    height = len(grid)

    new_grid = [list(range(height)) for _ in range(width)]

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            new_grid[col][row] = grid[row][col]

    return '\n'.join(''.join(row) for row in new_grid)


class Nonogram(object):
    def __init__(self, text):
        lines = text.split('\n')
        self.grid = [list(line) for line in lines]
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def colstr(self, n):
        return ''.join(row[n] for row in self.grid)

    def rowstr(self, n):
        return ''.join(self.grid[n])

    def columns(self):
        for idx in range(self.height):
            yield self.partition_sizes(self.colstr(idx))

    def rows(self):
        for idx in range(self.width):
            yield self.partition_sizes(self.rowstr(idx))

    def display_rows(self):
        rows = list(self.rows())
        max_numbers = max(len(r) for r in rows)
        fmt = '{:>'+str(max_numbers)+'}'

        print('Rows:')
        for row in rows:
            s = ''.join(str(n) for n in row)
            print(fmt.format(s))
        print()

    def display_cols(self):
        cols = list(self.columns())
        max_numbers = max(len(r) for r in cols)
        fmt = '{:>'+str(max_numbers)+'}'

        print('cols:')
        lines = []
        for col in cols:
            s = ''.join(str(n) for n in col)
            lines.append(fmt.format(s))
        output = '\n'.join(lines)
        print(rotate90(output))
        print()

    @staticmethod
    def partition_sizes(s):
        partitions = s.split()
        sizes = [len(p) for p in partitions]
        return sizes

n = Nonogram(data)
n.display_cols()
n.display_rows()

print()

n = Nonogram(data2)
n.display_cols()
n.display_rows()

print()

n = Nonogram(data3)
n.display_cols()
n.display_rows()
