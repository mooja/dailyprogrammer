#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 193 Eas
#
# https://www.reddit.com/r/dailyprogrammer/comments/2peac9/20141215_challenge_193_easy_a_cube_ball_cylinder/
#
# 30.April.2016

import math


def cube_dimensions(vol):
    side = vol**(1/3)
    return 'cube: {:.2}m width {:.2}m height {:.2}m tall'.format(
        side, side, side
    )

def cylinder_dimensions(vol):
    height = 3.0
    r = math.sqrt(vol / (math.pi*height))
    return 'cylinder: {:.2}m tall, {:.2}m radius'.format(height, r)


def sphere_dimensions(vol):
    r = ((3.0*vol)/(4*math.pi))**(1.0/3.0)
    return 'sphere: {:.2}m radius'.format(r)

def cone_radius(vol):
    h = (vol*3.0*math.pi)**(1/3)
    r = h**2
    return 'cone: {:.2}m radius, {:.2}m height'.format(r, h)

def main():
    vol = float(input('enter radius: '))
    for f in [cube_dimensions, cylinder_dimensions, sphere_dimensions, cone_radius]:
        print(f(vol))

if __name__ == '__main__':
    main()
