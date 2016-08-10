#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 273 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/4qg2eo/20160629_challenge_273_intermediate_twist_up_a/
#
# 10 August 2016

import requests
import fileinput

from random import choice
from bs4 import BeautifulSoup as BS


DATA_URL = 'http://pinyin.info/unicode/diacritics.html'


def dl_diatritics():
    r = requests.get(DATA_URL)
    if not r.status_code == 200:
        raise Exception('Could not download diatritics data')

    soup = BS(r.text, 'lxml')
    tags = [t for t in soup.find_all('tr')[2:-10]]

    def parse_symbol(tag):
        for i, child in enumerate(tag.children):
            if i == 3:
                symbol = child.contents[0]
                return symbol

    partitions = []
    for tag in tags:
        symbol = parse_symbol(tag)
        if 'class' in tag.attrs:
            partitions.append([symbol])
        else:
            partitions[-1].append(symbol)

    m = {p[0]: p[1:] for p in partitions}
    return m


def encode(mapping, text):
    cipher_chars = []
    for ch in text:
        if ch in mapping and mapping[ch]:
            cipher_chars.append(choice(mapping[ch]))
        else:
            cipher_chars.append(ch)
    return ''.join(cipher_chars)


if __name__ == "__main__":
    diatritics_map = dl_diatritics()
    for line in fileinput.input():
        print(encode(diatritics_map, line), end='')
