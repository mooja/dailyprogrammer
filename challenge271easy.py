#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 271 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4nvrnx/20160613_challenge_271_easy_critical_hit/
#
# 20 July 2016


def chance_gte(die_sides, target):
    """
    Returns the probabily of rolling higher than target number.
    """
    choice_space = range(1, die_sides+1)
    target_choices = [roll for roll in choice_space if roll >= target]
    return len(choice_space) / len(target_choices)


def kill_probability(d, h):
    """
    >>> kill_probability(4, 1)
    1.0
    >>> kill_probability(4, 4)
    0.25
    >>> kill_probability(4, 5)
    0.25
    >>> kill_probability(4, 6)
    0.1875
    >>> kill_probability(1, 10)
    1.0
    >>> kill_probability(8, 20)
    0.009765625
    """
    p = 1.0
    while h > d:
        p /= chance_gte(d, d)
        h -= d
    p /= chance_gte(d, h)
    return p


if __name__ == "__main__":
    import doctest
    doctest.testmod()
