#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 296 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/5jpt8v/20161222_challenge_296_intermediate_intersecting/
#
# 29 December 2016


from collections import namedtuple


Pos = namedtuple('Pos', ['x', 'y'])


class Rect(object):
    def __init__(self, x1, y1, x2, y2):
        left = min([x1, x2])
        right = max([x1, x2])
        top = max([y1, y2])
        bottom = min([y1, y2])
        self.topleft = Pos(left, top)
        self.botright = Pos(right, bottom)

    @property
    def area(self):
        return (self.botright.x - self.topleft.x)\
               * (self.topleft.y - self.botright.y)

    def __and__(self, other):
        r1, r2 = self, other
        if r1.topleft.x > r2.topleft.x:
            r1, r2 = r2, r1

        # rule out no intersection
        if r1.botright.x < r2.topleft.x:
            return Rect(0, 0, 0, 0)
        if r1.botright.y > r2.topleft.y:
            return Rect(0, 0, 0, 0)

        # find the intersection
        x1 = max([r2.topleft.x, r1.topleft.x])
        y1 = min([r1.topleft.y, r2.topleft.y])
        x2 = min([r1.botright.x, r2.botright.x])
        y2 = max([r1.botright.y, r2.botright.y])
        return Rect(x1, y1, x2, y2)

    def __str__(self):
        return '<Rect ({x1}, {y1}), ({x2}, {y2})>'.format(
            x1=self.topleft.x, y1=self.topleft.y,
            x2=self.botright.x, y2=self.botright.y
        )

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    r1 = Rect(-3.5, 4, 1, 1)
    r2 = Rect(1, 3.5, -2.5, -1)
    r3 = r1 & r2

    print(r3, 'area: ', r3.area)
