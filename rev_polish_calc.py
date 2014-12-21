#!/usr/bin/env python
# encoding: utf-8

# reverse polish calculator
import operator as op

funcs = dict()
funcs['+'] = op.add
funcs['-'] = op.sub
funcs['*'] = op.mul
funcs['/'] = op.div


def parsenum(s):
    try:
        n = int(s)
    except ValueError:
        n = float(s)
    return n

def calc(expr):
    tokens = filter(len, expr.split())
    stack = [0]

    for token in tokens:
        if token in funcs.keys():
            y, x = parsenum(stack.pop()), parsenum(stack.pop())
            stack.append(funcs[token](x, y))
        else:
            stack.append(float(token))

    return stack.pop()
