#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 107 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/122c4t/10252012_challenge_107_easy_all_possible_decodings/
#
# May.11.2015


from string import ascii_lowercase
from itertools import combinations


def break_down(num):
    digits = list(num)
    ns = range(1, len(digits))  # n = 1..(n - 1)

    for n in ns:  # split into 2, 3, 4... n parst
        for idxs in combinations(ns, n):
            yield [''.join(digits[i:j]) for i, j in zip((0,) + idxs, idxs + (None,))]


def is_valid_combination(combination):
    for num in combination:
        if int(num) == 0 or int(num) > 27:
            return False
    return True


def num2alpha(numstr):
    num = int(numstr)
    return ascii_lowercase[num-1]


def get_decodings(num):
    combs = []
    for comb in break_down(num):
        if is_valid_combination(comb):
            combs.append(''.join(map(num2alpha, comb)))

    return combs


if __name__ == '__main__':
    print '\n'.join(get_decodings('85121215'))
    # output: 

    # hello
    # heablo
    # heaubo
    # heauue
    # helabo
    # helaue
    # hellae
    # heababo
    # heabaue
    # heablae
    # heaubae
    # helabae
    # heababae

