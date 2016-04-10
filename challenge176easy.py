#!/usr/bin/env python3
# encoding: utf-8


# Daily Programmer Challenge 176 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2dvc81/8182014_challenge_176_easy_spreadsheet_developer/
#
# 10.April.2016

import re
from string import ascii_uppercase
from itertools import product


def bij2int(s):
    """
    >>> bij2int('A')
    1
    >>> bij2int('Z')
    26
    >>> bij2int('AA')
    27
    >>> bij2int('AB')
    28
    """
    n = 0
    for ch in s:
        n *= 26
        n += ascii_uppercase.find(ch) + 1
    return n


def colrow2coord(colrow_str):
    """
    >>> colrow2coord('A3')
    (1, 3)
    >>> colrow2coord('AA33')
    (27, 33)
    """
    m = re.match(r'([A-Z]+)([0-9]+)', colrow_str)
    if not m:
        raise Exception('cant parse {}'.format(colrow_str))
    row = bij2int(m.groups()[0])
    col = int(m.groups()[1])
    return (row, col)


def range2cells(range_str):
    """
    >>> range2cells('A1')
    [(1, 1)]
    >>> range2cells('A1:B2')
    [(1, 1), (1, 2), (2, 1), (2, 2)]
    """
    if ':' not in range_str:
        return [colrow2coord(range_str)]

    start_colrow = range_str.split(':')[0]
    end_colrow = range_str.split(':')[1]

    start_coords = colrow2coord(start_colrow)
    end_coords = colrow2coord(end_colrow)

    rows = tuple(range(start_coords[0], end_coords[0]+1))
    cols = tuple(range(start_coords[1], end_coords[1]+1))
    cells = list(product(rows, cols))

    return cells


def parse_unions(formula_str):
    """
    >>> parse_unions('A1:B2&A3:A4&A5:A7')
    [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 1), (2, 2)]
    """
    cells = []
    range_strings = formula_str.split('&')

    for rss in range_strings:
        cells.extend(range2cells(rss))

    # remove duplicates
    cells = list(set(cells))
    cells.sort()

    return cells


def parse(formula_str):
    """
    >>> len(parse("B1:B3&B4:E10&F1:G1&F4~C5:C8&B2"))
    29
    """

    if not '~' in formula_str:
        return parse_unions(formula_str)

    positive_ranges = formula_str.split('~')[0]
    negative_ranges = formula_str.split('~')[1]

    positive_cells = parse_unions(positive_ranges)
    negative_cells = parse_unions(negative_ranges)

    cells = list(set(positive_cells) - set(negative_cells))
    cells.sort()

    return cells


if __name__ == '__main__':
    import doctest
    doctest.testmod()
