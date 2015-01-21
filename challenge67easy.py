#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer challenge 67 Easy

# As we all know, when computers do calculations or store numbers, they don't
# use decimal notation like we do, they use binary notation. So for instance,
# when a computer stores the number 13, it doesn't store "1" and "3", it stores
# "1101", which is 13 in binary.
#
# But more than that, when we instruct it to store an integer, we usually tell
# it to store it in a certain datatype with a certain length. For (relatively
# small) integers, that length is usually as 32 bits, or four bytes (also
# called "one word" on 32-bit processors). So 13 isn't really stored as "1101",
# it's stored as "00000000000000000000000000001101".
#
# If we were to reverse that bit pattern, we would get
# "10110000000000000000000000000000", which written in decimal becomes
# "2952790016".
#
# Write a program that can do this "32-bit reverse" operation, so when given
# the number 13, it will return 2952790016.
#
# Note: just to be clear, for all numbers in this problem, we are using
# unsigned 32 bit integers.

# 15.01.21


# since python can store arbitrary length integers, we will have to emulate a
# 32-bit integer ourselves.

# on the other hand, it's less elegant but more steight forward to reason with
# strings

# TODO: convert to a numerical solution

def reverse_int(n, bytes=32):
    as_bin_str = bin(n)[2:]
    reversed_bin_str = ''.join(c for c in reversed(as_bin_str))
    padded = '{:0<32}'.format(reversed_bin_str)
    reversed_int = int(padded, 2)
    return reversed_int
