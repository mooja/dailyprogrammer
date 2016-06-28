#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 249 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/40h9pd/20160111_challenge_249_easy_playing_the_stock/
#
# 27 June 2016

from operator import attrgetter
from itertools import combinations
from collections import namedtuple


data1 = "19.35 19.30 18.88 18.93 18.95 19.03 19.00 18.97 18.97 18.98"
data2 = """
9.20 8.03 10.02 8.08 8.14 8.10 8.31 8.28 8.35 8.34 8.39 8.45 8.38 8.38 8.32
8.36 8.28 8.28 8.38 8.48 8.49 8.54 8.73 8.72 8.76 8.74 8.87 8.82 8.81 8.82 8.85
8.85 8.86 8.63 8.70 8.68 8.72 8.77 8.69 8.65 8.70 8.98 8.98 8.87 8.71 9.17 9.34
9.28 8.98 9.02 9.16 9.15 9.07 9.14 9.13 9.10 9.16 9.06 9.10 9.15 9.11 8.72 8.86
8.83 8.70 8.69 8.73 8.73 8.67 8.70 8.69 8.81 8.82 8.83 8.91 8.80 8.97 8.86 8.81
8.87 8.82 8.78 8.82 8.77 8.54 8.32 8.33 8.32 8.51 8.53 8.52 8.41 8.55 8.31 8.38
8.34 8.34 8.19 8.17 8.16
"""

def main(data):
    MarketPrice = namedtuple('Price', ['time', 'price'])

    chronological_prices = []
    for time, price in enumerate(map(float, data.split())):
        chronological_prices.append(MarketPrice(time, price))

    # trades are 2-tuples of prices in chronological order
    possible_trades = []
    for mp1, mp2 in combinations(chronological_prices, 2):
        # exclude trades within one tick
        within_one_tick = abs(mp1.time - mp2.time) == 1
        if within_one_tick:
            continue

        # make sure prices chronological order
        mp1, mp2 = sorted([mp1, mp2], key=attrgetter('time'))
        possible_trades.append((mp1, mp2))

    # sort possible trades by profit
    def profit(trade):
        return trade[1].price - trade[0].price
    possible_trades.sort(key=profit)

    best_trade = possible_trades[-1]
    print(best_trade[0].price, best_trade[1].price)

if __name__ == "__main__":
    main(data1)
    main(data2)
