#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 292 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/5d1l7v/20161115_challenge_292_easy_increasing_range/
#
# 28 November 2016

import re


def expand_increase(codetext):
    current_number = None
    tokens = re.split(r'(\d+)', codetext)
    for i in range(len(tokens)):
        token = tokens[i]
        m = re.match(r'^(\d+)$', token)
        if m:
            if current_number is None:
                current_number = int(token)
            else:
                current_number += 1
                while not str(current_number).endswith(token):
                    current_number += 1
            tokens[i] = str(current_number)
    return ''.join(tokens)


def expand_ranges(codetext):
    ranges = codetext.split(',')
    for r in ranges:
        r = r.strip()
        if re.match(r'^\d+$', r):
            yield int(r)
            continue

        elif re.match(r'^(\d+)(\.\.|:|-)(\d+)$', r):
            lo, hi = re.split(r'\.\.|:|-', r)
            lo, hi = int(lo), int(hi)
            for n in range(lo, hi+1):
                yield n


def expand(codetext):
    codetext = expand_increase(codetext)
    return list(expand_ranges(codetext))


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()

    inputs = [
        "1,3,7,2,4,1",
        "1,3,1,2",
        "1, 32, 32",
        "104-2",
        "104..02",
        "545,64:11"
    ]

    for inp in inputs:
        print(' '.join(map(str, expand(inp))))
