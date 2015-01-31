#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 70 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/vsv3g/6292012_challenge_70_easy/
#
# Write a program that takes a filename and a parameter n and prints the n most
# common words in the file, and the count of their occurrences, in descending
# order.
#
# January.31.2015

import argparse

from re import findall
from collections import Counter


def most_common_words(fname, n):
    with open(fname) as f:
        count = Counter()
        words = (word for line in f for word in findall(r'\w+', line))
        for word in words:
            count[word] += 1
    return count.most_common(n)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Count most common words in a file")
    parser.add_argument('fname', metavar='file', type=str,
                        help='file name')
    parser.add_argument('nwords', metavar='N', type=int,
                        help='the maximum number of most common words to display')
    args = parser.parse_args()

    most_common = most_common_words(args.fname, args.nwords)
    for word, count in most_common:
        print("{:>6}: {:>6}".format(word, count))
