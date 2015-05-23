#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 119 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/17f3y2/012813_challenge_119_easy_change_calculator/
#
# May.23.2015


from functools import partial


USA_CURRENCY = ((25, 'Quarters'), (10, 'Dimes'), (5, 'Nickles'), (1, 'Cents'))


def change(currency, money):
    output = []
    units = int(round(float(money), 2) * 100)
    for qty, denomination in currency:
        output.append('{}: {}'.format(units // qty, denomination))
        units = units % qty

    return '\n'.join(output)


USA_change = partial(change, USA_CURRENCY)


if __name__ == '__main__':
    challenge_inputs = ('10.24', '0.99', '5', '00.06')
    for qty in challenge_inputs:
        print '{}:'.format(qty)
        print USA_change(qty)
        print
