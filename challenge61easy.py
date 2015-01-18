#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#                          challenge 61 easy                          #
#######################################################################

from math import log
from math import floor
from itertools import imap


def bin_rotate(number, rotations=1):
    for i in range(rotations):
        remainder = number % 2
        num_length = int(floor(log(number, 2)))
        number = number >> 1

        # append 1 to the left of the number numerically
        if remainder:
            number += 2**(num_length)

    return number


def bin_rotate_seq(number):
    output = [number]

    while True:
        next_rot = bin_rotate(output[-1])
        if next_rot == output[-1]:
            return tuple(output)
        output.append(next_rot)


def main():
    for seq in imap(bin_rotate_seq, (19, 205, 357, 54321)):
        print ' -> '.join(imap(str, seq))


if __name__ == '__main__':
    main()
