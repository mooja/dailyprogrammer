#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 234 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/3moxid/20150928_challenge_234_easy_vampire_numbers/
#
# 11 June 2016

from operator import mul
from functools import reduce
from itertools import permutations


def get_fangs(num, nfangs):
    ndigits = len(str(num))
    step = ndigits // nfangs
    slices = [slice(i, i+step) for i in range(0, ndigits, step)]

    fangs = []
    for perm in permutations(str(num)):
         fang_candidates = []
         for s in slices:
             fang_candidates.append(int(''.join(perm[s])))

         product = reduce(mul, fang_candidates)
         if product == num:
             fangs.append(tuple(sorted(fang_candidates)))

    return set(fangs)


if __name__ == "__main__":
    inp = input()
    ndigits, nfangs = [int(x) for x in inp.strip().split()]

    lo = 10**(ndigits-1)
    hi = 10**(ndigits) - 1
    for n in range(lo, hi):
        fangs = get_fangs(n, nfangs)
        for fang in fangs:
            fangnums = '*'.join(str(fnum) for fnum in fang)
            print('{n}={fangnums}'.format(n=n, fangnums=fangnums))
