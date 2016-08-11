#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 272 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/4paxp4/20160622_challenge_272_intermediate_dither_that/
#
# 11 August 2016


import argparse

from PIL import Image
from itertools import product
from collections import defaultdict


def simple_error_diffuse(image):
    width, height = image.size
    px = image.load()
    error = 0
    for y, x in product(range(height), range(width)):
        greyscale_color = sum(px[x, y]) / 3
        avg_color = greyscale_color + error
        if avg_color < 128:
            px[x, y] = (0, 0, 0)
            error += greyscale_color
        else:
            px[x, y] = (255, 255, 255)
            error -= (255-greyscale_color)


def floyd_steinberg_diffuse(image):
    width, height = image.size
    px = image.load()

    spread_map = defaultdict(lambda: 0)
    for y, x in product(range(height), range(width)):
        greyscale_color = sum(px[x, y]) / 3
        avg_color = greyscale_color + int(spread_map[(x, y)])
        if avg_color < 128:
            px[x, y] = (0, 0, 0)
            spread_map[(x+1, y)] += 7*(greyscale_color / 16)
            spread_map[(x, y+1)] += 5*(greyscale_color / 16)
            spread_map[(x-1, y+1)] += 3*(greyscale_color / 16)
            spread_map[(x+1, y+1)] += 1*(greyscale_color / 16)
        else:
            px[x, y] = (255, 255, 255)
            spread_map[(x+1, y)]   -= 255 - (7*(greyscale_color / 16))
            spread_map[(x,   y+1)]   -= 255 - (5*(greyscale_color / 16))
            spread_map[(x-1, y+1)] -= 255 - (3*(greyscale_color / 16))
            spread_map[(x+1, y+1)] -= 255 - (1*(greyscale_color / 16))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('IMAGE', type=argparse.FileType('rb'))
    args = parser.parse_args()
    image = Image.open(args.IMAGE)
    simple_error_diffuse(image)
    image.show()

if __name__ == "__main__":
    main()
