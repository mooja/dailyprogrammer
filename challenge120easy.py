#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 120 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/17uw4s/020413_challenge_120_easy_log_throughput_counter/
#
# May.25.2015


import signal


COUNTER = 0


def recieve_alarm(signum, stack):
    global COUNTER
    print COUNTER
    COUNTER = 0
    signal.alarm(3)


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, recieve_alarm)
    signal.alarm(3)

    while True:
        tmp = raw_input()
        COUNTER += 1
