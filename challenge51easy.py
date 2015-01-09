#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#                          challenge 51 easy                          #
#######################################################################

def word_value(word):
    def letter_value(letter):
        return ord(letter.lower()) - ord('a') + 1
    return sum(map(letter_value, word))
