#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 141 Easy
#
# url
#
# June.16.2015


def fletcher_16(data):
    sum1, sum2 = 0, 0
    data = bytearray(data)

    for byte in data:
        sum1 = (sum1 + byte) % 255
        sum2 = (sum1 + sum2) % 255

    return (sum2 << 8) | sum1


def main():
    nlines = input()
    for _ in xrange(nlines):
        data = raw_input().strip()
        print '{:X}'.format(fletcher_16(data))


if __name__ == '__main__':
    main()
