#!/usr/bin/env python
# encoding: utf-8


#######################################################################
#             determine population count of a bit string              #
#######################################################################

def population_count(number):
    bit_string = bin(number)[2:]
    count = bit_string.count('1')
    return count
