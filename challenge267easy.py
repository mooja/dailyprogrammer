#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 267 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4jom3a/20160516_challenge_267_easy_all_the_places_your/
#
# 18 May 2016


def humanize_place(place):
    """
    >>> humanize_place(1)
    '1st'
    >>> humanize_place(2)
    '2nd'
    >>> humanize_place(11)
    '11th'
    >>> humanize_place(31)
    '31st'
    """
    if 11 <= place <= 13:
        suffix = 'th'
    else:
        r = place % 10
        if r == 1:
            suffix = 'st'
        elif r == 2:
            suffix = 'nd'
        elif r == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    return str(place) + suffix

def main():
    import doctest
    doctest.testmod()

    dog_place = int(input('What place was your dog?: '))
    other_places_iter = (
        humanize_place(p) 
        for p in range(1, 101) 
        if p != dog_place
    )
    print(' '.join(other_places_iter))


if __name__ == "__main__":
    main()
