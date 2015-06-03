#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 128 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1fnutb/06413_challenge_128_easy_sumthedigits_part_ii/
#
# June.03.2015


def sum_digits(n):
    n = abs(n)
    while True:
        yield n
        if n < 10:
            break
        n = sum(int(digit) for digit in abs(n))


def main():
    #  assumes correct input
    numbers = sum_digits(input("Enter a digit: "))
    for n in numbers:
        print n


if __name__ == '__main__':
    main()
