#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 326 Daily
#
# https://www.reddit.com/r/dailyprogrammer/comments/6s70oh/2017087_challenge_326_easy_nearest_prime_numbers/
#
# 19 August 2017

from math import sqrt
from random import randrange


def is_prime(n):
    if n in [2, 3]:
        return True

    for i in range(2, round(sqrt(n))):
        if n % i == 0:
            return False
    return True


def is_prime_miller_rabin(n, k=2):
    d = 2
    while (n-1) % d == 0:
        d *= 2
    d = d // 2
    r = (n - 1) // d

    for _ in range(k):
        a = randrange(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == (n - 1):
            continue

        witness_loop = False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                witness_loop = True
                break
        if witness_loop:
            continue
        return False
    return True


def nearest_prime(n):
    p1, p2 = n, n
    while not is_prime(p1):
        p1 -= 1
    while not is_prime(p2):
        p2 += 1
    return p1, n, p2


if __name__ == '__main__':
    print(is_prime_miller_rabin(653))
