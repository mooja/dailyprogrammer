#!/usr/bin/env python
# encoding: utf-8

# challenge 63 easy
# http://www.reddit.com/r/dailyprogrammer/comments/uw14f/6112012_challenge_63_easy/


def reverse_subseq(n_elems, seq):
    seq[:n_elems] = seq[n_elems-1::-1]
    return seq
