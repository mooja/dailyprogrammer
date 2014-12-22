#!/usr/bin/env python
# encoding: utf-8


import re
import unittest


def seperate_duplicates(s):
    orig = re.sub(r'(\w)\1+', r'\1', s)
    dupl = ''.join(m.group(2) 
        for m in re.finditer(r'(\w)(\1+)', s))

    return orig, dupl


class TestSeperateDuplicates(unittest.TestCase):

    def test_dailyprogramer(self):
        input = "ddaaiillyypprrooggrraammeerr"
        expected_output = ("dailyprogramer", "dailyprogramer")
        self.assertEqual(seperate_duplicates(input), expected_output)

    def test_noduplicates(self):
        input = "no duplicates in this string"
        expected_output = ("no duplicates in this string", "")
        self.assertEqual(seperate_duplicates(input), expected_output)

    def test_flaby_apples(self):
        input = "aabbccddeded"
        expected_output = ("abcdeded", "abcd")
        self.assertEqual(seperate_duplicates(input), expected_output)


if __name__ == '__main__':
    unittest.main()
