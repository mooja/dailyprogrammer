#!/usr/bin/env python


num_list = range(10)

def checksum(nlist, num):
    if len(nlist) < 2:
        return False

    x = nlist[0]
    for i in nlist[1:]:
        if x + i == num:
            return (x, y)

    return checksum(nlist[1:], num)
