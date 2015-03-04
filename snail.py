#!/usr/bin/env python
# encoding: utf-8

# Codewars.com Kata Challenge
#
# http://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
#
# March.04.2015


def square(row, col, size, seq):
    """
    >>> square(0, 0, 2, [[1, 2], [3, 4]])
    [1, 2, 4, 3]
    >>> square(0, 0, 3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 6, 9, 8, 7, 4]
    >>> square(0, 0, 1, [[1]])
    [1]
    """
    points = []
    # add top side
    r, c = row, col
    while c < col+size:
        points.append(seq[r][c])
        c += 1

    # add right side
    r, c = row+1, col+size-1
    while r < row+size:
        points.append(seq[r][c])
        r += 1

    # add bottom side
    r, c = row+size-1, col+size-2
    while c >= col:
        points.append(seq[r][c])
        c -= 1

    # add left side
    r, c = row+size-2, col
    while r > row:
        points.append(seq[r][col])
        r -= 1

    return points


def snail(arr):
    """
    >>> snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]
    >>> snail([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    [1, 2, 3, 4, 7, 11, 15, 14, 13, 12, 8, 4, 5, 6, 10, 9]
    >>> snail([[1]])
    [1]
    >>> snail([[]])
    []

    """
    points = []
    try:
        size = len(arr[0])
    except:
        size = 0
    x, y = 0, 0
    while size > 0:
        points.extend(square(x, y, size, arr))
        x += 1
        y += 1
        size -= 2
    return points



if __name__ == '__main__':
    import doctest
    doctest.testmod()
