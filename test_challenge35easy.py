#!/usr/bin/env python
# encoding: utf-8

import pytest


from challenge35easy import *


def test_triange():
    expected_output = ('7 8 9 10\n'
                       '4 5 6\n'
                       '2 3\n'
                       '1')
    assert triange(10) == expected_output
