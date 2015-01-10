#!/usr/bin/env python
# encoding: utf-8


#######################################################################
#                       challenge 52 easy                             #
#######################################################################

def merge_lists(list_a, list_b):
    result = []

    while list_a and list_b:
        if list_a <= list_b:
            result.append(list_a.pop(0))
        else:
            result.append(list_b.pop(0))

    while list_a:
        result.append(list_a.pop(0))
    while list_b:
        result.append(list_b.pop(0))

    return result
