#!/usr/bin/env python
# encoding: utf-8

import unittest2 as unittest


def append_unique(list_a, list_b):
    result = [x for x in list_a]
    for i in list_b:
        if i not in list_a:
            result.append(i)
    return result


class TestAppendUnique(unittest.TestCase):

    def test_append_unique(self):
        a, b = ['a', 'b', 'c', 1, 4], ['a', "x", 'b', 34, '4']
        expected_result = ["a", "b", 'c', 1, 4, "x", 34, '4']
        self.assertEqual(append_unique(a, b), expected_result)


if __name__ == '__main__':
    unittest.main()
