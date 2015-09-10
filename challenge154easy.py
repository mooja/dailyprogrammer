#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 154 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/217klv/4242014_challenge_154_easy_march_madness_brackets/
#
# September.10.2015


import re


def unbracket(text):
    tokens = re.split(r'([\[\]\(\)\{\}])', text)
    tokens = map(str.strip, tokens)
    tokens = filter(bool, tokens)

    stack = []
    output_queue = []

    for token in tokens:
        if token not in ')]}':
            stack.append(token)
        else:
            temp_stack = []
            while stack[-1] not in '([{':
                temp_stack.insert(0, stack.pop())
            output_queue.extend(temp_stack)
            stack.pop()

    return ' '.join(output_queue)


if __name__ == '__main__':
    print unbracket('((your[drink {remember to}]) ovaltine)')
    print unbracket('[can {and it(it (mix) up ) } look silly]')
