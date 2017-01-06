#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 298 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/5llkbj/2017012_challenge_298_easy_too_many_parentheses/
#
# 03 January 2017


def build_tree(text, pos=0):
    tree = []
    while pos < len(text):
        if text[pos] == '(':
            child, pos = build_tree(text, pos+1)
            if len(child):
                tree.append(child)
        elif text[pos] == ')':
            if len(tree) == 1 and isinstance(tree[0], list):
                return tree[0], pos+1
            return tree, pos+1
        else:
            tree.append(text[pos])
            pos += 1
    return tree


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(build_tree("(((abc)((cde))))"))
