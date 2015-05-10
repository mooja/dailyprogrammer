#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 106 Intermediate
#
# http://www.reddit.com/r/dailyprogrammer/comments/11xjfd/10232012_challenge_106_intermediate_jugs/
#
# May.10.2015

from collections import namedtuple
from itertools import combinations


Jug = namedtuple('Jug', 'gallons, capacity')


def is_full(jug):
    return jug.gallons >= jug.capacity


def is_empty(jug):
    return jug.gallons == 0


def fill_jug(jug):
    return Jug(jug.capacity, jug.capacity)


def empty_jug(jug):
    return Jug(0, jug.capacity)


def transf_from_1_to_2(jug1, jug2):
    avail_water = jug1.gallons
    avail_capacity = jug2.capacity - jug2.gallons
    total_transfer = min(avail_water, avail_capacity)

    jug1 = Jug(jug1.gallons - total_transfer, jug1.capacity)
    jug2 = Jug(jug2.gallons + total_transfer, jug2.capacity)

    return jug1, jug2


def jugs_total_gallons(jugs):
    return sum(jug.gallons for jug in jugs)


def gen_new_jug_states(jugs):
    successor_states = []

    # generate jug states by filling each jug that is not filled
    for jug in jugs:
        if not is_full(jug):
            new_jugs_state = [j for j in jugs if j != jug]
            new_jugs_state.append(fill_jug(jug))
            successor_states.append(new_jugs_state)


    # generate jug states by empying each jug that is not empty
    for jug in jugs:
        if not is_empty(jug):
            new_jugs_state = [j for j in jugs if j != jug]
            new_jugs_state.append(empty_jug(jug))
            successor_states.append(new_jugs_state)


    # generate jug states by transferring contents each jug into another
    pass
