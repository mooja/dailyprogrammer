#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 77 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/wn3ld/7162012_challenge_77_easy_enumerating_morse_code/

# Morse code, as we are all aware, consists of dots and dashes. Lets define
# a "Morse code sequence" as simply a series of dots and dashes (and nothing
# else). So ".--.-.--" would be a morse code sequence, for instance.
#
# Dashes obviously take longer to transmit, that's what makes them dashes.
# Lets say that a dot takes 1 unit of time to transmit, and a dash takes 2
# units of time. Then we can say that the "size" of a certain morse code
# sequence is the sum of the time it takes to transmit the dots and dashes.
#
# So, for instance "..-." would have a size of 5 (since there's three dots
# taking three units of time and one dash taking two units of time, for a
# total of 5). The sequence "-.-" would also have a size of 5.
#
# In fact, if you list all the the possible Morse code sequences of size 5,
# you get:
#
# .....  ...-  ..-.  .-..  -...  .--  -.-  --.
#
# Your task is to write a function called Morse(X) which generates all morse
# code sequences of size X and returns them as an array of strings (so
# Morse(5) should return the 8 strings I just mentioned, in some order).
# Use your function to generate and print out all sequences of size 10.
#
# February.12.2015

from itertools import permutations


def rotate(s):
    return '{}{}'.format(s[-1], s[:-1])


def morse(num):
    dots = '.' * num
    result = [dots]
    while '..' in result[-1]:
        i = result[-1].find('..')
        result.append('{}{}{}'.format(
            result[-1][:i],
            '-',
            result[-1][i+2:]))

        for k in range(len(result[-1]) - 1):
            result.append(rotate(result[-1]))

    return set(result)


def morseiter(num):
    combination = '.' * num
    yield combination

    while '..' in combination:
        i = combination.find('..')
        combination = '{}{}{}'.format(
            combination[:i], '-', combination[i+2:])

        if '..' not in combination:
            yield combination
            break

    return


def main(num=10):
    for comb in morseiter(num):
        print '{comb:>{width}}'.format(width=num, comb=comb)


if __name__ == '__main__':
    main(35)
