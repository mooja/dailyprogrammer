#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 90 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/ynw53/8222012_challenge_90_easy_walkaround_rasterizer/
#
# March.03.2015

LEGEND = {True: '#', False: ' '}


def rasterize(width, height, cmds):
    image = [[LEGEND[False] for _ in xrange(width)]
             for __ in xrange(height)]
    x, y = 0, 0
    for cmd in cmds.upper():
        if cmd == 'N':
            y -= 1
        elif cmd == 'S':
            y += 1
        elif cmd == 'E':
            x += 1
        elif cmd == 'W':
            x -= 1
        elif cmd == 'P':
            image[x][y] = LEGEND[True]

    output = '\n'.join(''.join(row) for row in image)
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(rasterize(5, 5, 'PESPESPESPESPNNNNPWSPWSPWSPWSP'))
