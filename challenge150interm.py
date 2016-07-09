#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 150 Intermediate
#
# https://www.reddit.com/r/dailyprogrammer/comments/1yzlde/022614_challenge_150_intermediate_reemvoweler_1/
#
# September.09.2015

from random import shuffle
from itertools import permutations


def find_anagram(target, word_list):
    sorted_target = sorted(target)
    for w in word_list:
        if len(sorted_target) != len(w):
            continue
        if sorted_target == sorted(w):
            return w
    return None


def re_emvowel(vowels, non_vowels):
    letters = list(vowels + non_vowels)

    with open('enable1.txt', 'r') as f:
        words_dict = [w.strip() for w in f]
    output_words = []

    while letters:
        for i in range(1, len(letters)):
            for word_candidate in permutations(letters, i):
                anagram = find_anagram(''.join(word_candidate), words_dict)
                if anagram:
                    print 'Found word {}'.format(anagram)
                    output_words.append(anagram)
                    for letter in word_candidate:
                        letters.remove(letter)
                    break

    if letters:
        return None
    return ' '.join(output_words)


if __name__ == '__main__':
    print re_emvowel('wwllfndffthstrds', 'eieoeaeoi')
