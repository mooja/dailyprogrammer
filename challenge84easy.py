#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 84 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/xilfu/812012_challenge_84_easy_searching_text_adventure/
#
# February.21.2015

from math import sqrt


class Position(object):
    """Keeps tack of a position on a grid using x and y coordinate"""

    def __init__(self, x, y):
        """ initialize position

        :x: x coordinate
        :y: y coordinate

        """
        self.x = x
        self.y = y

    def __eq__(self, obj):
        """ checks whether positions refer to the same coordinates
        :obj: a Position object

        """
        return (self.x, self.y) == (obj.x, obj.y)

    def __ne__(self, obj):
        return not self.__eq__(obj)

    def move(self, direction):
        """ moves the point n, e, s, w

        :direction: string of set ('n', 'e', 's', 'w')
        :returns: None

        """
        if direction not in ('n', 'e', 's', 'w'):
            raise ValueError()
        if direction is 'n':
            self.y += 1
        if direction is 'e':
            self.x += 1
        if direction is 's':
            self.y -= 1
        if direction is 'w':
            self.x -= 1

    def distance_to(self, pos):
        """calculaes and returns distance to position pos

        :pos: TODO
        :returns: TODO

        """
        distance = sqrt((pos.x - self.x)**2 + (pos.y - self.y)**2)
        return distance


def main(player_pos=None, quest_pos=None):
    if player_pos is None:
        player_pos = Position(0, 0)
    if quest_pos is None:
        quest_pos = Position(5, 3)

    while player_pos != quest_pos:
        distance = player_pos.distance_to(quest_pos)
        print("Your compass displays '{distance:.2f}'".format(distance=distance))
        direction = ''
        while direction not in ('n', 'e', 's', 'w'):
            direction = raw_input('Enter the direction your want to move (n, e, s, w): ')
        player_pos.move(direction)

    print("You've found the quest!")


if __name__ == '__main__':
    main()
