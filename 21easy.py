#!/usr/bin/env python
# encoding: utf-8

import unittest

from itertools import permutations


def next_perm(number_string):
    perms_set = set([''.join(perm) for perm in permutations(number_string)])
    perms_sorted = sorted(list(perms_set))

    if(perms_sorted[-1] == number_string):
        return number_string
    return perms_sorted[perms_sorted.index(number_string)+1]


class TestNextPerm(unittest.TestCase):

    def test_one_digit(self):
        self.assertEqual(next_perm("5"), "5")

    def test_normal(self):
        self.assertEqual(next_perm("123"), "132")
        self.assertEqual(next_perm("1234"), "1243")
        self.assertEqual(next_perm("01234"), "01243")


if __name__ == '__main__':
    unittest.main()
