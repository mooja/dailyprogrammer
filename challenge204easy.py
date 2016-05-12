#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 204 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2xoxum/20150302_challenge_204_easy_remembering_your_lines/
#
# 12 May 2016


def get_passages(fname):
    with open(fname, 'r') as f:
        passage_lines = []
        for line in f:
            if line.startswith('    '):
                passage_lines.append(line.strip())
                continue
            if passage_lines:
                yield '\n'.join(passage_lines)
                passage_lines = []

def find_passage(fname, quote):
    for passage in get_passages(fname):
        if quote in passage:
            return passage
    return None

def main():
    quote = input('Enter quote: ')
    passage = find_passage('macbeth.txt', quote)
    if not passage:
        print('Passage not found.')
    else:
        print(passage)

if __name__ == '__main__':
    main()
