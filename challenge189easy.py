#!/usr/bin/env python3
# encoding: utf-8


# Daily Programmer Challenge 189 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/2mlfxp/20141117_challenge_189_easy_hangman/
#
# 27.April.2016

import random


word_list = ['one', 'two', 'three']


def replace_positions(word, char, positions):
    new_word = list(word)
    for pos in positions:
        new_word[pos] = char
    return ''.join(new_word)

def main():
    target_word = random.choice(word_list)
    covered_word = '#'*len(target_word)
    wrong_guesses_left = 6;

    while wrong_guesses_left > 0 and covered_word != target_word:
        print('Turns remaining: {:2>} {:15}'.format(wrong_guesses_left, covered_word))
        guess_char = input('Enter Guess: ').strip()

        if guess_char in target_word:
            print('{} is correct!'.format(guess_char))
            char_positions = [i for i, c in enumerate(target_word) if c == guess_char]
            covered_word = replace_positions(covered_word, guess_char, char_positions)
        else:
            print('{} is incorrect.'.format(guess_char))
            wrong_guesses_left-=1
        print()

    if wrong_guesses_left:
        print('Victory! The word was {}'.format(covered_word))
    else:
        print('Defeat. You\'ve run out of turns')


if __name__ == '__main__':
    main()
