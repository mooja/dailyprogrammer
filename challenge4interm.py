#!/usr/bin/env python
# encoding: utf-8

import operator
import string
import itertools

from heapq import heappush


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div
}

precedence = {
    '+': 2,
    '-': 2,
    '*': 4,
    '/': 4
}


def tokenize(expr):
    tokens = []
    expr = expr.replace(' ', '')
    i = 0
    while i < len(expr):
        c = expr[i]
        if c in operators:
            tokens.append(c)
        if c in string.digits:
            while expr[i+1:] and expr[i+1] in string.digits:
                c += expr[i+1]
                i += 1
            tokens.append(int(c))
        i += 1
    return tokens


def prefix_calc(tokens):
    stack = [0]
    for token in tokens:
        if isinstance(token, int):
            stack.append(token)
        if isinstance(token, str):
            a = stack.pop()
            b = stack.pop()
            result = operators[token](b, a)
            stack.append(result)
    return stack[-1]


def calculate(expr):
    out_queue = []
    op_stack = []

    tokens = tokenize(expr)
    for token in tokens:
        if isinstance(token, int):
            out_queue.append(token)
        if isinstance(token, str):
            while op_stack and precedence[op_stack[-1]] >= precedence[token]:
                out_queue.append(op_stack.pop())
            op_stack.append(token)

    while op_stack:
        out_queue.append(op_stack.pop())

    return prefix_calc(out_queue)
