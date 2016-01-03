#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 163 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/25y2d0/5192014_challenge_163_easy_probability/
#
# January.02.2016


import random


def roll_distribution(nruns):
    distribution = [0, 0, 0, 0, 0, 0]
    for i in range(nruns):
        distribution[random.randrange(0, 6)] += 1
    return distribution


if __name__ == '__main__':
    print("# of Rolls 1s     2s     3s     4s     5s     6s")
    print("====================================================")

    for i in range(1, 6):
        nruns = 10**i
        distribution = roll_distribution(nruns)
        normalized = [n / float(nruns) for n in distribution]
        print("{:<10} {:>4.2%} {:>4.2%} {:>4.2%} {:>4.2%} {:>4.2%} {:>4.2%}".format(
            nruns, *normalized
        ))
