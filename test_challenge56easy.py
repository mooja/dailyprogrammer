#!/usr/bin/env python
# encoding: utf-8

#######################################################################
#                          challenge 55 easy tests                    #
#######################################################################

import pytest

from cStringIO import StringIO
from challenge56easy import add_letter
from challenge56easy import write_seq
from challenge56easy import file_window_iter

# fixtures

@pytest.fixture
def fh_empty():
    file_handle = StringIO()
    return file_handle

@pytest.fixture
def fh_a():
    file_handle = StringIO()
    file_handle.write('a')
    file_handle.seek(0)
    return file_handle

@pytest.fixture
def fh_aba():
    file_handle = StringIO()
    file_handle.write('aba')
    file_handle.seek(0)
    return file_handle

@pytest.fixture
def fh_abac():
    file_handle = StringIO()
    file_handle.write('abacaba')
    file_handle.seek(0)
    return file_handle


# tests

def test_add_letter(fh_empty):
    assert add_letter(fh_empty, 'a').read() == 'a'

def test_add_letter_to_a(fh_a):
    assert add_letter(fh_a, 'b').read() == 'aba'

def test_write_seq_b(fh_empty):
    assert write_seq(fh_empty, 'b').read() == 'aba'

def test_write_seq_c(fh_empty):
    assert write_seq(fh_empty, 'c').read() == 'abacaba'


def test_file_window_iter(fh_aba):
    file_contents = ''.join(c for c in file_window_iter(fh_aba, endpos=3, buffsize=2))
    assert file_contents == 'aba'

def test_file_window_iter2(fh_abac):
    file_contents = ''.join(c for c in file_window_iter(fh_abac, endpos=7, buffsize=6))
    assert file_contents == 'abacaba'
