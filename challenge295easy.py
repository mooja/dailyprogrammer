#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 295 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/5hy8sm/20161212_challenge_295_easy_letter_by_letter/
#
# 21 December 2016


def transform(w1, w2):
    """
    >>> list(transform('wood', 'book'))
    ['wood', 'bood', 'book']
    """
    state = w1
    yield state
    while state != w2:
        for idx, letter in enumerate(w2):
            if state[idx] != w2[idx]:
                state = list(state)
                state[idx] = w2[idx]
                state = ''.join(state)
                yield state


if __name__ == "__main__":
    import doctest
    doctest.testmod()
