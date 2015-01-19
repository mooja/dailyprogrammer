#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#                          challenge 54 easy                          #
#######################################################################

from random import choice
from string import lowercase


def matrix_cypher_encode(key, text):
    " returns a matrix cypher of text using key "
    end = (len(text) / key) * key
    rows = [text[i:i+key] for i in range(0, end, key)]
    output = []

    for i in range(key):
        for row in rows:
            if (i+1) > len(row):
                output.append(choice(lowercase))
            else:
                output.append(row[i])

    return ''.join(output)


def matrix_cypher_decode(key, text):
    colsize = len(text) / key
    end = key * colsize 
    output = []

    for col_index in range(colsize):
        for i in range(col_index, end, colsize):
            output.append(text[i])

    return ''.join(output)
