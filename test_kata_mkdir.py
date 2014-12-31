#!/usr/bin/env python
# encoding: utf-8

import os
import pytest

from kata_mkdir import *


def test_mkdirp():
    mkdirp('/tmp', 'kata', 'test')
    assert os.path.exists('/tmp/kata/test')
    assert os.path.isdir('/tmp/kata/test')
