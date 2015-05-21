#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 116 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/164zvs/010713_challenge_116_easy_permutation_of_a_string/
#
# May.20.2015


from itertools import permutations


def permute(word):
    return sorted(list(set(''.join(w) for w in permutations(word))))
