#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 273 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4q35ip/20160627_challenge_273_easy_getting_a_degree/
#
# 22 July 2016

import math


radians_converion_constants = {
    'r': 1,
    'd': 180 / math.pi
}


def as_unit(val, unit, target_unit):
    """
    >>> as_unit(3.1416, 'r', 'd')
    180.0
    >>> as_unit(90, 'd', 'r')
    1.57
    """
    val_rads = val / radians_converion_constants[unit]
    return round(val_rads * radians_converion_constants[target_unit], 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
