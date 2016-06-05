#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import argparse
import requests


TARGET = "http://api.bitcoincharts.com/v1/trades.csv"
MARKETS = 'bitfinex bitstamp btce itbit anxhk hitbtc kraken bitkonan bitbay rock cbx cotr vcx'
CURRENCIES = 'KRW NMC IDR RON ARS AUD BGN BRL BTC CAD CHF CLP CNY CZK DKK EUR GAU GBP HKD HUF ILS INR JPY LTC MXN NOK NZD PEN PLN RUB SAR SEK SGD SLL THB UAH USD XRP ZAR'
               
if __name__ == "__main__":
    # parse arguments
    p = argparse.ArgumentParser()
    p.add_argument('-m', type=str, choices=MARKETS.split(), 
                   required=True, help='market name')
    p.add_argument('-c', type=str, choices=CURRENCIES.split(), 
                   default='USD', help='display currency')
    args = p.parse_args()


    # make request
    params = {'symbol': args.m + args.c}
    r = requests.get(TARGET, params=params)

    if r.status_code != 200:
        print("Bad request.")
        exit(1)

    timestamp, price, amount = r.text.split('\n')[0].split(',')
    bitcoin_price = float(price) / float(amount)
    print("{market} bitcoin brice: {price}".format(
        market=args.m, price=bitcoin_price))
