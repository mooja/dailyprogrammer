#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 162 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/25clki/5122014_challenge_162_easy_novel_compression_pt_1/
#
# January.01.2016


import re


def decode(dict, encoded_text):
    output = []
    chunks = encoded_text.split()
    for chunk in chunks:
        m = re.match(r'(?P<num>\d+)(?P<modifier>.)?$', chunk)
        if m:
            word_num = int(m.groupdict()['num'])
            word_modifier = m.groupdict()['modifier']
            output.append(dict[word_num])
            if word_modifier:
                if word_modifier == '^':
                    output[-1] = output[-1].capitalize()
                if word_modifier == '!':
                    output[-1] = output[-1].upper()
                if word_modifier == '-':
                    output[-1] = output[-1] + '-'
        else:
            instruction = chunk
            if instruction in '.,?!:;':
                output[-1] = output[-1] + instruction
            if instruction == 'R':
                output.append('\n')
            if instruction == 'E':
                return output


if __name__ == '__main__':
    dictionary = ['is', 'my', 'hello', 'name', 'stan']
    encoded_line = '2! ! R 1^ 3 0 4^ . E'
    print(decode(dictionary, encoded_line))
