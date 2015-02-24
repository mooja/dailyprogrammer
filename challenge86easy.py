#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 86 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/xxbbo/882012_challenge_86_easy_runlength_encoding/
#
# February.24.2015

import re

def compress(s):
    """compress(s): compresses s by detecting repeated instanstes of a symbol
                    in a string and compressing them into a list of pairs of a
                    symbol and length.

       >>> compress("Heeeeelllllooooo nurse!")
       [(1, 'H'), (5, 'e'), (5, 'l'), (5, 'o'), (1, ' '), (1, 'n'), (1, 'u'), (1, 'r'), (1, 's'), (1, 'e'), (1, '!')]
    """
    result = [(len(reps), symbol)
              for reps, symbol in re.findall(r'((.)\2*)', s)]
    return result


def extract(rle_seq):
    """extract(rle_seq): takes RLE encodin of a string an returns the original string


       >>> extract(compress("helllloooooo nurse!"))
       'helllloooooo nurse!'
    """
    return ''.join(cnt*symbol for cnt, symbol in rle_seq)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
