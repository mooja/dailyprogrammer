#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 323 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/6melen/20170710_challenge_323_easy_3sum/
#
# 20 August 2017


def three_sum(ns):
    ns_set = set(ns)
    ns = list(ns_set)

    rv = set()
    for i in range(len(ns)):
        for j in range(i+1, len(ns)):
            a, b, c = ns[i], ns[j], -(ns[i]+ns[j])
            if c not in ns[j:]:
                continue
            a, b, c = sorted((a, b, c))
            rv.add((a, b, c))
    return sorted(rv)


if __name__ == '__main__':
    import sys
    ns = [int(n) for n in sys.argv[1:]]
    print(three_sum(ns))
