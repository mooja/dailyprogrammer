#!/usr/bin/env python3
# encoding: utf-8


# Daily Programmer Challenge 191 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2nynip/2014121_challenge_191_easy_word_counting/
#
# 28.April.2016

import re

from collections import Counter


if __name__ == '__main__':
    c = Counter()
    regexp = re.compile(r'\W')
    with open('birds-illustrated.txt') as f:
        for line in f:
            c += Counter(re.sub(regexp, '', w.lower()) for w in line.split())
    print(c.most_common(n=10))
