#!/usr/bin/env python
# encoding: utf-8


#######################################################################
#          challenge 49 easy - Monty Hall Problem Simulation          #
#######################################################################

from random import choice


DEBUG = True

def get_host_choice(doors, player_choice):
    host_open_candidates = [i for i, door in enumerate(doors)
                                 if (door == 0 and i != player_choice)]
    host_open_choice = choice(host_open_candidates)
    return host_open_choice


def montyhall_round(change_choice=True):
    """ 
    Simulates a round of Monty Hall game in which the player changes
    his door choice after the host opens a door with a goat.

    returns: 0 if picked a goat
             1 if picked a car
    """
    doors = [0, 0, 0]
    doors[choice(range(3))] = 1
    player_initial_choice = choice(range(3))

    # host opens a different door with a goat in it
    host_open_choice = get_host_choice(doors, player_initial_choice)

    # player switches his choice based on which door the host has opened
    if change_choice:
        player_final_choice = [i
            for i, door in enumerate(doors)
                if i not in
                    (player_initial_choice, host_open_choice)][0]
    # player keeps his initial choice
    else:
        player_final_choice = player_initial_choice

    return doors[player_final_choice]


def main(num_rounds=100):
    change_choice_wins = 0
    keep_choice_wins = 0

    for round in range(num_rounds):
        change_choice_wins += montyhall_round(change_choice=True)
        keep_choice_wins += montyhall_round(change_choice=False)

    return change_choice_wins, keep_choice_wins


if __name__ == '__main__':
    num_rounds = 10000
    change_choice_wins, keep_choice_wins = main(num_rounds=num_rounds)

    print "Statistics for {num_rounds} rounds:".format(**locals())
    print "Win percentage with changing initial choice: {}%".format(
        100*(change_choice_wins / float(num_rounds))
    )
    print "Win percentage without changing initial choice: {}%".format(
        100*(keep_choice_wins / float(num_rounds))
    )
    print 
