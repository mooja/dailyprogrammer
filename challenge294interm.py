#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 294 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/5h40ml/20161207_challenge_294_intermediate_rack/
#
# 28 December 2016

from operator import itemgetter
from string import ascii_lowercase


VALS = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
CHARVALS = dict(zip(ascii_lowercase, VALS))


def word_score(w):
    return sum((idx+1)*CHARVALS[ch] for idx, ch in enumerate(w))


def can_form(tiles, word):
    tiles = list(tiles)
    for ch in word:
        if ch not in tiles:
            return False
        tiles.remove(ch)
    return True


if __name__ == "__main__":
    inputs = [
        "iogsvooely",
        "seevurtfci",
        "vepredequi",
        "umnyeoumcp",
        "orhvtudmcz",
        "fyilnprtia"
    ]

    with open('enable1.txt') as f:
        words = (l.strip() for l in f)
        word_scores = [(w, word_score(w)) for w in words]
        word_scores.sort(key=itemgetter(1), reverse=True)

    for inp in inputs:
        for word, score in word_scores:
            if can_form(inp, word):
                print('highest("{}") -> {} ("{}")'.format(inp, score, word))
                break
