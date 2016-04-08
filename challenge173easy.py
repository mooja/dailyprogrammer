#!/usr/bin/env python

# daily programmer #173

# url: https://www.reddit.com/r/dailyprogrammer/comments/2bxntq/7282014_challenge_173_easy_unit_calculator/


length_conversions = {
    'metres': 1.0,
    'inches': 39.37,
    'miles': .000621,
    'attoparsecs': float('3.086e-16')
}

weight_conversions = {
    'grams': 1.0,
    'kilograms': 1000,
    'pounds': 453.592,
    'ounces': 28.3495
}


def convert_unit(u1, val, u2):
    """converts from unit1 to uni2

    :from: @todo
    :two: @todo
    :returns: @todo

    >>> convert_unit('metres', 1.0, 'metres')
    '1.00 metres is 1.00 metres'
    >>> convert_unit('metres', 1.0, 'inches')
    '1.00 metres is 39.37 inches'
    >>> convert_unit('metres', 3.0, 'inches')
    '3.00 metres is 118.11 inches'

    """
    length_units = list(length_conversions.keys())
    weight_units = list(weight_conversions.keys())
    all_units = length_units + weight_units

    if ((u1 not in all_units or u2 not in all_units)):
        return 'unknown units'

    if ((u1 in length_units and u2 in weight_units) or
        (u1 in weight_units and u1 in length_units)):
        return "{} can't be converted to {}".format(u1, u2)

    # use the proper conversions
    if u1 in length_conversions:
        conversions = length_conversions
    else:
        conversions = weight_conversions

    std_val = val * conversions[u1]
    u2_val = std_val * conversions[u2]
    return '{:.2f} {} is {:.2f} {}'.format(val, u1, u2_val, u2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
