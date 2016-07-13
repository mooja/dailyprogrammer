#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 263 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4fc896/20160418_challenge_263_easy_calculating_shannon/
#
# 13 July 2016

from __future__ import division
from collections import Counter
try:
    from math import log2
except ImportError:
    from math import log
    def log2(x):
        return log(x, 2)

def shannon_entropy(s):
    total = 0
    frequences = Counter(s)
    for i in frequences.values():
        total += i/len(s) * log2(i/len(s))
    return round(-total, 2)
