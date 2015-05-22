#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 117 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/16jiuq/011413_challenge_117_easy_hexdump_to_ascii/
#
# May.21.2015


import argparse


def hexdump(file):
    bytes = file.read()
    for i in xrange(0, len(bytes), 16):
        print '{:0>8X} '.format(i),
        for byte in bytes[i:i+16]:
            print '{:0>2X}'.format(ord(byte)),
        print


def main():
    parser = argparse.ArgumentParser(description='Hexdump a file.')
    parser.add_argument('FILE', type=argparse.FileType('rb'), help='file to dump')
    args = parser.parse_args()

    hexdump(args.FILE)



if __name__ == '__main__':
    main()
