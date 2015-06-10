#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 133 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1iambu/071513_challenge_133_easy_foottraffic_analysis/
#
# June.09.2015

import StringIO

from collections import namedtuple


LogEntry = namedtuple('LogEntry', 'visitor_id, room_id, action, timestamp')


def parse_log_file(fp):
    n_entries = int(fp.readline().strip())
    entries = []
    for _ in range(n_entries):
        entry = LogEntry._make(fp.readline().strip().split())
        entries.append(entry)
    return entries


def main():
    entries = parse_log_file(sample_file())

    for room_id in sorted(set(entry.room_id for entry in entries), key=lambda x: int(x)):
        room_total_visitors = 0
        room_total_in_time = 0
        room_total_out_time = 0

        for timestamp, action in ((entry.timestamp, entry.action) for entry in entries if entry.room_id == room_id):
            if action == 'I':
                room_total_in_time += int(timestamp)
            if action == 'O':
                room_total_out_time += int(timestamp)
            room_total_visitors += 1

        room_total_visitors /= 2
        room_total_time = room_total_out_time - room_total_in_time
        room_avg_visit = room_total_time / room_total_visitors
        room_avg_visit += 1

        print 'Room {}, {} minute average visit, {} visitor(s) total'.format(
            room_id, room_avg_visit, room_total_visitors
        )


def sample_file():
    sample_data = """
    36
    0 11 I 347
    1 13 I 307
    2 15 I 334
    3 6 I 334
    4 9 I 334
    5 2 I 334
    6 2 I 334
    7 11 I 334
    8 1 I 334
    0 11 O 376
    1 13 O 321
    2 15 O 389
    3 6 O 412
    4 9 O 418
    5 2 O 414
    6 2 O 349
    7 11 O 418
    8 1 O 418
    0 12 I 437
    1 28 I 343
    2 32 I 408
    3 15 I 458
    4 18 I 424
    5 26 I 442
    6 7 I 435
    7 19 I 456
    8 19 I 450
    0 12 O 455
    1 28 O 374
    2 32 O 495
    3 15 O 462
    4 18 O 500
    5 26 O 479
    6 7 O 493
    7 19 O 471
    8 19 O 458
    """.lstrip()

    return StringIO.StringIO(sample_data)


if __name__ == '__main__':
    main()
