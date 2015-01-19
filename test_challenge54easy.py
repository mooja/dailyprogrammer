#!/usr/bin/env python
# encoding: utf-8

import pytest

from challenge54easy import matrix_cypher_encode
from challenge54easy import matrix_cypher_decode


def test_matrix_cypher_encode():
    assert matrix_cypher_encode(3, 'The cake is a lie!') == "T kiaihces eea  l!"


def test_matrix_cypher_decode():
    assert matrix_cypher_decode(3, "T kiaihces eea  l!") == "The cake is a lie!"


@pytest.mark.xfail
def test_encode_to_decode():
    text = 'Welcome to the world of real!'
    assert matrix_cypher_decode(5, matrix_cypher_encode(5, text)) == text
