#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 310 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/64jesw/20170410_challenge_310_easy_kids_lotto/
#
# 14 April 2017

from random import shuffle


def randomized_lists(names, lotto_len):
    for idx, name in enumerate(names):
        rest = names[:idx] + names[idx+1:]
        shuffle(rest)
        lotto_list = '{name} -> {students}'.format(
            name=name,
            students='; '.join(rest[:lotto_len])
        )
        yield lotto_list


if __name__ == "__main__":
    names = "Rebbeca Gann;Latosha Caraveo;Jim Bench;Carmelina Biles;Oda Wilhite;Arletha Eason"
    lotto_len = 3
    for lotto_list in randomized_lists(names.split(';'), lotto_len):
        print(lotto_list)
