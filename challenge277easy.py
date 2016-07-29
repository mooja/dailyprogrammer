#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 277 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/
#
# 29 July 2016


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def simplify(numerator, denominator):
    common_div = gcd(numerator, denominator)
    return (numerator // common_div, denominator // common_div)


def main():
    data = '4 8, 1536 78360, 51478 5536, 46410 119340, 7673 4729, 4096 1024'
    rows = data.split(', ')
    fractions = (tuple(map(int, row.split())) for row in rows)
    simplified = [simplify(*frac) for frac in fractions]
    print(simplified)


if __name__ == "__main__":
    main()
