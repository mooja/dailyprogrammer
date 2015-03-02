#!/usr/bin/env python
# encoding: utf-8

# Daily Programmer Challenge 89 Easy
#
# http://www.reddit.com/r/dailyprogrammer/comments/yj2zq/8202012_challenge_89_easy_simple_statistical/
#
# March.02.2015

import math


def mean(xs):
    """ mean([ints...]): return the arithmetic mean (average) of the input
                         sequence

    >>> mean([1, 2, 3])
    2.0
    """
    return sum(xs) / float(len(xs))


def variance(xs):
    """ variance([ints...]): return the average of the squared differnces
                             from the mean
    >>> variance([1, 1, 1])
    0.0
    """
    mean_ = mean(xs)
    squared_difference = [(x-mean_)**2 for x in xs]
    variance_ = mean(squared_difference)
    return variance_


def stddev(xs):
    """ stddev([ints...]): return standard deviation: the square root of
                           the variance
        >>> stddev([1, 1, 1])
        0.0
    """
    _variance = variance(xs)
    return math.sqrt(_variance)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    data = """
    0.4081
    0.5514
    0.0901
    0.4637
    0.5288
    0.0831
    0.0054
    0.0292
    0.0548
    0.4460
    0.0009
    0.9525
    0.2079
    0.3698
    0.4966
    0.0786
    0.4684
    0.1731
    0.1008
    0.3169
    0.0220
    0.1763
    0.5901
    0.4661
    0.6520
    0.1485
    0.0049
    0.7865
    0.8373
    0.6934
    0.3973
    0.3616
    0.4538
    0.2674
    0.3204
    0.5798
    0.2661
    0.0799
    0.0132
    0.0000
    0.1827
    0.2162
    0.9927
    0.1966
    0.1793
    0.7147
    0.3386
    0.2734
    0.5966
    0.9083
    0.3049
    0.0711
    0.0142
    0.1799
    0.3180
    0.6281
    0.0073
    0.2650
    0.0008
    0.4552
    """
    data = [float(x) for x in data.strip().split()]

    print("mean: {}".format(mean(data)))
    print("variance: {}".format(variance(data)))
    print("std. deviation: {}".format(stddev(data)))
