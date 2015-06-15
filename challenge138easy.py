#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 138 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1ml669/091713_challenge_138_easy_repulsionforce/
#
# June.14.2015

from math import sqrt
from collections import namedtuple


Point = namedtuple('Point', 'mass, x, y')


def distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return round(sqrt(dx**2 + dy**2), 4)


def repulsion_force(p1, p2):
    return (p1.mass * p2.mass) / distance(p1, p2)**2


def main():
    p1 = Point._make(map(float, raw_input().strip().split()))
    p2 = Point._make(map(float, raw_input().strip().split()))
    print(repulsion_force(p1, p2))


if __name__ == '__main__':
    main()
