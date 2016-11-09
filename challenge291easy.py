#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Daily Programmer Challenge 291 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/5bn0b7/20161107_challenge_291_easy_goldilocks_bear/
#
# 09 November 2016


import fileinput


if __name__ == "__main__":
    lines = [line.strip() for line in fileinput.input()]
    datapoints = [tuple(map(int, line.split())) for line in lines]

    output = []
    weight, maxtemp = datapoints[0]
    for idx, (weight_capacity, temp) in enumerate(datapoints[1:]):
        if weight_capacity >= weight and temp < maxtemp:
            output.append(str(idx+1))

    print(' '.join(output))
