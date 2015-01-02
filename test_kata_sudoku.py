#!/usr/bin/env python
# encoding: utf-8

import pytest

from kata_sudoku import *


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

puzzle2 = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [6,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]


def test_calculate_square_corner():
    assert calculate_square_corner(1, 1) == (0, 0)
    assert calculate_square_corner(8, 8) == (6, 6)
    assert calculate_square_corner(8, 1) == (6, 0)
    assert calculate_square_corner(5, 5) == (3, 3)


def test_get_square_numbers():
    assert get_square_numbers(1, 1, puzzle) == [5,3,0,6,0,0,0,9,8]


def test_has_conflicts():
    assert has_conflicts(puzzle) == False
    assert has_conflicts(puzzle2) == True
    assert has_conflicts(solution) == False


def test_is_solved():
    assert is_solved(puzzle) == False
    assert is_solved(puzzle2) == False
    assert is_solved(solution) == True


def test_sudoku():
    assert sudoku(puzzle) == solution
