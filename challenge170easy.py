#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Daily Programmer Challenge 170 Easy
#
# https://www.reddit.com/r/dailyprogrammer/comments/29zut0/772014_challenge_170_easy_blackjack_checker/
#
# February.01.2016


def parse_card_val(card_text):
    """
    >>> parse_card_val('1')
    1
    >>> parse_card_val('ace')
    11
    """
    if 'ace' in card_text.lower():
        return 11
    return int(card_text.strip())


def parse_record(text):
    """
    >>> parse_record('nick bostrom: 1, ace, 5')
    ['nick bostrom', 1, 11, 5]
    """
    player_name, cards_texts = text.split(':')
    card_values = map(parse_card_val, cards_texts.split(','))
    return [player_name] + card_values


def main():
    nplayers = int(raw_input())
    totals = {}
    for i in range(nplayers):
        record = parse_record(raw_input().strip())
        totals[record[0]] = sum(record[1:])

    closest_to_21 = max(filter(lambda x: x <= 21, totals.values()))
    winners = [name for name, score in totals.iteritems()
                        if score == closest_to_21]
    print('{} have won!'.format(' ,'.join(winners)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
