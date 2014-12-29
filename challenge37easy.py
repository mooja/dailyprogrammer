#!/usr/bin/env python
# encoding: utf-8

################################################
#  simple line counter for challenge 37 easy.  #
################################################

import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Count lines in a file.")
    parser.prog = 'wc.py'
    parser.add_argument('files',
                         type=argparse.FileType('r'),
                         nargs='+',
                         help='files to process')
    args = parser.parse_args()

    count = 0
    for file in args.files:
        fcount = 0
        for line in file:
            fcount += 1

        count += fcount
        print("{wc:>5}: {fname:>5}".format(fname=file.name, wc=fcount))

    print("{wc:>5} total".format(wc=count))
