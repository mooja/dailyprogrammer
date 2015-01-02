#!/usr/bin/env python
# encoding: utf-8

from kata_gameoflife import *


def test_get_generations():
    start = [[1,0,0],
             [0,1,1],
             [1,1,0]]
    end = [[0,1,0],
          [0,0,1],
          [1,1,1]]

    assert get_generation(start, 0) == start
    assert get_generation(start, 1) == end
