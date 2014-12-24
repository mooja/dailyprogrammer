#!/usr/bin/env python
# encoding: utf-8

from kata_goodvsevil import *


def test_goodVsEvil():
    assert goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1') == 'Battle Result: Evil eradicates all trace of Good'
    assert goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0') == 'Battle Result: Good triumphs over Evil'
    assert goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0') == 'Battle Result: No victor on this battle field'
