#!/usr/bin/env python3
# encoding: utf-8



# Daily Programmer Challenge 178 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2f6a7b/9012014_challenge_178_easy_transformers_matrices/
#
# 15.April.2016


import math

from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


def translate(p, a, b):
    """
    >>> translate(Point(0, 0), 1, 2)
    Point(x=1, y=2)
    """
    return Point(p.x + a, p.x + b)

def rotate(p, center, angle):
    """
    >>> rotate(Point(1,0), Point(0, 0), 90)
    Point(x=0.0, y=1.0)
    """

    angle_radians = angle * (math.pi / 180.0)
    rotated_x = math.cos(angle_radians) * (p.x - center.x)\
                - math.sin(angle_radians) * (p.y - center.y)\
                + center.x
    rotated_y = math.sin(angle_radians) * (p.x - center.x)\
                + math.cos(angle_radians) * (p.y - center.y)\
                + center.y

    rotated_x = round(rotated_x, 5)
    rotated_y = round(rotated_y, 5)
    return Point(rotated_x, rotated_y)

def scale(p, center, c):
    """
    >>> scale(Point(1, 1), Point(0, 0), 5)
    Point(x=6, y=6)

    """
    dx = p.x - center.x
    dy = p.y - center.y
    return Point(p.x + c*dx, p.y + c*dy)

def reflect(p, axis_str):
    """
    >>> reflect(Point(1, 1), 'x')
    Point(x=1, y=-1)
    >>> reflect(Point(1, 1), 'y')
    Point(x=-1, y=1)
    """
    if axis_str == 'x':
        return Point(p.x, -p.y)
    if axis_str == 'y':
        return Point(-p.x, p.y)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

    p = Point(0, 5)
    p = translate(p, 3, 2)
    p = scale(p, Point(1, 3), 0.5)
    p = rotate(p, Point(3, 2), 90)
    p = reflect(p, 'x')
    p = translate(p, 2, -1)
    p = scale(p, Point(0, 0), -0.25)
    p = rotate(p, Point(1, -3), 180)
    p = reflect(p, 'y')
    print(p)
