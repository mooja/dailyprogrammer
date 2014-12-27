#!/usr/bin/env python
# encoding: utf-8

from pprint import pprint
from itertools import product
from copy import deepcopy


DEBUG = True


def calculate_square_corner(x, y):
    return ((x / 3) * 3), ((y / 3) * 3)


def get_square_numbers(r, c, puzzle):
    square_x, square_y = calculate_square_corner(r, c)
    numbers = [puzzle[x][y] for x,y in
                    product(range(square_x, square_x+3),
                            range(square_y, square_y+3))]

    return numbers


def has_conflicts(puzzle):
    # check each row and column for duplicates
    for r, c in product(range(9), range(9)):
        num = puzzle[r][c]

        row_numbers = puzzle[r][:c] + puzzle[r][c+1:]
        if num != 0 and num in row_numbers:
            return True

        col_numbers = [puzzle[i][c] for i in range(9) if i != r]
        if num != 0 and num in col_numbers:
            return True

    # check each square for duplicates
    for x, y in product(range(3), range(3)):
        square_numbers = get_square_numbers(x*3, y*3, puzzle)

        for i, num in enumerate(square_numbers):
            if num != 0 and num in (square_numbers[:i] + square_numbers[i+1:]):
                return True

    return False


def is_solved(puzzle):
    for r, c in product(range(9), range(9)):
        if puzzle[r][c] == 0:
            return False

    if has_conflicts(puzzle):
        return False

    return True


def generate_possible_numbers(r, c, puzzle):
    nums_in_row = puzzle[r]
    nums_in_col = [puzzle[x][c] for x in range(9)]
    nums_in_square = get_square_numbers(r, c, puzzle)
    possible_solutions = list(set(range(10)) -
        (set(nums_in_row) | set(nums_in_col) | set(nums_in_square)))

    return list(possible_solutions)


def sudoku(puzzle):
    queue = []
    queue.append(puzzle)

    while queue:
        state = queue.pop(0)
        if is_solved(state):
            return state

        for r, c in product(range(9), range(9)):
            if state[r][c] == 0:
                possible_numbers = generate_possible_numbers(r, c, state)
                for num in list(possible_numbers):
                    new_state = deepcopy(state)
                    new_state[r][c] = num
                    queue.insert(0, new_state)
                break

    return None


if __name__ == '__main__':
    puzzle = [[5,3,0,0,7,0,0,0,0],
              [6,0,0,1,9,5,0,0,0],
              [0,9,8,0,0,0,0,6,0],
              [8,0,0,0,6,0,0,0,3],
              [4,0,0,8,0,3,0,0,1],
              [7,0,0,0,2,0,0,0,6],
              [0,6,0,0,0,0,2,8,0],
              [0,0,0,4,1,9,0,0,5],
              [0,0,0,0,8,0,0,7,9]]

    solution = sudoku(puzzle)
    pprint(solution)
