#!/usr/bin/env python
# encoding: utf-8


from datetime import datetime


def fmt_datetime(fmt):
    now = datetime.now()
    fmt_map = {
       '%l': now.microsecond / 1000,
       '%s': now.second,
       '%m': now.minute,
       '%h': now.hour % 12,
       '%H': now.hour, 
       '%c': 'PM' if now.hour / 12 else 'AM',
       '%d': now.day,
       '%M': now.month,
       '%y': now.year
    }

    result = fmt
    for key in fmt_map:
        result = result.replace(key, str(fmt_map[key]))
    return result


if __name__ == '__main__':

    print fmt_datetime("%s.%l")
    print fmt_datetime("%s:%m:%h %M/%d/%y")
    print fmt_datetime("The minute is %m! The hour is %h.")
