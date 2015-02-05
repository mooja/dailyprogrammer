#!/usr/bin/env python
# encoding: utf-8


from turtle import *


def triangle_up(side_length):
    down()
    right(60)
    for i in range(3):
        forward(side_length)
        right(120)
    left(60)
    up()


def triangle_up_recurse(side_len, max_len=10):
    pos = position()
    pque = [(pos, side_len)]
    while pque:
        pos, len = pque.pop(0)
        half_len = len / 2.0
        if len < max_len:
            continue

        up()
        goto(pos)
        pque.append((position(), half_len))

        down()
        setheading(0)
        right(60)
        forward(half_len)
        pque.append((position(), half_len))
        forward(half_len)
        right(120)
        forward(len)
        right(120)
        forward(half_len)
        pque.append((position(), half_len))
        forward(half_len)


if __name__ == '__main__':
    speed(0)
    color('red', 'yellow')
    up()
    goto(-300, 300)
    triangle_up_recurse(600, 5)
    done()
