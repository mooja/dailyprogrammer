#!/usr/bin/env python
# encoding: utf-8

import unittest


def fizzbuzz(n):
    a, b, c = 0, 0, 0

    for i in xrange(1, n):
        if i % 3 == 0 and i % 5 == 0:
            c += 1
        elif i % 3 == 0:
            a += 1
        elif i % 5 == 0:
            b += 1

    return [a, b, c]


class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz1(self):
        self.assertEqual((fizzbuzz(20)), [5,2,1])

    def test_fizzbuzz2(self):
        self.assertEqual((fizzbuzz(2)), [0,0,0])

    def test_fizzbuzz3(self):
        self.assertEqual((fizzbuzz(30)), [8,4,1])

    def test_fizzbuzz4(self):
        self.assertEqual((fizzbuzz(300)), [80,40,19])


if __name__ == '__main__':
    unittest.main()
