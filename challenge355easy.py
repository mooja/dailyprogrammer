#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Daily Programmer Challenge 355 Easy
#
# https://np.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/
#
# 02 April 2018


from itertools import cycle
from string import ascii_lowercase


def shifted(n, alphabet):
    """
    >>> shifted(2, 'abcde')
    'cdeab'
    """
    return alphabet[n:] + alphabet[:n]


def encrypt_char(key, char):
    """
    >>> encrypt_char('s', 't')
    'l'
    """
    shift_by = ascii_lowercase.find(key)
    shifted_alphabet = shifted(shift_by, ascii_lowercase)
    char_idx = ascii_lowercase.find(char)
    return shifted_alphabet[char_idx]


def encrypt_message(key, message):
    """
    >>> encrypt_message('snitch', 'thepackagehasbeendelivered')
    'lumicjcnoxjhkomxpkwyqogywq'
    """
    rv = ''
    for (key_ch, message_ch) in zip(cycle(key), message):
        rv += encrypt_char(key_ch, message_ch)
    return rv


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    assert 'uvrufrsryherugdxjsgozogpjralhvg' == encrypt_message('bond', 'theredfoxtrotsquietlyatmidnight')
