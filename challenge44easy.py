#!/usr/bin/env python
# encoding: utf-8

import re


def longest_sentence(text):
    sentences = re.findall(r'[A-Z][^!\.?]+[\.!?]', text, re.MULTILINE)
    if sentences:
        sentences = [re.sub(r'\s+', ' ', sentence).strip() for sentence in sentences]
        sentences.sort(cmp=lambda x,y: cmp(len(x), len(y)), reverse=True)
        return sentences[0]
    return None
