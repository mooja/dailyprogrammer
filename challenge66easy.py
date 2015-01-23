#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 66 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/v89c4/6182012_challenge_66_easy/
# 
# Write a function that takes two arguments, x and y, which are two strings
# containing Roman Numerals without prefix subtraction (so for instance, 14
# is represented as XIIII, not XIV). The function must return true if and
# only if the number represented by x is less than the number represented by
# y. Do it without actually converting the Roman numerals into regular
# numbers.
# 
# 15.January.23


def cmp_roman(x, y):
    for numeral in "MDCLXVI":
        if x.count(numeral) < y.count(numeral):
            return True
    return False
