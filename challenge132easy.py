#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 132 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1hvh6u/070813_challenge_132_easy_greatest_common_divisor/
#
# June.07.2015


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    while True:
        try:
            a, b = map(int, raw_input().strip().split())
            print gcd(a, b)
        except:
            break


if __name__ == '__main__':
    main()
