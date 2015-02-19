#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 80 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/x0v3e/7232012_challenge_80_easy_anagrams/
#
# Write a program that given a word will find all one-word anagrams for that
# word. So, for instance, if you put in "LEPROUS", it should return
# "PELORUS" and "SPORULE". As a dictionary, use this file, which is a 1.8 mb
# text-file with one word listed on each line, each word listed in
# lower-case. In this problem description, I've used upper-case for all
# words and their anagrams, but that is entirely optional, it's perfectly
# all right to use lower-case if you want to.
# Using your program, find all the one-word anagrams for "TRIANGLE".
#
# February.18.2015

from collections import Counter


def is_anagram(w1, w2):
    counter1, counter2 = Counter(w1.upper()), Counter(w2.upper())
    return counter1.most_common() == counter2.most_common()


def anagrams(word):
    word = word.upper()
    with open("enable1.txt") as f:
        dictwords = (word_.upper()
                     for line in f
                     for word_ in line.strip().split())
        anagrams = (dword
                    for dword in dictwords
                    if len(dword) == len(word)
                       and dword != word
                       and is_anagram(word, dword))

        return list(anagrams)
