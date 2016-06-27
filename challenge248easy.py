#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 248 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/3zfajl/20160104_challenge_248_easy_draw_me_like_one_of/
#
# 26 June 2016

import math


class Image(object):
    def __init__(self):
        self.grid = None

    @staticmethod
    def from_ppm(filename):
        img = Image()
        with open(filename, 'rt') as f:
            items = f.read().split()

        img.fmt = items[0]
        img.width = int(items[1])
        img.height = int(items[2])

        pixels = (tuple(map(int, items[i:i+3])) for i in range(3, len(items), 3)) 
        img.grid = []
        for row in range(img.height):
            column = []
            for col in range(img.width):
                column.append(next(pixels))
            img.grid.append(column)

        return img

    @staticmethod
    def from_instructions(text):
        data = text.strip()
        items = data.split()
        lines = data.split('\n')

        img = Image()
        img.fmt = 'P3'
        img.width = int(items[0])
        img.height = int(items[1])

        img.grid = []
        for row in range(img.height):
            column = []
            for col in range(img.width):
                column.append((0, 0, 0))
            img.grid.append(column)

        for line in lines[1:]:
            columns = line.split()
            instruction = columns[0]
            color = tuple(map(int, columns[1:4]))
            coords = list(map(int, columns[4:]))

            if instruction == 'point':
                img.point(color, *coords)
            if instruction == 'line':
                img.line(color, *coords)
            if instruction == 'rect':
                img.rect(color, *coords)

        return img

    def point(self, color, row, col):
        self.grid[row][col] = color

    def line(self, color, r1, c1, r2, c2):
        dx = 1
        try:
            dy = (r2 - r1) / (c2 - c1)
        except ZeroDivisionError:
            dx = 0
            dy = 1 if r2 > r1 else -1

        while int(r1) <= r2 and int(c1) <= c2:
            self.point(color, int(r1), int(c1))
            r1 += dy
            c1 += dx

    def rect(self, color, r1, c1, height, width):
        top_left = (r1, c1)
        bot_right = (r1+height-1, c1+width-1)

        self.line(color, r1, c1, r1, c1+width-1)
        self.line(color, r1, c1, r1+height-1, c1)
        self.line(color, r1+height-1, c1, r1+height-1, c1+width-1)
        self.line(color, r1, c1+width-1, r1+height-1, c1+width-1)

    def pprint(self):
        print(self.fmt)
        print(self.width, self.height)
        print(225)

        color_fmt = '{0:<3} {1:<3} {2:<3}'
        for row in range(self.height):
            line = '  '.join(color_fmt.format(*color) for color in self.grid[row])
            print(line)

if __name__ == "__main__":
    instructions = """
    400 300
    rect 0 0 255 0 0 300 400
    line 255 255 255 0 0 299 399
    line 255 255 255 299 0 0 399
    rect 200 200 0 100 150 100 100
    point 0 0 0 150 200
    """

    img = Image.from_instructions(instructions)
    img.pprint()
