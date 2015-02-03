#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 5 Intermediate
#
# http://www.reddit.com/r/dailyprogrammer/comments/pnhtj/2132012_challenge_5_intermediate/
#
# Your challenge today is to write a program that can find the amount of
# anagrams within a .txt file. For example, "snap" would be an anagram of
# "pans", and "skate" would be an anagram of "stake".
#
#
# February.03.2015

import re

from collections import Counter


def nanagrams(words):
    words = Counter(words)
    count = 0
    for word in words:
        revrsed = word[::-1]
        if words[revrsed]:
            words[word] = 0
            words[revrsed] = 0
            count += 1
    return count


if __name__ == '__main__':
    fname = "pg2600.txt"  # war and peace
    with open(fname) as f:
        words = (word.lower()
                    for line in f
                    for word in re.findall(r'\w+', line))
        anagram_count = nanagrams(words)
        print("Number of anagrams in {}: {}".format(fname, anagram_count))
