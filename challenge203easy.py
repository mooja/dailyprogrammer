#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def square(size=5):
    top = '+' + '-'*(size-2) + '+' + '\n'
    bottom = top
    yield top
    for i in range(size-2):
        yield '|' + ' '*(size-2) + '|' + '\n'
    yield bottom


if __name__ == '__main__':
    if len(sys.argv) == 2:
        sys.stdout.writelines(square(int(sys.argv[1])))
    else:
        sys.stdout.writelines(square())
