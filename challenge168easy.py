#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Daily Programmer Challenge 168 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/28vgej/6232014_challenge_168_easy_final_grades_test_data/
#
# January.31.2016


import random


FIRST_NAMES = ['jon', 'ned', 'cat', 'rob', 'sansa', 'robert', 'stannis']
LAST_NAMES = ['snow', 'stark', 'lannister', 'griffith', 'baratheon']


def gen_student_record(nscores):
    name = ', '.join([random.choice(FIRST_NAMES), random.choice(LAST_NAMES)])
    scores = [random.randrange(0, 101) for n in range(nscores)]
    record = [name] + scores
    return record


if __name__ == "__main__":
    for i in xrange(10):
        srecord = gen_student_record(5)
        print('{:>16} {:>3} {:>3} {:>3} {:>3} {:>3}'.format(*srecord))
