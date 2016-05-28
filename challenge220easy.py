#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 220 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/3aqvjn/20150622_challenge_220_easy_mangling_sentences/
#
# 28 May 2016

import re


def get_punctuation_locs(word):
    """ returns indexes of all non alphabetic chars 
        >>> get_punctuation_locs('Mr.Smith.')
        (2, 8)
    """
    locs = []
    for idx, ch in enumerate(word):
        m = re.match(r'\W', ch)
        if m:
            locs.append(idx)
    return tuple(locs)

def get_capitalized_locs(word):
    """ returns indexes of all capitalized chars
        >>> get_capitalized_locs('Mr.Smith.')
        (0, 3)
    """
    locs = []
    for idx, ch in enumerate(word):
        m = re.match(r'[A-Z]', ch)
        if m:
            locs.append(idx)
    return tuple(locs)


def mangle_word(word):
    """
    >>> mangle_word('time-worn')
    'eimn-ortw'
    >>> mangle_word("Mickey's")
    "Ceikms'y"
    """
    if type(word) is not str:
        word = word.group(0)
    p_locs = get_punctuation_locs(word)
    c_locs = get_capitalized_locs(word)
    sorted_chars = sorted(re.sub(r'\W', '', word.lower()))

    # insert punctuation
    for loc in p_locs:
        sorted_chars.insert(loc, word[loc])

    # capitalize
    for loc in c_locs:
        sorted_chars[loc] = sorted_chars[loc].upper()

    return ''.join(sorted_chars)

def main():
    sentence = input().strip()
    mangled_sentence = re.sub(r'\S+', mangle_word, sentence)
    print(mangled_sentence)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
