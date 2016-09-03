#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 281 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/50hbtp/20160831_challenge_281_intermediate_dank_usernames/
#
# 02 September 2016


def is_substr(candidate, target):
    """
    >>> is_substr('abc', 'zz a zzz b zzz c')
    True
    >>> is_substr('abc', 'zz zzz b zzz a')
    False
    >>> is_substr('donut', 'donald knuth')
    True
    >>> is_substr('cannon', 'claude shannon')
    True
    """
    target_idx = 0
    for ch in candidate:
        ch_found = False
        while target_idx < len(target):
            if target[target_idx] == ch:
                target_idx += 1
                ch_found = True
                break
            else:
                target_idx += 1

        if not ch_found:
            return False

    return True


def is_dank(candidate, target):
    if candidate.lower()[0] != target.lower()[0]:
        return False
    return is_substr(candidate, target.lower())


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    with open('enable1.txt') as f:
        dictionary = [line.strip() for line in f]

    inputs = ['Donald Knuth', 'Alan Turing', 'Claude Shannon']
    for inp in inputs:
        dank_names = [w for w in dictionary if is_dank(w, inp)]
        if dank_names:
            print(inp, '->', sorted(dank_names, key=len)[-1])
        else:
            print('No dank name for {}'.format(inp))
