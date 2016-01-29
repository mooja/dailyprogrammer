#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 166 Easy
#
# url
#
# January.29.2016


import math

G = 6.67e-11


def planetary_mass(radius, density):
    total_volume = (4.0 / 3.0) * math.pi * radius**3
    total_mass = total_volume * density
    return total_mass


def grav_force(mass_a, mass_b, distance):
    return (G * mass_a * mass_b) / distance**2


def main():
    object_mass = 100
    mercury = {'radius': 3104500, 'density': 5009}
    mercury_mass = planetary_mass(mercury['radius'], mercury['density'])
    object_weight = grav_force(mercury_mass, object_mass, mercury['radius'])

    print('Object weight on the surface of mercury: {:5.2f} newtons'.format(object_weight))


if __name__ == "__main__":
    main()
