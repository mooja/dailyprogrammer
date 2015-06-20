#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 144 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1sob1e/121113_challenge_144_easy_nuts_bolts/
#
# June.19.2015


def main():
    nlines = input()

    prices1 = {}
    for _ in xrange(nlines):
        item_name, price_str = raw_input().strip().split()
        prices1[item_name] = int(price_str)

    prices2 = {}
    for _ in xrange(nlines):
        item_name, price_str = raw_input().strip().split()
        prices2[item_name] = int(price_str)

    for item, price in sorted(prices2.iteritems()):
        if prices1[item] != prices2[item]:
            print '{} {}'.format(item, prices1[item] - prices2[item])


if __name__ == '__main__':
    main()
