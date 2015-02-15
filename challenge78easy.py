#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 78 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/wrqbr/7182012_challenge_78_easy_keyboard_locale/
# 
# This one is inspired by an actual problem my friend had to deal with
# recently. Unfortunately, its a little bit keyboard-locale specific, so if
# you don't happen to use a us-EN layout keyboard you might want to get a
# picture of one.

# The en-us keyboard layout pictured here is one common layout for keys.
# There are character-generating keys such as '1' and 'q', as well as
# modifier keys like 'ctrl' and 'shift', and 'caps-lock'

# If one were to press every one of the character-generating keys in order
# from top to bottom left-to-right, you would get the following string:

# `1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./

# plus the whitespace characters TAB,RETURN,SPACE.

# Your job is to write a function that takes in a character representing
# a keypress, as well as a boolean for each 'modifier' key like
# ctrl,alt,shift,and caps lock, and converts it properly into the ascii
# character for which the key gets output.

# For example, my python implementation keytochar(key='a',caps=True)
# returns 'A'. However, keytochar(key='a',caps=True,shift=True) returns
# 'a'.

# BONUS: Read in a string containing a record of keypresses and output
# them to the correct string. A status key change is indicated by a ^
# character..if a ^ character is detected, then the next character is
# either an 's' or 'S' for shift pressed or shift released,
# respectively, a 'c' or 'C' for caps on or caps off respectively, and a
# 't' 'T' for control down or up, and 'a' 'A' for alt down or up.

# For example on the bonus, given the input

# ^sm^Sy e-mail address ^s9^Sto send the ^s444^S to^s0^S is
# ^cfake^s2^Sgmail.com^C

# you should output

# My e-mail address (to send the $$$ to) is FAKE@GMAIL.COM

# February.14.2015

from string import maketrans


SHIFT_TRANS = maketrans('`1234567890-=[]\\;\',./', '~!@#$%^&*()_+{}|:"<>?')

DEFAULT_MAPPING = '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./'
CAPS_MAPPING = maketrans(DEFAULT_MAPPING, DEFAULT_MAPPING.upper())
SHIFT_MAPPING = maketrans(DEFAULT_MAPPING,
                          DEFAULT_MAPPING.upper().translate(SHIFT_TRANS))
SHIFT_CAPS_MAPPING = maketrans(DEFAULT_MAPPING,
                               DEFAULT_MAPPING.translate(SHIFT_MAPPING).lower())


def key2char(key, caps=False, shift=False):

    if not caps and not shift:
        return key
    else:
        if caps and not shift:
            mapping = CAPS_MAPPING
        elif shift and not caps:
            mapping = SHIFT_MAPPING
        else:
            mapping = SHIFT_CAPS_MAPPING

        return key.translate(mapping)
