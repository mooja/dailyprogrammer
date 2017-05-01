#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 305 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/5xu7sz/20170306_challenge_305_easy_permutation_base/
#
# 01 May 2017

from itertools import product


def permbase2(idx):
    def iter():
        r = 1
        while True:
            for p in product('01', repeat=r):
                yield ''.join(p)
            r += 1

    for i, item in enumerate(iter()):
        if i == idx:
            return item

print(permbase2(234234))
