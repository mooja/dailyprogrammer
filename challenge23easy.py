#!/usr/bin/env python
# encoding: utf-8

import unittest


def split_in_half(lst):
    d = len(lst) // 2
    return lst[:d], lst[d:]


class TestSplitInHalf(unittest.TestCase):

    def test_split_in_half(self):
        input = [2, 3, 4, 6]
        output = [2, 3], [4, 6]
        self.assertEqual(split_in_half(input), output)


if __name__ == '__main__':
    unittest.main()
