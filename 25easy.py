#!/usr/bin/env python
# encoding: utf-8


import unittest

from collections import Counter


def get_winner(vote_list):
    if not vote_list:
        return None
    if len(vote_list) == 1:
        return vote_list[0]

    total_votes = len(vote_list)
    counts = Counter(vote_list)
    if counts.most_common()[0][1] == counts.most_common()[1][1]:
        return None
    if counts.most_common()[0][1] / float(total_votes) < 0.5:
        return None

    return counts.most_common()[0][0]


class TestGetWinner(unittest.TestCase):

    """Test case docstring."""

    def test_get_winner_one_vote(self):
        vote_list = ['eric']
        expected_result = 'eric'
        self.assertEqual(get_winner(vote_list), expected_result)

    def test_get_winner_tie(self):
        vote_list = ['eric', 'paul']
        expected_result = None
        self.assertEqual(get_winner(vote_list), expected_result)

    def test_get_winner_big_tie(self):
        vote_list = ['eric', 'eric', 'eric', 
                     'paul', 'paul', 'paul', 
                     'alice', 'alice', 'alice']
        expected_result = None
        self.assertEqual(get_winner(vote_list), expected_result)

    def test_get_winner_eric(self):
        vote_list = ['eric'] * 6 +\
                    ['paul'] * 2 +\
                    ['alice'] * 2
        expected_result = 'eric'
        self.assertEqual(get_winner(vote_list), expected_result)

    def test_get_winner_no_votes(self):
        vote_list = []
        expected_result = None
        self.assertEqual(get_winner(vote_list), expected_result)

if __name__ == '__main__':
    unittest.main()
