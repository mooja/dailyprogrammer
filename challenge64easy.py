#!/usr/bin/env python3
# encoding: utf-8

# ==================================
# Daily Programmer challenge 64 Easy
# ==================================
#
# The divisors of a number are those numbers that divide it evenly; for
# example, the divisors of 60 are 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60.
#
# The sum of the divisors of 60 is 168, and the number of divisors of 60 is 12.
# The totatives of a number are those numbers less than the given number and
# coprime to it; two numbers are coprime if they have no common factors other
# than 1.
#
# The number of totatives of a given number is called its totient. For example,
# the totatives of 30 are 1, 7, 11, 13, 17, 19, 23, and 29, and the totient of
# 30 is 8.
#
# Your task is to write a small library of five functions that compute the
# divisors of a number, the sum and number of its divisors, the totatives of a
# number, and its totient.
#
# 15.01.20

def divisors(n):
    result = []
    for i in xrange(1, n+1):
        if n % i == 0:
            result.append(i)
    return tuple(result)


def is_prime(n):
    return len(divisors(n)) == 2


def factors(n):
    return (1,) + filter(is_prime, divisors(n))


def sum_divisors(n):
    return sum(divisors(n))


def are_coprime(a, b):
    a_divs = divisors(a)
    b_divs = divisors(b)
    if len(set(a_divs) & set(b_divs)) == 1:
        return True
    return False


def totatives(n):
    def is_totative(x):
        return are_coprime(x, n)
    return tuple(filter(is_totative, range(2, n)))


def n_totatives(n):
    return len(totatives(n))


totative = n_totatives
