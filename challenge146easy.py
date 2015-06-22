#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 146 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1tixzk/122313_challenge_146_easy_polygon_perimeter/
#
# June.21.2015

import math


def get_perimeter(n, r):
    side = 2 * math.sin(math.pi/n) * r
    perimeter = side * n
    return perimeter


def main():
    n, r = map(float, raw_input().split())
    perimeter = get_perimeter(n, r)
    print "{0:.3f}".format(perimeter)


if __name__ == '__main__':
    main()
