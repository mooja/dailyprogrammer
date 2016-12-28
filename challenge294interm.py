#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 294 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/5h40ml/20161207_challenge_294_intermediate_rack/
#
# 28 December 2016

from operator import itemgetter
from collections import Counter
from string import ascii_lowercase


VALS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
CHARVALS = dict(zip(ascii_lowercase, VALS))


def word_score(w):
    return sum((idx+1)*CHARVALS[ch] for idx, ch in enumerate(w))


def can_form(tiles, word):
    return Counter(tiles) & Counter(word) == Counter(word)


def find_highest_score(tiles, word_scores):
    possible_words = ((w, s) for w, s in word_scores.items() if can_form(tiles, w))
    possible_words = sorted(possible_words, key=itemgetter(1))
    return possible_words[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    with open('enable1.txt') as f:
        dictionary = (l.strip() for l in f)
        word_scores = {w: word_score(w) for w in dictionary}

    inputs = ["iogsvooely", "seevurtfci", "vepredequi", "umnyeoumcp", "orhvtudmcz", "fyilnprtia"]
    for inp in inputs:
        hword, hscore = find_highest_score(inp, word_scores)
        print('highest("{}") -> {} ("{}")'.format(
            inp, hscore, hword
        ))
