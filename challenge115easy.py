#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 115 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/15ul7q/122013_challenge_115_easy_guessthatnumber_game/
#
# May.19.2015


from random import randrange


def asknum():
    while True:
        try:
            num = raw_input('Please enter your guess: ')
            num = int(num.strip())
            assert num < 101
            assert num > 0
            break
        except:
            print "Your guess must be a number between 1 and 100"

    return num


def main():
    rand_num = randrange(1, 101)
    guess_num = -1

    print "I'm thinking of a number between 1 and 100. Guess what it is!"
    print

    while rand_num != guess_num:
        guess_num = asknum()
        if guess_num > rand_num:
            print 'The number I\'m thinking of is less than {}'.format(guess_num)
        elif guess_num < rand_num:
            print 'The number I\'m thinking of is greater than than {}'.format(
                guess_num)

    print 'Number {} is correct!'.format(guess_num)


if __name__ == '__main__':
    main()
