#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 140 Easy
#
# url
#
# June.16.2015


from challenge49easy import montyhall_round


def main():
    nrounds = input()
    change_choice_wins = 0
    keep_choice_wins = 0

    for round in range(nrounds):
        change_choice_wins += montyhall_round(change_choice=True)
        keep_choice_wins += montyhall_round(change_choice=False)

    print "Tactic 1: {:.1f} winning chance".format(
        100*(keep_choice_wins / float(nrounds)))

    print "Tactic 2: {:.1f} winning chance".format(
        100*(change_choice_wins / float(nrounds)))


if __name__ == '__main__':
    main()
