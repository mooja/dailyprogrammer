#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 71 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/vx3bk/722012_challenge_71_easy/
#
# If a right angled triangle has three sides A, B and C (where C is the
# hypothenuse), the pythagorean theorem tells us that A2 + B2 = C2
#
# When A, B and C are all integers, we say that they are a pythagorean
# triple.  For instance, (3, 4, 5) is a pythagorean triple because 32 + 42 =
# 52 .
#
# When A + B + C is equal to 240, there are four possible pythagorean
# triples: (15, 112, 113), (40, 96, 104), (48, 90, 102) and (60, 80, 100).
#
# Write a program that finds all pythagorean triples where A + B + C = 504.
#
# February.01.2015


def pytriples(num):
    triples = set()
    for c in xrange(1, num):
        for a in xrange(1, num - c):
            b = num - c - a
            if a**2 + b**2 == c**2:
                triples.add(tuple(sorted((a, b, c))))
    return triples
