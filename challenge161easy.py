#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 161 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/24r50l/552014_161_easy_blackjack/

#
# December.23.2015


import random


def build_deck():
    deck = []
    deck.extend([i for i in range(2, 11)])  # cards 2-10
    deck.extend([10, 10, 10])  # cards Jack Queen and King
    deck.append(11)  # ace
    deck = deck*4  # four suits
    return deck


def generate_shuffled_decks(n):
    cards = [c for d in range(n) for c in build_deck()]
    random.shuffle(cards)
    return cards


DECK = build_deck()

if __name__ == '__main__':
    cards = generate_shuffled_decks(10)
    total_hands = len(cards)
    nhands_blackjacks = 0
    while cards:
        card1, card2 = cards.pop(), cards.pop()
        if card1 + card2 == 21:
            nhands_blackjacks += 1

    print('Natural Blackjacks were {} out of {} hands, at {}%'.format(
        nhands_blackjacks,
        total_hands, 
        round((nhands_blackjacks / total_hands)*100, 2)
    ))
