#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 293 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/5e4mde/20161121_challenge_293_easy_defusing_the_bomb/
#
# 30 November 2016


COLORS = set([
    'white',
    'black',
    'purple',
    'red',
    'green',
    'orange'
])

FSM = {
    'white': COLORS - set(['white', 'black']),
    'red': ['green'],
    'black': COLORS - set(['white', 'green', 'orange']),
    'orange': ['red', 'black'],
    'green': ['orange', 'white'],
    'purple': COLORS - set(['purple', 'green', 'orange', 'white'])
}


def defuses(instructions):
    current_color = instructions[0]
    for instr in instructions[1:]:
        if instr not in FSM[current_color]:
            return False
        current_color = instr
    return True


if __name__ == "__main__":
   input1 = 'white red green white'.split()
   input2 = 'white orange green white'.split()

   print(FSM)

   for inp in [input1, input2]:
       if defuses(inp):
           print('Bomb defused')
       else:
           print('Boom!')
