#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 275 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/4so25w/20160713_challenge_275_intermediate_splurthian/
#
# 06 August 2016

from __future__ import print_function


def possible_symbols(elm_name):
    alphabet = elm_name.lower()
    for i, ch in enumerate(alphabet):
        for ii, ch2 in enumerate(alphabet[i+1:]):
            yield (''.join([ch, ch2])).capitalize()


if __name__ == "__main__":
    with open('275interm.txt', 'rU') as f:
        elements = [l.strip() for l in f]

    symbols = []
    for elm in elements:
        found = False
        for symbol_candidate in possible_symbols(elm):
            if symbol_candidate not in symbols:
                symbols.append(symbol_candidate)
                found = True
                print('{}: {}'.format(elm, symbol_candidate))
                break
        if not found:
            print('Cannot find a name for', elm)
            break
