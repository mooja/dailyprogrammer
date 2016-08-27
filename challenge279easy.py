#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 279 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4xy6i1/20160816_challenge_279_easy_uuencoding/
#
# 19 August 2016


def encode3bytes(bts):
    """
    >>> encode3bytes('Cat')
    '0V%T'
    """
    if type(bts) is str:
        bts = bts.encode('ascii')

    three_bytes_ascii = [bin(byte)[2:].zfill(8) for byte in bts]
    bits_ascii = ''.join(three_bytes_ascii)
    four_groups = [bits_ascii[:6], bits_ascii[6:12],
                   bits_ascii[12:18], bits_ascii[18:24]]
    four_groups = [int(group, 2) for group in four_groups]
    four_groups = [n+32 for n in four_groups]
    four_ascii = [chr(n) for n in four_groups]
    return ''.join(four_ascii)


def uuencode(data):
    if type(data) is str:
        data = data.encode('ascii')

    output = []
    for i in range(0, len(data), 3):
        bts = data[i:i+3]
        while len(bts) < 3:
            bts += (0).to_bytes(1, 'big')
        output.append(encode3bytes(bts))
    return ''.join(output)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    data = 'I feel very strongly about you doing duty. Would you give me a little more documentation about your reading in French? I am glad you are happy — but I never believe much in happiness. I never believe in misery either. Those are things you see on the stage or the screen or the printed pages, they never really happen to you in life.'
    data = data.encode('utf8')
    print(uuencode(data))
