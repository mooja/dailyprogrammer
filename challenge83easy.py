#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 83 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/xdwyb/7302012_challenge_83_easy_long_scale_and_short/
#
# Your task today is to write a program that will print out the name of a
# number in both long-scale and short-scale. So, for instance, given
# 1234567891111, it should print out
#
# > Short scale: 1 trillion, 234 billion, 567 million, 891 thousand and 111
# > Long scale:  1 billion, 234 milliard, 567 million, 891 thousand and 111
#
# February.20.2015

import sys


MAPPING = {
    10**21: ('sextillion',  'trilliard'),
    10**18: ('quintillion', 'trillion'),
    10**15: ('quadrillion', 'billiard'),
    10**12: ('trillion',    'millard'),
    10**9:  ('billion',     'millard'),
    10**6:  ('million',     'million'),
    10**3:  ('thousand',    'thousand'),
    1:      ('', '')
}

HUMANIZE_MAPPING = {
    1:  "one",
    2:  "two",
    3:  "three",
    4:  "four",
    5:  "five",
    6:  "six",
    7:  "seven",
    8:  "eight",
    9:  "nine",
   10:  "ten",
   11:  "eleven",
   12:  "twelve",
   13:  "thirteen",
   14:  "fourteen",
   15:  "fifteen",
   16:  "sixteen",
   17:  "seventeen",
   18:  "eighteen",
   19:  "nineteen",
   20:  "twenty",
   30:  "thirty",
   40:  "fourty",
   50:  "fifty",
   60:  "sixty",
   70:  "seventy",
   80:  "eighty",
   90:  "ninety",
}

def humanize(num):
    if not (0 < num < 1000):
        raise ValueError("humanize() takes numbers between 1 and 999")

    output = []
    q_100, r_100 = divmod(num, 100)

    if q_100:
        output.append(HUMANIZE_MAPPING[q_100] + ' hundred')

    if r_100 != 0:
        r = r_100
        if q_100:
            output.append('and')

        for k in sorted(HUMANIZE_MAPPING.keys(), reverse=True):
            if r / k:
                output.append(HUMANIZE_MAPPING[k])
                r %= k

    return ' '.join(output)




def num2words(num):
    short, long = [], []
    for k in sorted(MAPPING.keys(), reverse=True):
        quotient, remainder = divmod(num, k)
        if quotient:
            short.append(humanize(quotient) + ' ' + MAPPING[k][0])
            long.append(humanize(quotient) + ' ' +  MAPPING[k][1])
        num = remainder
    short = ', '.join(short[:-1]) + ' and ' + short[-1]
    long  = ', '.join(long[:-1]) + ' and ' + long[-1]
    return short, long


def main(num):
    short, long = num2words(num)
    print("Number: {}", num)
    print("Short scale: {}".format(short))
    print("Long scale: {}".format(long))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
    else:
        num = 1234567891111
    main(num)
