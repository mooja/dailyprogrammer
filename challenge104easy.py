#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 104 Easy
#
# http://np.reddit.com/r/dailyprogrammer/comments/11paok/10182012_challenge_104_easy_powerplant_simulation/
#
# May.08.2015


def plantIsWorking(dayNum):
    """TODO: Docstring for planIsWorking.

    :dayNum: day number
    :returns: true if powerplant is working this day, otherwise false

    """
    return dayNum % 3 and dayNum % 14 and dayNum % 100


def numDaysWorking(ndays):
    return len(filter(plantIsWorking, range(1, ndays+1)))


if __name__ == '__main__':
    print numDaysWorking(10)
