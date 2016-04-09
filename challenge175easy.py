#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 175 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2d8yk5/8112014_challenge_175_easy_bogo/
#
# 09.April.2016

import random


def bogo_sort(s, target_s):
    s, target_s = list(s.lower()), list(target_s)
    counter = 0
    while s != target_s:
        random.shuffle(s)
        counter += 1
    return counter


if __name__ == '__main__':
    results = [str(bogo_sort('ollhe', 'hello')) for _ in range(10)]
    print(' '.join(results))
