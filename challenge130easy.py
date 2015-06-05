#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 130 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1givnn/061713_challenge_130_easy_roll_the_dies/
#
# June.05.2015


import os
import random
import fileinput

from challenge102easy import unpackDiceNotation


def get_rolls(a, b, _):
    rolls_list = []
    for i in range(a):
        rolls_list.append(random.randrange(1, b+1))
    return rolls_list


def main():
    # change seed each run
    random.seed(os.urandom(24))

    for line in fileinput.input():
        a, b, _ = unpackDiceNotation(line.strip())
        print ' '.join(str(i) for i in get_rolls(a, b, _))


if __name__ == '__main__':
    main()
