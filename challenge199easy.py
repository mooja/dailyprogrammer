#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 199 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2tr6yn/2015126_challenge_199_bank_number_banners_pt_1/
#
# 07.May.2016

import sys
import fileinput

from functools import wraps


def echo_f(f):
    @wraps(f)
    def f_(*args):
        result = f(*args)
        print('{}() returned: {}'.format(f.__name__, result))
        return result
    return f_

def get_banner(blines, banner_idx):
    banner = []
    for row in range(3):
        start_idx = banner_idx * 3
        end_idx = start_idx + 3
        banner.append(blines[row][start_idx:end_idx])
    return tuple(banner)

def print_banners(blines, banner_idxs):
    banners = [get_banner(blines, i) for i in banner_idxs]
    lines = [[] for _ in range(3)]
    for i in range(3):
        for banner in banners:
            lines[i].append(banner[i])
    lines = (''.join(line) for line in lines)
    for line in lines:
        yield line + '\n'

def main():
    banners_lines = (
      ' _     _  _     _  _  _  _  _ ',
      '| |  | _| _||_||_ |_   ||_||_|',
      '|_|  ||_  _|  | _||_|  ||_| _|',
    )

    for line in fileinput.input():
        line = line.strip()
        idxs = [int(ch) for ch in line]
        sys.stdout.writelines(print_banners(banners_lines, idxs))


if __name__ == '__main__':
    main()
