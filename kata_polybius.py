#!/usr/bin/env python
# encoding: utf-8

import unittest
from string import ascii_uppercase


def polybius(text):
    cypher_map = dict()
    cypher_map['J'] = '24'
    for m, n in enumerate(ascii_uppercase[:9]+ascii_uppercase[10:]):
        d = (m / 5) + 1
        r = (m % 5) + 1
        cypher_map[n] = str(d) + str(r)

    cyphered_sequence = []
    for letter in text:
        if letter in ascii_uppercase:
            cyphered_sequence.append(cypher_map[letter])
        else:
            cyphered_sequence.append(letter)

    return ''.join(cyphered_sequence)


class TestPolybius(unittest.TestCase):

    def test_a(self):
        self.assertEqual(polybius('A'), "11")

    def test_long_string_spaces(self):
        self.assertEqual(polybius('POLYBIUS SQUARE CIPHER'),
                         "3534315412244543 434145114215 132435231542")

    def test_short_string(self):
        self.assertEqual(polybius('IJ'), "2424")

    def test_codwars(self):
        self.assertEqual(polybius('CODEWARS'), "1334141552114243")


if __name__ == '__main__':
    unittest.main()
