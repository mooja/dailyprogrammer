#!/usr/bin/env python
# encoding: utf-8

import pytest

from challenge49easy import main


def test_main():
    num_change_choice_wins, num_keep_choice_wins = main(1000)
    assert 600 <= num_change_choice_wins <= 700
    assert 300 <= num_keep_choice_wins <= 400
