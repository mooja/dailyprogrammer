#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 247 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/3yiy2d/20151228_challenge_247_easy_secret_santa/
#
# 24 June 2016

import random
import fileinput


def main():
    families = {}
    for idx, line in enumerate(fileinput.input()):
        families[idx] = line.strip().split()

    def family_idx(target_person):
        for idx, family in families.items():
            for p in family:
                if target_person == p:
                    return idx

    persons = [person for family in families.values()
                      for person in family]

    ss_assignments = {}
    giftees_assigned = []
    for person in persons:
        family = families[family_idx(person)]
        giftee_choices = set(persons) - set(family) - set(giftees_assigned)
        giftee = random.choice(list(giftee_choices))
        ss_assignments[person] = giftee
        giftees_assigned.append(giftee)

    for ss, giftee in ss_assignments.items():
        print('{} -> {}'.format(ss, giftee))


if __name__ == "__main__":
    main()
