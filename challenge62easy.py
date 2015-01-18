#!/usr/bin/env python
# encoding: utf-8

# daily programmer challenge 62 easy
# http://www.reddit.com/r/dailyprogrammer/comments/urqcx/682012_challenge_62_easy/


def ullmans_puzzle(sum_threshold, element_threshold, number_seq):
    sorted_seq = sorted(number_seq)
    smallest_elements = sorted_seq[:element_threshold]
    return sum(smallest_elements) < sum_threshold
