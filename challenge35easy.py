#!/usr/bin/env python
# encoding: utf-8


def triange(num):
    rows = []

    row = []
    width = 1
    prev_width = width

    for index, i in enumerate(range(1, num + 1)):
        row.append(str(i))
        width = width - 1

        if width == 0:
            rows.append(' '.join(row))
            row = []
            width = prev_width + 1
            prev_width = width

            if (num - (index)) < (prev_width + 1):
                break

    return '\n'.join(reversed(rows))
