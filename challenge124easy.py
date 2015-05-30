#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 124 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1dsyrk/050613_challenge_124_easy_edge_sorting/
#
# May.30.2015


def sorted_edges(edges):
    return sorted(edges, key=lambda x: min(x[1], x[2]))


def main():
    edges = []
    num_edges = int(raw_input())
    for i in xrange(num_edges):
        (name, a, b) = raw_input().strip().split()
        edges.append((name, int(a), int(b)))

    for edge in sorted_edges(edges):
        print edge[0],


if __name__ == '__main__':
    main()
