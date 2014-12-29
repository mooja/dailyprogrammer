#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#      simple functional test for the challenge 37 line counter       #
#######################################################################

import pytest
import os

from subprocess import check_output


def test_wc():
    f1 = open('/tmp/test_{}'.format(os.getpid()), 'w+t')
    f2 = open('/tmp/test_{}'.format(os.getpid()+1), 'w+t')
    f1.writelines(['line one\n', 'line two\n'])
    f1.close()
    f2.close()

    output = check_output(["python", "challenge37easy.py"] + [
        f.name for f in [f1, f2]])
    assert '2' in output.strip().split('\n')[-1]
