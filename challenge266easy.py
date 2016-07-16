#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 266 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4ijtrt/20160509_challenge_266_easy_basic_graph/
#
# 16 July 2016


def main(data):
    lines = data.split('\n')
    num_nodes = int(lines[0].strip())
    adjacency_matrix = [[0 for _ in range(num_nodes)]
                        for _ in range(num_nodes)]

    for line in lines[1:]:
        a = int(line.strip().split()[0])
        b = int(line.strip().split()[1])
        adjacency_matrix[a-1][b-1] = 1
        adjacency_matrix[b-1][a-1] = 1

    for idx, adjacents in enumerate(adjacency_matrix):
        print("Node {} has a degree of {}" .format(idx+1, sum(adjacents)))

    print()

    for row in adjacency_matrix:
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    data = '''16
    1 2
    1 3
    2 3
    1 4
    3 4
    1 5
    2 5
    1 6
    2 6
    3 6
    3 7
    5 7
    6 7
    3 8
    4 8
    6 8
    7 8
    2 9
    5 9
    6 9
    2 10
    9 10
    6 11
    7 11
    8 11
    9 11
    10 11
    1 12
    6 12
    7 12
    8 12
    11 12
    6 13
    7 13
    9 13
    10 13
    11 13
    5 14
    8 14
    12 14
    13 14
    1 15
    2 15
    5 15
    9 15
    10 15
    11 15
    12 15
    13 15
    1 16
    2 16
    5 16
    6 16
    11 16
    12 16
    13 16
    14 16
    15 16'''
    main(data)
