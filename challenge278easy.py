#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 278 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4wqzph/20160808_challenge_278_easymed_weave_insert_part_1/
#
# 09 August 2016

from itertools import cycle
from itertools import repeat


def ins_weave(seq1, seq2):
    interweaved = [seq2[0]]
    for a, b in zip(cycle(seq1), seq2[1:]):
        interweaved.append(a)
        interweaved.append(b)
    return interweaved


def ins_bracket(seq1, seq2):
    interweaved = []
    for a, b in zip(seq1, repeat(seq2)):
        interweaved.append(b[0])
        interweaved.append(a)
        interweaved.append(b[1])
    return interweaved


if __name__ == "__main__":
    print(''.join(ins_weave('+-', '12345')))
    print(''.join(ins_bracket(['2+3', '4-5', '6+7'], '()')))
