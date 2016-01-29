#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 166 Easy
#
# url
#
# January.29.2016


import math

G = 6.67e-17


def planetary_mass(radius, density):
    total_volume = radius**3 * (4.0 / 3.0) * math.pi
    return total_volume * density


def grav_force(mass_a, mass_b, distance):
    return (G * mass_a * mass_b) / distance**2


def main():
    mercury = {'radius': 2439700, 
               'density': 5427}
    mass = planetary_mass(mercury['radius'], mercury['density'])
    weight = grav_force(mass, 100, mercury['radius'])
    print('RADIUS: {}, DENSITY: {}, MASS: {}, WEIGHT: {}'.format(
        mercury['radius'],
        mercury['density'],
        mass,
        weight
    ))


if __name__ == "__main__":
    main()
