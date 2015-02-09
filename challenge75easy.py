#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 75 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/wfhua/7122012_challenge_75_easy_function_transformation/
#
# You are going to write a home-work helper tool for high-school students
# who are learning C for the first time. These students are in the advanced
# placement math course, but do not know anything about programming or
# formal languages of any kind. However, they do know about functions and
# variables!
#
# They have been given an 'input guide' that tells them to write simple pure
# mathematical functions like they are used to from their homework with a
# simple subset grammar, like this:
#
#     f(x)=x*x big(x,y)=sqrt(x+y)*10
#
# They are allowed to use sqrt,abs,sin,cos,tan,exp,log, and the mathematical
# arithmetic operators +*/-, they can name their functions and variables any
# lower-case alphanumeric name and functions can have between 0 and 15
# arguments.
#
# In the this challenge, your job is to write a program that can take in
# their "simple format" mathematical function and output the correct C
# syntax for that function. All arguments should be single precision, and
# all functions will only return one float.  As an example, the input
#
#     L0(x,y)=abs(x)+abs(y) should output
#
#     float L0(float x,float y) { return fabsf(x)+fabsf(y); }
#
#
# February.09.2015

import re


def math2c(expr):
    for op in ['exp', 'log', 'sqrt', 'abs', 'sin', 'cos', 'tan']:
        expr = expr.replace(op, op+"f")
    expr = expr.replace("absf", "fabsf")

    m = re.match(r"""
    ^                          # beginning of string
    (?P<func_name> [\w\d_]+)   # function name
    \(                         # opening paranthesis
    (?P<args>      [\w\d,]+)   # function arguments
    \)                         # closing parenthesis
    =                          # equals
    (?P<math_expr> .+)         # math expression
    $                          # end of string
    """, expr, re.X)

    if not m:
        raise ValueError("Unable to parse provided expression '{}'".format(expr))

    components = m.groupdict()
    cfunc_args = ','.join(
        'float {}'.format(arg)
        for arg in components['args'].split(','))
    cfunc_signature = "float {}({})".format(
        components['func_name'],
        cfunc_args)
    cfunc_body = "\n{{\n    return {}\n}}".format(components['math_expr'])
    cfunc = "{}{}".format(cfunc_signature, cfunc_body)

    return cfunc
