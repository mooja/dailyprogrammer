#!/usr/bin/env python
# encoding: utf-8



import pytest

from challenge64easy import divisors
from challenge64easy import sum_divisors
from challenge64easy import are_coprime
from challenge64easy import totatives
from challenge64easy import n_totatives


@pytest.mark.parametrize("input, expected", [
    (10, (1, 2, 5, 10)),
    (7, (1, 7)),
])
def test_divisors(input, expected):
    assert divisors(input) == expected


@pytest.mark.parametrize("input, expected", [
    (10, 18),
    (7, 8),
])
def test_sum_divisors(input, expected):
    assert sum_divisors(input) == expected


@pytest.mark.parametrize("input, expected", [
    ((5, 7), True),
    ((2, 4), False),
])
def test_are_coprime(input, expected):
    assert are_coprime(*input) == expected


@pytest.mark.parametrize("input, expected", [
    (7, (2, 3, 4, 5, 6)),
])
def test_totatives(input, expected):
    assert totatives(input) == expected


@pytest.mark.parametrize("input, expected", [
    (7, 5),
])
def test_n_totatives(input, expected):
    assert n_totatives(input) == expected
