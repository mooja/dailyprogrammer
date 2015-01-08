#!/usr/bin/env python
# encoding: utf-8


#######################################################################
#                          challenge 50 easy                          #
#######################################################################

def pick_two(cash_total, item_list):
    """
    find two tiems in item_list whose sum is equal to cash_total
    returns a tuple with indexes of two items, in sorted order
    """
    for i, item_candidate1 in enumerate(item_list):
        other_items = item_list[i+1:]
        for k, item_candidate2 in enumerate(other_items):
            if item_candidate1 + item_candidate2 == cash_total:
                return tuple(sorted((i+1, i+k+2)))
    return None
