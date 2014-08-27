#!/usr/bin/env python

import string


title = "Necessities"
data = ['fairy', 'cakes', 'happy', 'fish',
        'disgsdfsdfsafustipated', 'melon-balls']


def max_len(a, b):
    if len(a) > len(b):
        return a
    return b


def draw_title_box(title, data):
    longest_word = reduce(max_len, [title]+data)
    box_width = len(longest_word) + 4

    print '+' + ('-'*(box_width-2)) + '+'
    print '|' + string.center(title, box_width-2) + '|'
    print '+' + ('-'*(box_width-2)) + '+'
    for word in data:
        print '|' + string.ljust(word, box_width-2) + '|'
    print '+' + ('-'*(box_width-2)) + '+'
