#!/usr/bin/env python
# encoding: utf-8


#######################################################################
#            challenge 58 easy - arbitrary base converter             #
#######################################################################


from string import digits
from string import ascii_lowercase


def to_base(base, number):
    alphabet = (digits + ascii_lowercase)[:base]
    result = []

    while number:
        quotient, remainder = divmod(number, base)
        result.insert(0, alphabet[remainder])
        number /= base

    return ''.join(result)


def main():
    print "19959694 in base 35 is {}".format(to_base(
        35, 19959694))
    print "376609378180550 in base 29 is {}".format(
        to_base(29, 376609378180550))


if __name__ == '__main__':
    main()
