#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Daily Programmer Challenge 172 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2ba3g3/7212014_challenge_172_easy/
#
# February.23.2016


def parse_alphabet():
    alphabet = {}
    with open('font.txt', 'r') as f:
        lines = f.readlines()
        while lines:
            letter = lines[0].strip()
            char_matrix = [line.strip() for line in lines[1:8]]
            alphabet[letter] = char_matrix
            del lines[:8]
    return alphabet


def text2pbm(text):
    alphabet = parse_alphabet()
    height = 7
    width = 5*len(text) + len(text)-1
    output_lines = ['P1', '{} {}'.format(height, width)]

    for i in range(7):
        line = []
        for ch in text:
            line.append(alphabet[ch.upper()][i])
        line = ' 0 '.join(line)
        output_lines.append(line)

    return output_lines


def main():
    with open('172output.pbm', 'w') as outfile:
        outfile.writelines('\n'.join(text2pbm('hello')))

if __name__ == "__main__":
    main()
