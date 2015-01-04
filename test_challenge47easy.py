#!/usr/bin/env python
# encoding: utf-8

from challenge47easy import ceasar_cypher


def test_ceasar_cyper():
    assert ceasar_cypher(1, 'A') == 'B'
    assert ceasar_cypher(1, 'Z') == 'A'
    assert ceasar_cypher(1, 'aaazzz') == 'bbbaaa'
