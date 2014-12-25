#!/usr/bin/env python
# encoding: utf-8


def two_largest_squared(a, b, c):
    x, y = sorted([a, b, c], reverse=True)[:2]
    return x**2 + y**2
