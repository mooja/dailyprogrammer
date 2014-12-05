#!/usr/bin/env python
# encoding: utf-8

import re
import unittest2 as unittest
import string
import operator


ROMAN_NUMERAL_RE = re.compile(r'[A-Z\' ]*[IXV]+\..*')
ALPHANUMERIC_RE = re.compile(r'\w')


def starts_with_roman_numeral(line):
    if re.match(ROMAN_NUMERAL_RE, line):
        return True
    return False

def count_alphanumeric(line):
    counter = 0
    for c in line:
        if re.match(ALPHANUMERIC_RE, c):
            counter += 1
    return counter


def count_characters(filename):

    with open(filename, 'r') as book:
        # remove footer and heater
        lines = book.readlines()
        lines = iter(lines[61:12690])

        # remove lines starting with roman numerals
        counts = (count_alphanumeric(line) for line in lines
                    if not starts_with_roman_numeral(line))

        total_count = reduce(lambda x,y: x+y, counts)

    return total_count


class TestStartsWithRomanNumeral(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_title_string(self):
        test_string = " IX. AN AWESOME TITLE."
        result = starts_with_roman_numeral(test_string)
        self.assertTrue(result)

    def test_bad_string(self):
        test_string = "this string shall not pass!"
        result = starts_with_roman_numeral(test_string)
        self.assertFalse(result)


if __name__ == '__main__':
    alphanumeric_character_count = count_characters("pg1661.txt")
    print("{} Total alphanumeric characters in the book.".format(
        alphanumeric_character_count))
