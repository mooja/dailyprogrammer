#!/usr/bin/env python3
# encoding: utf-8


# Daily Programmer Challenge 185 easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2jt4cx/10202014_challenge_185_easy_generated_twitter/
#
# 23.April.2016

import heapq


def main():
    with open("enable1.txt", 'rU') as f:
        abbr_f = (l.replace('at', '@') for l in f if 'at' in l)
        longest10 = heapq.nlargest(10, abbr_f, len)

    with open("enable1.txt", 'rU') as f:
        abbr_f = (l.replace('at', '@') for l in f if 'at' in l)
        shortest10 = heapq.nsmallest(10, abbr_f, len)

    print("10 longest")
    for w in longest10:
        print(w, end='')

    print()

    print("10 shortest")
    for w in shortest10:
        print(w, end='')


if __name__ == '__main__':
    main()
