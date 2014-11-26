#!/usr/bin/env python
# encoding: utf-8


def draw_triangle(height):
    output = ''
    for i in range(height):
        output += ('@' * (2**i)) + '\n'
    return output


print(draw_triangle(0))
print('\n')

print(draw_triangle(1))
print('\n')

print(draw_triangle(5))
print('\n')
