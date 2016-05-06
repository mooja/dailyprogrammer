#!/usr/bin/env python
# encoding: utf-8



# Daily Programmer Challenge 198 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2syz7y/20150119_challenge_198_easy_words_with_enemies/
#
# 06.May.2016

from collections import Counter


def collide_words(w1, w2):
    """
    >>> collide_words('hat', 'cat')
    0
    >>> collide_words('because', 'cause')
    2
    >>> collide_words('hello', 'bellow')
    -1
    """
    left_counter = Counter(w1)
    left_counter.subtract(Counter(w2))
    left_total = sum(n for n in left_counter.values())
    return left_total


def main():
    import doctest
    doctest.testmod()

    inp_str = """
    because cause
    hello below
    hit miss
    rekt pwn
    combo jumbo
    critical optical
    isoenzyme apoenzyme
    tribesman brainstem
    blames nimble
    yakuza wizard
    longbow blowup
    """
    lines = inp_str.strip().split('\n')

    for line in lines:
        w1, w2 = line.strip().split()
        result = collide_words(w1, w2)
        print('{:<10} --> <-- {:>10}: '.format(w1, w2), end='')
        if result == 0:
            print('Tie.')
        elif result > 0:
            print('Left side won.')
        else:
            print('Right side won.')



if __name__ == '__main__':
    main()
