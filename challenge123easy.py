#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 123 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1dbpm9/042913_challenge_123_easy_newline_troubles/
#
# May.29.2015


import argparse


def print_in_encoding(fp, encoding):
    for line in fp:
        if encoding == 'windows':
            print line.replace('\n', '\r\n'),
        else:
            print line,


def main():
    parser = argparse.ArgumentParser(description='Convert a file to a Windows or Unix encoding')
    parser.add_argument('FILE',
                         type=argparse.FileType('rU'),  # universal newline support
                         )
    parser.add_argument('encoding', choices=['windows', 'unix'])
    args = parser.parse_args()
    print_in_encoding(args.FILE, args.encoding)


if __name__ == '__main__':
    main()
