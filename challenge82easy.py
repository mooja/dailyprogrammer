#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 82 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/x8rl8/7272012_challenge_82_easy_substring_list/
# 
# Write a function that takes a number n as an argument and returns (or
# outputs) every possible unique substrings (not counting "") of the first n
# letters of the alphabet (in any order you like).
# 
# February.19.2015




from string import ascii_lowercase


def subs(n):
    output = [ascii_lowercase[i:j]
              for i in range(n+1)
              for j in range(i+1, n+1)]
    return sorted(output)


if __name__ == '__main__':
    print subs(5)
