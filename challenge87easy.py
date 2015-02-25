#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 87 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/y26pr/8102012_challenge_87_easy_rectangle_intersection/
#
# February.25.2015


from collections import namedtuple


Rect = namedtuple('Rect', 'x0, y0, x1, y1')


def rect_intersection(r1, r2):
    """ rect_intersection(r1, r2): returns a rectable representing an
          overlap between r1 and r2.

        >>> rect_intersection(Rect(3, 3, 10, 10), Rect(6, 6, 12, 12))
        Rect(x0=6, y0=6, x1=10, y1=10)
        >>> rect_intersection(Rect(1, 1, 2, 2), Rect(5, 5, 6, 6))
    """
    irect = Rect(max(r1.x0, r2.x0),
                 max(r1.y0, r2.y0),
                 min(r1.x1, r2.x1),
                 min(r1.y1, r2.y1))

    if irect.x0 >= irect.x1 or irect.y0 >= irect.y1:
        return None
    else:
        return irect


if __name__ == '__main__':
    import doctest
    doctest.testmod()
