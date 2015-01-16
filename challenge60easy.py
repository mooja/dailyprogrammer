#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#    challenge 60 easy - determine if a number is a polite number     #
#######################################################################

import math


def is_polite(politenum_candidate):
    nums = range(politenum_candidate)

    for i in xrange(politenum_candidate):
        for j in xrange(i, politenum_candidate):
            current_sum = sum(nums[i:j+1])
            if current_sum > politenum_candidate:
                break
            if current_sum == politenum_candidate:
                return True
    return False


def is_polite_alt(politenum_candidate):
    return bool(math.log(politenum_candidate, 2) % 1.0)
