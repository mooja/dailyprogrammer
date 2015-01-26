#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 69 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/vmblw/6262012_challenge_69_easy/
# 
#
# Write a program that takes a title and a list as input and outputs the
# list in a nice column. Try to make it so the title is centered. For
# example:
#
# title: 'Necessities'
# input: ['fairy', 'cakes', 'happy', 'fish', 'disgustipated', 'melon-balls']
#
# output:
#
#     +---------------+
#     |  Necessities  |
#     +---------------+
#     | fairy         |
#     | cakes         |
#     | happy         |
#     | fish          |
#     | disgustipated |
#     | melon-balls   |
#     +---------------+
# 
# 15.January.26


def columnize(title, tseq):
    maxlen = max(map(len, tseq))
    hor_sep = ''.join(['+-', '-'*maxlen, '-+'])

    def mk_row(text, center=False):
        prefix, postfix = ('| ', ' |')
        if center:
            spaces = ' '*((maxlen - len(text)) / 2)
            remainder = ' '*((maxlen - len(text)) % 2)
            prefix = prefix + spaces
            postfix = spaces + remainder + postfix
        else:
            spaces = ' '*(maxlen - len(text))
            postfix = spaces + postfix
        return ''.join([prefix, text, postfix])

    output = []
    output.append(hor_sep)
    output.append(mk_row(title, center=True))
    output.append(hor_sep)
    output.extend(map(mk_row, tseq))
    output.append(hor_sep)
    return '\n'.join(output) + '\n'
