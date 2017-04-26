#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 311 Intermediate
#
#
#
# 26 April 2017

from functools import reduce
from itertools import permutations


def ip2binary(addr):
    octets = [int(octet) for octet in addr.split('.')]
    def add_octets(a, b):
        return a*256 + b
    sum_ = reduce(add_octets, octets)
    return bin(sum_)[2:].zfill(32)


def cidr_mask(addr):
    addr, mask = addr.split('/')
    mask = int(mask)
    addr = ip2binary(addr)
    binmask = addr[:mask] + ('*'*(len(addr) - mask))
    return binmask


def covers(addr1, addr2):
    mask1 = cidr_mask(addr1)
    mask2 = cidr_mask(addr2)
    for bit1, bit2 in zip(mask1, mask2):
        if bit1 != '*' and (bit1 != bit2):
            return False
    return True


def smallest_cover(addresses):
    rv = set(addresses)
    for addr, addr2 in permutations(addresses, r=2):
        if covers(addr2, addr):
            rv.discard(addr)
    return rv


if __name__ == "__main__":
    inputs = ["172.26.32.162/32", "172.26.32.0/24", "172.26.0.0/16"]
    inputs2 = """\
192.168.0.0/16
172.24.96.17/32
172.50.137.225/32
202.139.219.192/32
172.24.68.0/24
192.183.125.71/32
201.45.111.138/32
192.168.59.211/32
192.168.26.13/32
172.24.0.0/17
172.24.5.1/32
172.24.68.37/32
172.24.168.32/32\
"""
    inputs2 = inputs2.split('\n')
    print(smallest_cover(inputs))
    print(smallest_cover(inputs2))
