#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#                          challenge 41 easy                          #
#                                                                     #
#   write a program that accepts a sentance as an input and outputs   #
#   the sentence surrounded in a banner                               #
#                                                                     #
#######################################################################


import fileinput


def in_banner(sentence):
    width = min(len(sentence), 76)
    lines = []

    if len(sentence) <= 76:
        lines = [sentence]
    else:
        words = sentence.split(' ')
        line = ''
        for word in words:
            if (len(line) + len(word) + 1) > 76:
                lines.append(line)
                line = word
            else:
                line = ' '.join(line.split() + [word])
        lines.append(line)

    for i, line_ in enumerate(lines):
        filler = (width - len(line_))*' '
        lines[i] = ('# ' + line_ + filler + ' #')

    lines.insert(0, '#'*(width + 4))
    lines.append('#'*(width + 4))
    return '\n'.join(lines)


if __name__ == '__main__':
    for line in fileinput.input():
        print in_banner(line.strip())
