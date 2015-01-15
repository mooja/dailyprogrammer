#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#                          challenge 59 easy                          #
#                       str.find method implementation                #
#######################################################################


def find_substring(substr, text):
    match = False

    for pos in xrange(len(text)):
        for j in xrange(len(substr)):
            if text[pos+j] != substr[j]:
                match = False
                break
            match = True

        if match:
            return pos

    return -1
