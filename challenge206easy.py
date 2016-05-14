#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 206 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2z68di/20150316_challenge_206_easy_recurrence_relations/
#
# 14 May 2016

import re
import operator
import fileinput


OP_MAP = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,
    '/': operator.floordiv
}

def parse_recurrance_steps(s):
    steps = []
    tokens = s.split()
    for token in tokens:
        m = re.match(r'([-+*/])(-?\d+)', token)
        if not m:
            raise ValueError("Can't parse '{}'".format(token))
        op = OP_MAP[m.group(1)]
        num = int(m.group(2))
        steps.append((op, num))
    return steps

def get_recurrence_answer(start, steps, nsteps):
    a = start
    for _ in range(nsteps):
        for op, b in steps:
            a = op(a, b)
    return a

def main():
    steps = parse_recurrance_steps(input())
    start = int(input())
    nsteps = int(input()) + 1

    for term in range(nsteps):
        result = get_recurrence_answer(start, steps, term)
        print('Term {:>2}: {:>5}'.format(term, result))

if __name__ == "__main__":
    main()
