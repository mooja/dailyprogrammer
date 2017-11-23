#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 341 Easy
#
# https://np.reddit.com/r/dailyprogrammer/comments/7eh6k8/20171121_challenge_341_easy_repeating_numbers/
#
# 22 November 2017

from collections import Counter


def all_repeating(text, minlen=2):
    total_count = Counter()
    substring_sizes = range(minlen, len(text))
    for size in substring_sizes:
        inner_count = Counter()
        substrings = (text[i:i+size] for i in range(len(text)-size+1))
        for substr in substrings:
            inner_count[substr] += 1
        for substr, n in inner_count.items():
            if n > 1:
                total_count[substr] = n
    return total_count

print(all_repeating('11325992321982432123259'))
