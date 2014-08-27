#!/usr/bin/env python


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def rotate_90(grid):
    new_grid = [ [] for i in range(len(grid))]

    for i in range(len(grid)):
        for k in range(len(grid)-1, -1, -1):
            new_grid[i].append(grid[k][i])

    return new_grid

print rotate_90(data)
