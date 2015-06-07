#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 131 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1heozl/070113_challenge_131_easy_who_tests_the_tests/
#
# June.07.2015


def reverse_string(s):
    return s[::-1]


def to_upper(s):
    return s.upper()


def main():
    func_map = {'0': reverse_string,
                '1': to_upper}

    num_lines = input()
    for _ in range(num_lines):
        n, a, b = raw_input().strip().split()
        if func_map[n](a) == b:
            print 'Good test data'
        else:
            print 'Mismatch! Bad test data'


if __name__ == '__main__':
    main()
