#!/usr/bin/env python
# encoding: utf-8

import os


def mkdirp(*dirs):
    path = ''

    for dname in dirs:
        path = os.path.join(path, dname)

        if not os.path.exists(path):
            os.mkdir(path, 0755)
