#!/usr/bin/env python
# encoding: utf-8



# Daily Programmer Challenge 179 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2ftcb8/9082014_challenge_179_easy_you_make_me_happy_when/
#
# 16.April.2016

import os
import sys
import argparse

from PIL import Image
from itertools import product


def grayscale(r, g, b):
    lightness = max(r, g, b) + min(r, g, b)
    return (lightness, lightness, lightness)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='image file to grayscale')
    args = parser.parse_args()

    if not os.path.exists(args.filename):
        print("File {} doesn't exist.".format(args.filename))
        exit()

    with Image.open(args.filename) as img:
        width, height = img.size
        grayscaled_img = Image.new("RGB", img.size)

        for pixel_loc in product(range(width), range(height)):
            color = img.getpixel(pixel_loc)
            grayscaled = grayscale(*color)
            grayscaled_img.putpixel(pixel_loc, grayscaled)

        grayscaled_img.save(args.filename.replace('.jpg', "_grayscaled.jpg"))
