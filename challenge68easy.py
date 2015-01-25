#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 68 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/vmblw/6262012_challenge_69_easy/
#
# An emirp ("prime" spelled backwards) is a prime whose (base 10) reversal
# is also prime, but which is not a palindromic prime. The first few are 13,
# 17, 31, 37, 71, 73, 79, 97, 107, 113, 149, 157, ... (OEIS A006567). A
# binary plot of the emirps is illustrated above.
#
# Emirp is an interesting concept. The explanation about it is provided in
# the link i just gave.

# Your task is to implement a function which prints out the emirps below a
# number(input) given by the user.
#
# 15.January.25


def is_prime(num):
    if num == 1:
        return False
    for i in xrange(2, num):
        if num % i == 0:
            return False
    return True


def is_palindrome(num):
    rnum = int(str(num)[::-1])
    if num == rnum:
        return True
    return False


def is_emirp(num):
    rnum = int(str(num)[::-1])
    return is_prime(num) and is_prime(rnum) and (not is_palindrome(num))


def gen_emirps(limit):
    result = [i for i in xrange(2, limit)
                    if is_emirp(i)]
    return result
