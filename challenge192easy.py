#!/usr/bin/env python3
# encoding: utf-8


# Daily Programmer Challenge 192 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2onyoq/2014128_challenge_192_easy_carry_adding/
#
# 29.April.2016


def carries(nlist):
    maxmag = len(str(max(nlist)))
    carrydigits = [0]
    for i in range(1, maxmag+1):
        total = 0
        for n in nlist:
            total += n % (10**i)
        d = (total // (10**i)) % 10
        carrydigits.append(d)
    carrydigits.reverse()
    return ''.join(str(d) for d in carrydigits)


def show_addition(nlist):
    maxdigits = len(str(max(nlist)))+1
    fmt = '{{:>{}}}'.format(maxdigits)
    for n in nlist:
        print(fmt.format(n))
    print('-'*maxdigits)
    print(fmt.format(sum(nlist)))
    print('-'*maxdigits)
    print(carries(nlist).replace('0', ''))



if __name__ == '__main__':
    nlist = [12, 34, 56, 78, 90]
    nlist2 = [1, 999999]

    show_addition(nlist)
    print()
    show_addition(nlist2)
