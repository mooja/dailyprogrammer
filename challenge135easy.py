#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 135 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/1k7s7p/081313_challenge_135_easy_arithmetic_equations/
#
# June.10.2015


import random


def generate_equation_str(lo, hi):
    equation_fmt = 'n o n o n o n'

    equation = ''
    for char in equation_fmt:
        if char == 'n':
            equation += str(random.randrange(lo, hi+1))
        elif char == 'o':
            equation += random.choice('+-*')
        else:
            equation += char

    return equation


def main():
    try:
        lo, hi = raw_input('>').strip().split()
        lo, hi = int(lo), int(hi)
    except:
        return

    while True:
        try:
            equation = generate_equation_str(lo, hi)
            user_answer = raw_input('> ' + equation + '\n')

            if user_answer == 'q':
                return

            if int(user_answer) == eval(equation):
                print '> Correct!'
            else:
                print '> Incorrect!'
            print
        except:
            print 'could not parse input.'
            return


if __name__ == '__main__':
    main()
