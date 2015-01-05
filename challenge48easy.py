#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#                          challenge 48 easy                          #
#######################################################################

def partition_evens(array):
    def cmpeven(a, b):
        return cmp(a % 2, b % 2)
    array.sort(cmp=cmpeven)
    return array
