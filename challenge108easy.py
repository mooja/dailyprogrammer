#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 107 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1268t4/10272012_challenge_108_easy_scientific_notation/
#
# May.12.2015


def sci_notation(num):
    """ sci_notation: return a scientific representation of num
        :num: number
        :returns: scientific notation string

        >>> sci_notation(100)
        '1.0 x 10^2'
        >>> sci_notation(.002)
        '2.0 x 10^-3'
        >>> sci_notation(123.456)
        '1.23456 x 10^2'
        >>> sci_notation(-123.456)
        '-1.23456 x 10^2'
    """
    if num == 0:
        return '0.0 x 10^1'

    magnitude = 0
    sign = 1 if num > 0.0 else -1
    num = abs(num)

    while num >= 10.0:
        num /= 10.0
        magnitude += 1  # Pop pop!

    while num < 1.0:
        num *= 10.0
        magnitude -= 1  # Pop... pop? :(

    return '{} x 10^{}'.format(sign*num, magnitude)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
