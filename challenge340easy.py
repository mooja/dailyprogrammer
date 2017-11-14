#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 340 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/7cnqtw/20171113_challenge_340_easy_first_recurring/
#
# 14 November 2017


def fist_reccuring(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return False
