#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 269 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/4lpygb/20160530_challenge_269_easy_basic_formatting/
#
# 18 July 2016

import re


data = """12
····
VAR I
·FOR I=1 TO 31
»»»»IF !(I MOD 3) THEN
··PRINT "FIZZ"
··»»ENDIF
»»»»····IF !(I MOD 5) THEN
»»»»··PRINT "BUZZ"
··»»»»»»ENDIF
»»»»IF (I MOD 3) && (I MOD 5) THEN
······PRINT "FIZZBUZZ"
··»»ENDIF
»»»»·NEXT"""


def indent(data):
    indentation_level = 0
    indentation_unit = data.split('\n')[1]

    source_lines = []
    for line in data.split('\n')[2:]:
        source_lines.append(re.sub(r'[·»]', '', line))

    for line in source_lines:
        statement = line.split()[0]
        if statement in ('NEXT', 'ENDIF'):
            indentation_level -= 1

        print(indentation_unit*indentation_level + line)

        if statement in ('FOR', 'IF'):
            indentation_level += 1

if __name__ == "__main__":
    indent(data)
