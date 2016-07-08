#!/usr/bin/env python
# encoding: utf-8

from challenge49easy import main


def test_main():
    num_change_choice_wins, num_keep_choice_wins = main(1000)
    assert 550 <= num_change_choice_wins <= 750
    assert 250 <= num_keep_choice_wins <= 450
