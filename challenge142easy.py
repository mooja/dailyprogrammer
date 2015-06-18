#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 142 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1rdtky/111113_challenge_142_easy_falling_sand/
#
# June.17.2015


class Grid(object):

    def __init__(self, ascii_lines):
        self.objects = Grid.__ascii2objects(ascii_lines)
        self.height = len(ascii_lines)
        self.width = len(ascii_lines[0])

    def apply_gravity(self):
        self.objects.sort(key=lambda x: x[0], reverse=True)
        for obj_idx in range(len(self.objects)):
            obj = self.objects[obj_idx]
            if obj[2] == '.':
                obj_below = self.__obj_below_pos(obj[0], obj[1])
                if obj_below:
                    continue
                if obj[0]+1 >= self.height:
                    continue
                new_obj = (obj[0]+1, obj[1], obj[2])
                self.objects[obj_idx] = new_obj

    def display(self):
        lines = []
        for row in range(self.height):
            line = []
            for col in range(self.width):
                obj_at_pos = self.__obj_at_pos(row, col)
                if obj_at_pos:
                    line.append(obj_at_pos[2])
                else:
                    line.append(' ')
            lines.append(''.join(line))
        return '\n'.join(lines)

    @staticmethod
    def __ascii2objects(lines):
        objects = []
        for row_index, row in enumerate(lines):
            for col_index, ch in enumerate(row):
                if ch != ' ':
                    objects.append((row_index, col_index, ch))
        return objects

    def __obj_at_pos(self, row, col):
        if row > self.height or col > self.width:
            return None

        for obj in self.objects:
            if obj[0] == row and obj[1] == col:
                return obj

        return None

    def __obj_below_pos(self, row, col):
        return self.__obj_at_pos(row+1, col)


def main():
    gridsize = input()
    world = []
    for _ in range(gridsize):
        line = raw_input().rstrip()
        world.append(line)

    grid = Grid(world)

    last_display = grid.display()
    while True:
        grid.apply_gravity()
        new_display = grid.display()
        if new_display == last_display:
            break
        last_display = new_display

    print grid.display()

if __name__ == '__main__':
    main()
