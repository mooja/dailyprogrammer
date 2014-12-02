#!/usr/bin/env python
# encoding: utf-8

import string
import unittest2 as unittest
import re


translation_table = string.maketrans('01ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                                     '0122233344455566677778889999')

def phone_literal_to_number(literal):
    if literal in string.digits or literal in string.ascii_letters:
        return string.translate(literal, translation_table)
    return literal


def phone_number_to_alphanumber(number_string):
    try:
        m = re.match(r'\d-\d{3}-([A-Z0-9]{3}[A-Z0-9]{4})', number_string)
        if not m:
            raise ValueError
    except:
        print "Ooops, the phone number format is unrecognized"
        import pudb; pudb.set_trace()
        raise ValueError

    last_five_digits = m.group(1)
    result = ''.join([phone_literal_to_number(x) for x in number_string])
    return result


class TestPhoneLiteralToNumber(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_numbers(self):
        phone_number = '1-111-1110000'
        expected_result = '1-111-1110000'
        self.assertEqual(phone_number_to_alphanumber(phone_number), expected_result)

    def test_number(self):
        phone_number = '1-800-COMCAST'
        expected_result = '1-800-2662278'
        self.assertEquals(phone_number_to_alphanumber(phone_number), expected_result)


if __name__ == '__main__':
    unittest.main()
