#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 139 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1pwl73/11413_challenge_139_easy_pangrams/
#
# June.14.2015


from string import ascii_lowercase


def is_panagram(s):
    """
    >>> is_panagram('The quick brown fox jumps over the lazy dog.')
    True
    >>> is_panagram('Saxophones quickly blew over my jazzy hair')
    False
    """
    letters = filter(lambda x: x.isalpha(), s.lower())
    return set(letters) == set(ascii_lowercase)


def main():
    nlines = input()

    for _ in range(nlines):
        print str(is_panagram(raw_input()))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    main()
