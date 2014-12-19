#!/usr/bin/env python
# encoding: utf-8

# simple abbreviation program for a kata challenge from Codewars.comjhhlll

import unittest
import re


def abbreviate(s):
    def abbr_word(match):
        submatch = re.match(r'^(\w)(\w+)(\w)$', match.group(0))
        return re.sub(submatch.group(2),
                      str(len(submatch.group(2))),
                      match.group(0))

    return re.sub(r'\w{4,}', abbr_word, s)


class TestAbbreviate(unittest.TestCase):

    def test_empty_string(self):
        input = "  "
        expected_output = "  "
        self.assertEqual(abbreviate(input), expected_output)

    def test_short_string(self):
        input = "non to abb"
        expected_output = "non to abb"
        self.assertEqual(abbreviate(input), expected_output)
        pass

    def test_i18n(self):
        pass

    def test_a11n(self):
        pass


if __name__ == '__main__':
    unittest.main()
