#!/usr/bin/env python
# encoding: utf-8


from string import maketrans, translate


querty_lowercase = """qwertyuiop[asdfghjkl;zxcvbnm,"""
querty_uppercase = """QWERTYUIOP{ASDFGHJKL:ZXCVBNM<"""
querty_map = querty_lowercase + querty_uppercase

wertyu_lowercase = """wertyuiop[]sdfghjkl;'xcvbnm,."""
wertyu_uppercase = """WERTYUIOP{}SDFGHJKL:"XCVBNM<>"""
wertyu_map = wertyu_lowercase + wertyu_uppercase

shift_left_trans = maketrans(wertyu_map, querty_map)


def shift_left(text):
    """
    >>> shift_left("Jr;;p ept;f")
    'Hello world'
    >>> shift_left("Lmiyj od ,u jrtp")
    'Knuth is my hero'
    """
    return translate(text, shift_left_trans)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
