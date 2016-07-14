#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 263 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4gc24w/20160425_challenge_264_easy_sort_my_code/
#
# 14 July 2016

import re

from collections import deque
from collections import defaultdict


class helpers(object):
    @staticmethod
    def braces_cmp(line):
        if line.replace(' ', '').startswith('{'):
            return 0
        elif line.replace(' ', '').startswith('}'):
            return 2
        return 1

    @staticmethod
    def startswith_int_cmp(line):
        if line.replace(' ', '').startswith('int'):
            return 0
        return 1

    @staticmethod
    def for_cmp(line):
        if line.replace(' ', '').startswith('for'):
            return 0
        return 1

def sort_code(text):
    # includes first
    lines = text.split('\n')
    includes = filter(lambda l: l.startswith('#'), lines)
    lines = filter(lambda l: not l.startswith('#'), lines)
    for line in includes:
        yield line

    # group by indentation level
    indentation = defaultdict(lambda: [])
    for line in lines:
        m = re.match(r'^(\s*).*$', line)
        level = len(m.group(1))
        indentation[level].append(line)

    for indent_level in sorted(indentation.keys()):
        indentation[indent_level].sort(key=helpers.braces_cmp)
        indentation[indent_level].sort(key=helpers.for_cmp)
        indentation[indent_level].sort(key=helpers.startswith_int_cmp)

    indent_level = 0
    max_indent = sorted(indentation.keys())[-1]
    line_queue = deque(indentation[indent_level])
    while line_queue:
        line = line_queue.popleft()
        yield line
        if line.replace(' ', '').startswith('{'):
            indent_level += 2
            inner_lines = indentation[indent_level]
            inner_lines.append(line.replace('{', '}'))
            inner_lines.reverse()
            line_queue.remove(line.replace('{', '}'))
            line_queue.extendleft(inner_lines)

if __name__ == "__main__":
    text = """    sum = i + sum;
  {
  }
  int sum = 0
  for (int i = 0; i <= 100; ++i)
  std::cout << sum;
  return 0;
{
}
#include <iostream>
int main()"""
    for line in (sort_code(text)):
        print(line)
