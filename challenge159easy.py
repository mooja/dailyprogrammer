#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 159 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/23lfrf/4212014_challenge_159_easy_rock_paper_scissors/
#
# September.21.2015

from random import choice


CHOICES = ['scissors', 'paper', 'rock', 'lizard', 'spock']


class Move(object):
    def __init__(self, movestr):
        self.move =  



def play_round(p1choice, p2choice):
    if p1choice not in CHOICES or p2choice not in CHOICES:
        return 'Unknown move.'

    if
