#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 106 Intermediate
#
# http://www.reddit.com/r/dailyprogrammer/comments/11xjfd/10232012_challenge_106_intermediate_jugs/
#
# May.10.2015

from operator import attrgetter
from collections import namedtuple
from itertools import combinations, permutations


Jug = namedtuple('Jug', 'gallons, capacity')

JugsState = namedtuple('JugsState', 'jugs, actions')


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


def sort_jugs_by_capacity(jugs):
    return sorted(jugs, key=attrgetter('capacity'))


def gen_new_jug_states(jugs_state):
    successor_states = []

    # generate jug states by filling each jug that is not filled
    for jug in jugs_state.jugs:
        if not is_full(jug):
            # copy state (other than the jug we're going to fill)
            new_jugs_state = JugsState([j for j in jugs_state.jugs if j != jug],
                                       [action for action in jugs_state.actions])
            new_jugs_state.jugs.append(fill_jug(jug))
            new_jugs_state.jugs.sort(key=attrgetter('capacity'))
            new_jugs_state.actions.append("> filled ({}, {})".format(
                jug.gallons, jug.capacity))
            new_jugs_state.actions.append("current state: {}".format(new_jugs_state.jugs))
            successor_states.append(new_jugs_state)


    # generate jug states by empying each jug that is not empty
    for jug in jugs_state.jugs:
        if not is_empty(jug):
            # copy state (other than the jug we're going to empty)
            new_jugs_state = JugsState([j for j in jugs_state.jugs if j != jug],
                                       [action for action in jugs_state.actions])
            new_jugs_state.jugs.append(empty_jug(jug))
            new_jugs_state.jugs.sort(key=attrgetter('capacity'))
            new_jugs_state.actions.append("> emptied ({}, {})".format(
                jug.gallons, jug.capacity))
            new_jugs_state.actions.append("current state: {}".format(new_jugs_state.jugs))
            successor_states.append(new_jugs_state)


    # generate jug states by transferring contents each jug into another
    for jug1, jug2 in permutations(jugs_state.jugs):
        if is_empty(jug1) or is_full(jug2):
            continue

        new_jugs_state = JugsState([j for j in jugs_state.jugs if j != jug1 and j != jug2],
                                   [action for action in jugs_state.actions])
        new_jugs_state.jugs.append(transf_from_1_to_2(jug1, jug2)[0])
        new_jugs_state.jugs.append(transf_from_1_to_2(jug1, jug2)[1])
        new_jugs_state.jugs.sort(key=attrgetter('capacity'))
        new_jugs_state.actions.append("> transfered {} to {}".format(
            jug1, jug2))
        new_jugs_state.actions.append("current state: {}".format(new_jugs_state.jugs))
        successor_states.append(new_jugs_state)

    return successor_states


def main():
    def is_wanted_jug_state(jugs_state):
        return jugs_total_gallons(jugs_state.jugs) == 4

    initial_jugs_state = JugsState([Jug(0, 3), Jug(0, 5)], actions=['initial'])
    jug_state_queue = [initial_jugs_state]

    while jug_state_queue:
        if is_wanted_jug_state(jug_state_queue[0]):
            print '\n'.join(jug_state_queue[0].actions)
            print "Wanted state reached!"
            break

        jug_state = jug_state_queue.pop(0)
        jug_state_queue.extend(gen_new_jug_states(jug_state))


    # output:

    # initial
    # > filled (0, 3)
    # current state: [Jug(gallons=3, capacity=3), Jug(gallons=0, capacity=5)]
    # > transfered Jug(gallons=3, capacity=3) to Jug(gallons=0, capacity=5)
    # current state: [Jug(gallons=0, capacity=3), Jug(gallons=3, capacity=5)]
    # > filled (0, 3)
    # current state: [Jug(gallons=3, capacity=3), Jug(gallons=3, capacity=5)]
    # > transfered Jug(gallons=3, capacity=3) to Jug(gallons=3, capacity=5)
    # current state: [Jug(gallons=1, capacity=3), Jug(gallons=5, capacity=5)]
    # > emptied (5, 5)
    # current state: [Jug(gallons=1, capacity=3), Jug(gallons=0, capacity=5)]
    # > transfered Jug(gallons=1, capacity=3) to Jug(gallons=0, capacity=5)
    # current state: [Jug(gallons=0, capacity=3), Jug(gallons=1, capacity=5)]
    # > filled (0, 3)
    # current state: [Jug(gallons=3, capacity=3), Jug(gallons=1, capacity=5)]
    # Wanted state reached!
