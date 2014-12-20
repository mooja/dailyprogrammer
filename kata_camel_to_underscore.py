#!/usr/bin/env python
# encoding: utf-8

import pytest
import re


def to_underscore(s):
    def camel2underscore(match):
        return match.group(1) + '_' + match.group(2).lower()
    s = str(s)
    s = re.sub(r'([a-z0-9])([A-Z])', camel2underscore, s)
    s = s.lower()
    return s


def test_to_underscore():
    assert to_underscore('CamelCase') == 'camel_case'
    assert to_underscore('normalword') == 'normalword'
    assert to_underscore('TestController') == 'test_controller'


if __name__ == '__main__':
    pytest.main(str(__file__))
