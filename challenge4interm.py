#!/usr/bin/env python
# encoding: utf-8

import operator
import string


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
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


def infix_calc(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, int):
            stack.append(token)
        if isinstance(token, str):
            a = stack.pop()
            b = stack.pop()
            result = operators[token](a, b)
            stack.append(result)


def calculate(expr):
    out_queue = []
    op_stack = []

    tokens = tokenize(expr)
    for token in tokens:
        if isinstance(token, int):
            out_queue.append(token)
        if isinstance(token, str):
            op_stack.append(token)

    while op_stack:
        out_queue.append(op_stack.pop())

    return ''.join(out_queue)
