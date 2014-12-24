#!/usr/bin/env python
# encoding: utf-8


def goodVsEvil(good, evil):
    good_races_strength = [1, 2, 3, 3, 4, 10]
    evil_races_strength = [1, 2, 2, 2, 3, 5, 10]

    good_strength = sum(good_races_strength[int(army_type)] * int(number)
        for army_type, number in enumerate(good.split()))

    evil_strength = sum(evil_races_strength[int(army_type)] * int(number)
        for army_type, number in enumerate(evil.split()))

    if good_strength > evil_strength:
        return "Battle Result: Good triumphs over Evil"
    elif evil_strength > good_strength:
        return "Battle Result: Evil eradicates all trace of Good"
    return "Battle Result: No victor on this battle field"
