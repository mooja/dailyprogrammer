#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 246 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/3xpgj8/20151221_challenge_246_easy_xmass_lights/
#
# 23 June 2016

BAT_CAPACITY = 1200
BAT_VOLTAGE = 9
LED_CURRENT = 20
LED_VOLTAGE = 1.7

def max_leds_per_time(hours):
    max_amps_per_hour = BAT_VOLTAGE / hours
    max_5_serial_leds = max_amps_per_hour / 20
    return int(max_5_serial_leds * 5)

def draw_5leds_parralel(n_parralel):
    for i in range(n_parralel):
        first = i == 0
        last = i == n_parralel - 1
        if first:
            yield '*--|>|---|>|---|>|---|>|---|>|--*'
        else:
            yield ' --|>|---|>|---|>|---|>|---|>|--'
        if not last:
            yield ' |                             |'

def calc_resitance(hours):
    amps_per_hour = BAT_CAPACITY / hours
    ohms = 0.5 / (amps_per_hour / 1000)
    return ohms

def part1():
    data = [1, 4, 8, 12, 20, 100]
    for item in data:
        print(max_leds_per_time(item))

def part2():
    data = [12, 6, 100]
    for item in data:
        n_leds = max_leds_per_time(item)
        for line in draw_5leds_parralel(n_leds // 5):
            print(line)
        print()

def part3():
    data = [1, 4, 8]
    for item in data:
        print(round(calc_resitance(item), 3))

part1()
part2()
part3()
