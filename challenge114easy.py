#!/usr/bin/env python
# encoding: utf-8


# Daily Programmer Challenge 114 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/149kec/1242012_challenge_114_easy_word_ladder_steps/
#
# May.18.2015


from string import ascii_lowercase


def wordladder(word_list, word):
    found_words = []
    word_letters = list(word)
    for char_index, char in enumerate(word_letters):
        for alphabet_letter in ascii_lowercase:
            new_word_letters = list(word_letters)
            new_word_letters[char_index] = alphabet_letter
            new_word = ''.join(new_word_letters)
            if new_word != word and new_word in word_list:
                found_words.append(new_word)

    return sorted(found_words)


def bonus1(word_list):
    for word in word_list:
        if len(wordladder(word_list, word)) == 33:
            return word
    return False



if __name__ == '__main__':
    word_list = [word.strip() for word in open('four-letter-words.txt', 'r')]
    for word in wordladder(word_list, 'puma'):
        print word

    # bonus 1
    print 
    thirty_three_neighbors_word = bonus1(word_list) 
    if thirty_three_neighbors_word:
        print 'word "{}" has 33 neighbors"'.format(thirty_three_neighbors_word)
