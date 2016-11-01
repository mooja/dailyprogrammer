#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 290 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/5aemnn/20161031_challenge_290_easy_kaprekar_numbers/
#
# 01 November 2016

import fileinput


def is_kaprekar(n):
    square = str(n**2)
    split_at = len(square) // 2
    left = square[:split_at]
    right = square[split_at:]
    if not left or not right:
        return False
    return n == (int(left) + int(right))


if __name__ == "__main__":
    for line in fileinput.input():
        lo = int(line.strip().split()[0])
        hi = int(line.strip().split()[1])
        kaprekars = [i for i in range(lo, hi+1) if is_kaprekar(i)]
        print(', '.join(str(k) for k in kaprekars))
