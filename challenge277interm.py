#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 277 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/4utlaz/20160727_challenge_277_intermediate_fake_coins/
#
# 01 August 2016

from collections import namedtuple


Statement = namedtuple('Statement', ['left', 'right', 'heavier'])


def determine_fake(statements):
    equals = []
    lighter = []
    for s in statements:
        if s.heavier == 'left':
            equals.extend(list(s.left))
            lighter.extend(list(s.right))
            lighter = [c for c in lighter if c not in s.left]
        if s.heavier == 'right':
            equals.extend(list(s.right))
            lighter.extend(list(s.left))
            lighter = [c for c in lighter if c not in s.right]
        if s.heavier == 'equal':
            equals.extend(s.left)
            equals.extend(s.right)
            lighter = [c for c in lighter if c not in s.right + s.left]

    equals = set(equals)
    lighter = set(lighter)
    if lighter & equals or len(lighter) > 1:
        return 'inconsistent'
    if not lighter:
        return 'no fakes'
    return '{} is lighter'.format(list(lighter)[0])


def main():
    data1 = 'a b left,a c equal'
    data2 = 'a c equal'
    data3 = 'a c equal,a b equal,c b left'
    data4 = 'ab xy left,b x equal,a b equal'
    data5 = 'a x equal,b x equal,y a left'
    data6 = 'abcd efgh equal,abci efjk left,abij efgl equal,mnopqrs tuvwxyz equal'
    data7 = 'abc efg equal,a e left'

    for i, data in enumerate([data1, data2, data3, data4, data5, data6, data7]):
        lines = data.split(',')
        statements = [Statement(*line.split()) for line in lines]
        print(data.replace(',', '\n'))
        print(determine_fake(statements))
        print()


if __name__ == "__main__":
    main()
