#!/usr/bin/env python
# encoding: utf-8

from challenge46easy import population_count


def test_population_count():
    assert population_count(0) == 0
    assert population_count(1) == 1
    assert population_count(2) == 1
    assert population_count(23) == 4
