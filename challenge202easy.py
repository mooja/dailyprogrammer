#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challeng 202 Easy
#
# 
#
# May 10 2016

import fileinput

from string import ascii_lowercase


def main():
    data = ''.join(l.strip() for l in fileinput.input())
    ints = (int(data[i:i+8], base=2) for i in range(0, len(data), 8))
    print(''.join(chr(i) for i in ints))

if __name__ == '__main__':
    main()
