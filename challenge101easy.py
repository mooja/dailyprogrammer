#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 101 Easy
#
# http://np.reddit.com/r/dailyprogrammer/comments/10l8ay/9272012_challenge_101_easy_nonrepeating_years/
#
# May.05.2015

# Write a program to count the number years in an inclusive range of years that
# have no repeated digits.

# For example, 2012 has a repeated digit (2) while 2013 does not. Given the
# range [1980, 1987], your program would return 7 (1980, 1982, 1983, 1984,
# 1985, 1986, 1987).

# Bonus: Compute the longest run of years of repeated digits and the longest
# run of years of non-repeated digits for [1000, 2013].


def hasUniqueDigits(year):
    """ hasUniqueDigits(year): returns True if all the digits in the year are unique,
                               otherwise false
        >>> hasUniqueDigits(2134)
        True
        >>> hasUniqueDigits(2012)
        False
    """
    ndigits = len(str(year))
    return len(set(str(year))) == ndigits


def numUniqueDigitYears(lo, hi):
    """ numUniqueDigitYears: returns a number of years with unique digits in an
                             inclusive range of years.
        >>> numUniqueDigitYears(1980, 1987)
        7
    """
    unique_years = [year for year in range(lo, hi+1)
                             if hasUniqueDigits(year)]
    return len(unique_years)


def longestRun(lo, hi, f):
    """ longestRun(lo, hi): compute the longest run of positive evals of f 
                            on the sequence [lo, hi] inclusive.
        >>> longestRun(1000, 1099, bool)
        100
        >>> longestRun(1000, 1015, hasUniqueDigits)
        0
        >>> longestRun(1, 15, hasUniqueDigits)
        10
    """
    longest_run = 0
    current_run = 0

    for x in range(lo, hi+1):
        if not f(x):
            current_run = 0
            continue
        current_run += 1
        if current_run > longest_run:
            longest_run = current_run

    return longest_run


def longestRunUnique(lo, hi):
    """ longestRunUnique: compute longest run of unique digit years in the sequence
                          [lo, hi] inclusive
        >>> longestRunUnique(1, 15)
        10
    """ 
    return longestRun(lo, hi, hasUniqueDigits)


def longestRunRepeated(lo, hi):
    """ longestRunRepated: compute longest run of repeated digit years in the sequence
                           [lo, hi] inclusive
        >>> longestRunRepeated(2000, 2015)
        13
    """
    return longestRun(lo, hi, lambda x: not hasUniqueDigits(x))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
