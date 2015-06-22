#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 145
#
# http://www.reddit.com/r/dailyprogrammer/comments/1t0r09/121613_challenge_145_easy_tree_generation/
#
# June.21.2015


def draw_tree(max_width, trunk_char, leaves_char):
    for i in range(1, max_width+1, 2):
        yield '{0:^{width}}'.format(leaves_char*i, width=max_width)
    yield '{0:^{width}}'.format(trunk_char*3, width=max_width)


def main():
    max_width, trunk_char, leaves_char = raw_input().split()
    max_width = int(max_width)

    for line in draw_tree(max_width, trunk_char, leaves_char):
        print line


if __name__ == '__main__':
    main()
