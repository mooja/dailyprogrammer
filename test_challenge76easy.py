#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 76 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/wjzly/7132012_challenge_76_easy_title_case/
#
# Write a function that transforms a string into title case. This mostly
# means: capitalizing only every first letter of every word in the string.
# However, there are some non-obvious exceptions to title case which can't
# easily be hard-coded. Your function must accept, as a second argument, a
# set or list of words that should not be capitalized. Furthermore, the
# first word of every title should always have a capital leter.
#
# February.10.2015


import pytest

from challenge76easy import titlecase


@pytest.mark.parametrize("input, expected", [
    (('the quick brown fox jumps over the lazy dog', ['jumps', 'over', 'the']),
     'The Quick Brown Fox jumps over the Lazy Dog'),
])
def test_titlecase(input, expected):
    assert titlecase(*input) == expected
