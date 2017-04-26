#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 312 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/67q3s6/20170426_challenge_312_intermediate_next_largest/
#
# 26 April 2017

import fileinput
from itertools import permutations


# warning grows O(n!) with number of digits
def next_largest(num):
    perms = [
        int(''.join(perm))
        for perm in permutations(str(num))
        if int(''.join(perm)) > num]
    if perms:
        return min(perms)
    return None

if __name__ == "__main__":
    for line in fileinput.input():
        nlargest = next_largest(int(line.strip()))
        print(nlargest)
