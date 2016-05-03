#!/usr/bin/env python3
# encoding: utf-8

# Daily Programmer Challenge 195 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2qmz12/20141228_challenge_195_easy_symbolic_link/
#
# 03.May.2016

import os

from collections import deque


def resolve_path(symlinks_dict, path):
    """
    >>> resolve_path({'/bin':'/usr/bin',\
                      '/usr/bin':'/usr/local/bin',\
                      '/usr/local/bin/log':'/var/log-2014'\
                     },\
                     '/bin/log/rc')
    '/var/log-2014/rc'

    """
    path = path[1:]
    path_tokens = deque(path.split('/'))

    current_path = '/'
    while path_tokens:
        current_path = os.path.join(current_path, path_tokens.popleft())
        while current_path in symlinks_dict:
            current_path = symlinks_dict[current_path]
    return current_path


if __name__ == '__main__':
    import doctest
    doctest.testmod()
