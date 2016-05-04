#!/usr/bin/env python3
# encoding: utf-8


# Daily Programmer Challenge 196 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2rfae0/20150105_challenge_196_practical_exercise_ready/
#
# 04.May.2016


class Set(object):
    def __init__(self, l):
        self.items = []
        for item in l:
            self.items.append(item) if not item in self.items

    def contains(self, item):
        return item in self.items

    def union(self, setb):
        unionset = Set(self.items)
        for item in setb.items:
            unionset.items.append(item) if not item in unionset.items
        return unionset

    def intersection(self, setb):
        unionset = Set(self.items)
        for item in setb.items:
            unionset.items.append(item) if item in self.items;
        return unionset

    def equals(self, setb):
        return sorted(self.items) == sorted(setb.items)
