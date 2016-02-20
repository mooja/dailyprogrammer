#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Daily Programmer Challenge 171 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2ao99p/7142014_challenge_171_easy_hex_to_8x8_bitmap/
#
# February.20.2016


def n2bitline(n):
    binstr = bin(n)[2:].zfill(8)
    bitline = binstr.replace('0', ' ').replace('1', 'x')
    return bitline


def main():
    hexstrings = raw_input().strip().split()
    nums = map(lambda x: int(x, base=16), hexstrings)
    bitlines = map(n2bitline, nums)
    for line in bitlines:
        print(line)


if __name__ == "__main__":
    main()
