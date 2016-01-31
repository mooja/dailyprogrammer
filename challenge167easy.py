#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 167 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/289png/6162014_challenge_167_easy_html_markup_generator/ 
#
# January.30.2016

import os
import tempfile
import subprocess as sp


TEMPLATE = """
<!DOCTYPE html>
<html>
    <head>
        <title></title>
    </head>

    <body>
        <p>{}</p>
    </body>
</html>
"""

def mk_html_file(paragraph):
    html = TEMPLATE.format(paragraph)
    with open("temp.html", 'w') as f:
        f.write(html)
    return 'temp.html'


if __name__ == "__main__":
    p = raw_input("Enter a paragraph: ")
    fname = mk_html_file(p)
    sp.call(['firefox', fname])
