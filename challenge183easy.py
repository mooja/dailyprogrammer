#!/usr/bin/env python3
# encoding: utf-8



# Daily Programmer Challenge 183 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2igfj9/10062014_challenge_183_easy_semantic_version_sort/
#
# 21.April.2016


import re

from operator import itemgetter


def parse_simver(simver_str):
    """
    >>> parse_simver("1.2.3-abc+metadata")
    (1, 2, 3, 'abc', 'metadata')
    >>> parse_simver("1.2.3")
    (1, 2, 3, None, None)
    """
    expr = re.compile(
    r"""(?P<major>\d+)
        \.
        (?P<minor>\d+)
        \.
        (?P<patch>\w+)
        (?P<label>\-\w+)?
        (?P<metadata>\+\w+)?
    """, re.X)
    m = expr.match(simver_str)
    version = [
        int(m.groupdict()['major']),
        int(m.groupdict()['minor']),
        int(m.groupdict()['patch']),
        None,
        None
    ]
    if 'label' in m.groupdict() and m.groupdict()['label'] is not None:
        version[3] = m.groupdict()['label'][1:]
    if 'metadata' in m.groupdict() and m.groupdict()['metadata'] is not None:
        version[4] = m.groupdict()['metadata'][1:]
    return tuple(version)


def sorted_simver(slist):
    """
    >>> sorted_simver(map(parse_simver, [\
        '2.0.11-alpha',\
        '0.1.7+amd64',\
        '0.10.7+20141005',\
        '2.0.12+i386',\
        '1.2.34',\
        '2.0.11+i386',\
        '20.1.1+i386',\
        ]))
    [(0, 1, 7, None, 'amd64'), (0, 10, 7, None, '20141005'), (1, 2, 34, None, None), (2, 0, 11, 'alpha', None), (2, 0, 11, None, 'i386'), (2, 0, 12, None, 'i386'), (20, 1, 1, None, 'i386')]
    """
    def label_keyfunc(simver):
        if simver[3] == None:
            return 1
        return 0

    slist = sorted(slist, key=label_keyfunc)
    slist = sorted(slist, key=itemgetter(2))
    slist = sorted(slist, key=itemgetter(1))
    slist = sorted(slist, key=itemgetter(0))
    return slist



if __name__ == '__main__':
    import doctest
    doctest.testmod()
