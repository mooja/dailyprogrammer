#!/usr/bin/env python
# encoding: utf-8

import unittest

from functools import partial


def find_primes(lower_limit, upper_limit):
    """ Find all primes between lower_limit and upper_limit

    :lower_limit: lower limit (inclusive)
    :upper_limit: upper limit (inclusive)
    :returns: a list of prime numbers between lower_limit and upper limit

    """
    if lower_limit <= 0 or upper_limit <= 0:
        raise ValueError
    if lower_limit > upper_limit:
        raise ValueError

    number_list = range(2, upper_limit+1)

    # generate prime numbers up to the upper_limit
    def not_divisible(divisor, n):
        return n % divisor != 0

    index = 0
    while(index+1 < len(number_list)):
        not_divisible_by_n = partial(not_divisible, number_list[index])
        number_list[index+1:] = filter(not_divisible_by_n, number_list[index+1:])
        index += 1

    # filter out numbers not included in given range
    def within_range(lower, upper, n):
        return lower <= n <= upper

    number_list = filter(
        partial(within_range, lower_limit, upper_limit),
        number_list)

    return number_list


class TestFindPrimes(unittest.TestCase):

    """ Test find_primes"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_primes_below_ten(self):
        lower_limit, upper_limit = 2, 10
        expected_result = [2, 3, 5, 7]
        self.assertEqual(find_primes(lower_limit, upper_limit), expected_result)

    def test_one(self):
        lower_limit, upper_limit = 1, 1
        expected_result = []
        self.assertEqual(find_primes(lower_limit, upper_limit), expected_result)

    def test_single_prime(self):
        lower_limit, upper_limit = 2, 2
        expected_result = [2,]
        self.assertEqual(find_primes(lower_limit, upper_limit), expected_result)

    def test_primes_bad_arguments(self):
        self.assertRaises(ValueError, find_primes, -1, 1)
        self.assertRaises(ValueError, find_primes, 1, -1)


if __name__ == '__main__':
    unittest.main()
