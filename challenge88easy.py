#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 88 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/y5sox/8132012_challenge_88_easy_vigen%C3%A8re_cipher/
#
# February.26.2015
from itertools import izip


def encrypt(k, m):
    """encrypt(k, m): Encrypts message string m using key string k.
       Uses simple Vigenere Cipher, and repeats k string if m is longer than k
       >>> encrypt('GLADOS', 'THECAKEISALIE')
       'ZSEFOCKTSDZAK'
    """
    k, m = k.upper(), m.upper()

    # expand k
    k = k*(len(m)//len(k) + 1)
    k = k[:len(m)]

    # convert integers and add mod 26
    kords = (ord(x) - ord('A') for x in k)
    mords = (ord(x) - ord('A') for x in m)
    cords = (ord('A') + ((x + y) % 26)
             for x, y in izip(kords, mords))

    # convert back to string
    c = ''.join(chr(x) for x in cords)
    return c


def decrypt(k, c):
    """decrypt(c, m): Decrypts ciphertext string m using key string k.
       Uses simple Vigenere Cipher, and repeats k string if c is longer than k
       >>> decrypt('GLADOS', 'ZSEFOCKTSDZAK')
       'THECAKEISALIE'
    """
    # expand k
    k = k*(len(c)//len(k) + 1)
    k = k[:len(c)]

    # convert to ints and subtract mod 26
    kords = (ord(x) - ord('A') for x in k)
    cords = (ord(x) - ord('A') for x in c)
    mords = (ord('A') + ((y - x) % 26)
             for x, y in izip(kords, cords))

    m = ''.join(chr(x) for x in mords)
    return m


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    c = ('HSULAREFOTXNMYNJOUZWYILGPRYZQVBBZABLBWHMFGWFVPMYWAVVTYISCIZRLVGOPGBRAKLUGJUZGLN'
         'BASTUQAGAVDZIGZFFWVLZSAZRGPVXUCUZBYLRXZSAZRYIHMIMTOJBZFZDEYMFPMAGSMUGBHUVYTSABB'
         'AISKXVUCAQABLDETIFGICRVWEWHSWECBVJMQGPRIBYYMBSAPOFRIMOLBUXFIIMAGCEOFWOXHAKUZISY'
         'MAHUOKSWOVGBULIBPICYNBBXJXSIXRANNBTVGSNKR')
    print decrypt('BEGINNING', c)
