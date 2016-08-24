#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 280 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/4zcly2/20160824_challenge_280_intermediate_anagram_maker/
#
# 24 August 2016


import re
import random
from collections import defaultdict


def random_partitions(seq):
    npartitions = random.randrange(1, len(seq))
    partitions = [[] for i in range(npartitions)]
    for elm in seq:
        partition_idx = random.randrange(0, len(partitions))
        partitions[partition_idx].append(elm)
    return [''.join(p) for p in partitions]


def find_anagram(dictionary, word):
    letters = ''.join(sorted(word.lower()))
    if letters in dictionary:
        return dictionary[letters][0]
    return None


def sentence_anagram(dictionary, sentence):
    letters = re.sub(r'\W', '', sentence)
    counter = 0
    while True:
        partitions = random_partitions(letters)
        anagrams = [find_anagram(dictionary, p) for p in partitions]
        if all(anagrams):
            return ' '.join(a.capitalize() for a in anagrams)
        if counter > 1000:
            return None


if __name__ == "__main__":
    dictionary = defaultdict(lambda: [])
    for line in open('enable1.txt', 'rt'):
        letters = ''.join(sorted(line.strip()))
        word = line.strip()
        dictionary[letters].append(word)

    inputs = [
        'Desperate',
        'Redditor',
        'Dailyprogrammer',
        'Sam likes to swim',
        'The Morse Code',
        'Help, someone stole my purse'
    ]
    for inp in inputs:
        print(inp, '->', sentence_anagram(dictionary, inp))
