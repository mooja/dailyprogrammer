#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 134 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1jtryq/080613_challenge_134_easy_ndivisible_digits/
#
# June.08.2015


def largest_ndivisible(n, m):
    """
    >>> largest_ndivisible(3, 2)
    998
    >>> largest_ndivisible(7, 4241275)
    8482550
    """
    hi = int('9'*n)
    lo = int('1' + '0'*(n-1))
    for i in xrange(hi, lo-1, -1):
        if i % m == 0:
            return i
    return None


def main():
    while True:
        try:
            n, m = map(int, raw_input().strip().split())
            print largest_ndivisible(n, m)
        except:
            break


if __name__ == '__main__':
    main()
