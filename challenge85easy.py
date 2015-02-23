#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 85 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/xq0yv/832012_challenge_85_easy_rowcolumn_sorting/
#
#
# February.23.2015


def sums_rows(lines):
    """ Calculate the sum of each row
    >>> sums_rows(['1 2', '3 4'])
    [3, 7]
    """
    results = []
    for line in lines:
        line_sum = sum(int(w) for w in line.strip().split())
        results.append(line_sum)
    return results


def sums_cols(lines):
    """ Calculate the sum of each column
    >>> sums_cols(['1 2', '3 4'])
    [4, 6]
    """
    num_matrix = [[int(w) for w in line.strip().split()]
                  for line in lines]
    nrows = len(num_matrix)
    ncols = len(num_matrix[0])
    col_sums = []
    for col in range(ncols):
        col_sums.append(sum(num_matrix[row][col]
                            for row in range(nrows)))
    return col_sums


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    matrix = ['10 5 4 20',
              '9 33 27 16',
              '11 6 55 3']
    print "Rows: {}".format(' '.join(map(str, sums_rows(matrix))))
    print "Cols: {}".format(' '.join(map(str, sums_cols(matrix))))
    print

    m1 = zip(sums_rows(matrix), matrix)
    m2 = zip(sums_cols(matrix), matrix)

    for _, l in sorted(m1):
        print l
    print

    for _, l in sorted(m2):
        print l
    print
