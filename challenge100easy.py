#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 100 Easy
#
# http://np.reddit.com/r/dailyprogrammer/comments/106go0/9202012_challenge_100_easy_sleep_cycle_estimator/
#
# May.04.2015


from datetime import datetime
from datetime import timedelta

def test_stuff(sadf):
    pass

def when2sleep(wakeup_datetime, cycle_minutes=90):
    """ takes in a wakeup datetime object and returns a list of four optimal
        times to fall asleep

    :cycle_minutes: minutes in a sleep cycle
    :wakeup_datetime: datetime object representing time to wake up
    :returns: a list of four datetime objects representing optimal times to
              fall alseep.

    """
    sleep_chunk = timedelta(minutes=cycle_minutes)
    chunks_in_8hours = (60 * 8) / cycle_minutes
    asleep_times = []
    for i in range(4):
        asleep_time = wakeup_datetime - (sleep_chunk * (chunks_in_8hours - 2 + i))
        asleep_times.append(asleep_time)

    return asleep_times


def test_when2sleep():
    wakeup_time = datetime(2015, 5, 4, 6, 30)
    expected_asleep_time = datetime(2015, 5, 3, 23, 0)
    sleeptimes = when2sleep(wakeup_time)
    assert expected_asleep_time in sleeptimes


if __name__ == '__main__':
    test_when2sleep()
