#!/usr/bin/env python
# encoding: utf-8


import math


from turtle import *


def triangle_up(x, y, height):
    up()
    goto(x, y - height)
    down()
    for i in range(3):
        forward(height)
        left(120)
    up()
    goto(x, y)

    sub_height = height / 2.0
    sub_y = y - (sub_height * (math.sqrt(3.0) / 2.0))
    sub_x = x + height - (sub_height * (math.sqrt(3.0) / 2.0))
    triangle_down(sub_x, sub_y, sub_height)


def triangle_down(x, y, height):
    up()
    goto(x, y)
    down()
    for i in range(3):
        forward(height)
        right(120)
    up()
    goto(x, y)


def square(x, y, height):
    up()
    goto(x, y)
    down()
    for i in range(4):
        forward(height)
        right(90)
    up()


if __name__ == '__main__':
    color('red', 'yellow')
    square(0, 0, 100)
    triangle_up(0, 0, 100)
    done()
