#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 270 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/4n6hc2/20160608_challenge_270_intermediate_generating/
#
# 17 August 2016

from random import choice
from collections import defaultdict


if __name__ == "__main__":
    with open('startrek.txt', 'rt') as f:
        words = [word for word in f.read().split()]

    chains = defaultdict(lambda: [])
    for i in range(0, len(words)-2):
        prefix = (words[i], words[i+1])
        postfix = words[i+2]
        chains[prefix].append(postfix)

    output = []
    counter = 100
    while counter > 0:
        prefix = tuple(output[-2:])
        if prefix in chains:
            suffix_candidates = chains[prefix]
            output.append(choice(suffix_candidates))
            counter -= 2
        else:
            prefix = choice(list(chains.keys()))
            postfix = choice(chains[prefix])
            output.extend(prefix)
            output.append(postfix)
            counter -= 3

    print(' '.join(output))
